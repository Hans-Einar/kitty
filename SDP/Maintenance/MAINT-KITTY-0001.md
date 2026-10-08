# MAINT-KITTY-0001 — Python 3.14 TUI event-loop startup

| Field | Value |
| --- | --- |
| id | MAINT-KITTY-0001 |
| project | KITTY |
| state | completed |
| PlanType | MaintenancePlan |
| BranchPolicy | current |
| CommitPolicy | milestone |

## Outcome, authority and analysis

Owner T003 reports Ctrl+Shift+R failing in kittens/tui/loop.py with no current
event loop. Reproduced with the source launcher and `from kittens.tui.loop import
Loop; Loop()`. Bundled Python 3.14 no longer implicitly creates a current loop.
Source: https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.get_event_loop

The shared TUI Loop owns initialization and supports multiple interactive kittens.
Preserve an existing current loop and the macOS SelectSelector special case.
If no loop exists on the normal path, explicitly create and register one.
This is a compatibility repair; no shortcut/session/layout policy changes.

## Route and Git policy

One phase/milestone: fix startup, cover absent and existing loops in regression
tests, then exercise resize opening, resizing and exit in an isolated Kitty GUI.
Use current wmkitty-multiline-file-links branch and one scoped local commit;
exclude pre-existing wrapped-link changes. No push or release. Owner bug report
authorizes repair of the local installation. No new binary build is expected:
the kitten loads Python source in a fresh process on invocation.

## Evidence and remaining work

Baseline HEAD: a4fc64b. Initial reproduction fails with the owner's RuntimeError.
Completed: `./kitty/launcher/kitty +launch test.py --module tui` passed all three
tests. The regression starts with no current loop, checks registration, runs a
callback and verifies reuse on a second TUI initialization.

The isolated Xvfb GUI check sent real Ctrl+Shift+R keyboard events through XTest,
observed the resize overlay, sent W and verified the active pane grew from 40 to
42 columns, then verified Escape closed the overlay. Reproduction script and
[result](../Verification/evidence/KittyResize/result.json) are retained in
[GUI check](../Verification/evidence/KittyResize/check.py). Run with system Python
from this workstation; it uses display :95 and its own temporary Kitty instance.

The source-loaded kitten runs in a fresh process, so the fix is effective on its
next invocation without restarting the user's terminal. No shared current loop
is replaced, and the macOS selector path is unchanged (not exercised on Linux).
No requirements/SDL changes are needed: this restores existing resize behavior.
These are agent self-checks, not an independent review. No remaining work for
this bounded repair. Follow-up in
[Session T003](../Sessions/session-%230001--Kitty-resume.md).

Tested source SHA256 (kittens/tui/loop.py):
`eb08a8d897c109ea873b5c6badeedd5e7dde51ef977155eb5c4521a32ae59f1f`.
