# SDP Framework

Framework-Version: 1.0.0
AGENTS-Contract-Version: 2.0.0

This directory is Toolkit-managed. A conforming installer refreshes only the
selected release inventory and backs up changed managed files according to
the installation protocol. Current releases use signed Go descriptors. Historical install-v1 records do
not select payloads or provide an alternate execution path.

Project-specific Mandate, Study, Requirements, Architecture, Design,
Implementation, Sprints, Refactors, Fixes, review, verification, release notes
and Traceability remain project-owned. Their neutral creation sources live under
`Template/`, not in this managed payload and not in the Toolkit
repository's live root records.

Canonical installed facts are generated in
`Framework/installed-toolkit.manifest.yaml`. Project release and development
state lives in `SDP-project.manifest.yaml`. In an extracted source archive
without trustworthy Git metadata, `sourceCommit: null` is correct. In a dirty
checkout, a non-null value is only the available `HEAD` baseline, not an
attestation that installed bytes equal that commit. Dynamic Git/build facts are
generated separately, not maintained by hand.

Core rules:

- repository documents are authoritative;
- design horizontally and implement vertically;
- use SemVer only for public releases and Toolkit releases;
- follow the installed workflow and selected plan, with proportionate work units;
- current shared management supports optional Sprints and direct typed plans;
- retain Slice/Fix/Iteration rules where the project still uses a legacy profile;
- Workers implement bounded work; Reviewers use fresh independent context;
- completion requires real verification and current traceability;
- tag and GitHub Release events may be recorded only after they exist;
- publication requires explicit human authorization;
- stop at the work boundary.

For the current five-phase profile, read ../README.md and ../SDP-DOCUMENT-GUIDE.md.
Model source guidance is in ../SDL/README.md when installed. Templates are
project-owned initial content; upgrades do not overwrite their local revisions.
