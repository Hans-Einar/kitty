# Kitty workstation development

This is a local clone of upstream Kitty v0.43.1. The working branch is
`wmkitty-multiline-file-links`; the personal fork is `Hans-Einar/kitty`.
The owner authorized committing and publishing the existing multiline file URL
changes on 2026-10-23. Keep them scoped separately from unrelated changes and
do not imply they are upstream releases.

Use the installed SDP 2.1.0 profile and project namespace KITTY for new work.
Existing PROJECT installation identities remain unchanged. Read the active
[resume Session](SDP/Sessions/session-%230001--Kitty-resume.md) for this multi-turn
goal and update its roadmap and turn journal before handing work back.
Documentation is English; conversation with the owner may be Norwegian.

Source models belong in SDP/SDL/Kitty. The upstream-compatible build command is
`./dev.sh build`; option changes also require `./kitty/launcher/kitty +launch gen config`.
The workstation launcher/profile integration is maintained separately in
`../Linux/mods/kitty-patched`. Window Maker Ctrl+E calls `~/bin/kitty`.

Owner-selected navigation: Alt+Left/Right cycle terminals within the current tab;
Alt+Up/Down cycle tabs. Ctrl+Alt+arrows remain Window Maker OS-window navigation.

Use plain absolute file:/// URLs in user-facing responses, one per line, with
reserved characters percent-encoded and no Markdown wrappers or line suffixes.
