tweet drafts: Hindsight's four-memory architecture (vectorize-io/hindsight)

— one-liner —
1a. Hindsight's real trick isn't retrieval — it's refusing to ever delete a memory.
1b. Most memory tools store transcripts. Hindsight stores opinions — and updates them.

— two-punch —
2a. 27K tokens per Hindsight query vs ~7K for Mem0. It's not cheaper memory — it's memory you pay 4x more to read.
2b. Everyone building agent memory right now is really deciding one thing: a growing archive to search, or a belief state that updates. Hindsight bet on the second.

— paragraph —
3a. Hindsight never deletes a memory — it just downgrades the ones it stops trusting. Which is either a genuinely good design call or the exact move your uncle pulls to avoid admitting he was wrong about crypto in 2018.
3b. Someone running Hindsight inside Hermes Agent said they were speechless at how good it is, then immediately flagged that running it locally eats RAM for breakfast. That's the whole tradeoff in one thread: better recall, heavier bill.

— long tweet —
4a. Hindsight splits agent memory into four networks — facts, experiences, observations, opinions — then runs a consolidation loop: importance filtering, merge, decay, and no eviction, nothing is ever deleted, just down-weighted. Recall fires four retrieval strategies in parallel (vector, BM25, graph, time-range) and costs zero extra LLM tokens per query. The expensive part is Reflect: a periodic LLM pass that turns raw facts into standing answers. 91.4% on LongMemEval is real. So is spending ~4x the tokens per query versus Mem0 to get there — a comparison nobody's published yet.
4b. Hindsight hits 91.4% on LongMemEval and 89.6% on LoCoMo, beating the next-best open memory system by 14 points. Impressive — except it also spends ~27K tokens per retrieval vs ~7K for Mem0, a 4x premium nobody's controlled for. Give Mem0 the same token budget and rerun the benchmark: does the gap survive, or is "better memory" just "more expensive memory" wearing a research paper?

— thread opener —
5a. Every agent memory framework right now is making a bet nobody says out loud: is memory a growing archive to search, or a belief state that updates itself? Hindsight (35.1k★, +4,463 stars today) is the sharpest argument yet for the second option.
---
- The four-network split — facts, experiences, observations, opinions — and why none of them ever get deleted
- TEMPR: four retrieval strategies fused in parallel, zero extra LLM cost per query
- Reflect: the one expensive step, turning "re-derive every time" into "just read the answer"
- The 4x token bill nobody's benchmarked against a same-budget Mem0
- What Hindsight's own FAQ admits it still can't do

5b. 91.4% on LongMemEval. 89.6% on LoCoMo, 14 points clear of the next-best open memory system. Hindsight just became the sharpest riser on GitHub Trending — +4,463 stars in a day. Here's the architecture behind the number, and the cost nobody's talking about.
---
- Four memory networks instead of one vector store, and a Retain/Reflect loop that compounds instead of just growing
- TEMPR: semantic + BM25 + graph + time-range fused in parallel, recall costs zero extra tokens
- The catch: ~27K tokens per retrieval vs ~7K for Mem0 — nobody's normalized for that yet
- Real-world signal: Hermes Agent users praising recall quality, flagging local RAM cost
- What still doesn't work: no cross-bank analysis, per Hindsight's own FAQ

best: #4b — long tweet / question — sharpest hook, carries the article's strongest unresolved critique (unverified 4x token-cost comparison) in one tweet

<!-- Correlation ID: chain-4f6bc21d5d98b566400251eab5e43827 -->
