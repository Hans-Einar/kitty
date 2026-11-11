"""Re-run existing GUI/PTY acceptance checks against an explicit candidate.

Usage: python3 check.py /absolute/path/to/kitty /absolute/output/directory
Only isolated Xvfb displays :94/:95 and disposable session state are used.
"""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

candidate = str(Path(sys.argv[1]).resolve())
output = Path(sys.argv[2]).resolve()
output.mkdir(parents=True, exist_ok=True)
evidence = Path(__file__).resolve().parent.parent
with tempfile.TemporaryDirectory(prefix="kitty-050-acceptance-") as temporary:
    root = Path(temporary)
    results = {}
    for name, source, directory in (
        ("roundtrip", "KittyResume/roundtrip.py", "resume"),
        ("picker", "KittyResume/pty-check.py", "resume"),
        ("resize", "KittyResize/check.py", "resize"),
    ):
        target = root / directory
        target.mkdir(exist_ok=True)
        code = (evidence / source).read_text()
        code = code.replace("/home/warloc/git/kitty/kitty/launcher/kitty", candidate)
        code = code.replace("/tmp/kitty-resume-check", str(root / "resume"))
        code = code.replace("/tmp/kitty-resize-check", str(root / "resize"))
        env = dict(os.environ, XDG_STATE_HOME=str(root / "state"))
        result = subprocess.run([sys.executable, "-c", code], env=env, capture_output=True, text=True, timeout=90)
        (output / (name + ".log")).write_text(result.stdout + result.stderr)
        results[name] = {"exit_code": result.returncode, "stdout": result.stdout}
        (output / "result.json").write_text(json.dumps(results, indent=2) + "\n")
        if result.returncode:
            for log in target.glob("*.log"):
                (output / (name + "-" + log.name)).write_bytes(log.read_bytes())
            raise SystemExit(f"{name} failed; see {output}")
        print(name + ": PASS")
