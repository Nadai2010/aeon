## Tweet Drafts: stars decoupled from maintenance (pablostanley/yoinks)

### Tier 1 — One-liner
**1a. Hot take**
> A star never expires. A commit date is the only number on GitHub that's actually alive.

**1b. Observation**
> Yoinks hasn't shipped a commit in 11 weeks. It just had its best day ever — 623 stars.

### Tier 2 — Two-punch
**2a. Data drop**
> 26% of installable AI repos with 10k+ stars haven't taken a commit in over a month. 63 have gone a full year. Between them: 1.27 million stars.

**2b. Reframe**
> Everyone checks star count before trusting a repo. Nobody checks pushed_at. That's the one field that tells you if the lights are still on.

### Tier 3 — Paragraph
**3a. Narrative**
> pablostanley/yoinks hasn't been touched since July 17. Today it pulled 623 stars, its biggest day ever, three months after the author stopped committing. Nobody shipped a feature. The spike was pure word-of-mouth.

**3b. Structural critique**
> An audit of 848 popular AI repos found 26% haven't committed in over a month, and 63 haven't committed in a year — holding 1.27M stars between them. Stars measure a moment of interest. They say nothing about who still maintains the thing.

### Tier 4 — Long tweet
**4a. Sardonic/ironic**
> pablostanley/yoinks pulled 623 stars today. Its last commit was July 17 — 11 weeks ago. The author isn't fixing bugs or shipping features; people are just finding it and starring it, one newsletter mention at a time. Zoom out and this is the median story, not the outlier: an audit of 848 AI repos with 10k+ stars found 26% haven't committed in over a month, 63 haven't in a year, and together they hold 1.27 million stars. GitHub turned "last commit" into a vanity metric and "star count" into the permanent record. That's backwards for anyone deciding whether to depend on the thing.

**4b. Builder's breakdown**
> Here's the split nobody talks about: Python repos go dormant at 36%, JavaScript at 32%, but Go sits at 7% and Rust at 16%. It's not a language quality thing — it's what gets built in each one. Python is where research demos live: a paper drops, the repo gets 30k stars in two weeks, the authors graduate, and nobody touches it again. Go is infrastructure — someone's running it in production and has to keep patching it, or it never got stars at all. Yoinks is the in-between case: good enough on day one that it never needed day-sixty maintenance to keep spreading.

### Tier 5 — Thread opener
**5a. Thesis-first**
> GitHub has a lying metric and everyone trusts it anyway. 'Stars' never expire. 'Last commit' does — and almost nobody checks it before depending on a repo. Here's what an 848-repo audit found when it finally measured the gap.
---
- 26% of 10k+-star AI repos haven't committed in a month, 63 haven't in a year, 1.27M stars between them
- yoinks: 623 stars today, zero commits in 11 weeks — pure word of mouth
- dormancy by language: Python 36%, JS 32% vs Go 7%, Rust 16% — not quality, it's what each gets used for
- the fix: check pushed_at, not stargazers_count, before you depend on something

**5b. Data-driven**
> nomic-ai/gpt4all: 77,402 stars, 432 days since the last commit. lencx/ChatGPT: 54,401 stars, 703 days silent. Popularity on GitHub stopped meaning "maintained" a while ago — here's the audit that puts a number on it.
---
- 848 AI repos audited, 26% dormant >1 month, 63 dormant >1 year
- yoinks' 623-star day came three months after its last commit
- dormancy splits by language: Python/JS research throwaways vs Go/Rust production code
- stargazers_count is permanent, pushed_at is the only live signal

**Best overall:** 4a — the yoinks-to-audit zoom-out lands the thesis with a concrete hook and a number, no hedging.
**Best per tier:** 1a (one-liner) · 2a (two-punch) · 3b (paragraph) · 4a (long tweet) · 5a (thread opener)

<!-- Correlation ID: chain-17752f93282df3e84a1df35fa94b309d -->
