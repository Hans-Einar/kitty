#!/usr/bin/env python
# License: GPLv3

import os
import tempfile
from pathlib import Path
from unittest.mock import Mock, patch

from kitty import resume
from kitty.session import default_save_as_session_opts, save_as_session_part2

from .base import BaseTest


class ResumeTest(BaseTest):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.catalog = self.root / 'state' / 'saved-sessions.json'
        self.patcher = patch.object(resume, 'catalog_path', return_value=self.catalog)
        self.patcher.start()
        self.addCleanup(self.patcher.stop)

    def test_catalog_remembers_arbitrary_paths_and_deduplicates(self):
        path = self.root / 'project with spaces'
        path.write_text('launch\n')
        resume.remember_session(str(path))
        resume.remember_session(str(path))
        self.assertEqual(resume.read_catalog(self.catalog), [str(path)])
        self.assertEqual(self.catalog.stat().st_mode & 0o777, 0o600)
        paths, warnings = resume.discover_sessions([])
        self.assertEqual(paths, [path])
        self.assertEqual(warnings, [])

    def test_discovery_directory_order_and_missing_files(self):
        old, new = self.root / 'old.kitty-session', self.root / 'new.session'
        old.write_text('launch\n')
        new.write_text('launch\n')
        os.utime(old, (10, 10))
        os.utime(new, (20, 20))
        (self.root / 'ignored.txt').write_text('launch\n')
        resume.remember_session(str(old))
        resume.remember_session(str(self.root / 'deleted'))
        paths, warnings = resume.discover_sessions([self.root, self.root / 'absent'])
        self.assertEqual(paths, [new, old])
        self.assertEqual(warnings, [])

    def test_corrupt_catalog_preserved_and_directory_still_works(self):
        self.catalog.parent.mkdir()
        self.catalog.write_text('{bad')
        path = self.root / 'valid.kitty-session'
        path.write_text('launch\n')
        with patch('kitty.utils.log_error') as log:
            resume.remember_session(str(path))
        log.assert_called_once()
        self.assertEqual(self.catalog.read_text(), '{bad')
        paths, warnings = resume.discover_sessions([self.root])
        self.assertEqual(paths, [path])
        self.assertTrue(warnings)
        self.catalog.write_text('[42]')
        with self.assertRaises(ValueError):
            resume.read_catalog(self.catalog)

    def test_native_save_registers_only_after_success(self):
        path = self.root / 'saved.kitty-session'
        opts = default_save_as_session_opts()
        opts.save_only = True
        boss = Mock()
        boss.serialize_state_as_session.return_value = ['launch']
        save_as_session_part2(boss, opts, str(path))
        self.assertEqual(path.read_text(), 'launch')
        self.assertEqual(resume.read_catalog(self.catalog), [str(path)])
        failed = self.root / 'failed.kitty-session'
        with patch('kitty.config.atomic_save', side_effect=OSError('read only')):
            with self.assertRaises(OSError):
                save_as_session_part2(boss, opts, str(failed))
        self.assertEqual(resume.read_catalog(self.catalog), [str(path)])
        boss.edit_file.assert_not_called()

    def test_validation_uses_native_parser_without_launching(self):
        path = self.root / 'sample.kitty-session'
        path.write_text('cd .\nlayout splits\nlaunch --title work bash\nnew_tab second\nlaunch codex resume example-id\n')
        resume.validate_session(path, ['NONE'])
        path.write_text('not_a_session_command nonsense\n')
        with self.assertRaisesRegex(ValueError, 'Unknown command'):
            resume.validate_session(path, ['NONE'])
        path.unlink()
        with self.assertRaises(OSError):
            resume.validate_session(path, ['NONE'])

    def test_serialized_relative_cwd_uses_session_directory(self):
        from kitty.config import defaults
        from kitty.session import parse_session

        raw = "cd first\nlaunch 'kitty-unserialize-data={\"id\": 1}' --cwd='second space'\n"
        sessions = list(parse_session(raw, defaults, session_path=str(self.root / 'saved.kitty-session')))
        self.assertEqual(sessions[0].tabs[0].windows[0].launch_spec.opts.cwd, str(self.root / 'second space'))

    def test_launch_argv_preserves_profile_and_literal_path(self):
        path = self.root / 'name $(touch BAD);.kitty-session'
        with patch('kitty.constants.kitty_exe', return_value='/real/kitty'):
            self.assertEqual(
                resume.launch_argv(path, ['profile a.conf', 'extra.conf'], 'wmkitty'),
                ['/real/kitty', '--config', 'profile a.conf', '--config', 'extra.conf', '--name', 'wmkitty', '--session', str(path)],
            )

    def screen(self, keys):
        screen = Mock()
        screen.getmaxyx.return_value = (20, 80)
        screen.get_wch.side_effect = keys
        return screen

    def test_picker_search_select_and_cancel(self):
        paths = [self.root / 'alpha.kitty-session', self.root / 'beta.kitty-session']
        with patch.object(resume.curses, 'curs_set'), patch.object(resume, 'validate_session') as validate:
            self.assertEqual(resume.choose_session(self.screen([*'beta.kitty', '\n']), paths, []), paths[1])
            validate.assert_called_once_with(paths[1], [])
            validate.reset_mock()
            self.assertIsNone(resume.choose_session(self.screen(['\x1b']), paths, []))
            validate.assert_not_called()

    def test_picker_invalid_session_stays_open(self):
        screen = self.screen(['\n', '\x1b'])
        with patch.object(resume.curses, 'curs_set'), patch.object(resume, 'validate_session', side_effect=ValueError('bad file')):
            self.assertIsNone(resume.choose_session(screen, [self.root / 'bad'], []))
        self.assertTrue(any('Cannot open session: bad file' in str(call) for call in screen.addnstr.call_args_list))

    def test_no_sessions_does_not_open_gui(self):
        with patch.object(resume, 'discover_sessions', return_value=([], [])), patch.object(resume.os, 'execv') as execute:
            with self.assertRaisesRegex(SystemExit, 'No saved sessions'):
                resume.main([])
        execute.assert_not_called()

    def test_display_sanitizes_control_characters(self):
        self.assertEqual(resume.display_text('a\x1b\n\tb'), 'a???b')
