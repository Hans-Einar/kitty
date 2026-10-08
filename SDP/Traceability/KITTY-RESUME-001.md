# KITTY-RESUME-001 — Resume baseline and design evidence

Date: 2026-10-08. Scope: initial research/design; no resume runtime delivered.
Management: KB-KITTY-001 and planned PLAN-KITTY-0001.

- Kitty baseline: upstream v0.43.1, commit 7f24dd68c98d8f4712457560f25e8056cce52ec8,
  with pre-existing uncommitted multiline file-link changes.
- SDP: `gh sdp /home/warloc/git/kitty install --plan-output
  /tmp/kitty-sdp-install-plan.json --json`, then `install --apply` of that plan.
  Preview: canApply true, zero conflicts. Result: completed,
  install-a60ed90e6fc467b63e247b8a, MAINT-PROJECT-0001. Installed receipt records
  signed release 2.1.0 and its descriptor digest. This is not an install of the
  changing SDP-vNow source tree.
- Source inspection: Kitty session parser, Boss/TabManager/Tab serializers and
  Window foreground-command handling. Exact tab-order and desktop geometry
  round trips have not been demonstrated.
- Codex: local `codex resume --help` accepts a SESSION_ID. Shell alias yolo expands
  to `codex --yolo`. Automatic current-ID acquisition remains unresolved.
- Navigation: loaded profile parsed with Kitty's own config loader; expected
  definitions checked with unittest assertions, then SIGUSR1 sent to matching
  Window Maker Kitty processes. Alt+Left/Right are previous_window/next_window;
  Alt+Up/Down are previous_tab/next_tab. Source is maintained in the Linux repo's
  kitty-patched module. This check establishes configuration, not a GUI test.
- SDL: canonicalized with `sdl format`, then `sdl check` returned valid true and
  zero diagnostics. The first check required canonical ordering; formatting
  resolved that finding. Tool SHA-256:
  `9f275f62b56828596fc5bf4f8959bbd0e47ff949eef949c9bcdba28f8b85f1dd`.
- `sdl viewpoints SDP/SDL/Kitty/Resume.design --format navigator --project kitty
  --output /tmp/kitty-resume-viewpoints` generated 15 navigation files, zero
  diagrams, revision `627bef3ce4bf394dfa423b2c0b98308258f3218e0e4410cf15d717744fb21521`.
  This establishes source parsing/navigation, not runtime behavior.
- All four management events validate against the installed event envelope and
  matching payload schemas, including the preserved installation events.
- All 22 relative links in the new project documents resolve.
- `gh sdp /home/warloc/git/kitty discover --json` completed successfully after
  authoring; `git diff --check` passed for tracked changes.

No independent review, owner design acceptance, autosave/restore run or blueprint
execution is claimed.
