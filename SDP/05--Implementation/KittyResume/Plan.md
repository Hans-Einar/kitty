# PLAN-KITTY-0002 — Manual session save and resume picker

| Field | Value |
| --- | --- |
| id | PLAN-KITTY-0002 |
| project | KITTY |
| state | completed |
| PlanType | ImplementationPlan |
| BranchPolicy | current |
| CommitPolicy | milestone |
| source | KB-KITTY-001; owner T002 manual-save scope |

## Outcome and authority

Implement the owner's selected manual-save workflow: native F1 saving and a
`kitty resume` terminal picker. Replaces canceled PLAN-KITTY-0001. The current
owner request authorizes this implementation and local workstation activation.

## Design and boundary

Reuse native session save/load, including native cwd and foreground invocation
handling. Remember successfully saved file paths only; also discover standard
session files in the Kitty config sessions directory. The TUI searches paths,
selects with arrows and restores with Enter; Escape cancels. Report unreadable
or malformed sessions without launching them. Preserve launch profile through
the Window Maker wrapper. Do not continuously observe programs, alter cd,
infer Codex IDs, rewrite saved commands or add custom geometry restoration.

## Git policy

Use current non-protected branch wmkitty-multiline-file-links. One milestone
commit contains only resume implementation/tests/docs and the installed SDP
foundation it uses. Exclude pre-existing link code/tests. No push or release.
Workstation module changes belong in the separate Linux repository and remain
uncommitted to preserve its existing mixed index/worktree.

## Milestone

| Phase | Milestone | Acceptance | State |
| --- | --- | --- | --- |
| P1 Manual workflow | M1 Saved session picker | Unit tests for catalog/error/argv handling; PTY picker selection/cancel; isolated GUI round trip of tabs/panes/cwd and explicit resume argv; config/F1 checks. | completed |

## Evidence

Record actual results in SDP/Verification/KittyResume.md before closure.

## M1 outcome

Delivered the bounded manual workflow. Native per-pane relative cwd parsing needed
a scoped correction discovered by the round-trip test. No observer/Codex adapter
was introduced. All selected acceptance checks passed; see the verification record.
