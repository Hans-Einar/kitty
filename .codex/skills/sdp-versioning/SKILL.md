---
name: sdp-versioning
description: Select an SDP release version from public compatibility impact and maintain development identity separately.
  Use for version decisions, not as mandatory ceremony for every code edit.
metadata:
  skillId: sdp-versioning
  skillVersion: 2.0.0
  minimumToolkitVersion: 0.2.0
  capabilities: sdp.versioning.select,sdp.versioning.development-identity,sdp.versioning.validate
  compatibilityNotes: Profile-aware workflow; native skill metadata. Supersedes the legacy procedure.
---

# SDP Versioning

Read the shared [Document workflow](../sdp/references/document-workflow.md)
for relevant SDP inputs, discovery handling and current-document updates.
Apply it within this role's write permissions; read-only assignments report
required updates instead of making them. Reuse an already loaded copy.

Read the installed version contract, latest actual release and intended public
compatibility boundary. Use SemVer under that contract, including its pre-1.0
and prerelease policy where applicable.

1. Identify actual changes to public behavior, API, data, installation or other
   supported compatibility promises. Do not use file count or effort as the
   reason for MAJOR/MINOR/PATCH.
2. Select the target and explain the compatibility rationale. Flag uncertainty
   rather than pretending a new workflow is a backward-compatible fix.
3. Keep Sprint/Refactor, Iteration, Slice/Fix, revision and Git identity separate
   from the release number. Preserve existing IDs and installed cardinalities.
4. Distinguish correction of an unaccepted candidate from changed outcome/scope
   and from correction of already accepted behavior. Use the local work contract
   to select revision or new work; do not rewrite accepted history.
5. Validate manifest/note/display consistency and record the decision using
   existing traceability. Do not present an unreleased build as an official
   release or claim a tag that does not exist.

This skill selects and checks version identity. It does not publish, impose
pilot ID rules or infer a product release from a proposal directory's name.
