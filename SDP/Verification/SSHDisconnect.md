# SSH disconnect terminal-state analysis

Date: 2026-11-11. Owner requested root-cause investigation and an upstream report.
Applied the installed SDP Change Analysis skill. This assignment changes no
product code, shell aliases, user terminal state or SSH configuration.

## Finding

Abrupt termination of plain SSH preserves terminal-emulator protocol state set
by the remote program. The kernel tty attributes are restored, but DEC modes
1003/1006 remain enabled and a pushed keyboard flag remains active. Real mouse
motion then generates SGR coordinate sequences, while ordinary keys can become
CSI-u sequences. This matches the observed garbage after a lost connection.
The exact mode-setting remote application in the owner's incident is unknown.

Pristine upstream v0.50.0 reproduces the same result as workstation fork
5f5cd0c7b. Normal remote cleanup clears the modes. Kitty's SSH kitten restores
them even when the connection drops. Hard terminal reset also recovers them.
This establishes a general terminal-state leak across a crashed transport,
not a regression attributable to the fork or to the 0.50.0 upgrade.

## Evidence and method

[Machine-readable results](evidence/SSHDisconnect/results.json) contain before,
after and reset protocol-query responses as hex and escaped text. A disposable
loopback Paramiko SSH server executes a fixed Python program in an isolated HOME;
OpenSSH 9.9p1 is the real client. The server closes the transport after receiving
confirmation that the mode-setting program ran. The post-exit client queries
DECRQM 1003/1006 and keyboard flags, captures XTest-generated mouse/key input,
and compares termios attributes before/after. Kitty runs in isolated Xvfb with
no user config and shell integration disabled. Local sockets are only used for
querying the test instance and invoking its reset action. No production SSH
connection or user terminal is touched.

| Build/client | Exit | Mouse/SGR after | Keyboard flags | Input |
| --- | --- | --- | --- | --- |
| Fork, plain SSH, disconnect | 255 | on/on | 8 | mouse coordinates; CSI-u a |
| Upstream 0.50.0, plain SSH, disconnect | 255 | on/on | 8 | same |
| Upstream 0.50.0, plain SSH, normal cleanup | 0 | off/off | 0 | a only |
| Upstream 0.50.0, kitten ssh, disconnect | 255 | off/off | 0 | a only |

All four cases restored termios; reset returned all queried modes to baseline.
Upstream tracked sources were unchanged at bb1aca6f279f1a5cfa3edd765a71650fe91b6472.
The application fixture intentionally selects keyboard flag 8; this does not
claim that the original incident used exactly that flag.

## Ownership and next steps

kitty/mouse.c encodes motion with no button as 35 and emits SGR coordinates.
kitty/screen.c owns the persistent mouse/keyboard state. Plain SSH restoration
of termios does not send the escape sequences needed to reset those states.
kittens/ssh/main.go saves private modes and pushes keyboard flags before launching
SSH, then restores/pops during deferred cleanup. The comparison confirms that
existing recovery path for the tested scenario. Arbitrary nested stacks or a
hard kill of the SSH kitten itself were not tested.

The upstream maintainer has already discussed this in issue 7603 and discussion
4038. Report the measured reproduction as an issue comment rather than create a
duplicate core bug. Recommend using `kitten ssh` for interactive sessions; keep
Ctrl+Shift+Delete available for recovery. No automatic alias replacement is made.
A product fix is not selected by this analysis.

## Upstream report

[Submitted text](evidence/SSHDisconnect/upstream-comment.md).
Published as [upstream issue 7603 comment](https://github.com/kovidgoyal/kitty/issues/7603#issuecomment-6791233430) by Hans-Einar.
The posted body was fetched back and verified against the prepared report.
The connector lacked upstream write access; publication used the authenticated
local GitHub CLI. No duplicate issue was created.
