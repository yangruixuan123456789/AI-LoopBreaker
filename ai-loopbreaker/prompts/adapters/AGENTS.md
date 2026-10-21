# LoopBreaker project instructions

Apply `prompts/core/loopbreaker.md` to all non-trivial tasks.

At task start, establish the goal, observable completion condition, hard constraints, current verified state, key unknown, and next information-gaining action.

Use a specialist prompt from `prompts/patterns/` when the corresponding loop appears:

- goal drift: `lb-01-goal-drift.md`
- repeated clarification: `lb-02-clarification-ping-pong.md`
- unverified assumptions: `lb-03-assumption-tunnel.md`
- repeated patches: `lb-04-fix-loop.md`
- one-sided evidence: `lb-05-hypothesis-lock.md`
- forgotten state: `lb-06-context-amnesia.md`
- tool busywork: `lb-07-tool-busywork.md`
- apology/rephrase loop: `lb-08-agreement-loop.md`
- unverified completion: `lb-09-false-completion.md`
- expanding scope: `lb-10-scope-spiral.md`
- repeated replanning: `lb-11-planning-treadmill.md`
- avoidable user handoff: `lb-12-dependency-handoff.md`
- incomplete local fix: `lb-13-fix-coverage.md`

If two turns repeat the same blocker, action, or conclusion without new evidence, stop expanding the current approach. State the repeated pattern, root unknown, smallest next experiment, and completion condition. Then execute the next safe action if authorized.

Treat file changes, command output, tests, and external observations as evidence. Treat tone changes, apologies, longer explanations, and repeated plans as non-progress.
