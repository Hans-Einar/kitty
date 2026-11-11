#!/usr/bin/env python
# License: GPLv3
"""Select a manually saved native Kitty session."""

import argparse
import curses
import fcntl
import json
import os
import sys
import tempfile
from datetime import datetime
from pathlib import Path


def catalog_path() -> Path:
    root = os.environ.get('XDG_STATE_HOME') or os.path.expanduser('~/.local/state')
    return Path(root) / 'kitty' / 'saved-sessions.json'


def read_catalog(path: Path) -> list[str]:
    try:
        data = json.loads(path.read_text())
    except FileNotFoundError:
        return []
    if not isinstance(data, list) or any(not isinstance(x, str) for x in data):
        raise ValueError(f'Invalid session catalog: {path}')
    return data


def remember_session(path: str) -> None:
    """Register only successful manual saves. Never make a saved file depend on this index."""
    try:
        catalog = catalog_path()
        catalog.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
        with open(str(catalog) + '.lock', 'a') as lock:
            fcntl.flock(lock, fcntl.LOCK_EX)
            paths = read_catalog(catalog)
            saved = str(Path(path).resolve())
            paths = [saved] + [p for p in paths if p != saved]
            fd, temporary = tempfile.mkstemp(dir=catalog.parent, prefix='.sessions-')
            try:
                with os.fdopen(fd, 'w') as stream:
                    json.dump(paths, stream, ensure_ascii=True, indent=2)
                    stream.write('\n')
                os.replace(temporary, catalog)
            finally:
                if os.path.exists(temporary):
                    os.unlink(temporary)
    except (OSError, ValueError) as e:
        from .utils import log_error

        log_error(f'Session saved, but could not update the resume catalog: {e}')


def discover_sessions(directories: list[Path]) -> tuple[list[Path], list[str]]:
    warnings: list[str] = []
    candidates: list[Path] = []
    try:
        candidates.extend(Path(p) for p in read_catalog(catalog_path()))
    except (OSError, ValueError) as e:
        warnings.append(str(e))
    for directory in directories:
        try:
            candidates.extend(p for p in directory.iterdir() if p.suffix in ('.kitty-session', '.session', '.kitty_session'))
        except FileNotFoundError:
            pass
        except OSError as e:
            warnings.append(str(e))
    found: dict[Path, float] = {}
    for path in candidates:
        try:
            path = path.expanduser().resolve()
            if path.is_file():
                found[path] = path.stat().st_mtime
        except OSError as e:
            warnings.append(str(e))
    return sorted(found, key=lambda p: (-found[p], str(p))), warnings


def validate_session(path: Path, configs: list[str]) -> None:
    from .config import load_config
    from .session import parse_session

    list(parse_session(path.read_text(), load_config(*configs), session_path=str(path)))


def launch_argv(path: Path, configs: list[str], name: str) -> list[str]:
    from .constants import kitty_exe

    argv = [kitty_exe()]
    for config in configs:
        argv.extend(('--config', config))
    if name:
        argv.extend(('--name', name))
    return argv + ['--session', str(path)]


def display_text(text: str) -> str:
    return ''.join(c if c.isprintable() else '?' for c in text)


def choose_session(screen: 'curses.window', paths: list[Path], configs: list[str]) -> Path | None:
    screen.keypad(True)
    try:
        curses.curs_set(0)
    except curses.error:
        pass
    query, message, selected = '', '', 0
    while True:
        matches = [p for p in paths if query.casefold() in str(p).casefold()]
        selected = min(selected, max(0, len(matches) - 1))
        height, width = screen.getmaxyx()
        screen.erase()

        def write(row: int, value: str, attribute: int = 0) -> None:
            if 0 <= row < height and width > 1:
                try:
                    screen.addnstr(row, 0, display_text(value), width - 1, attribute)
                except curses.error:
                    pass

        write(0, 'Kitty resume — Enter: open  Esc: cancel  ↑/↓: select', curses.A_BOLD)
        write(1, 'Search: ' + query)
        count = max(1, height - 5)
        start = max(0, selected - count + 1)
        for row, path in enumerate(matches[start : start + count], 2):
            try:
                modified = datetime.fromtimestamp(path.stat().st_mtime).strftime('%Y-%m-%d %H:%M')
            except OSError:
                modified = 'missing'
            write(row, f'{path.name}  {modified}', curses.A_REVERSE if row - 2 + start == selected else 0)
        if not matches:
            write(2, 'No matching sessions')
        elif height >= 5:
            write(height - 2, str(matches[selected]))
        write(height - 1, message or f'{len(matches)} session(s) • Type to search, Backspace to edit')
        screen.refresh()
        try:
            key = screen.get_wch()
        except KeyboardInterrupt:
            return None
        if key in ('\x1b', '\x03'):
            return None
        if key in ('\n', '\r', curses.KEY_ENTER) and matches:
            try:
                validate_session(matches[selected], configs)
            except (Exception, SystemExit) as e:
                message = f'Cannot open session: {e}'
            else:
                return matches[selected]
        elif key in (curses.KEY_DOWN, curses.KEY_UP, curses.KEY_NPAGE, curses.KEY_PPAGE):
            delta = {curses.KEY_DOWN: 1, curses.KEY_UP: -1, curses.KEY_NPAGE: count, curses.KEY_PPAGE: -count}[key]
            selected = max(0, min(len(matches) - 1, selected + delta))
        elif key == curses.KEY_HOME:
            selected = 0
        elif key == curses.KEY_END:
            selected = max(0, len(matches) - 1)
        elif key in ('\x7f', '\b', curses.KEY_BACKSPACE):
            query, selected, message = query[:-1], 0, ''
        elif isinstance(key, str) and key.isprintable():
            query, selected, message = query + key, 0, ''


def main(args: list[str]) -> None:
    from .constants import config_dir

    parser = argparse.ArgumentParser(prog='kitty resume', description='Select a manually saved native Kitty session.')
    parser.add_argument('--directory', action='append', default=[], help='Also search this directory for session files')
    parser.add_argument('--config', action='append', default=[], help='Kitty configuration used when restoring')
    parser.add_argument('--name', default='', help='Window name used when restoring')
    parser.add_argument('--list', action='store_true', help='Print available session paths without opening the picker')
    opts = parser.parse_args(args)
    directories = [Path(config_dir) / 'sessions'] + [Path(p).expanduser() for p in opts.directory]
    paths, warnings = discover_sessions(directories)
    for warning in warnings:
        print('kitty resume: ' + display_text(warning), file=sys.stderr)
    if opts.list:
        for path in paths:
            print(display_text(str(path)))
        return
    if not paths:
        raise SystemExit(f'No saved sessions. Save one with F1, or put .kitty-session files in {directories[0]}.')
    if not sys.stdin.isatty() or not sys.stdout.isatty():
        raise SystemExit('kitty resume needs an interactive terminal (use --list to list sessions).')
    path = curses.wrapper(choose_session, paths, opts.config)
    if path is not None:
        argv = launch_argv(path, opts.config, opts.name)
        os.execv(argv[0], argv)
