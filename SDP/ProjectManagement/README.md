# Shared project management

Profile sdp-project-management/0.2. Ledger.ndjson is the sole writable lifecycle
history. Keep documents current; Git stores revisions; the ledger stores actual
transitions. Never rewrite historical bytes or infer product completion from a
management state. Event envelope 1.0 applies; payload 0.1 history remains valid. New typed plans
and Sprint plan membership use management payload 0.2.

Management IDs are MAINT-<PROJECT>-<number>, SCRUM-<PROJECT>-<number>,
SPR-<PROJECT>-<number>, REVIEW-<PROJECT>-<number> and REFACTOR-<PROJECT>-<number>.
Use x-management:created/started/updated/completed/canceled. A created item is
planned or active; started changes planned to active; completed requires real
completion. Chain previousEventId with exact from/to states and SDP-relative
document paths. Installation events allocate EVT-PM-<PROJECT>-<number> from target history.
The distributed payload schema generalizes the project namespace; the Toolkit
repository retains its local SDP-specific validation policy.

Cards retain KB-<PROJECT>-<number>, x-kanban events and payload 0.1/0.2.
Card paths are KanBan-relative. Optional SprintId/ScrumId metadata groups work.
Never duplicate lifecycle events in Traceability.

Typed plans use one work record: Maintenance with MaintenancePlan, or Plan with
a supported PlanType and PLAN-<PROJECT>-<number> identity. Each plan declares
BranchPolicy and CommitPolicy. Sprint payload 0.2 separates direct card members
from plans; visible metadata must agree with both snapshots. Read managed
SDP/Framework/planning/Plans.md and Plan-template.md for the complete contract.
Historical project-owned notes may describe older rules; never rewrite history.
