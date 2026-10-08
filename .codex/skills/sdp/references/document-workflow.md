# SDP document workflow

Profile-aware operating guidance. Current project
contracts control record names, IDs, schemas, ownership and required gates.
This guide introduces no new schema, mandatory document type or work hierarchy.

## Read the current authority

Start at project instructions and the actual declared process profile. Read the
installed Framework/manifest and current index when present; absence of an
installed manifest does not invalidate an explicitly adopted local profile.
Follow relevant intent/Feature links to Requirements, Architecture and Design,
including enclosing-system decisions and their reasons. Search historical
work and GitHub comments when current documents omit the reason or conflict;
do not read the entire archive on every task.

Separate current accepted decisions, proposed decisions, implementation
observations and superseded history. Neither a recent comment nor existing
code automatically overrides the current contract. Establish the source's
status and scope. If precedence remains unresolved and changes the solution,
identify that exact conflict before the dependent implementation.

## Shared-management profile

When adopted by the project, the five phases are Mandate, Requirements,
Architecture, Design and Implementation. Study belongs with the affected phase;
phase directories do not assign abstraction levels. Organize architecture by
Systems and actual containers; a shared library is not automatically a container.
Do not assume this local profile is already installed in every consuming project.

Use the shared KanBan board and existing cards for scope discoveries. A Scrum may
select Maintenance directly; Sprint membership is optional. CardState belongs in
one visible metadata row: queued stays in backlog; ready, in-progress and
concrete gate-review belong in active. A delivered card does not remain active
merely to point at later work. Maintain links and append the actual transition.

ProjectManagement/Ledger.ndjson records management lifecycles. Traceability records
system design/code changes and evidence, referring to management identities.
Pure planning/board changes do not get duplicate Traceability events. Keep current
explanations in their documents and revision history in Git. Write maintained
documentation in English; preserve frozen records and intentional localized UI.

For typed-plan projects, read [Planning](../../sdp-planning/SKILL.md) when creating
or revising a plan. Honor the selected plan's BranchPolicy and CommitPolicy;
retain explicit phase/milestone commitments for existing large plans. Update
its plan and evidence for each delivered milestone; phase push, PR, merge,
release and owner acceptance are separate operations with their own authority.

## Read and update by consequence

Use the project's corresponding paths, which may differ from these labels.
Read relevant rows before implementation; update them when their meaning
changes. A routine implementation detail need not change every lifecycle file.

| Changed meaning | Read / maintain | Required content |
|---|---|---|
| Product purpose, actors or scope | Mandate; existing Use Case/Feature records | Intended outcome, boundaries and actual decision source |
| Uncertain cause or integration impact | Study / Design Analysis | Evidence, alternatives, assumptions and disposition |
| Required observable behavior or constraint | Requirements | Testable obligation, source and affected acceptance scenarios |
| Responsibility, interface or shared invariant | Architecture / decision record | Ownership, reason, applicability, exceptions and supersession |
| Workflow, state transitions or interaction | Design | Current behavior, invalid/error/recovery cases and links to requirements |
| Implementation sequence or assignment | Implementation / current Slice or Fix | Bounded outcome, affected contracts and verification boundary |
| Evidence or review result | Verification / Review | Exact candidate, method, result, uncertainty and unresolved findings |
| Links or real work-state transition | Relations / CurrentIndex / Ledger | Schema-valid links and truthful transitions, preserving history |
| Published behavior or compatibility | Release records / release notes | Evidence-backed contents and actual publication state |

The ledger records an event; it does not replace the current requirement or
design explanation. An implementation report does not become the only place
where a durable behavioral rule can be found.

## Discoveries during implementation

Record the observation and its source before deciding what it means:

- **Existing obligation:** implementation does not satisfy an existing rule.
  Correct within scope and link the governing rule; do not rewrite it to match
  the implementation.
- **Derived obligation:** a necessary consequence of accepted requirements.
  Explain the derivation, record the testable consequence in the appropriate
  current document, and link its parent. Necessary means logically required,
  not merely a convenient design preference.
- **Product/design choice:** several valid behaviors or tradeoffs remain.
  Record options and obtain the disposition required by existing authority.
  Continue unrelated authorized work; do not invent owner acceptance.
- **Implementation detail:** a local choice preserves external behavior and
  governing contracts. Resolve it within scope; do not manufacture a Feature.

For a discovery outside an assigned Worker's write boundary, return the target
document, proposed change, reason and affected evidence to Master. Master owns
reconciliation before claiming completion, or records the explicitly deferred
gap without claiming the affected outcome is complete.

## Durable capability versus current work

When a project already has Features, link work to the existing capability and
its current behavioral authority. Describe its purpose separately from its
functions: observable actions, state transitions, inputs/outputs and failure
behavior. User-facing and internal system behavior are useful views of the
same contract; do not create separate UserFeature/SystemFeature entity types
unless the project has actually adopted them.

Where Features are not installed, use existing requirement/design sections and
normal links. Do not invent FEAT IDs, introduce FeatureBacklog schemas or remove
required Sprint/Iteration records as part of routine work. A backlog entry does
not activate work or authorize implementation.

For cross-layer work, verify the affected integrated user workflow in addition
to isolated component checks. A reviewed Slice is evidence about that Slice,
not automatic acceptance of the entire Feature or acceptance by the owner.

## Tier vocabulary

The historical Tier proposal means a coherent vertical capability across
horizontal layers. A layer owns a responsibility; a contract joins boundaries;
a Tier delivers working behavior through them. Sprint is execution grouping or
timebox; Iteration concerns a development cycle. They are different dimensions.
Use Tier only when the project adopts it and it adds meaning beyond Slice.
Do not rename existing work records to Tiers automatically.

## Closeout check

In the existing handoff, list changed governing documents and why they changed,
or briefly explain why existing contracts remain accurate. Check links and
installed schemas where applicable. Independent review checks that current
Requirements/Architecture/Design match the intended integrated behavior, not
only that a work report and ledger exist. Preserve previous verification when
a change makes it stale and identify the new evidence gap.
