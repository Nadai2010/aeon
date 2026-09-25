# Aeon (Nadai2010/aeon) — "Click the Receipt" — Video Script

**Runtime target:** ~4:00
**Framing:** receipts-first (open on a live "Verify the run" click-through)
**Byline:** github.com/Nadai2010/aeon
**One-line pitch:** A public page where every claim about the agent links straight to the unedited GitHub Actions log that proves it.
**Rev:** v1, 2026-09-25 — plain-language pass baked in; every technical term explained in one line or cut.

## Cold open — 0:00 – 0:20

**VO:**
> This page makes a claim. I'm going to click the button next to it and show you the actual log.

**On screen:**
- Browser on `nadai2010.github.io/aeon` (showcase page), scrolled to the card labeled `UC-01 · digest`.
- Cursor clicks **"Verify the run"**.
- Cut to the GitHub Actions run it opens: `github.com/Nadai2010/aeon/actions/runs/36006300827` — status `completed`, conclusion `success`, timestamped `2026-09-24 13:32 UTC`.
- Caption in `backticks`: `run #36006300827 — matches the card`.

## Context — 0:20 – 0:55

**VO:**
> This is Aeon. It's an agent that runs on a schedule, in the cloud, without a machine you have to leave on. No chat window, no one prompting it — it just fires on cron and does the job.
>
> The problem with most agent demos is you can't check them. A screen recording proves nothing. So this repo built a page where every single claim is a link to the real run behind it.

**On screen:**
- Text overlay: `scheduled · unattended · GitHub Actions`
- Quick cut: repo root showing `aeon.yml` (the schedule file) and `skills/` folder.

## How it works — 0:55 – 1:55

**VO:**
> Here's the mechanism. Each card on the page names a skill, shows what it returned, and links to the exact Actions run that produced it — same day, same timestamp, nothing re-run for the camera.
>
> Some of it is routine work done on time: a daily digest, a market overview, a trending-repo roundup. Some of it is knowing when to stay quiet — one run checked GitHub for anything that needed attention, found nothing, and sent nothing. That restraint is on the page too, with its own run link.

**On screen:**
- Split screen: card text next to the matching Actions log, side by side.
- Card: `UC-03 · defi-overview` — "TVL $94.07B, down 2.1% on the day" next to run `#36008059766`.
- Card: `UC-02 · github-monitor` — "nothing crossed a threshold, so it sent nothing" next to run `#36009830256`, both showing `success`.

## What's new — 1:55 – 2:55

**VO:**
> This page itself is the newest thing here — it shipped this week. Ten runs are linked directly from it right now, grouped into three plain buckets: doing a routine job on schedule, knowing when to act versus hold back, and finishing real work — an article, a site audit, a set of ranked ideas.
>
> One card points at a full written piece, not just a summary — an article the agent wrote and committed straight to the repo, sources included.

**On screen:**
- Scroll through the three section headers: "Running a routine," "Acting, and holding back," "Making and completing."
- Land on `UC-10 · article` card, click through to `output/articles/project-lens-2026-09-24.md` in the repo.
- Caption: `committed to the repo — not a screenshot`.

## Straight talk — 2:55 – 3:30

**VO:**
> Be clear about the size of this. This fork is brand new — created yesterday. Ten runs are linked, not thousands. And the page says outright what it doesn't do: no travel booking, no purchases, no phone calls, no email replies, no group chats. If there's no run to show for something, it doesn't claim it.

**On screen:**
- Flat cut to the page's own disclosure box: `"What Aeon does not claim."` text, shown verbatim, no music sting.

## Close + CTA — 3:30 – 4:00

**VO:**
> You don't have to take any of this on faith. Go to the page, pick any card, click "Verify the run," and read the log yourself. That's the whole pitch.

**On screen:**
- Final card: URL `nadai2010.github.io/aeon` large, centered.
- Small caption: `github.com/Nadai2010/aeon`.

---

## Plain-language glossary

