# SDL source authoring instructions

Read README.md in this directory and the affected System's README before editing
models. Keep system sources under their owning System, container details under
Containers, and declarative screens under SDUI/<UIContainer>. Shared libraries
are not automatically containers. Do not create a separate SDP process per System.

Maintain one authoritative definition per concern. Use the selected language
profile and its supported input mechanism; folders do not implement imports or
namespaces. Mark unsupported experimental syntax and do not report an inventory
check as parser validation. Keep generated outputs distinct from authored source.

For moves, update source references and reproducible verification together.
Navigation is rediscovered from sources; do not maintain a navigation.json registry.
Existing model homes remain authoritative until an explicitly selected migration.
Document language is English. Follow root instructions and the installed SDP
skills for planning, implementation and evidence; this file adds source-placement
rules, not a separate workflow or publication authorization.
