# SDL source organization

This is the project convention for authored system models. Read this guide before
adding or moving `.design` or `.sdui` files. Source organization is separate from
language grammar, runtime deployment and generated documentation.

## One source tree, one shared process

Use `SDP/SDL/<System>/` for each software system described by this project.
Keep one shared KanBan, planning and Traceability area under SDP. A System is a
modeling boundary; a container is an application/service with a distinct runtime
responsibility. Shared libraries are not containers merely because they have
folders. The repository may be a monorepo or contain subrepos; physical Git
boundaries do not change this model ownership rule.

Use this shape as needed; do not create empty files or every optional directory:

```text
SDP/
  SDL/
    README.md
    AGENTS.md
    <System>/
      README.md
      System.design
      Features.design
      Ports.design
      State.design
      Containers/
        <Container>/
          README.md
          Domain.design
          Views.design
      Shared/
        README.md
        Libraries/<Library>/
        UI/
      Contracts/
      Scenarios/
      Governance/
      SDUI/
        <UIContainer>/
          MainPage.sdui
```

The names below are responsibilities, not required parser entry points:

| Location | Owns |
| --- | --- |
| System.design | System boundary, overview and container/channel topology |
| Features.design | System-wide features, functional intent and relationships |
| Ports.design | Public system boundary ports, not copies of every container port |
| State.design | System-wide modes/state; local state stays with its owner |
| Containers/<Container>/ | That container's responsibilities, local behavior, ports, state and detailed design; split by coherent concern |
| Shared/Libraries/ | Library/module designs reused by this system; no implied deployment container |
| Shared/UI/ | Common UI composition or design concepts, not a second owner of container screens |
| Contracts/ | Shared channel/data contracts with one authoritative declaration |
| Scenarios/ | Cross-container interactions, examples and verification scenarios |
| Governance/ | Model-level constraints and policy; management plans/history remain in their SDP areas |
| SDUI/<UIContainer>/ | Declarative screen prototypes belonging to that UI container |

Use additional small files such as Actors.design, UseCases.design or Data.design
when the model warrants them. Avoid a single file containing every abstraction
level. Do not split solely to meet a size limit or copy declarations into several
views. Container-local contracts/scenarios may stay with their container; put
cross-container definitions in the shared system areas and refer to them.

For example, BuckingUI and SimulatorUI are separate containers with separate
screen folders. Their container designs describe projections, user intents,
callbacks and renderer boundaries; `.sdui` files describe the screens. Concrete
React/Fyne/FOX code remains in the implementation source tree. Choosing this
folder layout does not select a renderer or claim working runtime bindings.

## Scope and reuse

Start shared material within its owning System. In Shared/README.md, distinguish
system-specific composition from candidates for broader reuse. Extract across
systems only after selecting an owner, dependency contract and migration; do not
create a global Shared dumping ground or duplicate a library in every System.
A collaborating system maintained elsewhere keeps its own SDP installation and
is referenced as external, without assuming a local checkout exists.

## System index and language support

Each System README records:

- purpose, boundary, owner and actual containers;
- authoritative source files and the responsibilities of shared definitions;
- language/profile and tool version used, supported validation commands and gaps;
- source-owned entry files, includes and contains references;
- how to reproduce selected outputs and where generated artifacts belong.

Folder placement does not create namespaces, imports, dependency ordering or
source-set support. Use only the constructs supported by the selected parser.
Do not invent a `system` declaration or `#include` preprocessor because this
layout uses those concepts. Experimental models must identify their profile and
unsupported constructs explicitly; inventory inspection is not successful parsing.
SDPTool discovers source files throughout SDP and returns navigation in memory.
No navigation.json or registration command is needed. An empty SDL directory
contains no models; adding sources makes them visible on the next discovery.
Viewers own filesystem watching and manual refresh.

## Authored source and documentation

The numbered folders hold process inputs, studies, decisions, plans and reader
views. Their numbers do not assign abstraction levels to model facts. Keep SDL
facts here in the source tree and link to them from phase documentation. Generated
viewpoints can be produced on demand or exported into clearly marked reports in
the numbered folders. They must record source identity/revision, tool version,
selection and generation command. Never hand-edit generated diagrams or maintain
an alternative prose model with conflicting facts.

Mandates, rationale, unresolved questions, plans and verification narratives may
remain authored Markdown. SDL does not replace those records or require every
sentence to be executable. SDUI prototypes and their previews do not prove domain
logic, live data, event handling or SDL integration.

## Migration and installation

Apply this convention to new model work. Existing source locations remain
canonical until an explicit migration updates source references, navigation,
links and verification together. Preserve identities, facts and immutable evidence;
separate semantic changes from moves. Do not migrate an unsupported model by
concatenating it into a pretend supported entry file.

This guide and AGENTS.md are project-owned installation seeds. Missing files are
initialized; upgrades preserve existing project documents. To adopt a newer guide
in an existing project, review its differences and reconcile local decisions.
Published release descriptors, not the current source checkout, determine what
`gh sdp install` or `gh sdp upgrade` installs.
