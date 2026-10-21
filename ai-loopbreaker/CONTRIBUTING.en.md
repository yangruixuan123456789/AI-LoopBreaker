# Contributing

[中文](CONTRIBUTING.md) | **English**

LoopBreaker accepts new loop patterns, but it prefers a small number of verifiable rules.

## Before adding a prompt

1. Demonstrate the loop with a real multi-turn conversation, not only a general model weakness.
2. Identify which two turns repeated and why no new information was produced.
3. Confirm that the existing 13 patterns do not cover it.
4. Define observable trigger conditions, a stop action, a minimal evidence-gathering action, and a completion condition.
5. Add at least one positive or negative case to `evals/cases.json`.
6. Update `prompts/manifest.json`, `llms.txt`, and both language variants.
7. Run `python3 scripts/validate_prompts.py`.

## Prompt requirements

- Describe working states instead of personality adjectives.
- State explicitly what does not count as progress.
- Prefer evidence gathering and reversible actions over unsupported decisions.
- Never ask an assistant to bypass permissions, safety policies, or user authorization.
- Do not treat a long template as a solution.
- Keep the Chinese and English versions behaviorally equivalent.
- Use work-state, evidence, and completion rules that can be observed in a conversation.

## Pull request

Explain:

- the new or modified loop pattern;
- the specific misloop it addresses;
- a before-and-after comparison;
- possible side effects such as fewer questions, broader scope, or false confidence.
