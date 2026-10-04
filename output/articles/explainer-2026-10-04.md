# The Trick That Lets an AI Coding Agent Forget Everything and Still Remember It All

**Key idea in one sentence:** claude-mem doesn't keep your last coding session in context — it compresses it into a searchable database and makes the next session ask for pieces of it, instead of rereading the whole thing.

## The Setup

Every AI coding agent has the same problem: the context window ends, and so does the memory. Claude Code's native fix — a `MEMORY.md` file injected at session start — has its own ceiling: a 200-line index and a 5-file-per-turn cap, so older notes get dropped by position, not by relevance, and you never find out which ones fell off. claude-mem (thedotmack/claude-mem), today's top AI/ML riser on GitHub trending at 627 stars gained in a day on its way to 95,843 total, replaces that truncated index with a real database and a query step — context survives not because more of it is loaded, but because less of it has to be.

## The Intuition Pump

Think of the difference between keeping every email you've ever received open in fifty browser tabs versus using Gmail's search bar. The tabs approach is what a growing context window does — it's complete, but it gets heavier every session until it collapses. Search is what claude-mem does: it throws the raw tabs away but keeps an index, and when you need something, you type a few words and pull just that one thread back. The breakdown: search only finds what you can describe. If next session's question doesn't share vocabulary with how the memory was indexed, the index can't surface it — unlike the open tab, which is still readable no matter what you call it.

## How It Actually Works

1. **Capture** — five lifecycle hooks (`SessionStart`, `UserPromptSubmit`, `PostToolUse`, `Stop`, `SessionEnd`) intercept Claude Code at each of those moments and log every tool call and observation as it happens, not after the fact.
2. **Compress** — at `Stop`/`SessionEnd`, the raw observation log is handed to Claude's own Agent SDK, which rewrites it into short semantic summaries: "fixed null check in trade engine" instead of the full diff and tool output that produced it. This step is lossy by design.
3. **Store** — summaries land in a local SQLite database (`~/.claude-mem/claude-mem.db`) with FTS5 full-text indexing, plus a parallel Chroma vector store (`~/.claude-mem/chroma/`) for semantic (embedding) search alongside keyword search.
4. **Serve** — a background worker service, managed by Bun, runs a local HTTP API (and a web viewer) so queries don't have to reload the database cold each time.
5. **Inject** — on the next `SessionStart`, claude-mem doesn't paste the full history back in; it injects only what's judged relevant right now.
6. **Query on demand** — if Claude needs more, the `mem-search` skill exposes a three-layer progressive-disclosure query: `search` returns a thin index (~50-100 tokens per hit), `timeline` reconstructs what happened around a hit, and `get_observations` fetches the full original detail (500-1,000 tokens) — but only for the hits worth expanding.
7. **Repeat across tools** — the same hook-capture-compress-inject loop is wired into Codex, Gemini, Copilot, OpenCode, and three other agent CLIs, so the memory store outlives any single tool, not just a single session.

## Numbers That Anchor It

- 95,843 stars / 8,471 forks as of today, up from a project created 2025-08-31 — thirteen months to become one of GitHub's most-forked agent-memory tools ([github.com/thedotmack/claude-mem](https://github.com/thedotmack/claude-mem))
- ~10x token savings claimed from the search → timeline → get_observations progressive disclosure versus dumping full history back into context ([thedotmack/claude-mem README](https://github.com/thedotmack/claude-mem))
- 89 open issues on the repo right now — a maturity signal, not a defect count, for a tool this widely forked ([github.com/thedotmack/claude-mem](https://github.com/thedotmack/claude-mem))
- A rival project, claude-mem-lite, claims ~600x lower cost by batching observations into 5-8 episode-level LLM calls per 50-tool-call session instead of ~50 per-tool-use calls, cutting total tokens from an estimated 100K-250K down to 1K-4K ([github.com/sdsrss/claude-mem-lite](https://github.com/sdsrss/claude-mem-lite)) — a direct bet that claude-mem's per-tool-call compression step is the expensive part of the design
- The native problem this architecture is answering: Claude Code's built-in `MEMORY.md` caps out at a 200-line index with 5 files processed per turn, after which older entries silently stop being read ([mem0.ai: How Claude Code Memory Actually Works](https://mem0.ai/blog/how-memory-works-in-claude-code))

## What Would Break This

If a user's next-session question uses different words than the compressed summary did — "that bug we fixed" versus a stored observation phrased as "resolved null pointer in trade engine" — and the embedding search also fails to bridge the gap, the fact is retrievable in principle (it's in the database) but invisible in practice (it never surfaces). That's a different failure mode than `MEMORY.md`'s position-based truncation, not a cure for the category of failure: important context going silently missing.

## Why It Matters

Anyone running long-lived agent sessions — a solo dev iterating on one codebase for months, not just one sitting — hits the same wall claude-mem is built around: context windows reset, but the work doesn't. Splitting memory into a cheap-to-query index plus an on-demand detail fetch is the same shape as how search engines, not browser tabs, scaled to the size of the web. Whether that shape holds here depends on whether compression keeps the right 10% and whether retrieval can find it again under a different name next time.

## Sources
- [thedotmack/claude-mem — GitHub](https://github.com/thedotmack/claude-mem) — primary, repo README and metadata
- [thedotmack/claude-mem — CLAUDE.md](https://github.com/thedotmack/claude-mem/blob/main/CLAUDE.md) — primary, internal architecture notes
- [sdsrss/claude-mem-lite — GitHub](https://github.com/sdsrss/claude-mem-lite) — competing cost benchmark claim
- [How Claude Code Memory Actually Works: MEMORY.md, Auto Dream, 200-Line Limit — mem0.ai](https://mem0.ai/blog/how-memory-works-in-claude-code) — the native-memory limit this project answers
