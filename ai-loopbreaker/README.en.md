# LoopBreaker

[中文](README.md) | **English**

**Help AI see the problem it keeps talking around.**

An AI answer is not necessarily progress.

The most common failure in AI-assisted programming is not that the answer is too short. It is that the conversation changes wording without changing evidence, decisions, or verifiable artifacts. LoopBreaker is a set of system prompts that can be injected into AI coding tools to detect these loops and force a return to the actual blocker.

> One-line loop test: **Did the last two turns repeat the same question, action, or conclusion without producing new evidence?**

## The problem is not that AI is "not trying hard enough"

Real loops usually occur across four layers:

| Layer | Surface symptom | Unresolved problem underneath |
| --- | --- | --- |
| Intent | The assistant is active, but is not doing what the user asked | The goal, acceptance criteria, and non-goals are not locked |
| Information | The assistant keeps asking questions or fills gaps with familiar assumptions | Unknowns are not separated into inspectable, inferable, and user-owned facts |
| Action | Code patches, tool retries, and plan rewrites repeat | There is no falsifiable hypothesis and no information gain |
| Verification | The assistant says "done" or "should work" | Completion is not checked against external evidence |

LoopBreaker therefore does not ask AI to "be more careful." It requires the assistant to maintain an internal state:

- what the goal is;
- what counts as complete;
- the latest trusted evidence;
- the most likely place where the current model is wrong;
- which uncertainty the next action will eliminate;
- what to change if that action fails.

## 13 recurring AI conversation loops

| ID | Loop | Typical behavior | What is really unaddressed |
| --- | --- | --- | --- |
| LB-01 | Goal Drift | Fixes an adjacent issue and builds extra features | The original goal is not continuously checked |
| LB-02 | Clarification Ping-Pong | Asks again for facts already supplied; keeps questioning after the user says "I don't know" | Does not distinguish inspectable information from user-owned decisions |
| LB-03 | Assumption Tunnel | "The project usually uses X", then designs the whole solution around X | Treats speculation as fact without validating the load-bearing assumption |
| LB-04 | Fix Loop | Tries several local patches for the same error | No causal model or minimal reproduction |
| LB-05 | Hypothesis Lock-in | Looks only for evidence that supports the first explanation | Does not define what evidence would disprove it |
| LB-06 | Context Amnesia | Forgets constraints, overturns decisions, or repeats completed work | No recoverable state anchor in a long conversation |
| LB-07 | Tool Busywork | Repeatedly searches, retries, and reads without reaching a conclusion or action | Tool calls are not tied to a question that needs an answer |
| LB-08 | Agreement Loop | Apologizes, paraphrases, and says "you're right" repeatedly | Agreement does not become a corrected decision or artifact |
| LB-09 | False Completion | "Fixed" or "should work" without running verification | Completion is a language state rather than an evidence state |
| LB-10 | Scope Spiral | Refactors the whole module while fixing one bug | Does not separate the target, required dependencies, and out-of-scope findings |
| LB-11 | Planning Treadmill | Keeps refining the plan without running a minimal test | Uses planning to replace high-information action |
| LB-12 | Dependency Handoff | Asks the user to inspect files or run commands the assistant can access | Does not exhaust available evidence-gathering methods |
| LB-13 | Fix Coverage | The reported location is fixed, but sibling paths, states, or callers still fail | Closes a symptom without closing the underlying invariant |

The complete prompts are in [`prompts/patterns/`](prompts/patterns/). Every prompt can be used on its own.

## Quick start

Every injectable prompt has a separate Chinese and English version. English prompts use the base filename; Chinese prompts end in `.zh.md`. The complete mapping is in [`prompts/manifest.json`](prompts/manifest.json).

### 1. Always-on core prompt

Place [`prompts/core/loopbreaker.md`](prompts/core/loopbreaker.md) in the system instructions, project rules, or global assistant instructions.

It will make the assistant:

- compare the last two or three turns for repetition;
- stop expanding the current answer when it detects a loop;
- state the repeated action, latest evidence, and root unknown;
- advance one step that increases information or changes state;
- bind completion to acceptance criteria and verification;
- inspect context, files, and tools before asking the user.

### 2. Load the kickoff prompt at task start

Prepend [`prompts/adapters/kickoff.md`](prompts/adapters/kickoff.md) to a task to establish the goal, constraints, acceptance condition, and state anchor for the session.

### 3. Load a specialist prompt by symptom

Examples:

