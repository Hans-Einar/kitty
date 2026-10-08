# KB-KITTY-001 — Resume a Kitty workspace

| Field | Value |
| --- | --- |
| id | KB-KITTY-001 |
| project | KITTY |
| type | Proposal |
| CardState | completed |
| created | 2026-10-08T08:08:42Z |
| source | Owner conversation, 2026-10-08; manually summarized in Session T001 |
| Systems | Kitty; external Codex |
| PlanId | PLAN-KITTY-0002 |

## Outcome

F1 invokes native `save_as_session --use-foreground-process --relocatable`.
`kitty resume` provides a searchable terminal picker for these saved files and
starts the selected native session. Native per-pane working directories and
explicit `codex resume <ID>` / `yolo resume <ID>` invocations are retained.
The owner prepares Codex commands before saving. No autosave or command tracking.

## Delivered work

[PLAN-KITTY-0002](../../05--Implementation/KittyResume/Plan.md) implements the
owner's T002 scope reduction. Native snapshot semantics remain authoritative;
custom desktop geometry/order preservation is outside this selected scope.

## Working material

- [Session and roadmap](../../Sessions/session-%230001--Kitty-resume.md)
- [Accepted design](../../04--Design/KittyResume/Study.md)
- [Requirements](../../02--Requirements/KittyResume.md)
- [SDL ownership model](../../SDL/Kitty/Resume.design)
- [Baseline evidence](../../Traceability/KITTY-RESUME-001.md)

## Worklog

- 2026-10-08: Registered the owner's request. Inspected Kitty v0.43.1 session
  serialization, installed SDP 2.1.0 through gh sdp, and prepared a design draft.
  Confirmed yolo is a shell alias for `codex --yolo`, not `--yolp`.
- T001 remaining items were superseded by the owner's T002 manual-save scope.

- T002: Owner selected manual saving and offered to launch Codex with explicit
  resume IDs before saving. Activated the bounded implementation plan.

- T002 completed: native F1 mapping, save-path catalog, searchable resume TUI,
  wrapper profile preservation and serialized relative cwd fix. Eleven unit tests,
  three PTY cases and isolated native GUI round trip passed; existing 41 screen
  and three layout tests passed. See [verification](../../Verification/KittyResume.md).
