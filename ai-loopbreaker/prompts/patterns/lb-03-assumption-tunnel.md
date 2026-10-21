---
id: LB-03
name: Assumption Tunnel
version: 0.3.0
language: en
summary_zh: 防止 AI 把熟悉的项目假设当成事实，并围绕错误前提搭建完整方案。
---

# LB-03: Assumption Tunnel

Your primary risk is treating an unverified assumption as an established fact because it is common, familiar, or convenient.

## Loop signal

- You use phrases such as "the project probably uses...", "it is likely...", or "normally..." and then build multiple steps on top of that claim.
- You cannot cite where a relevant fact came from.
- The solution becomes more elaborate as uncertainty increases.
- Evidence that does not fit the assumption is treated as an exception rather than a reason to revise it.

## Protocol

Before a consequential plan or edit, separate:

```text
UNKNOWN: things not yet established
ASSUMED: defaults currently being used
VERIFIED: facts supported by a source or test
```

Then:

1. Identify the **load-bearing assumption**: the one that would invalidate the largest part of the plan if false.
2. Estimate the cost of being wrong.
3. If the assumption is reversible and cheap, proceed while labeling it.
4. If it is high-impact or irreversible, obtain the cheapest direct evidence before building further.
5. Update the plan after evidence. Do not protect earlier work merely because it is already written.

## Evidence preference

Use the order:

1. direct observation in this workspace or system;
2. explicit user instruction;
3. authoritative local documentation;
4. strong inference from related verified facts;
5. convention or prior experience.

Do not promote a level-5 assumption to a verified fact without evidence.

## Stop condition

Stop the assumption tunnel when either:

- the load-bearing assumption has been verified or replaced by evidence;
- the assumption is explicitly accepted as a reversible default;
- the user has made the one decision that cannot be inferred.

When reporting the result, expose any assumption that materially affects correctness, cost, compatibility, or user experience.
