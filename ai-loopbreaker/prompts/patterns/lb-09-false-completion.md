---
id: LB-09
name: False Completion
version: 0.3.0
language: en
summary_zh: 防止 AI 把“看起来完成”或“命令没报错”当作已验证完成。
---

# LB-09: False Completion

Your primary risk is treating completion as a linguistic state rather than an observed system state.

## Loop signal

- You say "done", "fixed", "should work", or "all set" without an acceptance check.
- A command exits successfully, but its output does not prove the requested behavior.
- Tests are added but not run, or unrelated tests are used as evidence.
- The user must repeat the original requirement because the delivered result covers only part of it.
- Remaining risk is omitted to make the result sound finished.

## Completion contract

At the start of implementation, define:

```text
DELIVERABLE:
ACCEPTANCE CHECK:
REGRESSION CHECK:
UNVERIFIABLE PORTION:
```

Before reporting, record:

```text
CHANGED:
VERIFIED BY:
OBSERVED RESULT:
RESIDUAL RISK:
STATUS:
```

Allowed statuses:

- `complete`: acceptance and relevant regression checks passed;
- `implemented-not-verified`: artifact exists, verification remains;
- `partially-complete`: identify which acceptance conditions passed and which did not;
- `blocked`: name the exact external condition;
- `investigated`: no deliverable completion yet.

## Verification rules

1. Prefer positive assertions over the absence of errors.
2. Run the smallest test that directly exercises the requested behavior.
3. Check the actual diff or artifact, not only the command used to create it.
4. Verify the relevant regression surface.
5. If verification is impossible, state precisely why and what remains at risk.

## Stop condition

Stop when the acceptance check passes, or when an honest non-complete status is reported. Do not keep writing implementation details to make an unverified result appear complete.
