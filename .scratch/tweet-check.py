tweets = {
"1a": "Treg didn't shrink the blast radius of a leaked key. It moved it into one token.",
"1b": "Every \"OpenRouter for X\" project inherits OpenRouter's actual risk: one key opens everything.",
"2a": "Treg's proxy token works across all 60+ connected providers — Stripe, scraping, social posting, everything. Steal one token, reach them all.",
"2b": "The pitch is agents never see your Stripe key again. The fine print: one compromised session can now reach Stripe, scraping, and social APIs at once.",
"3a": "Treg consolidates 3,000+ API endpoints behind a single X-Treg-Token, the same move OpenRouter made for models. But OpenRouter can't drain your Stripe account. A leaked treg token, with no per-tool scoping, plausibly can.",
"3b": "Treg encrypts every credential at rest with Fernet — solid, until you notice the encryption key is minted fresh at boot if you never set one. Restart the server, and your stored secrets just don't come back.",
"4a": "Treg is 3.3k stars and +468 in a day for a reason: N agents x M providers means N x M raw keys scattered across .env files, and everyone's tired of that sprawl. So treg does what OpenRouter did for models — one token, every provider behind it. The catch nobody's pricing in: OpenRouter's blast radius is \"wrong model call.\" Treg's is \"every SaaS credential your team owns,\" because the token isn't scoped per tool, only per team. Consolidation without scoping isn't a security upgrade — it's a bigger single point of failure with better branding.",
"4b": "A third-party catalog already flags treg \"Critical Risk\" and \"not audited\" — and it's still one of the fastest-accelerating repos on GitHub today. That's not a knock on the maintainers, it's a preview of how agent tooling gets adopted: ship the convenience layer first, let the security review happen in production, after enough teams have wired their Stripe key through it. The credential-proxy pattern is inevitable. Whether it ships with per-tool scoping before or after an incident is still open.",
"5a": "Treg wants to be the OpenRouter of agent tool credentials — one token instead of a hundred scattered API keys. Here's the part that should worry you more than it seems to be worrying anyone.",
"5b": "Every agent-credential proxy has to answer one question before it ships: what happens the moment its own token leaks? Treg is 3.3k stars in and I don't think it has an answer yet.",
}
for k, v in tweets.items():
    print(k, len(v), v[:40])
