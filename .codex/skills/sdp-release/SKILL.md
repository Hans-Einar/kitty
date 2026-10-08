---
name: sdp-release
description: Prepare or reconcile an explicitly scoped SDP release using exact-candidate evidence, compatibility
  and truthful publication records. Publication requires existing explicit authorization.
metadata:
  skillId: sdp-release
  skillVersion: 2.0.0
  minimumToolkitVersion: 0.2.0
  capabilities: sdp.release.prepare,sdp.release.gate,sdp.release.reconcile
  compatibilityNotes: Profile-aware workflow; native skill metadata. Supersedes the legacy procedure.
---

# SDP Release

Read the shared [Document workflow](../sdp/references/document-workflow.md)
for relevant SDP inputs, discovery handling and current-document updates.
Apply it within this role's write permissions; read-only assignments report
required updates instead of making them. Reuse an already loaded copy.

Use only for release work. Read the installed release lifecycle and its actual
gate commands, manifests, notes, selected contents, reviews and verification.
Do not substitute a generic gate for the project's release contract.

## Prepare

1. Identify the prior actual release, proposed version and included outcomes.
   Apply the versioning contract; use `sdp-versioning` when available. A merged
   branch is not proof that every included outcome is accepted.
2. Confirm the exact candidate, compatibility/migration obligations and required
   evidence. Check that review and verification still apply to that candidate.
3. Run the installed deterministic release gate. Report unavailable evidence
   without claiming success. Preserve immutable released history.
4. Prepare notes and release record using the existing schema. Keep publication
   identities null until real; distinguish prepared, approved and published.
5. Prepare concrete publication commands/artifacts. Execute only within explicit
   existing authorization; otherwise return the reviewable result for the final
   publication decision. Do not request the same permission repeatedly.

## Reconcile authorized publication

Verify the real annotated tag/candidate and GitHub Release or project's actual
publication surface. Record only observed identities and supported transitions.
If publication is partial or uncertain, inspect the remote state before retrying
and report the remaining gap. Do not backdate, pre-claim publication or expand
release contents during reconciliation.

Return the exact candidate, included scope, gate results, publication state and
remaining uncertainty. Release completion does not authorize physical deployment
or other separately restricted actions.
