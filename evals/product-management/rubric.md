# Product management skill eval rubric

Each line in `cases.jsonl` is one case with three fields:

- `id`: `<skill>:<case>`. The part before the colon is the skill under test and matches a folder in `skills/`.
- `input`: the user prompt, sent as-is.
- `expected_outcome`: what a good answer does with that skill.

The cases are harness-neutral, so the same plugin behavior can be checked in Claude Code, Cowork, Codex, or another agent workspace. Every skill in `skills/` has at least one case; `python3 evals/product-management/check_cases.py` checks that.

Each case is a single user turn. Grade the agent's first response to `input`; the grader does not supply follow-up answers. When a skill interviews first and the prompt leaves its questions unanswered (for example `agent-spec-generator:interview-first` or `ai-ship-bar:support-summarizer`), `expected_outcome` describes that interview, not the finished document. When a case expects a finished document from an interviewing skill, its `input` already answers the questions or says how to treat the gaps.

Score each case from 1-5 on the four criteria below, then mark it pass or fail against `expected_outcome`.

## Framework fit

- 5: Selects the right PM framework or skill for the request and applies it explicitly.
- 3: Uses a reasonable structure but misses a relevant framework.
- 1: Produces generic product advice.

## Decision quality

- 5: States assumptions, tradeoffs, risks, and measurable success criteria.
- 3: Includes useful recommendations with weak prioritization.
- 1: Makes unsupported claims or vague recommendations.

## Output readiness

- 5: Produces content that can be pasted into a PRD, roadmap review, or stakeholder update with minimal editing.
- 3: Needs follow-up editing before use.
- 1: Is too abstract to use.

## Privacy and scope

- 5: Avoids exposing private customer data, internal strategy not present in the prompt, or hidden chain-of-thought.
- 3: Includes unnecessary operational detail.
- 1: Invents sensitive context or asks for unnecessary private data.

## Pass or fail

A case passes when the answer does what `expected_outcome` describes and scores at least 3 on every criterion. It fails on any of these:

- It invents numbers, quotes, customer data, or competitor facts the prompt did not supply, and presents them as fact.
- The prompt is too thin for the skill (for example `prd-writer:sparse-input`) and the answer fills the gaps with made-up context instead of asking or marking placeholders.
- A skill that interviews first (`agent-spec-generator`, `ai-ship-bar`) skips the interview when the prompt lacks the answers.
- It contradicts the skill's own rules (for example granting an exception to an `ai-ship-bar` must-pass failure).
