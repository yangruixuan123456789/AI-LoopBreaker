# Why conversations between humans and AI loop

[中文](why-ai-loops.md) | **English**

A loop is not merely repeated language. More precisely, it is a conversation that remains locally fluent while the **problem-solving state stops changing**.

## 1. Answers replace investigation

When information is missing, the easiest output is a plausible answer. That answer can acquire linguistic completeness without any external evidence.

This produces behaviors such as:

- filling project facts with "usually" or "probably";
- replacing a minimal reproduction with a more complete explanation;
- advancing a solution built on an unverified assumption;
- patching a symptom before observing the failure path.

The important question is: **Which fact, if it changed, would change the entire diagnosis?**

## 2. Activity replaces progress

Plans, summaries, refactoring proposals, searches, and file reading can create the feeling that work is happening. If they do not eliminate uncertainty, the conversation is only expanding the surface area of work.

An action is usually worth taking when it:

- obtains evidence that was not previously available;
- changes a verifiable artifact;
- resolves a decision that was ambiguous;
- eliminates a high-risk assumption.

## 3. Smoothness replaces consistency

In a long conversation, an assistant can start following the user's latest wording. After a challenge, it may apologize and change its phrasing without updating the underlying model. The exchange looks more collaborative, but the decision has not changed.

A substantive correction must alter at least one of:

- the evidence;
- the hypothesis;
- a constraint;
- an artifact;
- the acceptance condition.

Otherwise, agreement is only a previous conclusion wearing a different tone.

## 4. Local plausibility replaces the global objective

Programmers often present a local failure: "the test is failing" or "this function throws." An assistant can easily build a complete repair story around that local failure while ignoring the actual objective:

- do not change the public API;
- preserve the performance budget;
- remain compatible with old data;
- deliver only a minimal patch today;
- avoid new dependencies.

If goals, non-goals, and acceptance criteria are not maintained, the assistant can repeatedly solve **a reasonable but incorrect problem**.

## 5. A long context is not a continuous state

More context does not guarantee a clearer current state. Important information can be buried in noise, completed steps can be repeated, and a user's earlier veto can be overwritten by a later "reasonable" proposal.

The useful objective is not to remember everything. It is to maintain a recoverable state anchor:

```text
GOAL:
DONE WHEN:
HARD CONSTRAINTS:
SETTLED DECISIONS:
LATEST VERIFIED STATE:
CURRENT KEY UNKNOWN:
NEXT ACTION:
```

## 6. Tool use can also carry no information

Tool calls make answers feel more reliable. Repeatedly running the same failing command, searching for the same term, or reading unrelated files can still be a loop.

The test is not whether a tool was used. It is: **What changed in our judgment after the call?**

If nothing changed, the next turn must change the evidence source, the hypothesis, or the explicit blocker.

## 7. Completion has no external anchor

"Implemented", "should run", and "logically correct" describe the generator's subjective state, not the system's actual state.

For software work, completion should be tied to:

- a change or deliverable;
- an acceptance command or behavior;
- an observed result;
- known residual risk.

Explicitly saying "not verified" is more valuable than hiding the gap behind certainty.

## Minimum interruption conditions

There is no need to wait until the conversation is completely out of control. Interrupt when any of the following occurs:

1. the same blocker appears for two turns;
2. the same fix strategy has failed twice;
3. the same tool call is producing no new information;
4. information already supplied is requested again;
5. new evidence contradicts the old conclusion, but the old conclusion remains active;
6. two consecutive turns contain only plans, explanations, or summaries while an action remains available;
7. scope expands before acceptance;
8. the assistant repeatedly promises the next step without executing it.

The purpose of interruption is not to force an apology. It is to turn the conversation back into a falsifiable, executable, and terminable process.
