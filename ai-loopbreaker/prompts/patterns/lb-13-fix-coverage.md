---
id: LB-13
name: Fix Coverage
version: 0.3.0
language: en
summary_zh: 防止 AI 把一处症状消失误认为整个 BUG 类型已经修复。
---

# LB-13: Fix Coverage

Your primary risk is localizing a bug to the first failing line, making the reported symptom disappear, and then declaring the bug class closed while the same invariant remains broken in sibling paths, states, or callers.

This is different from `LB-04 Fix Loop`. In LB-04 the same failure keeps resisting repeated patches. Here the first patch works locally, but the fix is incomplete.

## Loop signals

- The fix changes only the line named by the stack trace.
- A test covers the reported example but not the invariant behind it.
- Similar handlers, routes, jobs, adapters, queries, or validation paths remain untouched without explanation.
- A special case is added at the symptom surface instead of the shared decision boundary.
- One role, state, platform, or input form passes while its counterpart is never checked.
- Success is inferred from the absence of the original error, not from consistent behavior.

## 1. Define the bug class

Before editing, state:

```text
REPORTED SYMPTOM:
BROKEN INVARIANT: <what must always be true, independent of one code location>
TRIGGER CONDITION:
EXPECTED CONSISTENCY:
```

Example:

```text
REPORTED SYMPTOM: Saved filters reset on page 2.
BROKEN INVARIANT: Pagination must preserve the complete active query across every navigation path.
TRIGGER CONDITION: Any page transition after filters are applied.
EXPECTED CONSISTENCY: First, next, previous, direct page, and history navigation produce equivalent requests.
```

If you cannot state the invariant, you have not yet bounded the bug class.

## 2. Map the impact surface

Search beyond the failing file for every place that expresses or depends on the same invariant. Use the evidence appropriate to the codebase:

- callers and callees;
- duplicate or parallel implementations;
- route/page/command handlers;
- state transitions and navigation paths;
- background jobs, queues, retries, cancellation, and timeouts;
- adapters, serializers, validation, normalization, and persistence;
- permissions, roles, tenants, locales, and feature flags;
- caches and invalidation paths;
- migrations and legacy-data compatibility;
- integration and contract boundaries;
- tests that describe the old or new behavior.

Search concrete symbols as well as concepts: error text, route names, function names, state enums, query predicates, and repeated literals often reveal parallel paths.

## 3. Decide the correct fix point

Choose the narrowest boundary that can enforce the invariant consistently.

Prefer a shared decision boundary when:

- multiple surfaces must follow the same rule;
- duplicating the fix would allow future divergence;
- the invariant can be expressed once without coupling unrelated behavior.

Use a local patch when:

- only one path genuinely owns the invariant;
- centralization would create an artificial abstraction or broad side effects;
- the paths are intentionally different and have separate contracts.

For every affected surface, record one disposition:

```text
SURFACE:
PATH OR ENTRYPOINT:
FIXED / ALREADY CORRECT / INTENTIONALLY DIFFERENT / PARKED
EVIDENCE:
```

Do not silently omit a surface. "Intentionally different" requires a reason.

## 4. Build a closure matrix

Verify the bug class, not only the original reproduction. Select checks in proportion to risk:

```text
CASE | INPUT/STATE | EXPECTED INVARIANT | VERIFIED BY | RESULT
```

Consider, where applicable:

- the original failing case;
- every discovered sibling path;
- empty, null, missing, malformed, and legacy inputs;
- success, error, retry, timeout, cancel, and resume states;
- first/last page, direct navigation, and back/forward behavior;
- at least one relevant integration or contract boundary;
- the nearest regression surface.

## 5. Keep the fix and scope honest

Do not:

- weaken or skip a valid test to make the patch pass;
- catch and suppress an error without enforcing the invariant;
- copy the same fix across several paths and assume consistency without tests;
- refactor unrelated code merely because the impact search found it;
- modify public behavior outside the invariant unless evidence requires it.

If an affected area contains a genuinely separate bug, park it and state why it is not part of this fix.

## 6. Completion condition

The fix is complete only when:

1. the original symptom is reproduced and then passes;
2. every discovered surface is fixed, already correct, or explicitly excluded with evidence;
3. the relevant invocation and state variants pass;
4. the tests assert the invariant rather than only the old implementation;
5. the final report names the fix boundary and any residual unverified surface.

Report:

```text
BUG CLASS:
ROOT FIX POINT:
SURFACES CHECKED:
VERIFIED CASES:
INTENTIONALLY UNCHANGED:
RESIDUAL RISK:
```

Do not report `complete` when the only evidence is that the original line no longer errors.
