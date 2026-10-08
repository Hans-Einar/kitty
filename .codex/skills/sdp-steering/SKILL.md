---
name: sdp-steering
description: Assist an explicitly assigned SDP Steering or project-owner decision by assessing evidence, framing
  unresolved choices and recording actual dispositions. Does not authorize the agent to impersonate owner approval.
metadata:
  skillId: sdp-steering
  skillVersion: 1.0.0
  minimumToolkitVersion: 0.2.0
  capabilities: sdp.steering.assist
  compatibilityNotes: Initial adopted profile-aware role.
---

# SDP Steering

Read the shared [Document workflow](../sdp/references/document-workflow.md)
for relevant SDP inputs, discovery handling and current-document updates.
Apply it within this role's write permissions; read-only assignments report
required updates instead of making them. Reuse an already loaded copy.

Assist product direction and acceptance for the assigned boundary. Distinguish
your recommendation from the owner's decision and from independently verified
implementation. Existing authorization remains valid; do not ask again merely
because work reaches a named gate.

## Prepare a decision

Read the short owner request, current work and relevant governing decisions.
Require the responsible agent to recover system context rather than asking the
owner to enumerate every invariant. Inspect actual repository/runtime evidence
before assessing a Master's completion claim.

Present only unresolved material choices: the user outcome, options, consequences,
recommendation and what existing authority does not settle. Technical choices
within the accepted boundary remain with the responsible role. A role-playing
exercise may explore user needs but is not owner acceptance.

## Preserve the interaction

Use the existing project Steering record convention, including an existing Scrum, work card or Maintenance decision section when
appropriate; create a separate record only when assigned:

1. Preserve the exact material assignment prompt and its source/time.
2. Preserve the Master's complete received response separately from assessment.
3. Inspect the referenced diff, candidate, checks and review; then add an assessment
   with evidence and unresolved issues. Pending sections are truthful states.
4. Record the actual authorized disposition and exact candidate/scope when given.
   Label agent recommendations as recommendations, never human approval.
5. Add dated corrections without silently replacing prior prompts or responses.
   Redact secrets/unnecessary private content before repository recording and
   identify that redaction occurred; do not claim a redacted record is verbatim.

Link material interactions to existing work/decision records. Use only supported
Ledger events; absence of an event type does not authorize a new schema. Do not
send external messages, publish or extend the assignment merely by holding this
role. Return the decision needed or actual disposition and the next bounded step.
