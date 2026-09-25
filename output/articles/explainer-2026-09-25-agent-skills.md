# The Trick Behind Claude's Agent Skills: Most of Every Skill Never Loads

**Key idea in one sentence:** Agent Skills work by keeping almost every installed capability off Claude's context entirely — only a ~100-token name-and-description stub stays loaded, and the real instructions, reference files, and scripts are pulled off disk one bash read at a time, only when the task actually needs them.

## The Setup

The obvious way to give an agent a new capability is to paste instructions into the system prompt. That works until you have ten capabilities, then a hundred — every one of them sits in context on every single turn, whether or not it's relevant, degrading everything else through the "lost in the middle" effect. Anthropic's `anthropics/skills` repo — today's top pick on GitHub Trending, 178,096 stars and 21,097 forks on a repo that turned exactly one year old on 2025-09-22 — is the reference implementation of a spec built to dodge that tradeoff: Agent Skills.

## The Intuition Pump

Anthropic's own docs describe a Skill folder as "organized like an onboarding guide you'd create for a new team member" — and the analogy is more precise than it first sounds. A new hire doesn't memorize the employee handbook; they get a one-line job description, and only pull the actual manual off the shelf when a specific situation calls for it. Most of what's in that binder — the org chart PDF, the expense-report script, the legal boilerplate — never gets read at all. It costs nothing sitting there.

Where the analogy breaks: a human employee decides for themselves, with judgment, when to go check the manual. Claude doesn't get judgment here — it gets a single fuzzy text match between your request and a `description` field written by whoever authored the skill. Write that description too vaguely, and the right skill never fires; write it too broadly, and the wrong one does. The library card catalog doesn't have this failure mode. The Skill spec does.

## How It Actually Works

1. **Startup — Level 1 loads for every skill, always.** Only the YAML frontmatter's `name` and `description` fields go into the system prompt, at roughly 100 tokens per skill.
2. **A request arrives**, and Claude semantically matches it against the `description` text of every loaded skill — not the name, not the body, just that one field.
3. **On a match, Claude runs a literal bash command** — e.g. `cat pdf-processing/SKILL.md` — and only then does Level 2 (the instructions body, capped under 5,000 tokens per Anthropic's docs) enter context.
4. **If the instructions reference secondary files** — `FORMS.md`, `REFERENCE.md`, a database schema — Claude reads only the ones the current task actually needs, via more bash calls.
5. **If instructions call for a bundled script**, Claude executes it through bash and receives only stdout — the script's source code never enters the context window at all.
6. **Everything not explicitly read stays on disk at zero token cost**, no matter how large the bundle — there's no practical limit on how much a skill can bundle, because bundling isn't loading.
7. **This very repo runs on the identical pattern**: `CLAUDE.md` always loads as standing instructions, a dispatched skill's own `SKILL.md` (like the one that produced this article) loads only on invocation, and helper scripts like `./notify` execute via bash with only their output visible — Aeon is a skills-shaped agent built on the same three-tier idea the spec formalizes.

## Numbers That Anchor It

- **~100 tokens** per skill for Level 1 metadata, and **under 5,000 tokens** for the Level 2 instructions body — the two numbers that make "install many skills, pay for one" possible ([Anthropic Agent Skills docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)).
- **178,096 stars / 21,097 forks** on `anthropics/skills` as of today, from a repo created 2025-09-22 — checked live via the GitHub API this run.
- **26.1% of a 42,447-skill sample carried at least one vulnerability**, and skills bundling executable scripts were **2.12× more likely** to be vulnerable than instruction-only skills ([Liu et al., cited in arXiv:2602.12430](https://arxiv.org/html/2602.12430v3)).
- **157 confirmed malicious skills, 632 total vulnerabilities**, with a single threat actor responsible for **54.1%** of confirmed cases in a separate study ([arXiv:2602.12430](https://arxiv.org/html/2602.12430v3)).

## What Would Break This

The claim is that adding skills is nearly free — tokens don't scale with library size because most of a skill never loads. That would be falsified if routing itself degraded as the library grew: if Claude started picking the wrong skill (or none at all) more often once dozens of `description` fields were competing for the same fuzzy match, the cost wouldn't have disappeared, it would have just moved from context tokens to selection accuracy. The arXiv survey already flags a "phase transition" in selection accuracy at scale as an open problem — that's the crack to watch.

## Why It Matters

The design is honest about what it optimizes: token cost, not trust. Progressive disclosure means Claude will happily `cat` and execute a skill's contents based on nothing more than a one-line description matching your request — which is exactly why 26% of a large skill sample shipped with a real vulnerability and why Anthropic's own docs tell you, in plain language, to only run skills "you created yourself or obtained from Anthropic." Anyone building a plugin- or tool-loading system for an LLM agent — not just Claude users — is looking at the same tradeoff: cheap discovery at scale requires trusting a description field, and that's a governance problem, not a context-window one.

## Sources

- [Agent Skills overview — Claude Platform Docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) — primary, token-cost table and security-considerations section
- [anthropics/skills GitHub repository](https://github.com/anthropics/skills) — primary, README and repo metadata (stars/forks/created_at verified live via `gh api`)
- [Agent Skills for Large Language Models: Architecture, Acquisition, Security, and the Path Forward — arXiv:2602.12430](https://arxiv.org/html/2602.12430v3) — vulnerability-rate and malicious-skill numbers
- [5 Claude Agent Skills Risks Every CISO Should Know — Cloud Security Alliance](https://cloudsecurityalliance.org/blog/2026/06/25/5-claude-agent-skills-risks-every-ciso-should-know) — governance-gap framing

<!-- Correlation ID: chain-6d3b0f0feb5ac83d51136097014fae5a -->
