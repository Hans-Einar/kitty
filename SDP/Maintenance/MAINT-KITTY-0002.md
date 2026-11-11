# MAINT-KITTY-0002 — Upgrade workstation fork to Kitty 0.50.0

| Field | Value |
| --- | --- |
| id | MAINT-KITTY-0002 |
| project | KITTY |
| state | active |
| PlanType | MaintenancePlan |
| BranchPolicy | current |
| CommitPolicy | milestone |

## Outcome and authority

On 2026-11-11 the owner authorized the proposed upgrade to stable Kitty 0.50.0.
Merge the upstream release into the personal fork, preserve all existing history,
manual save/resume, serialized relative cwd, Python 3.14 TUI compatibility and
opt-in wrapped local file links. Build and test in an isolated worktree before
updating the workstation checkout and publishing personal/main. Existing running
terminal windows must not be terminated. This is a fork maintenance delivery,
not a new upstream release or a change to SSH shell behavior.

## Baseline and implementation

Baseline main: f8877e1bd (customized Kitty 0.43.1). Upstream: v0.50.0.
One milestone on upgrade/kitty-0.50.0, followed by a fast-forward of main and
push to the owner's personal remote. Keep origin pointing to upstream and fetch
its master branch as well as the original pinned tag.

Resolve nine conflicted files against the newer implementation. Move the custom
test callback to upstream's new kitty_tests/base.py; preserve the new regex URL
recognizer and honor the new mark=False URL detection contract. Regenerate
configuration artifacts. Preserve event-loop registration/reuse, which our
existing test requires beyond upstream's missing-loop fallback.

## Acceptance and evidence

Build succeeds; focused resume, TUI, screen, layout and configuration tests pass;
run broader upstream tests as supported by the environment. Re-run isolated GUI
save/restore and resize checks against the candidate. Record the exact candidate,
commands, outcomes and limitations before completing this record. Existing
requirements/design remain applicable; no new user workflow is selected.

## Progress

Merge conflicts resolved; isolated build, all 1397 tests (12 skipped), lint and
GUI/PTY acceptance passed. See [verification](../Verification/Kitty050Upgrade.md).
Installation into the main checkout and publication remain pending.
