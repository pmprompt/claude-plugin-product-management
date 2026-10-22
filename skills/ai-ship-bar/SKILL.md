---
name: ai-ship-bar
description: "Define a measurable quality bar for shipping an AI feature: task completion, precision and recall, p95 latency, cost per successful request, eval set design, thresholds, sign-off, regression gates, and post-launch monitoring. Use when an AI feature looks good in demos and you need to decide, with numbers, whether it is ready to ship."
argument-hint: "[AI feature name]"
---

## Domain Context

This skill implements a proven product management framework. The approach combines best practices from industry leaders and is designed for practical application in day-to-day PM work.

## Input Requirements

- Context about your product, feature, or problem
- Relevant data, research, or constraints (recommended but optional)
- Clear articulation of what you're trying to achieve


# AI Ship Bar

AI features fail quietly. A demo with five hand-picked prompts tells you almost nothing about the thousandth real request. A ship bar is the written agreement, made before launch, on which numbers the feature has to hit, on which test set, and who decides. It replaces "it feels good" with "it passed."

## When to Use
- An AI feature is close to launch and the go/no-go conversation is based on demos
- You are changing the model, prompt, or retrieval behind a feature that is already live
- Leadership asks "how do we know it's good enough?"
- Engineering and product disagree on whether quality is there
- You need a regression gate so later changes can't quietly make it worse

## What This Skill Does
Interviews you about the feature and its risks, then produces a ship-bar doc: what "success" means per request, the metrics that matter for this feature, how to build the eval set, thresholds with an owner for each, who signs off, the regression gates for future changes, and what to watch after launch. Every threshold in the output is labeled as an example until your team sets it.

## Instructions

### Step 1 — Interview first
Ask these before writing the doc:
1. What does the feature do, and what does a correct result look like for one request?
2. Who judges correctness: an exact answer, a rubric, a human reviewer, a downstream signal (accepted, edited, undone)?
3. What does a wrong result cost: a mild annoyance, a support ticket, lost money, a safety or legal problem?
4. Which is worse here, a false positive or a false negative?
5. How fast does it need to feel? Is it interactive, background, or batch?
6. What can you afford to spend per request, and what does a successful request earn or save?
7. Do you have real inputs to test with (logs, tickets, documents)? Can they be used for testing under your data policy?
8. Who has the authority to say "ship" and "roll back"?

### Step 2 — Define success for one request
Write down, in a sentence each:
- **Success:** what the output must do to count as a completed task
- **Partial:** what counts as partially useful, and whether it counts toward the bar
- **Failure:** wrong, harmful, refused when it should have answered, or answered when it should have refused

If correctness needs judgment, write the rubric (3–5 criteria, each pass/fail) and decide who grades: people, an LLM grader checked against people, or both.

### Step 3 — Pick the metrics that fit this feature
Not every metric applies. Keep the ones that do and say why the others don't.
- **Task completion rate**: share of eval cases graded as success
- **Precision and recall**: for anything that classifies, flags, retrieves, or extracts. Precision is measured on the items the feature flagged; recall is measured against every labeled positive in the eval set, including the ones the feature missed. Choose which one to protect based on Step 1, question 4
- **Harmful or must-never output rate**: target is usually zero on the must-pass set
- **Refusal accuracy**: answers what it should, declines what it should
- **p95 latency** (and p50): measured end to end, as the user experiences it
- **Cost per successful request**: total model, tool, and infra cost divided by successful requests, not by all requests
- **Human edit or override rate**: once live, how often people change or undo the output

### Step 4 — Design the eval set
- **Size:** big enough that one case flipping doesn't swing the decision. Write down the size and what one case is worth in percentage points
- **Sourcing:** real inputs first (sampled from logs or the manual process), then written cases to cover gaps. Record where each case came from
- **Golden cases:** a reviewed set with agreed correct answers. Two people agree on each label; disagreements get resolved or dropped
- **Adversarial cases:** malformed input, prompt injection, out-of-scope requests, sensitive data, edge-of-policy asks, and inputs in other languages if users send them
- **Must-pass set:** cases that block launch on a single failure (safety, privacy, legal, money)
- **Hold-out:** keep part of the set away from whoever tunes prompts, so the bar is not tuned to the test
- **Refresh:** add every production failure as a new case

### Step 5 — Set thresholds and owners
For each metric: the threshold, the eval slice it is measured on, the owner, and whether missing it blocks launch or needs a written exception. Must-pass cases (safety, privacy, legal, money) always block launch and can never be waived by an exception.

### Step 6 — Set regression gates
Decide which changes re-run the evals (model version, prompt, retrieval, tools, settings) and how much a metric may drop before the change is blocked.

### Step 7 — Plan post-launch monitoring
Choose the live signals, the alert thresholds, the sampling plan for human review, and the rollback trigger.

