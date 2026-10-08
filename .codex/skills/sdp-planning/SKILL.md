---
name: sdp-planning
description: Create, select or revise a proportionate SDP plan and coordinate its KanBan, Scrum and Sprint references. Use for explicit planning or replanning; not for every implementation step or unrelated factual questions.
metadata:
  skillId: sdp-planning
  skillVersion: 1.0.0
  minimumToolkitVersion: 0.2.0
  capabilities: sdp.planning.v1
  compatibilityNotes: Typed-plan guidance with explicit adoption; management profile 0.2 for new machine-readable plan records.
---

# SDP Planning

Read the project's instructions and existing selected work, then the shared
[plan contract](references/plans.md). Use its types/lifecycle only when adopted;
in an older project, propose or describe a plan without silently migrating records.
Preserve the user's chosen deliverable, language/design boundaries and authorization.

Start from intent and current evidence. Reuse an adequate existing plan; revise
only what changed. Choose MaintenancePlan, RequirementPlan, ArchitecturePlan,
DesignPlan, ImplementationPlan or VerificationPlan by its outcome, not file location.
A plan is one work record; do not wrap an existing Maintenance plan in another plan.
The [template](references/plan-template.md) is a starting point, not a requirement
to create every section or a new file for each thought.

Define phases and milestones with observable acceptance. One of each is enough
for a small job. Select BranchPolicy and CommitPolicy explicitly: normally current
working branch with phase/milestone commits; phase branches for large work when
useful or already required. Keep protected-target rules and existing commitments.
A plan never grants execution, push, merge or release permission by itself.

Keep one authoritative plan and link source cards and any Scrum/Sprint records.
Planning normally stays in backlog/queued; activate execution cards when the
plan starts. A planning-only Study may complete with its explicit successor.
A Sprint groups one or more selected plans and/or direct cards; it is optional.
Use the project's management ledger for actual transitions, preserving historical
bytes. System-change evidence belongs in Traceability with management references.
Do not mark proposed tests passed or planning as implementation.

For material unresolved design choices, route to
[Architect](../sdp-architect/SKILL.md). For an authorized execution request,
hand the bounded plan to [Master](../sdp-master/SKILL.md) or the explicitly assigned
[Worker](../sdp-worker/SKILL.md), respecting host delegation rules. Do not stop
for approval when execution is already authorized. When only planning was asked
for, finish the reviewable plan and stop before implementation.
