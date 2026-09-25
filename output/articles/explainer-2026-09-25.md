# How Treg Turns Every SaaS API Key Into One Proxy Call

**Key idea in one sentence:** Treg puts a single proxy token between an agent and every tool it uses, resolving and injecting the real provider credential server-side so the agent — and anyone who compromises it — never sees the underlying key.

## The Setup

Agents that do real work need real tools: Stripe, scraping APIs, social platforms, enrichment services. Wiring N agents to M providers the naive way means N×M raw API keys scattered across `.env` files, scripts, and CI secrets — a sprawl problem that's already solved once, for models, by OpenRouter: one API, one key, N providers behind it. [superdesigndev/treg](https://github.com/superdesigndev/treg) applies the identical consolidation move to tool credentials instead of model calls, and it's trending today with 468 new stars in 24 hours on top of 3,300 total.

## The Intuition Pump

Think of it like a corporate card issued through an expense platform: an employee swipes one card number, and the network — not the employee — resolves which vendor account gets billed and which payment rail actually moves the money. The employee never learns the underlying bank details. Treg does this for API calls: one `X-Treg-Token` header stands in for every provider's real key. The analogy breaks down at scope: a corporate card can be vendor-locked or spend-capped per employee, but treg's token is identical across *every* tool in the catalog — there's no per-tool scoping baked into the credential itself, only into what the server chooses to authorize.

## How It Actually Works

1. The agent sends a request to treg's `/call` endpoint carrying only its `X-Treg-Token` — no provider credentials attached.
2. Treg resolves the target tool by matching the request's URL host and longest `base_url` prefix, or by an explicit tool name if one is given.
3. It picks a credential using a fixed resolution order: the team's own registered key for that provider first, then a team-stored secret injected through a "virtual tool," and only then treg's own shared key — billed against the team's prepaid balance.
4. Whatever secret is selected gets decrypted from storage. Secrets are encrypted at rest with Fernet under a `TREG_SECRET_KEY`; if that key isn't configured, treg mints an ephemeral one at boot, which means stored secrets silently don't survive a restart.
5. The provider's declared auth shape decides how the credential gets attached: `env` for a plain key, `secret_file` for a JSON token with field extraction, `oauth` for a JSON token that auto-refreshes when a refresh token and client credentials are present, or `cli_auth` for material pulled from a CLI's own keychain.
6. From there treg acts as a "faithful relay" — it only touches hop-by-hop transport headers, its own control headers, and the injected credential; everything else in the request and response passes through verbatim, with responses buffered up to 8 MiB for cost settlement (anything larger returns a 502 without a charge).
7. An audit record is written asynchronously after the call, and if the team's balance can't cover the estimated cost up front, treg returns HTTP 402 with `balance_micro`, `estimated_cost_micro`, and a `topup_url` instead of completing the request.

## Numbers That Anchor It

- 3,000+ catalogued endpoints across 60+ providers ([superdesigndev/treg README](https://github.com/superdesigndev/treg))
- 3.3k total GitHub stars, +468 in the last 24 hours — the fastest-accelerating devtool on today's trending list (repo, via chain context)
- 8 MiB response-buffer ceiling before settlement fails with an uncharged 502 ([repo](https://github.com/superdesigndev/treg))
- 10 teams max per account ([repo](https://github.com/superdesigndev/treg))
- Flagged "Critical Risk" and "not audited" in third-party catalog metadata ([Skillstore listing](https://skillstore.io/skills/superdesigndev-treg))

## What Would Break This

The pitch is that centralizing credentials makes agent fleets *safer* because raw keys never reach the agent. That claim breaks if a leaked treg token turns out to carry the same blast radius as leaking every underlying key at once — since the token is identical across all 60+ connected providers rather than scoped per tool, a single compromised agent session could plausibly reach Stripe, scraping, and social-posting credentials alike. If that pattern shows up in a real incident, the security story shifts from "keys never leave the server" to "we moved the single point of failure, we didn't shrink it."

## Why It Matters

Every team running more than a handful of agents against more than a handful of SaaS providers hits this sprawl problem within weeks, and right now most solve it with `.env` files nobody audits. Treg is a bet that the OpenRouter pattern generalizes past model routing: consolidate first, then figure out per-tool scoping later. If it catches on, a credential proxy becomes the thing security teams point to first when an auditor asks "which services can your agents actually touch" — the same role OpenRouter now plays for "which models are you actually calling."

## Sources
- [superdesigndev/treg](https://github.com/superdesigndev/treg) — primary, official README
- [feat(auth): add managed API key controls, PR #377](https://github.com/superdesigndev/treg/pull/377) — recent auth-control work
- [treg: Unified API Gateway for Agent Tools — DSH Plugin](https://dsh-plugin.org/plugins/superdesigndev/treg)
- [treg — Skillstore listing](https://skillstore.io/skills/superdesigndev-treg) — third-party risk rating