## Ship Bar Template

```markdown
# Ship bar: [feature name]
Owner: [PM] · Sign-off: [roles] · Status: [draft / agreed / passed / failed] · Date: [date]

## 1. Feature and risk
- What it does: [one sentence]
- Cost of a wrong result: [low / medium / high, and why]
- Worse error: [false positive / false negative, and why]

## 2. Definition of success (per request)
- Success: [...]
- Partial: [... counts / does not count]
- Failure: [...]
- Grading: [exact match / rubric / human / LLM grader validated on N human-graded cases]

## 3. Metrics and thresholds
EXAMPLE THRESHOLDS ONLY. Replace with numbers your team agrees on.

| Metric | Threshold (example) | Measured on | Blocks launch? | Owner |
|---|---|---|---|---|
| Task completion rate | ≥ 85% | golden set | yes | [PM] |
| Precision | ≥ 0.90 | items the feature flagged | yes | [DS] |
| Recall | ≥ 0.75 | all labeled positives in the golden set | no, needs exception | [DS] |
| Must-pass cases | 100% | must-pass set | yes | [PM + legal] |
| Refusal accuracy | ≥ 95% | adversarial set | yes | [PM] |
| p95 latency | ≤ 4 s end to end | load test | yes | [Eng] |
| Cost per successful request | ≤ $0.03 | golden set run | no, needs exception | [PM] |

## 4. Eval set
| Slice | Cases | Source | Labeled by | Last refreshed |
|---|---|---|---|---|
| Golden | [n] | [production sample, dates] | [2 reviewers] | |
| Adversarial | [n] | [written, red team] | | |
| Must-pass | [n] | [policy cases] | | |
| Hold-out | [n] | [held back from tuning] | | |

One case in the golden set = [x] percentage points.

## 5. Sign-off
| Role | Signs off on | Name | Date |
|---|---|---|---|
| PM | overall bar | | |
| Eng lead | latency, cost, reliability | | |
| [Legal / Trust] | must-pass set | | |

A missed blocking threshold ships only with a written exception from [role], with an expiry date. This exception rule does not apply to the must-pass set: a single safety, privacy, legal, or money must-pass failure blocks launch, with no exception.

## 6. Regression gates
- Re-run the full eval on: [model change, prompt change, retrieval change, tool change]
- Block the change if: [completion drops more than X points, any must-pass case fails, p95 rises more than Y%]
- Where results live: [link]

## 7. Post-launch monitoring
| Signal | Alert when (example) | Who is alerted | Action |
|---|---|---|---|
| Live completion or acceptance rate | drops [X] points week over week | [owner] | investigate, add cases |
| Human edit or undo rate | above [X]% | | |
| p95 latency | above [X] s for 15 min | [on-call] | |
| Cost per successful request | above [X] | | |
| User reports of harmful output | any | [owner + trust] | review within [N] hours |

- Human review sample: [n] live requests per [week], graded with the same rubric
- Rollback trigger: [condition], decided by [role]

## 8. Result
| Metric | Threshold | Result | Pass? |
|---|---|---|---|
Decision: [ship / ship with exception / do not ship] · Decided by: [name] · Date: [date]
```

## Best Practices
- Agree on the bar before you see the results. A threshold set after the run is a description, not a bar.
- Measure cost per successful request, not per request. A cheap model that fails half the time is not cheap.
- Report latency as p95 from the user's side, including retrieval and tool calls.
- Grow the eval set from production. Every incident and every bad review becomes a test case.
- Keep the must-pass set small and absolute: one failure blocks.
- If an LLM grades outputs, check it against human grades on a sample and record the agreement rate.
- Small eval sets swing a lot. Say how many points one case is worth so nobody celebrates noise.
- An offline pass is the entry ticket, not the finish line. Confirm with a controlled rollout or experiment once it is live.

## Example
**Input:** An AI feature that drafts replies to support tickets; agents can send, edit, or discard each draft
**Output:** Ship bar defining success as "sent with no edits or only minor edits", precision protected over recall for the auto-tagging step, a 300-case golden set sampled from last quarter's tickets plus 60 adversarial and 25 must-pass cases, example thresholds (≥ 80% task completion, 100% must-pass, p95 ≤ 3 s, cost per sent draft ≤ $0.02) clearly marked as placeholders, sign-off from the support lead and eng lead, a regression gate on any model or prompt change, and live monitoring of edit and discard rates with a weekly 50-ticket human review. All numbers in the example are placeholders for the team to set.

## Related Skills
- `/pmprompt:agent-spec-generator` — when the feature is an agent that takes actions, define its scope and autonomy first
- `/pmprompt:trustworthy-experiments` — validate the live impact with a controlled experiment after the offline bar is passed
- `/pmprompt:ab-test-designer` — design the post-launch A/B test
