tweet drafts: Agent Skills — progressive disclosure & the trust gap

— one-liner —
1a. Claude doesn't decide to load a skill. It just loses a fuzzy-match roulette.
1b. 3.8 million SKILL.md files exist. Almost none of them have been read by a human.

— two-punch —
2a. 178,096 stars on anthropics/skills in a year. 26% of skills in the wild ship with a real vulnerability. Adoption outran review.
2b. Everyone is excited that skills are nearly free to install. Nobody is asking what "nearly free" does to the incentive to actually read one before running it.

— paragraph —
3a. Progressive disclosure means Claude reads a skill's real instructions only after a one-line description convinces it to. That's not judgment, it's a coin flip written by whoever authored the description. 26% of skills in the wild fail that flip.
3b. A new hire doesn't memorize the handbook, they read a one-line job title and ask when they're stuck. Anthropic built Agent Skills on exactly that analogy. The gap: a human employee has judgment about when to check the manual. Claude has a string match.

— long tweet —
4a. Agent Skills work because almost nothing loads: about 100 tokens of metadata per skill, always in context, and the real instructions - under 5,000 tokens - only load if your request matches a one-line description. Everything else, scripts included, sits on disk at zero cost until Claude decides to run it. That's the trick that let 3.8 million SKILL.md files ship across 282,200 repos in about a year. It's also why 26% of a large sample carried a real vulnerability - the description field is the entire security boundary, and nobody's reviewing it.
4b. The standard has already spread past Claude - OpenAI Codex and GitHub Copilot support the same Agent Skills format now. That's the part worth sitting with: an entire ecosystem is converging on "a folder plus a description field" as the interface between an agent and a new capability. Nobody would ship an OS where installing an app meant trusting one sentence the app wrote about itself. That's exactly what every agent using this spec does today, and it's spreading faster than anyone is auditing it.

— thread opener —
5a. Anthropic's Agent Skills stay almost entirely off Claude's context - one ~100-token stub per skill, everything else loaded on demand. It's the reason installing 100 skills costs about the same as installing 5. It's also why 26% of them ship a real vulnerability.
---
- How the 3-tier load actually works: metadata, then instructions, then scripts — each gated behind a bash read
- Why a fuzzy-matched description field is the entire trust boundary
- The onboarding-guide analogy Anthropic uses, and exactly where it breaks
- The numbers: 178k stars, 3.8M SKILL.md files, 26% vulnerable, 157 confirmed malicious skills
- What would actually break the "adding skills is nearly free" claim as libraries scale

5b. Would you let a new hire read one sentence about a task, then hand them the keys to run whatever script sits on the shelf labeled with that sentence? That's how every Claude Agent Skill gets executed.
---
- The metadata-only default and what "matching a description" actually authorizes
- The trust-gap numbers: 632 vulnerabilities found, one threat actor behind 54% of confirmed malicious skills
- Anthropic's own advice ("only run skills you wrote or got from Anthropic") vs. a 3.8M-file open ecosystem
- Where the new-hire analogy breaks down: judgment vs. string match
- The open question researchers are flagging: does routing accuracy collapse as the skill library grows?

best: #4a — long tweet / structural critique. It's the one that actually proves the claim with numbers instead of asserting it: names the token budget, ties it to the adoption number, then ties that same mechanism to the vulnerability rate. Runner-up: #3a for compression of the same idea into one paragraph.
