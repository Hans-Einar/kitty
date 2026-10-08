# Project SDP area

This project uses sdp-five-phase/0.1 with shared project management.
Read installed release/profile facts in Framework/installed-toolkit.manifest.yaml;
project identity and release state belong in SDP-project.manifest.yaml.

Start with [the document guide](SDP-DOCUMENT-GUIDE.md). Author system models in
[SDL](SDL/README.md), grouped by System and actual container responsibility.
Numbered folders express process responsibilities, not fixed abstraction levels
or required source locations. Keep studies with the phase they inform. Maintain
all documentation in English.

| Area | Purpose |
| --- | --- |
| [01--Mandate](01--Mandate/README.md) | Owner intent, boundaries and stakeholders |
| [02--Requirements](02--Requirements/README.md) | Needs, actors, use cases and obligations |
| [03--Architecture](03--Architecture/README.md) | System/container boundaries and connections |
| [04--Design](04--Design/README.md) | Detailed contracts, behavior and design rationale |
| [05--Implementation](05--Implementation/README.md) | Selected delivery plans and implementation evidence pointers |
| [SDL](SDL/README.md) | Authored SDL models and system-owned SDUI screens |
| [KanBan](KanBan/README.md) | Ideas, proposals and active work |
| [ProjectManagement](ProjectManagement/README.md) | Management history; cards, Scrum, Sprints and plans |
| [Traceability](Traceability/README.md) | Design/code relationships and verification evidence |

A card or plan being completed does not prove a system feature implemented.
Prefix new traceability IDs with their owning System. Use the actual installed
skills and selected plan; no mandatory Sprint or new wrapper card for every task.

For work spanning turns/plans, use [Sessions](Sessions/README.md): recover the
goal, keep the roadmap first, link plans/cards, and record honest turn outcomes.
Sessions are manual project documents; lifecycle authority remains in cards/plans.
