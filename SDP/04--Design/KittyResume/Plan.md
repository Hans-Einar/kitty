# PLAN-KITTY-0001 — Resolve the Kitty resume design

| Field | Value |
| --- | --- |
| id | PLAN-KITTY-0001 |
| project | KITTY |
| state | canceled |
| PlanType | DesignPlan |
| BranchPolicy | current |
| CommitPolicy | milestone |
| source | KB-KITTY-001; owner conversation of 2026-10-08 |

## Outcome and authority

Prepare an implementable design for autosaved Kitty workspaces and exact Codex
resume. The owner requested SDP setup and exploration of this capability. An
initial study/model is available; the choice to also build a first runtime was
asked asynchronously and has not yet been answered. No runtime implementation
or owner acceptance is claimed. [Study](Study.md) ·
[Session](../../Sessions/session-%230001--Kitty-resume.md).

## Baseline and scope

Local Kitty v0.43.1 with existing uncommitted link changes; signed SDP 2.1.0;
X11/Window Maker; normal codex and the owner's yolo alias. Reuse native sessions.
The plan resolves the Codex-ID interface, snapshot lifecycle, visible order and
geometry preservation before selecting runtime increments. It does not deliver
process-memory checkpointing, remote hosts or future SDP blueprints.

## Git policy

Use current working branch `wmkitty-multiline-file-links` for the design draft.
Commit only the coherent resume/SDP milestone paths when that milestone is
completed; preserve and exclude pre-existing link changes. Runtime work should
select its own bounded plan/branch before editing. No push, PR, merge or release
is requested. No milestone commit has been made for this planned work.

## Phases and milestones

| Phase | Milestone | Acceptance | State |
| --- | --- | --- | --- |
| P1 Evidence and contracts | D1 Identity/lifecycle decisions | Demonstrate exact Codex ID acquisition for two panes in one cwd, including in-app session switching; settle close/replay policies. | Planned; baseline study prepared |
| P2 Integrated design | D2 Restore contract | Round-trip visible tab order, split sizes/focus and X11 geometry; document atomic-write and recovery cases; validate updated SDL. | Planned |
| P3 Delivery selection | D3 Implementation handoff | Select observable runtime increments, tests and scope; record actual owner direction on first implementation. | Planned |

Suggested runtime increments after design: native save/restore catalog and TUI;
change-driven autosave/close handling; exact Codex adapter; integrated recovery
and workstation activation. These are proposed work, not completed milestones.

## Evidence and remaining work

See [baseline record](../../Traceability/KITTY-RESUME-001.md). Current checks cover
installation, existing CLI/source facts, configuration and structural model
validity. They do not prove autosave, resume TUI or Codex restoration.

## T002 owner scope replacement

The owner selected manual native saving plus a resume picker. Autosave, automatic
Codex-ID discovery and custom geometry restoration are removed from this work.
This unexecuted design plan is canceled and replaced by PLAN-KITTY-0002.
