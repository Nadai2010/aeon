---
repo: HKUDS/CLI-Anything
severity: high
cwe: CWE-94
status: pending-operator-send
channel: pvr
auto_send: false                    # not an email draft — GitHub PVR submission blocked by token scope, needs a credential, not the C4 email caps
pvr_enabled: true
pvr_endpoint: /repos/HKUDS/CLI-Anything/security-advisories/reports
blocked_reason: "gh api POST returned 403 'Resource not accessible by integration' — this run only had the default Actions installation token (GITHUB_TOKEN, scoped to aeonframework/aeon) available, no GH_GLOBAL / cross-repo PAT. PVR IS enabled on the target repo and SECURITY.md explicitly designates GitHub PVR as the intake channel — this is a credential-scope failure in THIS run, not a routing decision or a PVR-disabled case."
target_commit: 34f519533bc175d2fe287ab8316b0dd99bb9cc43
poc_verdict: verified (local-command, finding_sha256 2f38a0d09c5c82f4211c01a659d3d3788961e682c0ca7b051ee931a7647dce5d)
detected_at: 2026-09-25T07:54:00Z
---

# Staged PVR submission — HKUDS/CLI-Anything

**Operator-facing notes** (not part of the report body): PVR is enabled on
this repo and SECURITY.md explicitly says to use GitHub's private
vulnerability reporting ("Security tab > Report a vulnerability") — this is
the correct, designated channel (A5.0 case c). The submission itself failed
only because this run's `gh` token is the default GitHub Actions
installation token scoped to `aeonframework/aeon`; it cannot act on
`HKUDS/CLI-Anything` (`403 Resource not accessible by integration`). A run
with `GH_GLOBAL` (or any PAT with classic `repo` scope) set can submit this
directly with:

```
gh api -X POST "/repos/HKUDS/CLI-Anything/security-advisories/reports" \
  -H "X-GitHub-Api-Version: 2022-11-28" --input <payload-below-as-json>
```

The finding was independently PoC-verified in this run (local-command
verifier, exercised the real unmodified `render_project()` production
entrypoint, confirmed an attacker-controlled layer field is spliced
unescaped into the executed Script-Fu batch script) — see
`memory/vuln-scanned.json` and today's log for the summary; raw PoC
artifacts were not persisted (private, per policy).

<!-- REPORT-PAYLOAD-START -->
{
  "summary": "Script-Fu code injection via unvalidated numeric layer fields in loaded .gimp-cli.json projects",
  "severity": "high",
  "cwe_ids": ["CWE-94"],
  "vulnerabilities": [{"package": {"ecosystem": "pip", "name": "cli-anything"}}],
  "description": "See gimp/agent-harness/cli_anything/gimp/utils/gimp_backend.py::_build_layer_script() and gimp/agent-harness/cli_anything/gimp/core/project.py::open_project(). Full description staged at /tmp/pvr-body.md during the run that generated this draft (not persisted to the repo — regenerate from this file's summary/location notes if the temp file is gone by the time this is submitted: numeric layer fields width/height/opacity/offset_x/offset_y/font_size are spliced into the generated Script-Fu batch script unescaped and unvalidated, unlike string fields which go through _script_fu_escape(); open_project() only checks for 'version'/'canvas' keys, no layers schema validation; reachable via export render on any loaded project file. Verified commit 34f519533bc175d2fe287ab8316b0dd99bb9cc43, finding_sha256 2f38a0d09c5c82f4211c01a659d3d3788961e682c0ca7b051ee931a7647dce5d. Suggested fix: validate/coerce these fields to int/float in open_project() or format them via a numeric-only formatter at the point of use in _build_layer_script()."
}
<!-- REPORT-PAYLOAD-END -->
