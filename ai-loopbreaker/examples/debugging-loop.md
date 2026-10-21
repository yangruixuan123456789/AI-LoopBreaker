# Example: breaking a repeated patch loop

[中文](debugging-loop.zh.md) | **English**

## Without LoopBreaker

```text
User: The auth integration test still fails after the timeout change.

Assistant: The likely issue is the mock clock. I'll adjust the mock.

User: Still failing.

Assistant: The mock probably needs a larger delay. I'll increase it again.

User: Same stack trace.

Assistant: The real issue may be the test runner configuration. I'll rewrite
the test setup and update the shared test harness.
```

This appears to progress because each turn contains a new diagnosis and a new patch. In reality, the root cause has not been observed. The stack trace did not change, the patch count is increasing, and the proposed scope is expanding.

## With LoopBreaker

```text
LOOP: LB-04 Fix Loop
REPEAT: Two mock-timing changes have targeted the same test, while the first
        failing boundary in the stack trace is unchanged.
NEW EVIDENCE: The timeout change did not move the failure.
ROOT UNKNOWN: Whether the auth request reaches the token exchange at all.
NEXT ACTION: Run the smallest failing case with request and token-exchange
             logging, then locate the first incorrect state transition.
DONE WHEN: The minimal auth case passes and the existing integration suite
           remains green.
DECISION NEEDED: None.
```

The second response does not solve the bug immediately. It does something more important: it changes the form of the work from speculative patching to observing the execution boundary.

## Why this works

- The repeated failure is named.
- The unchanged evidence is distinguished from the extra effort.
- The broad rewrite is rejected as an escape from diagnosis.
- The next action is small, observable, and capable of changing the hypothesis.
- Completion is defined before another patch is attempted.
