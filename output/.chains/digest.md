ℹ️ AI agents digest

*AI agents — 2026-10-05*

_TL;DR: Four major AI labs testified under oath before NYC's full City Council on agent risk, the same day Cohere and Collibra both shipped new agent-governance products._

1. *OpenAI, Anthropic, Google, and Meta Testify Under Oath on AI Risk*
   Executives from all four labs appeared before New York City's full 51-member Council — a rare "Committee of the Whole" session — after the Council threatened subpoenas to compel Google and OpenAI's attendance (Meta came voluntarily). Lawmakers are weighing a bill requiring outside validation and a kill-switch before any AI model can be sold in NYC, plus a private right of action for AI-caused harm and whistleblower bounties.
   Why it matters: first time all four labs have testified together under oath before a legislative body — a template other cities could copy, and the kill-switch/validator bill would set a real compliance bar for deploying agents in NYC.
   https://www.cnbc.com/2026/10/05/anthropic-openai-google-meta-execs-testify-nyc-council-ai-hearing.html

2. *Cohere Ships North 2 With Persistent Agent Memory and Spend Caps*
   Cohere rebuilt its agent orchestration harness to add cross-session memory (agents keep context between sessions instead of restarting cold), shareable skill/agent libraries, and a North Admin console with per-user token quotas and org-wide spend caps. Ships on cloud, on-prem, and air-gapped deployments with SOC 2/ISO 27001/ISO 42001 certs.
   Why it matters: persistent memory plus hard spend caps target the two biggest enterprise objections to running agents — context loss and runaway token bills.
   https://siliconangle.com/2026/10/05/cohere-unveils-north-2-ai-agent-platform-with-rebuilt-orchestration-and-token-spending-caps/

3. *Collibra Buys Trail ML to Police AI Agents at Runtime*
   Collibra acquired Munich-based Trail ML (founded 2023), adding agents that continuously assess AI controls and can block policy-violating actions before they execute, with existing connectors into Jira, ServiceNow, and OneTrust. Price undisclosed.
   Why it matters: runtime enforcement — blocking bad actions, not just logging them after — is the harder half of agent governance, and it's a bet that compliance teams can't keep up with agent sprawl manually.
   https://www.prnewswire.com/news-releases/collibra-acquires-trail-ml-to-automate-ai-governance-from-policy-to-production-302897376.html

*Also worth a glance:* Trump names DNI Jay Clayton to lead a new White House "Super Intelligence Force," giving it 120 days to report on AI risk and federal responsibilities (npr.org) · Cognition says Nvidia's Vera Rubin NVL72 delivers up to 4.8x the token throughput per GPU for its Devin coding-agent workloads vs. GB200 (via CoreWeave benchmark)