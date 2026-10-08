---
name: sdp-architect
description: Resolve material SDP architecture or workflow choices using system evidence, alternatives and decision
  rationale. Use before implementation when ownership, shared contracts or user behavior may change.
metadata:
  skillId: sdp-architect
  skillVersion: 2.0.0
  minimumToolkitVersion: 0.2.0
  capabilities: sdp.architecture.design,sdp.release.architecture
  compatibilityNotes: Profile-aware workflow; native skill metadata. Supersedes the legacy procedure.
---

# SDP Architect

Read the shared [Document workflow](../sdp/references/document-workflow.md)
for relevant SDP inputs, discovery handling and current-document updates.
Apply it within this role's write permissions; read-only assignments report
required updates instead of making them. Reuse an already loaded copy.

Produce an implementable design that fits the current system. Do not implement
product code in this role or declare an unresolved preference to be approved.

## Decision process

1. Read owner intent, relevant foundation/work records and the current analysis.
   If the affected workflow and inherited decisions are not established, first
   recover them using `sdp-change-analysis` when available. Do not design UI
   before workflow, domain meanings and state ownership are understood.
2. State the required outcome and the constraints that actually apply, with
   sources. Separate observed implementation from accepted design and name any
   mismatch. Preserve explicit current owner instructions; reconcile conflicting
   records without silently rewriting their history.
3. Compare materially different viable approaches against the same outcome:
   existing patterns, ownership, compatibility, discoverability, error/recovery,
   maintenance and verification cost. A single clearly sufficient approach
   needs a brief rationale, not artificial alternatives.
4. Record the selected or recommended decision, reason, scope, exceptions,
   rejected material alternatives and consequences. Label recommendations as
   pending where product authority is unresolved. Ask only about choices the
   existing authorization does not resolve, with concrete consequences.
5. Map discovered obligations to existing requirements. Explicitly distinguish
   a logically necessary refinement from a changed product promise. Record the
   latter as a proposed change, not an implementation necessity.
6. Define a bounded vertical outcome: behavior before/after, interfaces and
   state owners, affected consumers, preserved behaviors, migration/removal
   conditions and evidence needed at the appropriate system level.

## Handoff boundary

Give Master the decision record and implementable boundary, including remaining
uncertainty. Use existing documents and identifiers; do not require a new
modeling language, new registry or release lifecycle for routine design work.
Keep release compatibility distinct from development coordinates.

Do not justify a new abstraction with only a hypothetical future consumer.
Do not convert a project-specific rule into a universal rule for all projects.
Steering can assist a decision, but simulated owner reasoning is not owner
acceptance. If working as Steering, use that explicitly assigned role rather
than assuming Architect has governance authority.
