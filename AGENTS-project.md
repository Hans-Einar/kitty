# Kitty workstation development

This is the workstation fork published at `Hans-Einar/kitty`, based on upstream
Kitty v0.50.0 after MAINT-KITTY-0002. `main` tracks `personal/main`; `origin`
points to `kovidgoyal/kitty`. Preserve manual save/resume, Python 3.14 TUI loop
registration and the opt-in wrapped local file URL extension. These are fork
changes, not claims about an upstream release.

Use the installed SDP 2.1.0 profile and project namespace KITTY for new work.
Existing PROJECT installation identities remain unchanged. Read the completed
[resume Session](SDP/Sessions/session-%230001--Kitty-resume.md) for historical context. Current upgrade work is tracked by
[MAINT-KITTY-0002](SDP/Maintenance/MAINT-KITTY-0002.md).
Documentation is English; conversation with the owner may be Norwegian.

Source models belong in SDP/SDL/Kitty. The upstream-compatible build command is
`./dev.sh build`; option changes also require `./kitty/launcher/kitty +launch gen config`.
The workstation launcher/profile integration is maintained separately in
`../Linux/mods/kitty-patched`. Window Maker Ctrl+E calls `~/bin/kitty`.

Owner-selected navigation: Alt+Left/Right cycle terminals within the current tab;
Alt+Up/Down cycle tabs. Ctrl+Alt+arrows remain Window Maker OS-window navigation.

Use plain absolute file:/// URLs in user-facing responses, one per line, with
reserved characters percent-encoded and no Markdown wrappers or line suffixes.
