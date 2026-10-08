---
name: sdp
description: Use the project's System Design Process for SDP-governed study, development, review or maintenance.
  Resolve current project authority, select the relevant SDP role and keep durable project documents aligned with
  the work. Use when explicitly invoked or when the project requires SDP.
metadata:
  skillId: sdp
  skillVersion: 1.1.0
  minimumToolkitVersion: 0.2.0
  capabilities: sdp.route
  compatibilityNotes: Initial adopted profile-aware role.
---

# SDP entrypoint

For a trivial factual question or unrelated task, answer directly without starting
SDP lifecycle work.

Translate a short owner request into the appropriate existing SDP workflow.
This is a method entrypoint, not a new management role or an authorization to
implement, delegate, publish or migrate a project.

## Establish context

Read applicable project instructions, its SDP entry instructions and installed
Framework/manifest when present. Resolve the actual project and document roots;
the Toolkit repository's own lifecycle records are not consuming-project seeds.
Use current work pointers to find relevant intent, requirements and design.
Read [Document workflow](references/document-workflow.md) for the read/update
obligations. Reuse this context within an assignment, refreshing changed facts.

For methodology/history questions or conflicting SDP versions, also read
[Source map](references/source-map.md). Do not apply historical proposals as
installed project rules. Report missing authority with its practical effect.

## Route the work

Preserve an explicitly assigned role. Otherwise select the smallest applicable
set below and read those entrypoints; do not load all roles for every task.
Paths assume this collection is distributed together. If a required
role or reference is absent, report the gap; do not claim it was loaded or
silently install a different version. Continue only work supported by available
project instructions and authorization.

| Request or need | Read |
|---|---|
| Create, select or revise a plan; coordinate KanBan/Scrum/Sprint | [Planning](../sdp-planning/SKILL.md) |
| Unexplained symptom or new capability | [Change Analysis](../sdp-change-analysis/SKILL.md) |
| Material design alternatives or conflicting contracts | [Architect](../sdp-architect/SKILL.md) |
| Coordinate an authorized implementation assignment | [Master](../sdp-master/SKILL.md) |
| Implement an assigned milestone, Maintenance task, Slice/Fix | [Worker](../sdp-worker/SKILL.md) |
| Independent review | [Reviewer](../sdp-reviewer/SKILL.md) |
| Establish evidence for a claimed outcome | [Verifier](../sdp-verifier/SKILL.md) |
| Maintain decision/work/evidence links | [Traceability](../sdp-traceability/SKILL.md) |
| Explicit supervisory work or unresolved owner disposition | [Steering](../sdp-steering/SKILL.md) |
| Inspect installation or record consistency | [Auditor](../sdp-auditor/SKILL.md) |
| Behavior-preserving structural migration | [Vertical Refactor](../sdp-vertical-refactor/SKILL.md) |
| Release compatibility/version selection | [Versioning](../sdp-versioning/SKILL.md) |
| Authorized release preparation/publication | [Release](../sdp-release/SKILL.md) |

Method explanations can be answered from the shared references without starting
an execution workflow. A question about a defect is not release work. Routing
to a skill does not require spawning an agent; preserve required independence
when review is actually performed.

## Make the result durable

Name the relevant governing documents and the selected role briefly. Maintain
one linked handoff: owner outcome, governing decisions, changed behavior,
affected documents and evidence. Update canonical project documents within the
authorized assignment; route out-of-scope updates with concrete destinations.
Do not close implementation work while a material document inconsistency is
hidden behind a completed ledger entry. For read-only work, report proposed
updates instead of making them.
