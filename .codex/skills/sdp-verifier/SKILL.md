---
name: sdp-verifier
description: Establish whether SDP test and inspection evidence proves the claimed outcome on the actual candidate,
  at the correct function, service, workflow, application or release level.
metadata:
  skillId: sdp-verifier
  skillVersion: 2.0.0
  minimumToolkitVersion: 0.2.0
  capabilities: sdp.verification.validate,sdp.release.evidence
  compatibilityNotes: Profile-aware workflow; native skill metadata. Supersedes the legacy procedure.
---

# SDP Verifier

Read the shared [Document workflow](../sdp/references/document-workflow.md)
for relevant SDP inputs, discovery handling and current-document updates.
Apply it within this role's write permissions; read-only assignments report
required updates instead of making them. Reuse an already loaded copy.

Read the owner outcome, applicable contracts and required verification matrix.
Choose evidence by the claim's level and consequence, not by which test is
easiest to run. Existing project safety and environment restrictions apply.

## Evidence contract

For each material obligation, identify the scenario, expected observable result,
candidate, environment and evidence source. Reuse current evidence when it still
applies; do not create tests that only mirror implementation wording.

- Function/unit evidence supports local logic.
- Service/integration evidence supports interfaces, persistence and recovery.
- Workflow/application evidence supports the user's complete operation.
- UI layout claims require the actual enclosing shell and relevant profiles,
  states and input methods; a standalone screenshot is supplementary.
- Release claims require the selected release candidate and installed gate.

Inspect commands and artifacts, and run the meaningful checks available in the
authorized environment. For missing dependencies or an unavailable environment,
record the gap and its consequence; use a justified alternative where possible.
Do not silently turn an unrun check into a pass.

## Candidate and result integrity

Record a commit for committed work, or HEAD plus a reproducible diff/artifact
identity for uncommitted work. Include relevant fixtures and environment facts.
When the candidate changes, identify which evidence remains applicable and which
must be repeated. Do not claim exact final-commit validation from an older run.

Classify results as passed, failed or not verified, with blocked reasons where
applicable. A required unverified item prevents an overall verified claim; it
is not itself proof of a product defect.

If a test expectation changes, verify the underlying behavior decision rather
than merely approving the new assertion. Report removed coverage and remaining
obligations. Do not edit product behavior or weaken acceptance criteria to
obtain a pass.

Return evidence per obligation and precise limits. Verification, independent
review, owner acceptance and publication are distinct states.
