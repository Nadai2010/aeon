⚠️ Heartbeat: fleet DEGRADED

🔴 FAILED: github-trending — stuck in a failed state since 2026-09-28 (2 consecutive failures, last failure 2026-09-30, same fleet-wide weekly-limit outage already reported yesterday). It's now `enabled: false` in aeon.yml, so it can't self-recover on its own schedule → status page flipped to 🔴 DEGRADED. Needs a call: re-enable + fix it, or clear its stale cron-state entry.
🟡 WATCH: chain:benchmark-chain also failed in that same outage window and hasn't recovered (workflow_dispatch only, no cron — so it just sits until next manual dispatch).