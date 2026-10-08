# <ID> — <outcome>

| Field | Value |
| --- | --- |
| id | <existing MAINT identity or new PLAN identity> |
| project | <project namespace> |
| state | planned |
| PlanType | <one of the six supported plan types> |
| BranchPolicy | current |
| CommitPolicy | phase |
| source | <owner request, card or Scrum reference> |

## Outcome and authority

State what is to be achieved, who selected it, and whether execution is authorized.

## Scope and baseline

Relevant current evidence, boundaries, non-goals, dependencies and decisions.

## Git policy

Name the working branch strategy and commit boundaries. State actual publication
permissions. Use phase branches/milestone commits only when selected for this plan.

## Phases and milestones

| Phase | Milestone | Acceptance | State |
| --- | --- | --- | --- |
| <phase> | <milestone> | <observable result> | Planned |

## Verification and outcome

Candidate, checks, evidence, limitations and remaining work. Update with actual
results; a proposed verification command is not a passed test.
