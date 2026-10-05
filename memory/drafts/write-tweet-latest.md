## Tweet Drafts: tester-army/e2e — record once, replay without the model

### Tier 1 — One-liner
**1a. Hot take**
> AI testing isn't expensive because LLMs are bad at clicking buttons. It's expensive because nobody cached the click.

**1b. Observation**
> tester-army/e2e pays the model once per test, then replays the exact same test for free, forever.

### Tier 2 — Two-punch
**2a. Data drop**
> One cached `act` step: 9,412 input tokens, $0.0198, once. Every run after that: $0.
>
> That's the whole pitch of tester-army/e2e.

**2b. Reframe**
> Agent-based E2E testing fixed brittleness by re-asking the model every run. tester-army/e2e asks the obvious next question: why pay for the same answer twice?

### Tier 3 — Paragraph
**3a. Observation**
> Selenium IDE recorded pixels and XPaths, so it broke the moment a button moved. LLM-driven testing fixed that by asking the model to look at the screen every single run — robust, but you're paying inference on every PR, forever. tester-army/e2e splits the difference: record the role+name+testId once, replay that for free, only call the model back when the UI actually changes.

**3b. Narrative**
> A real log from tester-army/e2e: "Cache 4 replayed · 1 handed off · 1 missed." Four of six steps in that test ran with zero model calls. The two that didn't are exactly where the system is supposed to spend money — not where it's forced to.

### Tier 4 — Long tweet
**4a. Builder's breakdown**
> The actual mechanism in tester-army/e2e is more interesting than "it caches stuff." First run, the model gets a text-only snapshot — roles, names, states, never a screenshot — and picks an action. That action gets cached as a semantic key: control role + name + testId + the route before and after + what appeared or vanished. Next run, it walks that cached list and matches controls by that key instead of asking anything. Four specific triggers kick it back to the model: target gone, target ambiguous, wrong route, or the expected end-state controls didn't show up. It's not "replay until it breaks, then fail" like old record-and-playback — it's "replay until it breaks, then let the model finish the step and record a fresh cache entry." The exception path heals itself.

**4b. Reframe**
> Nobody asks whether their CI pipeline is cost-rational because VM-minutes are cheap. LLM-driven E2E testing quietly imported a different cost model — every assertion re-invokes a model, multiplied by test count times run frequency — and most teams haven't noticed yet because the per-call price looks small until the invoice multiplies by your commit volume. tester-army/e2e is a bet that most of a test suite's actions are identical run over run, so most of that spend was always avoidable.

### Tier 5 — Thread opener
**5a. Thesis-first**
> AI test suites have a cost problem nobody's pricing correctly: every test, every run, re-invokes a model just to click the same button it clicked yesterday. tester-army/e2e is the first project I've seen fix this at the right layer.
---
- The brittleness problem LLM-driven testing solved (vs. Selenium IDE XPaths) — and the new cost problem it created
- How the cache actually works: role+name+testId, not pixels, not prompts
- The 4 triggers that hand control back to the model, and why that's the real design
- The number that matters: 61% of one cached call already hit prompt caching, and cache mode avoids the other 39% entirely
- What breaks it: nobody's published a real-world cache-hit rate yet

**5b. Question**
> If your CI suite re-runs the same AI-driven test 50 times a week, how many of those runs actually needed a fresh model decision?
---
- Most agent-based E2E tools answer "all of them" by design
- tester-army/e2e's answer: almost none, if the UI didn't change
- The mechanism: semantic caching on role+name+testId, verified against route + end-state
- The failure modes baked into the docs (route-sensitivity, ambiguous controls) read like scar tissue from hitting this in production
- The open question: does the hit rate hold up outside demo apps

**Best overall:** 4a — long tweet / builder's breakdown. The mechanism is the whole story here, and the healing-cache-on-failure detail (model finishes the step and records a fresh entry, instead of just failing) is the part nobody else covering this repo is saying.
**Best per tier:** 1b (one-liner) · 2a (two-punch) · 3a (paragraph) · 4a (long tweet) · 5a (thread opener)

<!-- Correlation ID: chain-a70eaae9d1138eca80f826294a9cc55d -->