- **GitHub Actions run** → "the log of exactly what the agent did, timestamped, public." (cut "CI/CD pipeline" — too much jargon for this script)
- **Cron / schedule** → "it fires on its own, on a timer — nobody has to open a chat and ask."
- **Skill** → "one job the agent knows how to do" (e.g. write a digest, check a wallet, audit a site).
- **Commit** → "saved into the repo's history, not just shown once and gone."
- **Fork** → cut entirely; not explained on screen, not needed for this audience.

## Assets checklist

- [ ] Screen capture: `nadai2010.github.io/aeon` full scroll, desktop resolution — **capture day-of** (page content can change)
- [ ] Screen capture: click-through from card → Actions run for `#36006300827`, `#36008059766`, `#36009830256` — **capture day-of**
- [ ] Screen capture: `output/articles/project-lens-2026-09-24.md` rendered on GitHub — **capture day-of**
- [ ] Screen capture: repo root file tree showing `aeon.yml` and `skills/`
- [ ] Lower-third graphic: "run #" caption style used across cuts (keep consistent template)
- [ ] End card: URL card asset

## Anti-tells checklist

- [ ] No "game-changer" / "revolutionary" / "insane" / "let's dive in" / "in this video" anywhere in VO
- [ ] Don't call this "thousands of runs" or otherwise inflate — say ten, because ten is what's linked and countable
- [ ] Don't repeat the page's own "13 tested runs" stat in VO — it isn't reconcilable against the ten linked cards (see Verify list) and this script only asserts what was independently counted
- [ ] Don't dunk on staged agent demos by name — describe the problem, not a competitor
- [ ] On-screen captions reworded from VO, not verbatim repeats
- [ ] Straight-talk section stays flat, no music swell, no minimizing language before or after it

## Verify before recording

- [ ] Confirm `nadai2010.github.io/aeon` still resolves and still shows the same page (HTTP 200 confirmed 2026-09-25; re-check day-of — GitHub Pages can lag a redeploy)
- [ ] Re-open run `#36006300827`, `#36008059766`, `#36009830256` and confirm they still show `completed` / `success` (confirmed 2026-09-25)
- [ ] Reconcile the page's "13 tested runs" stat vs. the 10 "Verify the run" links actually present — either the page undercounts its links or the stat includes unlisted runs; get this from the operator before repeating either number on screen
- [ ] Re-check skill count: page says "84 skills," the `skills/` directory currently lists 85 (includes `video-script` itself) — confirm which number the operator wants quoted, or cut the number from VO
- [ ] Confirm `output/articles/project-lens-2026-09-24.md` is still present at that path on `main`

## Receipts

- Showcase page live at `https://nadai2010.github.io/aeon/` — HTTP 200, verified 2026-09-25.
- Run `#36006300827` ("skill: digest (AI agents)") — `status: completed`, `conclusion: success`, `created_at: 2026-09-24T13:32:00Z`. Source: `gh api repos/Nadai2010/aeon/actions/runs/36006300827`, verified 2026-09-25.
- Run `#36008059766` ("skill: defi-overview") — `status: completed`, `conclusion: success`, `created_at: 2026-09-24T14:01:xx Z` range per page. Source: `gh api`, verified 2026-09-25.
- Run `#36009830256` ("skill: github-monitor") — `status: completed`, `conclusion: success`, `created_at: 2026-09-24T14:01:59Z`. Source: `gh api`, verified 2026-09-25.
- Run `#36011187240` ("skill: unlock-monitor") — `status: completed`, `conclusion: success`, `created_at: 2026-09-24T14:13:10Z`. Source: `gh api`, verified 2026-09-25.
- `output/articles/project-lens-2026-09-24.md` exists on `main`. Source: `gh api repos/Nadai2010/aeon/contents/output/articles/project-lens-2026-09-24.md`, verified 2026-09-25.
- Repo `Nadai2010/aeon` created `2026-09-24T13:21:00Z` (this fork is one day old as of script-writing). Source: `gh api repos/Nadai2010/aeon`, verified 2026-09-25.
- `skills/` directory currently lists 85 entries (page states 84 — see Verify list). Source: `gh api repos/Nadai2010/aeon/contents/skills`, verified 2026-09-25.
- Showcase page links exactly 10 distinct "Verify the run" Actions URLs, not the 13 the hero stat states (see Verify list). Source: manual count of `docs/index.html`, verified 2026-09-25.
