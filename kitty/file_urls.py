# License: GPLv3
"""Recover local file URLs hard-wrapped inside application text margins."""

import os
import re
from functools import lru_cache
from time import monotonic
from urllib.parse import unquote, urlsplit

from .fast_data_types import Screen

MAX_LINES = 16
fragment = re.compile(r"[A-Za-z0-9._~:/?#\[\]@!$&()*+,;=%-]+\Z")


@lru_cache(maxsize=128)
def ranges_for_lines(lines: tuple[str, ...], epoch: int, excluded: str) -> tuple[tuple[int, int, int], ...]:
    # The short-lived cache avoids repeated stat calls for each cell of a URL.
    del epoch
    for start, line in enumerate(lines):
        indent = len(line) - len(line.lstrip(' '))
        first = line.strip(' ')
        if not first.startswith(('file:///', 'file://localhost/')):
            continue
        url = ''
        ranges: list[tuple[int, int, int]] = []
        match: tuple[tuple[int, int, int], ...] = ()
        for row in range(start, min(len(lines), start + MAX_LINES)):
            raw = lines[row]
            if len(raw) - len(raw.lstrip(' ')) != indent:
                break
            part = raw.strip(' ')
            if not fragment.fullmatch(part) or any(c in excluded for c in part):
                break
            if row > start and '://' in part:
                break
            url += part
            ranges.append((indent, row, indent + len(part) - 1))
            try:
                parsed = urlsplit(url)
                if parsed.netloc not in ('', 'localhost') or parsed.query or parsed.fragment:
                    break
                path = unquote(parsed.path, errors='strict')
                if os.path.exists(path):
                    match = tuple(ranges)
            except UnicodeError:
                # A line can end in the middle of a percent-encoded character.
                continue
            except (ValueError, OSError):
                break
        if len(match) > 1:
            return match
    return ()


def detect_wrapped_file_url(screen: Screen, x: int, y: int, excluded: str) -> tuple[tuple[int, int, int], ...]:
    if '\n' in excluded:
        return ()
    # Try nearby starts separately so another link above cannot hide this one.
    for start in range(y, max(-1, y - MAX_LINES), -1):
        line = str(screen.visual_line(start))
        if not line.lstrip(' ').startswith(('file:///', 'file://localhost/')):
            continue
        lines = tuple(str(screen.visual_line(i)) for i in range(start, min(screen.lines, start + MAX_LINES)))
        ranges = ranges_for_lines(lines, int(monotonic() * 2), excluded)
        if any(row + start == y and left <= x <= right for left, row, right in ranges):
            return tuple((left, row + start, right) for left, row, right in ranges)
    return ()
