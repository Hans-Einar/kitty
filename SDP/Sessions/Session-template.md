# Session — <goal title>

## Session roadmap

Show current/latest recorded turn and next step, then a Gantt/timeline projection
and its step table. Each step lane has one planned task; activity segments and
events do not silently create additional planned tasks. Label its time basis:
measured time with turn boundaries, ordinal turns, or synthetic sequence only. The table is authoritative
for this manual format; generated event timelines are a separate future capability.

Sequence-only example: synthetic dates are placement slots, not an estimate.
Replace the labels and keep this projection aligned with the table.

```mermaid
gantt
    title Session route - sequence only
    dateFormat YYYY-MM-DD
    section Route
    NEXT S1 Plan :s1, 2000-01-01, 1d
    PLANNED S2 Work :s2, after s1, 1d
```

| State | Step | Work and linked plan milestone | Prerequisites | Authorization | Completion evidence / outcome |
| --- | --- | --- | --- | --- | --- |
| next | S1 | Prepare/select the bounded plan | Inputs available | Proposed, or actual instruction | Pending |
| planned | S2 | Execute the selected plan | S1 | Unselected until authorized | Pending |

Event-derived rendering is not supplied by this template. Mark event/card/document
activity and current/as-of position only from observed records. Do not fabricate
turn timestamps, elapsed durations or live state for a manual/static document.

Manual Session format 1; not a new typed-plan or ledger schema.

| Field | Value |
| --- | --- |
| Session reference | SESSION-<PROJECT>-NNNN (project-local document identity) |
| Status | proposed / active / paused / completed / canceled |
| Primary card | Link to the entry card |
| Snapshot date | Actual observation date |
| Current step | Stable step ID or none |
| Proposed next step | Stable ID and reason |
| Execution authority | Actual owner instruction / selected plan; unknown if absent |

## Goal

Describe the observable outcome, completion evidence, scope and explicit exclusions.
A changed goal needs its own recorded decision, not a silent rewrite.

## Affected cards

| Card | Role | Initial lifecycle / CardState | Planned final disposition | Current snapshot | Actual final disposition |
| --- | --- | --- | --- | --- | --- |
| Link | Primary / included / context-only | Observed, with date | Outcome sought | Dated projection | Pending until disposed |

## Plan register

| Local ref | Plan type and document | Document readiness | Canonical plan lifecycle | Depends on | Outcome / evidence |
| --- | --- | --- | --- | --- | --- |
| P1 | DesignPlan — not yet created; add real link when created | planned | Not registered | Input | Bounded outcome |

Do not create broken links or allocate authoritative plan IDs before registration.
Reuse valid existing plans. Readiness does not replace canonical lifecycle.

## Route changes and decisions

| Date / turn | Previous route | Change and reason | Authority | Affected steps/cards |
| --- | --- | --- | --- | --- |

Keep completed steps; canceled/superseded steps name reasons and successors.

## Turn journal

### T001 — <date and topic>

- Capture mode: exact observed messages / manually summarized; never imply both.
- Host thread/turn/item IDs: observed values, otherwise unknown.
- Request category, routine ID/version/run and provenance: known facts or unknown.
- Skills loaded: names/paths with agent-reported provenance, not proof of enforcement.
- Steps touched and outcome: include interrupted/failed/blocked status.
- Owner prompt(s): verbatim blockquotes or links to captured message artifacts.
- Assistant final response: exact captured text, or explicitly labeled work summary
  if the actual final response is unavailable to the writer.
- Decisions, evidence, remaining work and next-step reason.

Additional steering prompts in the same turn get separate message identities.
Add entries; correct past entries with a visible correction and source.

## Closeout

Actual goal outcome, final card dispositions, plan/step evidence and remaining
work with successor links. Closing the chat or reaching a turn boundary does not
close this Session. Include the next Session only if one is actually selected.
