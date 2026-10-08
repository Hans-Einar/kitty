---
name: sdp-change-analysis
description: Analyze an SDP user-reported symptom or new capability before choosing an implementation. Recover the
  affected workflow, governing decisions and change impact; reuse current analysis for already specified work.
metadata:
  skillId: sdp-change-analysis
  skillVersion: 1.0.0
  minimumToolkitVersion: 0.2.0
  capabilities: sdp.change.analyze
  compatibilityNotes: Initial adopted profile-aware role.
---

# SDP Change Analysis

Read the shared [Document workflow](../sdp/references/document-workflow.md)
for relevant SDP inputs, discovery handling and current-document updates.
Apply it within this role's write permissions; read-only assignments report
required updates instead of making them. Reuse an already loaded copy.

Turn a short owner prompt into an evidence-backed change boundary. Do not
implement product code or invent owner preferences during this pass.

## Recover the relevant context

1. State the user task and observed obstacle without selecting a solution.
   Distinguish an explicit requested design from a suggested explanation of a
   symptom. Preserve explicit owner constraints.
2. Read applicable project instructions and the current work record. Inspect
   the actual behavior and follow one complete affected workflow through state
   ownership, persistence, consumers and error/recovery paths as relevant.
3. Find governing requirements and design decisions in both the local feature
   and its enclosing system: shared shell, domain service, data format or other
   owner. Read their rationale, applicability, exceptions and replacement
   history. A rule need not mention the edited filename to govern it.
4. Compare declared design with observed code/runtime. Existing code may be an
   unaccepted addition or a regression. Historical prose may be superseded.
   Report conflicts and missing authority rather than silently selecting the
   source that supports the first proposed fix.

Stop expanding the investigation when the affected outcome, governing
boundaries, material consumers and evidence needed to distinguish plausible
causes are identified. If a specific missing fact could change the solution,
resolve it or state the bounded question; do not read the entire repository.

## Describe the change before prescribing it

Record, in an existing work/Study section where possible:

- user outcome and observed failure, with source locations or runtime evidence;
- current workflow and ownership, applicable decisions and why they apply;
- facts, assumptions and unresolved questions, explicitly distinguished;
- plausible causes and the observation that supports or rejects each;
- a proposed boundary, preserved behavior and relevant verification contexts.

Classify discoveries. A necessary consequence of an existing requirement is a
derived obligation: link the parent and explain the derivation. A new user
workflow or tradeoff is a product/design choice: present it for the appropriate
decision. A preferred implementation is neither a requirement nor authority.
Use existing project record types; do not introduce a schema to capture a
single discovery.

If a proposal makes another existing operation unreachable, changes where
state is owned, or changes the meaning of an action, return to the boundary
analysis. Do not repair the proposal by silently adding a second feature.
Present material alternatives and consequences to Architect/owner as needed.

## Handoff

Return the evidence map, remaining decision and readiness for implementation.
A concise note is enough for a known low-impact change. A still-current prior
analysis may be reused after checking its assumptions against the candidate.
Study findings do not by themselves authorize implementation or acceptance.
