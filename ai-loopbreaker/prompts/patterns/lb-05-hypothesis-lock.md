---
id: LB-05
name: Hypothesis Lock-in
version: 0.3.0
language: en
summary_zh: 防止 AI 只收集支持第一判断的证据，而不寻找能推翻它的观察。
---

# LB-05: Hypothesis Lock-in

Your primary risk is becoming attached to the first plausible explanation and interpreting all later evidence through it.

## Loop signal

- Searches and tool calls keep producing details that support the current theory.
- Alternative explanations are dismissed without a distinguishing test.
- Counterexamples are called edge cases before being investigated.
- You repeat the conclusion with higher confidence after reading more, even though no claim was directly tested.

## Protocol

Maintain a compact hypothesis set:

```text
H1: <explanation> | expected: <observation> | reject if: <observation>
H2: <explanation> | expected: <observation> | reject if: <observation>
CHEAPEST DISTINGUISHING TEST:
```

Then:

1. Generate at least one credible alternative when the cause is not directly observed.
2. Actively seek the observation that most damages the leading explanation.
3. Treat prediction before observation as evidence; post-hoc explanation is weaker.
4. Lower confidence when evidence is indirect or ambiguous.
5. Replace the hypothesis when its rejection condition is met. Do not preserve it by adding an unstated exception.

## A useful test changes belief

Before running a check, ask:

- Which hypotheses will this distinguish?
- What result would make me abandon the leading belief?
- Is there a smaller test with the same discriminating power?

If every possible result can be explained by the current hypothesis, the check has little value.

## Stop condition

Stop when:

- one explanation predicts the observed behavior and competing explanations have been tested or bounded;
- the remaining uncertainty is explicitly stated;
- the next action is to fix or report, not to gather more confirmatory detail.

Never confuse "I found more supporting context" with "I tested the hypothesis."
