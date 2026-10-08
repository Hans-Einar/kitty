---
name: sdp-vertical-refactor
description: Plan and perform an authorized SDP architecture migration through complete runnable workflows while
  preserving declared behavior and compatibility. Not for cosmetic file splitting or unrequested redesign.
metadata:
  skillId: sdp-vertical-refactor
  skillVersion: 2.0.0
  minimumToolkitVersion: 0.2.0
  capabilities: sdp.refactor.vertical,sdp.compatibility.preserve
  compatibilityNotes: Profile-aware workflow; native skill metadata. Supersedes the legacy procedure.
---

# SDP Vertical Refactor

Read the shared [Document workflow](../sdp/references/document-workflow.md)
for relevant SDP inputs, discovery handling and current-document updates.
Apply it within this role's write permissions; read-only assignments report
required updates instead of making them. Reuse an already loaded copy.

Apply within the assigned role: Architect plans, Master coordinates, Worker
implements and Reviewer independently reviews. This task skill does not grant
all roles or waive their boundaries.

1. Establish a baseline of user workflows, ownership, dependencies, accepted
   behavior and relevant runtime/rendered evidence. Separate existing defects
   from behavior to preserve.
2. Identify the structural problem and target ownership/contracts with measurable
   exit criteria. Use established system decisions; resolve material changes
   before migration rather than calling them implementation details.
3. Plan runnable vertical outcomes through the required layers. Avoid layer-only
   migrations that leave the actual user workflow unintegrated.
4. Move one complete workflow behind an explicit contract. Keep one state owner.
   Give each temporary adapter a consumer inventory and removal condition tied
   to real migration work.
5. Verify behavior, compatibility, error/recovery and application integration at
   each boundary. Use fresh review under the project's contract.
6. Remove old paths only after actual consumers have migrated and evidence
   supports removal. Record remaining debt and the next authorized boundary.

Do not silently add visual redesign, new features or a global framework to a
behavior-preserving migration. Smaller files and fewer lines are not completion
evidence. Select release versions by compatibility impact, not refactor size.
