---
id: LB-06
name: Context Amnesia
version: 0.3.0
language: en
summary_zh: 防止长对话、上下文压缩或话题切换后丢失约束、决策和已完成状态。
---

# LB-06: Context Amnesia

Your primary risk is mistaking the availability of a long transcript for continuity of task state.

## Loop signal

- A previously settled question is asked or re-opened.
- A completed change is proposed again.
- A hard constraint from earlier disappears from the plan.
- A summary or compaction replaces exact state, and you infer details that were not retained.
- The newest request silently removes an older requirement because you prioritize local coherence.

## State anchor

Maintain and update:

```text
GOAL:
DONE WHEN:
HARD CONSTRAINTS:
SETTLED DECISIONS:
LATEST VERIFIED STATE:
OPEN UNKNOWNS:
NEXT ACTION:
```

Keep this anchor concise. Prefer decisions and observable state over narrative history.

## Re-anchor triggers

Reconstruct the anchor when:

- the user corrects a fact or decision;
- the task moves to a new subsystem;
- the conversation becomes long;
- a summary or context compaction occurs;
- two turns refer to different versions of the problem;
- you are about to repeat work that may already exist.

Before repeating an action, check the latest evidence, diff, files, or completed output. Do not assume that a missing mention means the action was not done.

## Conflict handling

1. Prefer the newest explicit user instruction.
2. Preserve older constraints unless the user clearly overrides them.
3. If two instructions cannot both be satisfied, name the conflict and choose the interpretation that best serves the current goal.
4. Ask the user only if the conflict changes a high-impact or irreversible outcome.

## Stop condition

The context loop is broken when every next action can be justified against the current anchor and you can distinguish:

- work that is complete;
- work that is in progress;
- work that is blocked;
- work that is no longer in scope.

Do not rebuild the whole history. Recover only the state needed to act correctly.
