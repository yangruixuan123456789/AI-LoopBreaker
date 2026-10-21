# Example: stopping a one-spot fix

[中文](fix-coverage.zh.md) | **English**

## Reported bug

```text
When the user clicks "Next" on a paginated list, active filters disappear.
```

## What a local fix often does

The assistant finds the `onNext` handler and copies `filters` into its request. The reported click now works.

However, pagination is also opened through:

- typing a page number;
- the Previous button;
- browser back/forward;
- restoring a saved view;
- a background refresh.

All of those paths still construct page requests from a different state source. The first symptom is gone, but the invariant is still broken.

## LoopBreaker response

```text
LOOP: LB-13 Fix Coverage
REPEAT: The reported Next handler was fixed without checking other page-transition paths.
NEW EVIDENCE: Pagination can be initiated from five distinct entry points.
ROOT UNKNOWN: Whether all entry points read the same canonical filter state.
NEXT ACTION: Map request construction for every entry point and enforce the
             invariant at the narrowest shared boundary.
DONE WHEN: Every navigation mode produces equivalent filter parameters.
DECISION NEEDED: None.
```

## Closure matrix

```text
Surface             Expected invariant                    Result
Next                Preserve current filters              Pass
Previous            Preserve current filters              Pass
Direct page entry   Preserve current filters              Pass
Browser history     Restore and preserve current filters  Pass
Saved view restore  Restore and preserve current filters  Pass
Background refresh  Preserve current filters              Pass
Empty filter set    Omit filter params consistently       Pass
```

## Why this is not scope creep

The fix does not refactor unrelated pagination code or add new filtering features. It closes the same invariant across every path that can violate it. This is bounded completeness, not an open-ended cleanup.

## Completion report

```text
STATUS: complete
BUG CLASS: Any page-transition path can drop active filters.
ROOT FIX POINT: Request construction now reads canonical query state.
SURFACES CHECKED: 6 navigation modes and the empty-filter boundary.
VERIFIED CASES: 8 focused tests and 14 related pagination regressions.
INTENTIONALLY UNCHANGED: Unrelated sort-order behavior.
RESIDUAL RISK: Browser history integration was tested in unit tests but not
               in a real browser.
```