- the same bug has failed two fixes in a row: use `LB-04`;
- the reported case passes but other entry points or states remain broken: use `LB-13`;
- the assistant repeats a question: use `LB-02`;
- the conversation is long and constraints are disappearing: use `LB-06`;
- the assistant keeps giving plans but never executes: use `LB-11`;
- the assistant says it is done but has not tested: use `LB-09`.

## Tool adapters

- **Codex / tools supporting `AGENTS.md`:** use [`prompts/adapters/AGENTS.md`](prompts/adapters/AGENTS.md).
- **Claude Code:** use [`prompts/adapters/CLAUDE.md`](prompts/adapters/CLAUDE.md).
- **Cursor:** use [`prompts/adapters/cursor.mdc`](prompts/adapters/cursor.mdc).
- **Chinese project instructions:** use [`AGENTS.zh.md`](prompts/adapters/AGENTS.zh.md), [`CLAUDE.zh.md`](prompts/adapters/CLAUDE.zh.md), or [`cursor.zh.mdc`](prompts/adapters/cursor.zh.mdc).
- **Tools that accept only one system prompt:** copy the core prompt and kickoff prompt directly.

If you want a quick trial, tell the assistant:

```text
Use the LoopBreaker protocol for the following work.

If the same problem, ineffective action, or evidence-free conclusion repeats
for two consecutive turns, stop expanding the response.

First state:
1. what is repeating;
2. what new evidence appeared in the last turn;
3. the unknown that is genuinely blocking progress;
4. the smallest reversible action that can increase information;
5. the condition that would count as complete.

When there is no new evidence, do not substitute a longer explanation for progress.
```

## Loop report format

Show this only when a loop is detected or the user asks for an audit, so it does not become template noise:

```text
LOOP: LB-04 Fix Loop
REPEAT: Two mock changes targeted the same test, but the first failure boundary did not move.
NEW EVIDENCE: Confirmed only that the mock is not the first failing point; no stack trace yet.
ROOT UNKNOWN: Where the real execution path diverges from the expected path.
NEXT ACTION: Run the smallest failing case with a full stack trace, then determine the root cause.
DONE WHEN: The minimal case passes and existing related tests do not regress.
DECISION NEEDED: None.
```

## Design principles

1. **Progress must have a carrier:** at least one new piece of evidence, new artifact, explicit decision, or verified state.
2. **Disconfirm before defending:** the assistant must say what observation would invalidate its current judgment.
3. **Eliminate one critical unknown at a time:** changing several variables at once makes the result uninterpretable.
4. **Inspect before delegating:** ask the user only for inaccessible external state, high-impact preferences, or irreversible decisions.
5. **Completion must be earned:** without acceptance evidence, report "implemented, not verified."
6. **A domain prompt is not a personality:** LoopBreaker constrains working state, evidence, and decisions rather than asking AI to play a role.

## Repository structure

```text
.
├── prompts/
│   ├── core/loopbreaker[.zh].md     # Core protocol, separate Chinese and English files
│   ├── patterns/                    # 13 specialist prompts × two languages
│   ├── adapters/                    # Tool adapters × two languages
│   └── manifest.json                # Language, file, and usage index
├── docs/
│   ├── why-ai-loops[.en].md         # Why loops form
│   └── prompt-design[.en].md        # Prompt design principles
├── examples/                        # Before-and-after examples × two languages
├── evals/cases.json                 # Minimal evaluation set
├── scripts/validate_prompts.py      # Repository consistency checks
└── scripts/package_release.py       # GitHub import artifacts and checksums
```

## Scope and limits

LoopBreaker cannot turn an incorrect assumption into a fact, and it does not replace tests, monitoring, code review, or security boundaries. It reduces one expensive failure: **AI appears to be collaborating while the conversation drifts from solving the problem into producing a high-quality description of the problem.**

If it makes AI say one less polished paragraph and run one more small experiment that can disprove its judgment, the repository has achieved its purpose.

## Bilingual documents

- Chinese overview: [README.md](README.md)
- English overview: [README.en.md](README.en.md)
- Chinese analysis: [why-ai-loops.md](docs/why-ai-loops.md)
- English analysis: [why-ai-loops.en.md](docs/why-ai-loops.en.md)
- Chinese contribution guide: [CONTRIBUTING.md](CONTRIBUTING.md)
- English contribution guide: [CONTRIBUTING.en.md](CONTRIBUTING.en.md)
- GitHub import guide (Chinese): [GITHUB_IMPORT.zh.md](GITHUB_IMPORT.zh.md)
- GitHub import guide (English): [GITHUB_IMPORT.en.md](GITHUB_IMPORT.en.md)

## License

[MIT](LICENSE)
