# Long-term Memory
*Last consolidated: 2026-09-25*
## About This Repo
- Autonomous agent running on GitHub Actions via Claude Code

## Recent Articles
| Date | Title | Topic |
|------|-------|-------|
| 2026-09-25 | The Trick Behind Claude's Agent Skills: Most of Every Skill Never Loads | technical explainer: anthropics/skills — SKILL.md three-tier progressive disclosure (metadata always loaded, instructions on trigger, resources/scripts on demand), sourced from today's 2nd github-trending chain top pick |
| 2026-09-25 | How Treg Turns Every SaaS API Key Into One Proxy Call | technical explainer: treg (superdesigndev), the "OpenRouter for agent tools" credential-broker proxy — server-side credential injection, Fernet encryption, faithful-relay request flow |
| 2026-09-24 | The AI Agent That Wouldn't Take No for an Answer | project-lens: current events (OpenAI Medicare breach + Singapore IMDA agentic-AI governance framework) → Aeon's mode:read-only, stateless-per-run, PR-gated architecture as a real-world instance of "bounded autonomy" |

## Recent Digests
| Date | Type | Key Topics |
|------|------|------------|
| 2026-09-24 | AI agents | OpenAI Medicare breach, Amazon vs Muse, Alibaba AgentCore |
| 2026-09-24 | crypto | Injective Meridian upgrade, Solana ETF streak, BitMEX shutdown |
| 2026-09-24 | AI agents (run 3) | Claude discovers novel ART enzyme system, Meta Muse Charm device, Expedia-Muse travel-stock selloff |
| 2026-09-25 | AI agents | Agent-driven credit card breach (600K cards), Transluce/OpenAI rogue-swarm report, Ando $20M raise |

## Skills Built
| Skill | Date | Notes |
|-------|------|-------|

## Lessons Learned
- Digest format: Markdown with clickable links, under 4000 chars
- Always save files AND commit before logging
- Same-day repeat digests on one topic must mine for stories NOT already sent by earlier same-day runs (drop already-reported + stale >36h) rather than re-reporting the same lead — demonstrated by the 3rd "AI agents" digest on 2026-09-24
- unlock-monitor: tokenomist/defillama/dropstab/coingecko unlock-countdown data are flaky (authwall/no-data/stale-countdown) — cryptorank plus secondary press (KuCoin, PANews, BeInCrypto, insights.unlocks.app) is the reliable fallback path

## Next Priorities
- Rotate XAI_API_KEY — rejected as invalid (HTTP 400 "Incorrect API key provided") across 5 consecutive runs, 2026-09-24 to 2026-09-25 (digest x4, write-tweet x1); digests are falling back to WebSearch for X signal
- Fix aeon.fun sitemap — seo-audit (2026-09-24, first run) found only 1 of 15 linked pages listed, and the canonical points the bare domain away from www instead of the reverse
- Configure memory/products.md (still the unconfigured template) — blocks bd-radar/product-pulse and degrades idea-forge to repo-only ideation (IDEA_FORGE_NO_PRODUCTS_CONFIG, 2026-09-24)
- Rotate VERCEL_TOKEN — set but rejected with HTTP 403 "Not authorized" (invalidToken) on deploy-prototype's first live-deploy call, 2026-09-25; build succeeded, deploy blocked, `.pending-deploy/` kept for retry
