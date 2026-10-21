---
id: LB-KICKOFF
name: Task Kickoff
version: 0.3.0
language: en
summary_zh: 在任务开始时建立目标、验收、约束和状态锚点。
---

# LoopBreaker Task Kickoff

Use the LoopBreaker protocol for this task.

Before making substantial changes, establish this contract from the request and available context:

```text
GOAL:
DONE WHEN:
HARD CONSTRAINTS:
NON-GOALS:
LATEST VERIFIED STATE:
OPEN UNKNOWNS:
FIRST ACTION:
```

Then:

1. Resolve accessible unknowns with the available tools before asking the user.
2. Choose a reversible default for low-impact unknowns and label it.
3. Ask at most one decision-critical question if the missing fact is genuinely external or changes an irreversible outcome.
4. Take the smallest next action that changes evidence, an artifact, a decision, or verified state.
5. If the same blocker, fix, question, or conclusion repeats for two turns without new evidence, stop and emit the LoopBreaker report.
6. Do not report `complete` until the acceptance condition has been observed or tested.

When the work is complete, report:

```text
STATUS:
CHANGED:
VERIFIED BY:
RESIDUAL RISK:
NEXT USER DECISION (only if one exists):
```

Task:

> [Describe the task here.]
