# The Trick That Lets an AI Test Suite Stop Paying the Model to Click the Same Button Twice

**Key idea in one sentence:** tester-army/e2e lets an LLM agent perform a browser or mobile test exactly once, records *what it meant to do* rather than *where it clicked*, and replays that intent on every later run without calling the model again — until the UI actually changes underneath it.

## The Setup

AI agent testing tools (Browser Use, Stagehand, Magnitude, TesterArmy's own hosted platform) fixed the brittleness of classic record-and-playback tools like Selenium IDE: instead of a hard-coded XPath, an LLM looks at the screen and decides what to click, every run. That's robust to UI drift, but every test, every run, re-invokes a model — cost multiplied by CI frequency. A 200-test suite on every PR becomes a line item. `tester-army/e2e` (4,073 stars, created 2026-07-22, +1,430 stars in a single day on 2026-10-05) attacks that cost directly: pay the model once per test, replay free forever, fall back only when the cheap path breaks.

## The Intuition Pump

Think of a new employee shadowing a manager through a store's closing routine on day one — lock the register, dim the lights, set the alarm, lock the door — then writing down not the manager's exact footsteps but the *checklist of named tasks*. From day two on, the employee runs the checklist alone, matching tasks to whatever's actually in front of them ("the register" is still "the register" even if it moved six inches). The manager only gets called back in if a step on the checklist doesn't exist anymore — the alarm panel got replaced, say. That's the system: cheap, memorized execution with an expensive human (model) as the exception path, not the default path.

Where the analogy breaks: a human checklist-follower recognizes "the register" even if its sign is torn off, using the kind of fuzzy real-world judgment e2e's replay step explicitly does *not* have. Replay matches on role, visible name, and `testId` — not pixels, but still a fixed semantic key. If that key disappears (the button loses its accessible name, the route changes), the system doesn't improvise like the employee would; it stops and calls the model.

## How It Actually Works

1. **First run ("live mode"):** for each `agent.act()` step, e2e sends the LLM a redacted, text-only snapshot of the screen — roles, visible names, states — never raw HTML, screenshots, or secrets.
2. **The model picks actions** (tap, scroll, type, select, navigate), executed against Playwright (web) or agent-device (iOS/Android simulators).
3. **Every action gets cached** to `.e2e/cache/<hash>.json`: control role + name + testId + context, the route before and after, which controls appeared or vanished at the end — not the prompt, conversation, or a screenshot.
4. **Second run onward ("cache mode"):** the runner checks the starting route matches (ignoring IDs/timestamps), then walks the cached action list, locating each control by its recorded role/name/testId instead of asking the model anything.
5. **It verifies the ending state** — same target route, same controls appeared or vanished — and if everything lines up, the step completes with zero model calls.
6. **Four triggers hand control back to the LLM:** `target-not-found` (control gone after a 15-second wait), `target-ambiguous` (two matches), `wrong-context` (final route doesn't match), `end-mismatch` (expected controls didn't appear/disappear as recorded).
7. **Partial hand-off, not replay-or-fail:** once the model takes over mid-step, it can finish the step and record a fresh version for next time — unlike Selenium IDE playback, which just fails outright on any DOM mismatch.

## Numbers That Anchor It

- 4,073 stars at 75 days old, with a single day (2026-10-05) adding 1,430 — larger than the repo's entire prior lifetime total ([github.com/tester-army/e2e](https://github.com/tester-army/e2e))
- A real cached `act` step logged "9412/388" input/output tokens, 61% (5,740 tokens) hitting the provider's prompt cache, for a one-time cost of $0.0198 — the cost that cache mode then avoids on every subsequent run ([docs/reference/cli.mdx](https://raw.githubusercontent.com/tester-army/e2e/main/docs/reference/cli.mdx))
- A typical debug run reports "Cache 4 replayed · 1 handed off · 1 missed" per test — i.e. 4 of 6 steps in that run needed zero model calls ([docs/cache.mdx](https://raw.githubusercontent.com/tester-army/e2e/main/docs/cache.mdx))
- Recordings truncate — and stop being replayable — past 50 actions or 4,096 typed characters per step, a hard ceiling on how long a "free" cached step can be ([docs/cache.mdx](https://raw.githubusercontent.com/tester-army/e2e/main/docs/cache.mdx))
- The project's commercial parent, TesterArmy, reported 30+ teams using the hosted platform daily at its Hacker News launch ([news.ycombinator.com/item?id=48586299](https://news.ycombinator.com/item?id=48586299))

## What Would Break This

If cache hit rate collapses on real-world apps with routine UI churn — say, most teams see `target-not-found` or `end-mismatch` on a majority of steps within a few weeks of normal feature shipping — the "skip the model, cut recurring cost" pitch doesn't hold, because every run would quietly fall back to full-price agent mode anyway. Nobody has published that number yet, including TesterArmy itself; the docs' extensive list of failure modes (ambiguous controls, route-sensitivity down to a single path segment, "derived value" steps that read text off the screen) reads like a team that has already hit this wall internally.

## Why It Matters

Every team running LLM-driven E2E tests in CI is paying a model-call tax on every PR, multiplied by test count and run frequency — the same cost structure that made traditional browser farms expensive, just with token pricing instead of VM-minutes. If semantic caching holds up across real apps rather than just demo apps, it's the difference between "AI testing" being a cost center you ration and a tool you run on every commit without thinking about the bill. The people who should care first are teams already running agent-based E2E tools (Stagehand, Magnitude, TesterArmy's own hosted product) who've felt that per-run cost directly.

## Sources

- [tester-army/e2e — GitHub repository](https://github.com/tester-army/e2e) — primary, README/code/license
- [docs/cache.mdx — cache & replay mechanics](https://raw.githubusercontent.com/tester-army/e2e/main/docs/cache.mdx) — primary, replay triggers and failure modes
- [docs/reference/cli.mdx — CLI token/cost output](https://raw.githubusercontent.com/tester-army/e2e/main/docs/reference/cli.mdx) — primary, numbers
- [Example cache entry (real JSON)](https://raw.githubusercontent.com/tester-army/e2e/main/apps/mobile-benchmark/.e2e/cache/0e691404e147a4cd7dad695ca7bae7b9bcc1067e559fa6b20dc7f93e8fdc6845.json) — primary
- [TesterArmy Hacker News launch thread](https://news.ycombinator.com/item?id=48586299) — external, adoption numbers and criticism
