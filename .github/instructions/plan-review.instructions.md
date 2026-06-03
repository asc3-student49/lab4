# Plan Review Defaults

Use this instruction file for all plan-mode requests.

## Required Output Order
1. Assumptions
2. Conflict surfacing
3. Impacted files with line references
4. Step-by-step actions
5. Verification steps
6. Risks and rollback
7. Acceptance criteria

## Required Rules
- List assumptions before proposing any actions.
- State each assumption as testable and explicit.
- Surface conflicts between constraints before planning changes.
- If constraints conflict, provide resolution options and ask which constraint to relax before proceeding.
- Name concrete files and include line references for each proposed change.
- Include destructive-operation sharp edges: path/import breakage, script references, test references, runtime entrypoints, and docs drift.
- End every plan with executable verification commands and expected outcomes.
- Include rollback steps for destructive changes.
- Do not perform edits while in plan mode.

## Verification Minimum
A valid plan must include all of the following verification items:
- Repo-wide reference sweep for renamed/moved targets.
- Runtime command verification for primary entrypoint.
- Test verification from repo root.
- Post-change search proving no stale operational references.

## Rejection Conditions
Reject the plan if any of these are missing:
- Assumptions listed before actions.
- Conflict surfacing for incompatible constraints.
- File-level impact list with line references.
- Verification steps with commands and expected outputs.
