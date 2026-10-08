# Kitty resume — manual snapshots and a terminal picker

## Accepted direction (owner T002)

Reuse Kitty 0.43.1 native `save_as_session --use-foreground-process --relocatable`
and native `--session` restoration. Bind F1 in the workstation navigation include.
The owner chooses the save filename, reviews the native file in their editor,
and explicitly starts Codex/yolo with `resume <ID>` when appropriate.

`kitty resume` is a Python entry point with a curses picker: type to filter full
paths, arrows to select, Enter to validate and open, Escape to cancel. Display
filename, modification time and selected full path. The wrapper forwards the
wmkitty name and existing xterm.conf. No shell interpolation is used for launch.

Successful native saves register their resolved path in an atomic, locked JSON
catalog under XDG_STATE_HOME/kitty. The catalog contains paths only. Discovery
also scans config_dir/sessions and optional --directory roots, non-recursively,
for conventional session extensions. Missing files are skipped. Catalog errors
are reported, corrupt catalogs preserved, and readable directory files remain
available. Registration failure never invalidates the saved native session.

## Working directories and foreground commands

Native Window.cwd_for_serialization already reads process cwd and shell-reported
cwd. No cd alias is needed. Native foreground serialization preserves explicit
resume command arguments; no Codex-ID lookup or command rewriting is added.

A round-trip test found native per-pane `launch --cwd` values from relocatable
snapshots were resolved against the launching process instead of the session
file. The parser now resolves relative paths on serialized launch records against
the session directory, matching serialized tab `cd` semantics. Ordinary manual
launch commands keep their existing behavior. Regression and GUI tests cover it.

## Ownership and boundaries

NativeSessionCodec owns snapshot contents and restoration. SavedSessionCatalog
owns successful-save path registration and discovery. ResumePicker owns selection
and preflight validation. The executable launcher uses native --session afterward.

T001's automatic observer, Codex adapter, geometry integration and custom snapshot
format are superseded by this owner decision; PLAN-KITTY-0001 is canceled.
The bounded implementation is [PLAN-KITTY-0002](../../05--Implementation/KittyResume/Plan.md).
Native scope, tab ordering and window-manager behavior remain native. Programs
restart; application memory is not captured. No future blueprint tooling is
introduced.
