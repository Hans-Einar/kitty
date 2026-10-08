# Kitty resume M1 verification

Date: 2026-10-08. Candidate: base HEAD
7f24dd68c98d8f4712457560f25e8056cce52ec8 plus the working-tree implementation
identified by [source hashes](evidence/KittyResume/source-sha256.json).
Linux x86_64, source-built Kitty 0.43.1, bundled Python, Xvfb with software GL.
The tested worktree also contains the prior uncommitted wrapped-file-URL patch.
Tests are self-verification; no independent review or actual Codex conversation
was launched. A sleeping Python stand-in verifies explicit resume argument replay.

## Results

| Check | Command / method | Result |
| --- | --- | --- |
| Catalog, picker, native parsing and cwd regression | `./kitty/launcher/kitty +launch test.py --module resume` | 11 passed |
| Existing screen behavior | `./kitty/launcher/kitty +launch test.py --module screen` | 41 passed |
| Existing layout behavior | `./kitty/launcher/kitty +launch test.py --module layout` | 3 passed |
| Real terminal picker | `python3 SDP/Verification/evidence/KittyResume/pty-check.py` | select, cancel, invalid-file: passed |
| Native GUI save/load | `python3 SDP/Verification/evidence/KittyResume/roundtrip.py` | 2 tabs, 3 panes, layout/focus, distinct cwd, explicit resume argument, catalog registration: passed |
| Workstation mapping | Parse installed navigation.conf; inspect resolved actions and flags | F1 + foreground/relocatable; Alt pane/tab actions: passed |
| Wrapper entry point | `/home/warloc/bin/kitty resume --help` | Resume help, preserves profile arguments |
| SDL | `sdl check`; navigator generation | Valid, zero diagnostics; views generated |
| Ledger | jsonschema envelope and versioned payload validation | Passed before and after closure |
| Diff hygiene | `git diff --check` | Passed |

The GUI script creates its temporary workspace under /tmp/kitty-resume-check,
uses display :94 and terminates only its test instances. Run it before the PTY
script to create a valid snapshot and isolated catalog. PTY launch is intercepted
after real selection to inspect the exact argument vector without opening another
GUI. Actual native restoration is covered by the separate GUI script.

## Findings and fixes

The first GUI run exposed a native bug: serialized relative per-pane `--cwd`
used the invoker's working directory. Fix: resolve serialized launch records
against the saved file's directory, matching native tab `cd`. The regression
and GUI rerun passed, including a directory with a space.
An initial search test accidentally matched its randomized temporary parent path;
the test now searches the filename. The PTY harness initially used a lambda whose
name lookup was invalid inside Kitty's +runpy exec; corrected harness, then passed.
No acceptance was removed to hide a runtime failure.

## Activation and boundaries

Installed Linux/mods/kitty-patched with the existing Linux installer. Reloaded
profile mappings in running wmkitty processes. Python runtime changes require a
new Kitty instance (Ctrl+E). F1 retains the native filename prompt and editor.
Previously saved files are discovered in the config sessions directory or with
--directory; arbitrary save paths are remembered by newly loaded save code.

Native save scope and loader semantics apply, including native tab ordering and
window-manager behavior. This implementation restarts saved commands, not memory
or unsaved buffers. No autosave, cd alias, inferred Codex IDs or custom geometry.
The unrelated existing `allow_remote_contro` profile typo remains unchanged;
no remote-control permission was enabled in the user's profile.

## Traceability

REQ-001/008/012: unit + PTY checks. REQ-002/003: GUI round trip and cwd regression.
REQ-010: existing tests and wrapper/config checks. REQ-011: installed mapping and
native save hook coverage. See [requirements](../02--Requirements/KittyResume.md)
and [implementation plan](../05--Implementation/KittyResume/Plan.md).
