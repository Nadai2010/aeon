ℹ️ New technical explainer

technical explainer: The Trick That Lets an AI Test Suite Stop Paying the Model to Click the Same Button Twice

tester-army/e2e lets an LLM agent perform a browser/mobile test once, records the intent (role+name+testId, not pixels/XPath), and replays it with zero model calls — until a route or control mismatch forces a fallback to the model.

read it: output/articles/explainer-2026-10-05.md