# Kitty 0.50.0 fork upgrade verification

Date: 2026-11-11. Candidate: merge of fork f8877e1bde04b716737d762f14a59bd413c28d50
and upstream v0.50.0 (bb1aca6f279f1a5cfa3edd765a71650fe91b6472), plus the
[source hashes](evidence/Kitty050Upgrade/source-sha256.json).
Environment: Linux x86_64, GCC 14, bundled Python 3.14, Go 1.27.1;
Xvfb and software GL for isolated GUI checks. Agent self-verification only.

## Results

| Check | Evidence | Result |
| --- | --- | --- |
| Build | `./dev.sh build` | Complete, including C extensions, shaders and Go kittens |
| Configuration generation | `kitty/launcher/kitty +launch gen config`; scoped formatting of generated C | Generated option plumbing retained; generated Python is excluded from formatting by upstream policy |
| Resume regressions | `kitty/launcher/kitty +launch test.py --module resume` | 11 passed |
| TUI regressions | `kitty/launcher/kitty +launch test.py --module tui` | 3 passed |
| Complete upstream + fork suite | `kitty/launcher/kitty +launch test.py` | 1397 tests, OK, 12 skipped; [log](evidence/Kitty050Upgrade/tests.log) |
| GUI/PTY workflow | `python3 SDP/Verification/evidence/Kitty050Upgrade/check.py /absolute/candidate/kitty /tmp/output-directory` | Round trip, picker select/cancel/invalid-file, real Ctrl+Shift+R resize/exit all passed; [results](evidence/Kitty050Upgrade/gui-result.json) |
| Source lint/format | `ruff check kitty kittens kitty_tests`; `ruff format --check kitty kittens kitty_tests` | Passed; 245 Python files already formatted |
| Local patch hygiene | `git diff --check v0.50.0` | Passed |
| Management history | jsonschema validation of event envelopes and versioned payloads | Passed |

The whole upstream import has existing whitespace findings and RST separator
lines that `git diff --check` labels conflict markers; these are present in the
release, not unresolved merge entries. All nine actual merge conflicts were
resolved. Generation initially lacked the formatter tool; it wrote the option
artifacts successfully, and the required formatters were then used separately.

## Preserved behavior and compatibility

The native save hook still registers only successful saves. The picker, explicit
resume arguments, relative per-pane working directories and owner's navigation
remain unchanged. The test callback moved into upstream's new base module.
Wrapped local file URLs coexist with upstream regex URL detection, explicit
hyperlinks retain precedence, and the new mark=False detection contract is honored.
The Python 3.14 event loop remains registered for reuse.

No SSH wrapper or automatic terminal reset is introduced. A dropped SSH session
can still leave mouse/keyboard reporting enabled; Ctrl+Shift+Delete resets the
active terminal. Upgrade completion is not evidence of resolving that symptom.

## Activation

The tested source will be fast-forwarded into the workstation main checkout and
built there because the development launcher embeds its source path. Existing
Kitty processes are left running. New windows use the upgraded build. Final
installation/publication evidence is recorded in
[MAINT-KITTY-0002](../Maintenance/MAINT-KITTY-0002.md).
