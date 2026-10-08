---
name: sdp-traceability
description: Maintain SDP links between owner intent, current design decisions, work and evidence using installed
  records and schemas. Use for material decisions, state transitions and handoffs, not decorative bookkeeping.
metadata:
  skillId: sdp-traceability
  skillVersion: 2.0.0
  minimumToolkitVersion: 0.2.0
  capabilities: sdp.traceability.update,sdp.traceability.release-events
  compatibilityNotes: Profile-aware workflow; native skill metadata. Supersedes the legacy procedure.
---

# SDP Traceability

Read the shared [Document workflow](../sdp/references/document-workflow.md)
for relevant SDP inputs, discovery handling and current-document updates.
Apply it within this role's write permissions; read-only assignments report
required updates instead of making them. Reuse an already loaded copy.

Make the next agent able to find what governs a change and why. Read installed
ID/schema conventions and existing current pointers before creating records.

## Preserve decision meaning

In the existing Study/Architecture/Design or work record, maintain the decision's
scope, reason, source of authority, status, exceptions and material consequences.
Link rejected alternatives when they explain a likely future mistake. Link the
feature/component to shared enclosing decisions rather than copying their rules
into every assignment. Use the installed relation vocabulary; if no suitable
typed edge exists, use a normal document link and report the schema limitation.

Separate facts, assumptions, recommendations and accepted decisions. A discovered
obligation must cite its parent requirement and derivation. A new behavior choice
needs a decision source. Agent-written prose is not evidence of owner approval.
Preserve superseded decisions and explain their replacement; do not leave two
apparently current contradictory sources.

## Maintain work and evidence

Under the shared-management profile, card/Scrum/Sprint/Maintenance/Review/Refactor
transitions go only to ProjectManagement/Ledger.ndjson. System design/code and
verification go to Traceability, referencing management IDs/events. A completed
card is not proof of an implemented feature. Use current system-prefixed IDs;
retain historical IDs and report schema limitations without rewriting history.


1. Update CurrentIndex only for actual current work under the installed contract.
2. Update Relations with resolvable requirement, decision, assignment/Slice/Fix,
   review, verification and release links where the schema supports them.
3. Append real Ledger events. Never rewrite history to conceal corrections or
   invent event types, IDs, acceptance or publication facts.
4. Distinguish declared intent, observed Git/runtime state and evidence-qualified
   acceptance in existing records. A candidate change may stale verification;
   preserve the old result and mark the current gap explicitly.
5. Parse YAML/JSON/NDJSON as appropriate and validate against installed schemas.
   Check referenced paths/IDs, statuses and candidate identities agree.

Prefer one maintained reason with useful links over duplicated narratives.
Do not migrate a project to pilot schemas, rename historical work coordinates
or create a second system model as part of a routine update. Report changed
records, validated links, unresolved gaps and the real transition recorded.
