# Working Sessions — manual format 1

A Session follows one goal across turns, cards, plans and replacement agents.
Use session-#NNNN--Topic.md, unique within this project, copied from
[Session-template.md](Session-template.md). Start from a primary card and link
back from every affected card. Small factual answers do not require a Session.
Read this guide when resuming a goal that spans turns or multiple plans.

## Authority and routine

The Session owns the goal, roadmap, route changes and turn summaries. Cards own
CardState; plans own phases, milestones, Git policy and acceptance. Session tables
are dated projections, not a new lifecycle authority. Use existing
[KanBan](../KanBan/README.md) and [project management and planning](../ProjectManagement/README.md).
Do not introduce a Session ledger kind or duplicate lifecycle ledger.

Before each turn, recover the goal/current step, check request scope and applicable
procedures, and explain a needed route change. During work, link new cards/plans
and record discoveries. At return, update the step states and evidence and state
what is next. A completed turn does not complete a step, card or goal.

## Roadmap first

Place the roadmap immediately after the title: a Gantt followed by a step table.
Show planned, next, on-going, waiting, blocked, completed, canceled or superseded
with text labels as well as colors. Normally one next step is selected; explicit
parallel work can have separate lanes. Keep dependencies, authority and evidence.
When timing is unknown, label synthetic Gantt dates **sequence only**. Do not use
axisFormat, todayMarker or init directives in the conservative XFMD example.
The manual Gantt and table must agree. Automatic event/turn timelines are not
implemented by this format.

## Cards, plans and history

Record card links with initial, planned-final, current and actual-final states.
Plans retain their detailed milestones; link instead of copying them. Document
readiness (planned/planning/ready/on-going/completed) is separate from canonical
plan lifecycle. Preserve completed steps and previous direction with dated reasons.
If a table is stale, reconcile against the actual card/plan; never change a card
only to make the projection agree.

## Turn capture

Record local turn identifiers, owner inputs, assistant outcome, decisions, relevant
procedure/skill use and evidence. Distinguish exact observed quotations from manual
summaries. Unknown host IDs, attachments and timing remain unknown. Do not invent
an eventual final response before it has been sent. Record visible messages only,
never private reasoning or credentials. No automatic app-server transcript capture,
MCP observer or enforced routine engine is supplied by this format.

## Closeout and upgrades

Close only when goal evidence exists and every included card/plan/step has an
explicit disposition. Remaining work names a successor; do not claim it completed.
A replacement thread continues the same durable Session. This template and guide
initialize only when missing. Upgrades preserve project-authored Sessions, guides
and templates; no SDP repository conversations or Session 0001 are installed.
The receipt advertises sdp.sessions.manual.v1 when provided by the release.
