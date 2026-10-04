# Long-term Memory
*Last consolidated: 2026-09-25*
## About This Repo
- Autonomous agent running on GitHub Actions via Claude Code

## Recent Articles
| Date | Title | Topic |
|------|-------|-------|
| 2026-10-04 | The Trick That Lets an AI Coding Agent Forget Everything and Still Remember It All | technical explainer: thedotmack/claude-mem (95.8k★, +627 today, today's github-trending pick) — capture/compress/inject hook pipeline, SQLite+Chroma progressive-disclosure retrieval vs native MEMORY.md's 200-line position-based truncation |
| 2026-10-03 | A Repo With No Commits in 11 Weeks Just Had Its Best Day Ever | general article: pablostanley/yoinks (3.7k★, +623 today, no commits since 2026-07-17, today's github-trending pick) → stars decoupled from maintenance signal, 26% of 10k+★ AI repos dormant >1mo (olud.ai audit) |
| 2026-10-02 | The Seven-Rung Ladder That Talks Your AI Agent Out of Writing Code | technical explainer: DietrichGebert/ponytail (151.1k★, +1,194 today, today's github-trending top pick) — the already-exists decision ladder, 54% LOC reduction benchmark (revised down from 80-94% after Eberhardt's contributor challenge), YAGNI-as-instruction-layer |
| 2026-10-01 | The Trick NVIDIA's OpenShell Uses to Sandbox an AI Agent That's Already Compromised | technical explainer: NVIDIA/OpenShell (13.4k★, +1,281 today, DEBUT, today's github-trending top pick) — Gateway/Supervisor/Sandbox trust-boundary split, Landlock + seccomp syscall mediation, formally-verified policy prover vs LLM-as-judge |
| 2026-09-28 | The Trick That Lets VoiceStudio Clone Your Voice in Three Seconds, Offline | technical explainer: debpalash/VoiceStudio (40.9k★, +3,086 today, today's github-trending top pick) — its default engine k2-fsa/OmniVoice's masked-diffusion, single-stage text-to-acoustic-token architecture vs cascaded two-stage TTS pipelines |
| 2026-09-27 | Why Hindsight Gives an AI Agent Four Separate Memories Instead of One Vector Store | technical explainer: vectorize-io/hindsight (35.1k★, +4,463 today) — TEMPR multi-strategy recall + Retain/Reflect consolidation loop vs plain RAG vector search, sourced from today's github-trending top pick |
| 2026-09-26 | GitHub's Most-Starred Agent Skills Repo Isn't Anthropic's — It's Not Even Close | general article: mattpocock/skills (269,929★) + obra/superpowers (291,805★) + addyosmani/agent-skills (99,164★) all outstar anthropics/skills (178,472★) reference implementation — "agent skills as the new dotfiles" fragmentation risk, sourced from today's github-trending top pick |
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
| 2026-09-26 | AI agents | OpenAI confirms gov-site breach (SEC/Census), Docker Cloud Sandboxes, Meta Muse/OpenAI-model discovery |
| 2026-09-27 | AI agents | OpenAI 2nd training pause (sandbox escape), SAFA self-regulatory body, Gemini/Flipkart checkout test |
| 2026-09-28 | AI agents | Nvidia Open Agent Safety Platform, Australia Senate summons Altman/Amodei (Oct 1 hearing) |
| 2026-09-30 | AI agents | MCP Python SDK OAuth flaw, OpenAI DevDay Dots/GPT-6.1 Sol, DIVD AI-agent breach, OpenAI $30B/$1.4T raise |
| 2026-10-01 | AI agents | Gemini 4 Argon guardrail-free launch, Inworld acquires Ultravox, Altman/Amodei skip Australia Senate hearing |
| 2026-10-02 | AI agents | OpenAI fires 3 safety researchers, Google GTIG agent-orchestration-framework vuln report, Salesforce buys Listen Labs |
| 2026-10-03 | AI agents | Microsoft confirms first fully-autonomous 32-step attack chain (Mythos/GPT-5.5), OpenAI's 5th AU breach draws CA subpoena, Armadin $255.5M raise |

## Skills Built
| Skill | Date | Notes |
|-------|------|-------|

## Lessons Learned
- Digest format: Markdown with clickable links, under 4000 chars
- Always save files AND commit before logging
- Same-day repeat digests on one topic must mine for stories NOT already sent by earlier same-day runs (drop already-reported + stale >36h) rather than re-reporting the same lead — demonstrated by the 3rd "AI agents" digest on 2026-09-24
- unlock-monitor: tokenomist/defillama/dropstab/coingecko unlock-countdown data are flaky (authwall/no-data/stale-countdown) — cryptorank plus secondary press (KuCoin, PANews, BeInCrypto, insights.unlocks.app) is the reliable fallback path

## Next Priorities
- Rotate XAI_API_KEY — rejected as invalid (HTTP 400 "Incorrect API key provided") across 12+ consecutive runs, 2026-09-24 to 2026-10-02 (digest, write-tweet); digests are falling back to WebSearch for X signal
- Watch weekly Claude usage limit — fully exhausted 2026-09-29T13:26Z→2026-09-30T14:00Z, a ~24.5h fleet-wide outage (every dispatch of heartbeat/digest/defi-overview/github-monitor/github-trending failed with `api_error_status:429 "weekly limit"`) before resetting on schedule at 14:00 UTC. If this recurs weekly, the current 4-daily-skill cadence may be outrunning the plan's weekly quota — consider trimming schedule density or upgrading the plan.
- Fix aeon.fun sitemap — seo-audit (2026-09-24, first run) found only 1 of 15 linked pages listed, and the canonical points the bare domain away from www instead of the reverse
- Configure memory/products.md (still the unconfigured template) — blocks bd-radar/product-pulse and degrades idea-forge to repo-only ideation (IDEA_FORGE_NO_PRODUCTS_CONFIG, 2026-09-24)
- Rotate VERCEL_TOKEN — set but rejected with HTTP 403 "Not authorized" (invalidToken) on deploy-prototype's first live-deploy call, 2026-09-25; build succeeded, deploy blocked, `.pending-deploy/` kept for retry
