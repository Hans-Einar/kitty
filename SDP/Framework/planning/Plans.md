# Typed plans — planning contract 1.0

Adopted by owner decision KB-SDP-029, 2026-09-25. This contract applies when the
project selects typed planning; installed management profile 0.2 supports its
machine-readable records. Do not silently migrate an older project.

## One plan, one work record

A plan states the intended outcome and the bounded route to it. It remains the
authoritative execution record as progress and evidence are added. Cards capture
intent and selection; Scrum records consolidation/decisions; Sprint groups work.
Link the plan from those records instead of copying its phases into each one.
A plan may originate from a card, multiple cards, Scrum or a direct owner request.
None requires a wrapper card or Sprint. Registration/planning is not execution
or publication authorization.

| PlanType | Outcome | Usual home below SDP |
| --- | --- | --- |
| MaintenancePlan | Process, documentation, tooling or repository upkeep | Maintenance/<work>/Plan.md |
| RequirementPlan | Establish or refine testable needs, actors and use cases | 02--Requirements/<scope>/Plan.md |
| ArchitecturePlan | System/container responsibilities and contracts | 03--Architecture/<scope>/Plan.md |
| DesignPlan | Detailed behavior and design within selected boundaries | 04--Design/<system>/<container-or-scope>/Plan.md |
| ImplementationPlan | Deliver selected design through runnable increments | 05--Implementation/<scope>/Plan.md |
| VerificationPlan | Establish evidence for defined claims on a candidate | Verification/<scope>/Plan.md |

These are types of work, not mandatory sequential stages or new SDL keywords.
Existing well-formed documents can serve as plans without renaming or copying.
Phase directories organize material; they do not assign abstraction levels.
Maintenance uses its existing MAINT-<PROJECT>-<number> identity and management
kind Maintenance. Other new standalone plans use PLAN-<PROJECT>-<number> and kind
Plan. CodeReview/Refactor records may link a plan; they need no duplicate plan
when their existing bounded record is sufficient. Historical records keep their
original types and meaning. Do not retrofit PlanType into old event bytes.

## Minimum useful content

Use one visible metadata table: id, project, state and PlanType. Source cards,
ScrumId, SprintId and Systems are optional relevant links, not compulsory layers.
State is planned, active, completed or canceled, following management history.
A typed plan also declares BranchPolicy (current or phase) and CommitPolicy
(phase or milestone). Explain the selected branch and publication authority in
its Git policy section. A reference to a concrete existing policy may supply
the explanation; the selected metadata must still be unambiguous.

The body contains outcome/authority, scope/non-goals, relevant baseline and
choices, phases with milestone acceptance, dependencies, verification/evidence
and remaining work. One phase and one milestone are enough for a small task.
Do not create empty study/design/review documents to fill a template. Changes
in scope need a reason and updated acceptance, not a restart of the hierarchy.

## Card and execution lifecycle

The normal card outcome is a selected plan. While only planning it, keep a new
card in backlog (queued if selected next) and record planning progress in its
worklog and reviewed events. When the authorized plan starts execution, move
linked execution cards to active: ready while awaiting work, in-progress while
working, gate-review only for a concrete owner review. Keep one CardState row.
No new planning state or queue directory is required. Planning alone must not
make a feature/implementation card completed.

A Study/Question whose bounded deliverable is only a plan or answer may close
with that outcome and an explicit successor. The separate plan then owns execution;
do not reopen a completed Study merely to track its successor. Historical active
planning cards retain their meaning. Further changes to a completed plan select
new work and link the predecessor; never rewrite prior closure evidence.

## Sprint grouping and ledger

Use the existing ProjectManagement/Ledger.ndjson; no plan-only ledger. Payload
0.2 adds Plan kind, typed plan metadata and a Sprint plans snapshot. Read old
payload 0.1 unchanged. A Sprint can group one or more plans without direct cards;
legacy/direct card members remain supported. Never put plan IDs in the legacy
members array. Plans is a separate visible Sprint metadata row, matching its
plans ID array. Each selected plan carries the corresponding SprintId.

On sprint start, begin its selected planned plans and activate their linked
execution cards; already active work keeps its state. Completed predecessor
cards are references, not execution members. A sprint can list direct cards too,
but a card is selected for execution once, not duplicated as work. Every selected
member needs an explicit disposition at closure. Before closing a Sprint, its
remaining plans must be completed/canceled. Remove unfinished or deferred plans
through an explicit membership-update event with reasons and reciprocal SprintId
updates; keep predecessor links in the documents/history. If every member is
deferred, that explicit removal may leave an empty Sprint for closure; creation
and start still require selected work. Do not falsely complete
or cancel work to close a Sprint. A deferred active plan may stay active with a
documented pause; card onHold describes that pause without a new plan state.

Management transitions record plan selection/start/progress/closure; system
design/code verification goes to Traceability with management references. Pure
planning or bookkeeping does not produce system implementation evidence.

## Scaled Git policy

For small plans, use the current appropriate working branch and commit per phase
or meaningful milestone. Never develop directly on a protected target branch;
create one working branch if needed, or to preserve a completed delivery branch.
For large implementation plans, phase branches stacked on preceding deliveries
and milestone commits remain useful. State this explicitly in that plan.

An adopted plan's Git policy overrides a general default for its selected scope;
owner instructions and protected-target rules still apply. Do not retroactively
change an existing plan's promised branch history. Push/PR/merge/release are
separate permissions: recording a Git policy grants none of them by itself.

## Compatibility and capability

The five-phase layout remains sdp-five-phase/0.1; management profile becomes
sdp-project-management/0.2 and capability sdp.planning.v1 advertises typed plans.
Consumers must understand 0.2 before writing it. Old 0.1 records remain valid;
no bulk conversion is required. The new installer supports explicit 0.1 → 0.2
adoption, preserving history and project documents. Old readers reject unsupported
profile facts. Managed planning guidance is authoritative for the new capability;
retained project-owned README text can describe an older baseline and must not be
automatically overwritten to conceal that difference.
