# Kitty resume — selected manual-save behavior

Source: [KB-KITTY-001](../KanBan/completed/%23001--Proposal--Kitty-resume.md), owner T002.
These obligations replace the T001 automatic-snapshot proposal.

| ID | Obligation | Acceptance |
| --- | --- | --- |
| KITTY-REQ-001 | `kitty resume` presents a searchable keyboard picker. | Select with arrows/Enter; Escape cancels without launching. |
| KITTY-REQ-002 | Restore tabs, panes and layouts using native session semantics. | Native save/load round trip with two tabs and three panes. |
| KITTY-REQ-003 | Retain each pane's cwd and saved foreground invocation. | Three different directories, including one containing a space; explicit resume argument retained. |
| KITTY-REQ-008 | Report unreadable/invalid files without launching; preserve saved files. | Validation error stays in picker; damaged catalog does not overwrite data. |
| KITTY-REQ-010 | Retain link/navigation behavior and the wmkitty profile. | Existing screen/layout tests pass; wrapper preserves xterm.conf/name; Alt mappings unchanged. |
| KITTY-REQ-011 | F1 manually invokes native save with foreground and relocatable flags. | Installed mapping parses; native save registers its path only after success. |
| KITTY-REQ-012 | Discover saved files without monitoring commands. | Remember successful manual-save paths and scan configured session directories; duplicate/missing paths handled. |

T002 dispositions: REQ-004 custom desktop geometry, REQ-005 autosave, REQ-006
inferred Codex identity and REQ-009 independent automatic window records are
withdrawn. REQ-007 mode/identity specialization is replaced by the owner's
explicit Codex/yolo resume invocation under REQ-003. REQ-002 promises native
serialization semantics, not extra ordering or window-manager behavior.

The owner chooses what to save and prepares application resume arguments.
Application memory, unsaved buffers and background jobs are not captured.
