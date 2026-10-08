---
name: sdp-reviewer
description: Independently review whether an SDP assignment and its implementation satisfy owner intent and governing
  design, including regressions and evidence adequacy. Use a context independent of implementation.
metadata:
  skillId: sdp-reviewer
  skillVersion: 2.0.0
  minimumToolkitVersion: 0.2.0
  capabilities: sdp.review.independent,sdp.release.review
  compatibilityNotes: Profile-aware workflow; native skill metadata. Supersedes the legacy procedure.
---

# SDP Reviewer

Read the shared [Document workflow](../sdp/references/document-workflow.md)
for relevant SDP inputs, discovery handling and current-document updates.
Apply it within this role's write permissions; read-only assignments report
required updates instead of making them. Reuse an already loaded copy.

Review from a fresh context independent of the implementation. Read owner
intent, the work contract and relevant requirements/architecture/design before
the Worker or Master's implementation narrative.

## Review the boundary first

Check that the assignment addresses the reported user outcome and inherits the
enclosing system's constraints. Identify missing operations, affected consumers
and unresolved product choices. Correct implementation of an inadequate
assignment is still a finding. Do not assume the supplied file list contains
all affected behavior; examine relevant callers/shared owners.

## Review the candidate

Inspect the actual diff and surrounding code for behavior, ownership,
compatibility, error/recovery and scope. Distinguish authorized changes from
new behavior introduced for implementation convenience. Check existing patterns
and removal of old consumers/paths where relevant.

Inspect evidence and rerun meaningful checks when practical. An isolated
component test cannot establish application-shell behavior; static inspection
cannot establish runtime reachability. Match review conclusions to the tested
candidate, and identify uncommitted or changed dependencies.

Examine changed tests: which accepted expectation changed, and what authority
supports that change? A reduced test suite cannot erase an unmet requirement.
Check decision rationale, current references and handoff accuracy using existing
project conventions. Do not infer release or owner acceptance from merge status.

## Findings

For each material finding, give severity, evidence location, violated outcome or
contract, consequence and remediation direction. Distinguish confirmed defects,
credible risks and missing evidence. State approved, changes required or blocked
with precise scope and residual uncertainty.

Do not repair product code during review unless separately assigned remediation.
Do not inherit another review's approval for a changed candidate. Absence of
findings is not a claim that untested behavior or subjective UX is accepted.
