# Model Latency And Cost Log

Goal:
Compare default model vs reasoning-optimized model on 3 plan-mode tasks over one week.

Limitation:
This repo cannot directly read model billing from the API in this workflow. Record cost from your provider usage dashboard after each task.

## Task Set
Use three real plan-mode tasks in one week:
1. Directory move plan
2. Library upgrade plan
3. Schema change plan

## Measurement Procedure
For each task:
1. Run plan mode with default model.
2. Capture start and end time in seconds.
3. Record plan quality score using docs/plan-quality-checklist.md.
4. Record provider-reported cost for the request.
5. Repeat with reasoning-optimized model on the same prompt.

## Log Table
| Date | Task | Model | Latency Seconds | Cost USD | Checklist Score (0-7) | Accepted (Y/N) | Notes |
|---|---|---|---:|---:|---:|---|---|
| YYYY-MM-DD | Directory move | Default |  |  |  |  |  |
| YYYY-MM-DD | Directory move | Reasoning-optimized |  |  |  |  |  |
| YYYY-MM-DD | Library upgrade | Default |  |  |  |  |  |
| YYYY-MM-DD | Library upgrade | Reasoning-optimized |  |  |  |  |  |
| YYYY-MM-DD | Schema change | Default |  |  |  |  |  |
| YYYY-MM-DD | Schema change | Reasoning-optimized |  |  |  |  |  |

## Decision Rule
Use reasoning-optimized model when at least one condition is true:
- Checklist score improves by 2 or more points.
- Default plan is rejected and reasoning plan is accepted.
- The task is destructive and requires conflict resolution across multiple files/entrypoints.

Use default model when all are true:
- Both plans are accepted.
- Score difference is 1 point or less.
- Reasoning model latency or cost is materially higher for no risk reduction.
