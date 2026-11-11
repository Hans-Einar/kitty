# MAINT-KITTY-0002 — Upgrade workstation fork to Kitty 0.50.0

| Field | Value |
| --- | --- |
| id | MAINT-KITTY-0002 |
| project | KITTY |
| state | completed |
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
Installed source commit: `1b0a167c002dd3f1ffc6ca2ce950e1153e29df28`.
The main checkout was fast-forwarded and `./dev.sh build` completed there.
`/home/warloc/bin/kitty --version` reports 0.50.0; resume help works; Python
imports resolve to the main checkout. An isolated GUI startup through the real
wrapper and owner profile passed. The existing saved session parsed successfully.
Source hashes still match the tested candidate.

Published implementation commit 1b0a167c0 to `personal/main` and verified the
GitHub ref with `git ls-remote`. This closeout is a documentation-only follow-up.
All pre-upgrade commits remain ancestors of main; no force push was used.
The local upstream fetch mapping now includes master as well as the old tag.

Backup: `/home/warloc/.local/state/kitty-upgrade-backup/20261111-0.43.1` contains
the old source archive, compiled runtime files and commit manifest. Local branch
`backup/pre-kitty-0.50.0-20261111` also retains the old main tip. No running user
terminal was killed or reset. New windows use 0.50.0; old processes remain on
their loaded version until the owner closes them.

No remaining work for this upgrade. Automatic terminal-mode cleanup after SSH
disconnection remains a separate, unimplemented improvement; this delivery
makes no claim that upgrading alone fixes stale mouse reporting.
