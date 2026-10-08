# Document and source guide

## Where work belongs

| Material | Home | Authority |
| --- | --- | --- |
| Owner mandate, stakeholders, constraints | 01--Mandate | Authored owner input and clarified decisions |
| Requirements and their rationale | 02--Requirements | Authored needs; modeled facts reference SDL sources |
| Architecture overview and tradeoffs | 03--Architecture | Decisions plus generated or linked model views |
| Detailed design and rationale | 04--Design | Decisions and contract explanations linked to source |
| Implementation plans | 05--Implementation | Selected phases, milestones, Git policy and acceptance |
| System models and declarative screens | SDL/<System> | Authored .design and .sdui files; see SDL/README.md |
| Study | The phase it informs | Findings, alternatives, uncertainty and selected outcome |
| New idea or scope change | KanBan | Proposal and disposition; not implementation authorization |
| Scrum and Sprint | Agents/Scrum and Sprints | Optional review/grouping, not duplicate work copies |
| Maintenance, review and refactor | Maintenance, CodeReview, Refactors | Bounded plan/work records and evidence pointers |
| Technical evidence and verification | Verification and Traceability | Actual candidate, commands, results and limits |
| Lifecycle events | ProjectManagement/Ledger.ndjson | Append-only management history |

Use the [source convention](SDL/README.md) when choosing model boundaries and file
names. A requirements, architecture or design viewpoint may read the same model;
do not duplicate declarations into numbered folders. The phase containing a report
does not force every fact in it to a single abstraction level.

## Keep documentation useful

Use small concern-oriented documents with a clear authority and links, rather than
parallel descriptions of the same model. Phase READMEs act as navigation pages.
Do not create placeholder documents simply to fill the tree. For multiple Systems,
phase reports may use System subfolders; their source still has one canonical home.

Generated Markdown/diagrams are derived views. Identify the source, tool version,
selection and command; rebuild instead of editing them. On-demand views need not
be committed. Stable exported views can live in a clearly marked Generated/
subfolder of the relevant phase. Preserve dated evidence instead of relabeling it
as current. Decisions, studies, owner intent and plans remain authored prose where
SDL cannot or should not express them.

## Agent entry and installation

Read repository instructions, this area README, the affected System README and
applicable SDL/AGENTS.md. Use installed SDP skills for the selected role. Do not
infer language support from a file extension or a successful folder migration.

Templates initialize missing project-owned files. Upgrades preserve local prose;
a newer template is not an automatic rewrite of existing documentation. Managed
Framework/skills and generated installation receipts have different ownership.
Consult installed facts before migration; preserve project history and decisions.

For work spanning turns/plans, use [Sessions](Sessions/README.md): recover the
goal, keep the roadmap first, link plans/cards, and record honest turn outcomes.
Sessions are manual project documents; lifecycle authority remains in cards/plans.
