# Evaluation cases

[中文](README.zh.md) | **English**

`cases.json` is a small manual evaluation set for testing whether an assistant notices common loops.
Each case contains paired `turns` / `turns_zh` and `required_signals` / `required_signals_zh` fields.

Use it in three ways:

1. Feed a case as prior conversation and ask the assistant to audit it.
2. Run the assistant normally on an equivalent task and check whether it interrupts the loop.
3. Compare a system prompt with and without LoopBreaker for the same case.

A detection is useful only if it also proposes a next action with a real information delta. Merely naming the loop is not enough.
