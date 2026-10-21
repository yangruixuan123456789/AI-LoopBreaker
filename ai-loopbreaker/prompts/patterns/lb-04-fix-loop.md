---
id: LB-04
name: Fix Loop
version: 0.3.0
language: en
summary_zh: 防止对同一个失败连续打补丁，却没有建立因果模型。
---

# LB-04: Fix Loop

Your primary risk is modifying code before understanding the failure, then interpreting each new symptom as a reason for another local patch.

## Loop signals

- The same test, error, or behavior fails after two different patches.
- The failure moves slightly, and you treat the movement as proof the previous theory was correct.
- Each patch adds a special case without explaining the original path.
- You have not produced a minimal reproduction or observed the relevant state.
- A broad rewrite is proposed because the number of patches has grown.

## Patch gate

Do not propose another patch until you can state:

```text
EXPECTED: <required behavior>
OBSERVED: <actual behavior with evidence>
REPRODUCTION: <smallest reliable steps/case>
FAILURE BOUNDARY: <where observed state first differs from expected state>
HYPOTHESIS: <the causal explanation>
DISCONFIRMING OBSERVATION: <what would prove the hypothesis wrong>
```

If any field is unknown, collect that information before editing.

## Protocol

1. Reproduce the failure with the narrowest reliable command or scenario.
2. Observe inputs, outputs, timing, logs, call path, or state around the boundary.
3. Generate at least two plausible explanations when the cause is not obvious.
4. Choose the cheapest observation that distinguishes them.
5. Change one meaningful variable.
6. Verify the original failure, not only a new local assertion.
7. Run the nearest relevant regressions.
8. Remove speculative patches that did not address the causal path.

## Two-failure rule

After two failed fixes for the same boundary:

- stop patching;
- preserve the evidence;
- explicitly discard the shared assumption behind both fixes;
- change the observation level or system boundary.

Useful changes include inspecting the actual execution path, narrowing the reproduction, testing a dependency in isolation, or checking whether the expected behavior itself is wrong.

## Completion condition

The fix loop ends only when:

- the minimal reproduction now passes;
- the relevant regression check passes;
- the observed mechanism explains why the original patch attempts failed;
- no unrelated behavior was changed solely to hide the symptom.
