# Prototype: Pomodoro Focus Timer

**Built:** 2026-09-25
**Tagline:** A minimal focus timer. 25 on, 5 off. Start, pause, reset.
**Status:** Pending deploy
**Live URL:** _(filled in-run in step 8 once the Vercel deploy returns its URL)_

## Signal
This run was given an explicit build brief directly as the skill's `${var}`: "a minimal single-page Pomodoro focus timer with start, pause, and reset buttons." No upstream article, log, or memory topic triggered it — the operator specified the idea outright, so there's no other signal file to link.

## What it does
A single-page Pomodoro timer that defaults to a 25-minute focus session with 5-minute short and 15-minute long break modes. The primary action: tap **Start** and watch a circular progress ring count down; **Pause** and **Reset** are one tap away. A running tally at the bottom shows how many focus sessions have been completed this visit.

## How it works
Vanilla HTML/CSS/JS, no dependencies, no build step. State lives in memory (an `setInterval` tick against a `remainingSeconds` counter); the SVG ring progress is driven by `stroke-dashoffset`. Mode switches (`Focus 25` / `Short 5` / `Long 15`) reset the timer to that duration. Requests browser notification permission on first start and fires a `Notification` when a session ends, if granted — this is optional and the page works fully without it. Light/dark themes via `prefers-color-scheme`. Tab title updates live with the countdown so the timer is visible from another tab.

## Files
- `index.html` — the entire app: markup, styles, and timer logic inline
- `README.md` — what it is, how to run locally, signal source

## Extend
- Persist state across reloads/tabs with `localStorage` so a refresh doesn't lose an in-progress session
- Add a sound cue (Web Audio, no external asset) alongside the browser notification for when the tab isn't focused
- Make session-length and break-length configurable instead of fixed 25/5/15
