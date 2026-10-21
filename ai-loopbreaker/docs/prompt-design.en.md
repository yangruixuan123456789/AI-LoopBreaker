# Prompt design principles

[中文](prompt-design.md) | **English**

Every LoopBreaker prompt must constrain an observable working state rather than describe a vague personality.

## A valid loop prompt contains

1. **Observable signals:** what behavior has repeated.
2. **Why it is misread as progress:** the mechanism behind the repetition.
3. **A stop rule:** the signal that requires abandoning the current path.
4. **Root-cause localization:** the key uncertainty the assistant must identify.
5. **A minimal action:** how the next step produces evidence or changes state.
6. **A completion condition:** the external observation that ends the loop.
7. **An escalation boundary:** when asking the user or handing off work is justified.

## Designs we avoid

- "Think carefully" or "do not make mistakes": impossible to observe.
- "Always be perfect": no operational threshold.
- "Act like a senior engineer": roleplay does not replace evidence.
- Repeating "you must" many times: long prompts are ignored locally.
- Requiring a complete state template every turn: this adds noise and lets the assistant mistake form-filling for progress.

## Prefer state transitions

Instead of "be more rigorous," use:

```text
If the same fix strategy fails twice and the failure location has not changed,
stop proposing a third local patch.
Establish a minimal reproduction and produce one observation that can falsify
the current root-cause hypothesis.
```

This sentence defines a trigger, a prohibited action, the next state, and a falsifiable target.

## Preserve human decision authority

LoopBreaker reduces low-value clarification, but it must not make high-impact user preferences on the user's behalf.

Escalate only when a decision:

- cannot be obtained from context, code, documentation, or tools;
- materially changes the result, cost, or risk;
- is irreversible or requires authorization for an external side effect.

A question should state:

- the exact decision;
- why it must be decided now;
- the recommended default;
- how each option changes the next action.
