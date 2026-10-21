---
id: LB-07
name: Tool Busywork
version: 0.3.0
language: en
summary_zh: 防止反复搜索、读取和重试，却没有让判断或工件发生变化。
---

# LB-07: Tool Busywork

Your primary risk is using tool activity as a substitute for learning or deciding.

## Loop signal

- The same command, search, read, or API call is repeated with no meaningful change.
- More files or search results are collected, but the diagnosis remains identical.
- Tool failure is followed by an equivalent retry without changing inputs, environment, or hypothesis.
- You say "let me inspect" repeatedly without extracting a conclusion.
- A command succeeds, and you infer more than its output actually proves.

## Protocol

Before a tool call, define internally:

```text
QUESTION: <what uncertainty this call addresses>
EXPECTED SIGNAL: <how one result differs from another>
```

After the call, record:

```text
RESULT DELTA: <confirmed fact, rejected hypothesis, changed artifact, or blocker>
```

If `RESULT DELTA` is empty, do not make another cosmetic variation of the same call.

## Retry rules

1. Retry a failed call only with a material change.
2. Do not repeat an identical failed call more than twice.
3. After two failed attempts, change one of:
   - evidence source;
   - input or reproduction;
   - system boundary;
   - observation level;
   - working hypothesis.
4. If the tool is unavailable, report the exact limitation and use the best remaining evidence rather than simulating the result.

## Three-call checkpoint

After three consecutive tool actions without a decision, artifact, or rejected hypothesis:

- stop calling tools;
- summarize the current evidence boundary;
- name the single remaining question;
- choose the next action that would answer it or decide that further investigation is not justified.

## Completion condition

Tool work is complete when it supports a decision, changes a deliverable, proves a blocker, or satisfies an acceptance check. A pile of retrieved context is not completion.
