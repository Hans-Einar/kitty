---
name: sdp-auditor
description: Perform a read-only SDP consistency audit of installation, skill availability, current decisions, traceability
  and evidence claims. Report gaps without applying migrations or repairs.
metadata:
  skillId: sdp-auditor
  skillVersion: 2.0.0
  minimumToolkitVersion: 0.2.0
  capabilities: sdp.audit.consistency,sdp.audit.release-state
  compatibilityNotes: Profile-aware workflow; native skill metadata. Supersedes the legacy procedure.
---

# SDP Auditor

Read the shared [Document workflow](../sdp/references/document-workflow.md)
for relevant SDP inputs, discovery handling and current-document updates.
Apply it within this role's write permissions; read-only assignments report
required updates instead of making them. Reuse an already loaded copy.

Inspect only the requested repository/environment boundary. Do not install,
migrate, rewrite historical records or repair product code during this audit.

## Installation and availability

Read Toolkit/project/installed manifests, AGENTS references and skill metadata.
Compare expected files and versions with actual contents and supported host
discovery locations. Check required skill name/description and missing references.
Distinguish file presence, native catalog discovery, explicit loading through
instructions and demonstrated use. A file on disk does not prove it is active;
absence from an initial catalog alone may need further investigation.

Record the inspected host/environment and limits. Do not claim all user machines,
containers or sessions share a local installation. Do not equate valid SDP-specific
metadata with valid host skill metadata.

## Project consistency

Check active work, decision applicability/supersession, current pointers,
relations, ledger, notes, reviews and evidence. Find missing authority, stale
candidate results, conflicting current decisions and claims unsupported by
actual commits, tests, tags or releases. Separate declared, observed and accepted
states. Preserve historical provenance rather than marking every old record as
an error merely because current conventions differ.

For each finding return severity, exact source, discrepancy, consequence and a
bounded repair recommendation. State what was not inspected. A clean structural
audit is not proof that the product meets user needs or that agents follow the
skills behaviorally.
