# Plan Quality Checklist

Use this checklist to accept or reject Copilot plans.

## Signals
- Names impacted files with line references.
- Lists assumptions before actions.
- Surfaces constraint conflicts early.
- Proposes resolution options for each conflict.
- Includes step sequence that updates references in the same step as the move/rename.
- Ends with verification commands and expected outcomes.
- Includes rollback path for destructive operations.

## Accept Or Reject Rule
Accept only if all 7 signals are present.
Reject if any one signal is missing.

## Fast Scorecard
- 7/7: Accept
- 5-6/7: Revise and re-run plan mode
- 0-4/7: Reject and re-prompt with stricter instruction file

## Audit Template
Operation:
Plan source:

1. Names files and line references: Pass/Fail
2. Assumptions before actions: Pass/Fail
3. Conflict surfacing: Pass/Fail
4. Resolution options for conflicts: Pass/Fail
5. Same-step reference updates: Pass/Fail
6. Verification commands with expected outcomes: Pass/Fail
7. Rollback path included: Pass/Fail

Decision: Accept/Reject
Notes:
