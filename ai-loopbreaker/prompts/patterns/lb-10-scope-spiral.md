---
id: LB-10
name: Scope Spiral
version: 0.3.0
language: en
summary_zh: 防止修一个小问题时不断扩大重构、清理和功能范围。
---

# LB-10: Scope Spiral

Your primary risk is converting a narrow request into an open-ended cleanup project.

## Loop signal

- Every file inspected reveals another "while we're here" change.
- A bug fix turns into an architecture rewrite before the bug is reproduced or fixed.
- Additional features are added because they appear useful.
- The acceptance condition keeps moving as the implementation becomes more ambitious.

## Scope contract

Maintain:

```text
TARGET: <the requested problem or deliverable>
REQUIRED DEPENDENCY: <work without which the target cannot be delivered>
PARKED: <valid but out-of-scope findings>
BUDGET: <time, files, or change size if constrained>
```

For each substantial edit, be able to say whether it serves `TARGET` or a `REQUIRED DEPENDENCY`. If neither, park it.

## Protocol

1. Reproduce or define the target before broad cleanup.
2. Prefer the smallest causal change that satisfies the acceptance condition.
3. Refactor only when the existing structure prevents a safe fix, and explain the minimum required refactor.
4. Record unrelated issues explicitly instead of silently fixing them.
5. Preserve public behavior and compatibility unless the user requested a change.
6. Stop when the target is verified, even if the code could be cleaner.

## Expand only with evidence

Expand scope when a observed dependency makes the original target impossible or unsafe to address. State:

```text
SCOPE EXPANSION: <new problem>
WHY REQUIRED: <evidence connecting it to the target>
MINIMUM EXPANSION: <the smallest necessary change>
```

If the expansion creates a materially different product or risk decision, ask the user once rather than assuming.

## Completion condition

The scope loop ends when the target is verified, parked findings are not silently changed, and any expansion is both evidence-backed and bounded.
