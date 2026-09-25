⚠️ Vuln Scanner

*Vuln Scanner — HKUDS/CLI-Anything*
1 confirmed finding (HIGH, CWE-94 Script-Fu code injection).
Disclosed via: PVR — enabled + designated by SECURITY.md, but filing blocked this run by token scope (403, not PVR-disabled). Staged for a properly-credentialed follow-up run.
Scanners: semgrep=ok, trufflehog=ok, trufflehog-git=ok (shallow clone), osv=ok, fuzz=skip, agentic=ok. PoC gate: verified.
Also noted: 14 public dependency CVEs (npm, low severity) — bump PR also blocked by the same token-scope limit, not individually staged.
Full report: output/articles/vuln-scan-2026-09-25.md