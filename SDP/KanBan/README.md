# Project KanBan

Maintain one shared board. Register ideas and scope changes before implementation;
a card alone does not authorize execution. Primary types: Idea, Proposal,
Question, Study, Change, Bug, Decision, Ref, CodeReview and Refactor.

Use a visible Field/Value table with id, project, type, created, source and
exactly one CardState. Optional Systems, PlanId, SprintId and ScrumId retain ownership.
States: backlog or queued in backlog; ready, in-progress or gate-review in
active; onHold, completed, canceled, superseded and irrelevant in matching
folders. Queued cards explain predecessor and next work. Gate-review is for a
concrete owner review. Close delivered work and link the successor.

IDs never change or get reused. Keep working notes/evidence in cards and append
transitions to the ledger declared in board.json. Preserve merge/split sources
and record all successors and remaining scope. Do not duplicate primary cards.
All maintained prose is English. Do not copy another project's live records.

Normally a card produces a selected plan. Keep planning in backlog/queued; move
to active when the authorized plan executes. A planning-only Study can complete
with an explicit successor. Link one authoritative plan instead of copying phases.
The managed planning contract lives at SDP/Framework/planning/Plans.md.
