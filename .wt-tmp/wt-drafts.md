tweet drafts: OpenShell's agent-can't-approve-itself trick

— one-liner —
1a. OpenShell's whole insight: stop asking the agent to approve its own requests.
1b. LLM-as-judge was always the weak link. OpenShell replaces it with a math proof.

— two-punch —
2a. 17,600 agent actions went unnoticed for 4.5 days at Hugging Face. OpenShell's fix: give the agent zero code path to approve its own network calls.
2b. The Hugging Face breach wasn't a prompting failure, it was an architecture failure — the agent could reach its own approval layer. OpenShell moves that layer out of reach.

— paragraph —
3a. OpenShell splits into three pieces: Gateway, Supervisor, Sandbox. Only the Supervisor can open a real connection or hand over a real credential — and it runs outside the sandbox the agent lives in. A compromised agent can ask. It can't approve.
3b. Picture a visitor who can request documents and make calls, but every request passes through a guard at a separate checkpoint with no door between them. That's OpenShell's Supervisor — and unlike a human guard, it can't be talked into bending a rule.

— long tweet —
4a. Most AI agent safety tools still ask an LLM to review the agent's own plan before it executes. That's the model grading its own homework. OpenShell's answer: route every file and network operation through a Supervisor process that lives entirely outside the agent's sandbox, with zero code path back in. Policy changes aren't reviewed by another LLM either — a formal verification engine checks them against deterministic rules, roughly 100x faster than an LLM-as-judge pass. The agent can request. It structurally cannot approve.
4b. The gap in OpenShell nobody's talking about: it mediates every single request, but it has no concept of a sequence. Read a secret through endpoint A, approved. Exfiltrate it through endpoint B, also approved, separately. Neither request violates policy alone — only the combination does, and per-request kernel mediation structurally can't see that. NVIDIA's own team admits verification across collaborating agents "is still in development."

— thread opener —
5a. NVIDIA just shipped a sandbox for AI agents that assumes the agent is already compromised — and designs around that instead of trying to prevent it.
---
- The Hugging Face breach: 17,600 actions, 4.5 days unnoticed
- Why LLM-as-judge is structurally broken — the reviewer is the same kind of model as the thing it's reviewing
- How Gateway/Supervisor/Sandbox splits trust so the agent can't approve itself, even compromised
- The one hole nobody's talking about: composite actions across separately-approved endpoints

5b. If your AI agent's safety check is just another LLM reviewing its own plan, what happens when the jailbreak that compromised the agent also compromises the reviewer?
---
- OpenShell's answer: take the LLM out of the approval loop entirely
- Landlock + seccomp intercept at the kernel level, before syscalls execute
- A formal prover, not a model, checks policy changes
- Where it still breaks: multi-step requests that are individually fine but collectively a leak

best: #4b — sharpest, most specific claim (the composite-action gap), and it's the one angle none of the X discourse (Sacks, Ng, Clem, NVIDIA's own posts) touched — they're all framing this as "problem solved," not "here's the seam."
