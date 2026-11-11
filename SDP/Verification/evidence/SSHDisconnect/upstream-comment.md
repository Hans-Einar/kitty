Adding a measured 0.50.0 reproduction to this existing issue, including the mouse-reporting symptom from discussion #4038, rather than opening a duplicate.

**Environment:** unmodified upstream v0.50.0 (`bb1aca6f279f1a5cfa3edd765a71650fe91b6472`), Linux x86_64 / AlmaLinux 10.2, X11/Xvfb, OpenSSH_9.9p1. Kitty was started with `--config NONE` and shell integration disabled. The only other overrides enabled X11 and a local remote-control socket for the isolated test. The same result occurs with our workstation fork; the upstream reproduction contains none of our patches.

**Controlled reproduction:** a disposable loopback SSH server executes a minimal remote Python program that enables all-motion mouse reporting (`CSI ? 1003 h`), SGR mouse encoding (`CSI ? 1006 h`), and pushes keyboard flag 8 (`CSI > 8 u`). After those bytes reach Kitty, the test closes the SSH transport without a normal channel exit. The local SSH process exits 255. The server uses Paramiko and an isolated remote HOME; no tmux or remote interactive-shell configuration is involved.

The remote program is equivalent to:

```python
import sys, time
sys.stdout.write("\x1b[?1003h\x1b[?1006h\x1b[>8u")
sys.stdout.flush()
try:
    time.sleep(60)  # break the SSH transport while this is running
finally:
    sys.stdout.write("\x1b[?1003l\x1b[?1006l\x1b[<u")
    sys.stdout.flush()
```

Run it through `ssh -tt HOST python3 /path/to/repro.py`. Use a disposable test terminal and break the transport from outside that terminal; normal completion is the control case.

**Measured results** (DECRQM for 1003/1006 and `CSI ? u`, with real XTest mouse movement and an `a` keypress after SSH exits):

| Case | SSH exit | Mouse 1003 / SGR 1006 after exit | Keyboard flags | Input received after exit |
| --- | --- | --- | --- | --- |
| Plain SSH, remote program completes and cleans up | 0 | reset / reset | 0 | `a`, no mouse reports |
| Plain SSH, transport abruptly closed | 255 | set / set | 8 | `ESC[<35;12;5M` etc. and `ESC[97u` |
| `kitten ssh`, same transport closure | 255 | reset / reset | 0 | `a`, no mouse reports |

`kitten ssh` was tested with connection sharing disabled (`--kitten share_connections=no`). The local `termios` attributes matched their pre-SSH values in all three cases. A hard terminal reset also restored both mouse modes and keyboard flags in the plain-SSH failure case.

This confirms the distinction discussed above: restored tty attributes do not restore the emulator's protocol state. In practice the mouse reports surface as coordinate garbage in a shell after a dropped connection, sometimes persisting into the next SSH connection. We have not established which remote application enabled each mode in the original user incident; the synthetic program isolates the failure mechanism.

It also gives a useful existing mitigation: `kitten ssh` saves/restores these modes around the child SSH process. Would a troubleshooting/FAQ note directing users with this symptom to `kitten ssh`, and documenting Ctrl+Shift+Delete recovery, be appropriate? This is not a claim that the terminal core can infer arbitrary remote process crashes, nor that 0.50.0 introduced a regression.
