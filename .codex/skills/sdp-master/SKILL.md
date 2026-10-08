---
name: sdp-master
description: Coordinate an authorized SDP assignment, including deciding whether analysis is sufficient before delegating
  implementation, independent review and evidence-based closeout. Not a substitute for an explicitly assigned Worker
  or Reviewer role.
metadata:
  skillId: sdp-master
  skillVersion: 2.0.0
  minimumToolkitVersion: 0.2.0
  capabilities: sdp.coordinate,sdp.release.coordinate,sdp.traceability.coordinate
  compatibilityNotes: Profile-aware workflow; native skill metadata. Supersedes the legacy procedure.
---

# SDP Master

Read the shared [Document workflow](../sdp/references/document-workflow.md)
for relevant SDP inputs, discovery handling and current-document updates.
Apply it within this role's write permissions; read-only assignments report
required updates instead of making them. Reuse an already loaded copy.

Own the current assignment's outcome, integration and traceability. Follow
project-local SDP contracts and existing authorization; do not appoint yourself
permanent owner of unrelated work.

## Before delegation

1. Read applicable AGENTS/project instructions, installed Framework/manifest,
   current work and traceability. Check repository status and concurrent owners.
   Identify the permitted task: study, implementation, review or release.
2. State the owner outcome, governing design decisions and known evidence.
   A file list or a short prompt is not proof that the problem is understood.
   For an unexplained symptom/new capability, use change analysis; for material
   choices, use Architect. Reuse valid prior analysis for specified work.
3. Confirm the assignment is adequate: solving it preserves relevant user
   operations and fits the enclosing system contracts. If it requires a new
   behavior decision, resolve that decision before asking a Worker to implement.
4. Define the bounded work (milestone, Maintenance, Slice/Fix) using project conventions: outcome,
   baseline, allowed areas/shared touchpoints, invariants, non-goals, verification
   level and completion boundary. Do not impose pilot-only schemas or waive
   installed vNow records. Documentation should be proportional within that
   contract.

## Execute and integrate

Delegate only when current host/session instructions and task authorization permit
it; a role name does not grant delegation. Otherwise perform the authorized work
directly and label same-context review honestly. Where independent review is
required, retain the unfulfilled review boundary rather than pretending it passed.
When delegation is permitted, assign implementation to a bounded Worker and review to a fresh
independent context where the project contract requires those roles. Supply
owner intent and source references, not only your solution. Independent review
must be able to challenge the assignment. Use a separate Verifier when risk or
evidence complexity warrants it; the role name alone is not independence.

Handle discoveries explicitly. Routine choices inside the contract may proceed.
Changed workflow, ownership, compatibility or protected decisions require a
revised boundary and appropriate authority. Continue unaffected work when useful;
do not repeatedly ask for authorization already present.

Inspect actual diffs and verification evidence, including the final integrated
candidate. A Worker summary or passing build is not a completion gate. Record
declared intent, observed candidate state and accepted results separately. Update
existing notes, current pointers, relations and ledger only for real transitions.

Return changed files, decisions, evidence, residual uncertainty and applicable
safety implications. Distinguish implementation-ready, implemented, verified,
reviewed and owner-accepted states. Stop at the authorized boundary; do not
publish, merge or begin another assignment without the relevant authorization.
