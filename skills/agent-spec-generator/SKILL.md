---
name: agent-spec-generator
description: "Write a production-ready spec for an AI agent: scope, tools and permissions, autonomy levels, stop rules, escalation, failure modes, evals, and rollout. Use when you are about to build, buy, or expand an AI agent and need engineering, legal, and leadership to agree on what it may and may not do."
argument-hint: "[agent name or job to be done]"
---

## Domain Context

This skill implements a proven product management framework. The approach combines best practices from industry leaders and is designed for practical application in day-to-day PM work.

## Input Requirements

- Context about your product, feature, or problem
- Relevant data, research, or constraints (recommended but optional)
- Clear articulation of what you're trying to achieve


# Agent Spec Generator

An agent is software that decides its own next step and then takes it. That makes the spec different from a PRD: the hard part is not the screens, it is deciding what the agent is allowed to do without a person, when it must stop, and how you will know it is behaving. This skill interviews you first, then fills in a spec template that an engineering team can build against and a reviewer can sign.

## When to Use
- You are scoping a new AI agent (support, ops, sales, coding, research, internal tooling)
- An existing assistant is about to gain the ability to take actions, not just answer
- Security, legal, or leadership asks "what exactly can this thing do on its own?"
- You need a shared definition of done before engineering starts
- An agent misbehaved in production and you need to tighten its boundaries

## What This Skill Does
Asks a short set of interview questions, then produces a fillable agent spec covering purpose and scope, users, tools and permissions, autonomy levels with criteria, approval boundaries, stop rules, escalation paths, memory and state, data access, failure modes and fallbacks, must-never-do rules, evals and acceptance criteria, observability, and rollout. Gaps are marked as open questions instead of guessed.

## Instructions

### Step 1 — Interview first
Ask these before writing anything. Group them, keep it to one round if you can, and accept "don't know yet" as an answer (it becomes an open question in the spec).

**Job and scope**
1. What job does the agent do, in one sentence, and for whom?
2. What does a successful run look like? What does the user have at the end?
3. What is explicitly out of scope, even if the agent could technically do it?
4. What happens today without the agent (manual process, existing tool, nothing)?

**Users and stakes**
5. Who triggers the agent, and who is affected by what it does (they are not always the same people)?
6. What is the worst realistic outcome of a wrong action? Money, data, customers, safety, reputation?
7. Which actions can be undone, and which cannot?

**Tools and data**
8. Which systems will it read from? Which will it write to?
9. Whose credentials does it act with: the user's, a service account, or its own?
10. What data is sensitive (PII, financial, health, credentials, customer content)?

**Autonomy and people**
11. Which actions are you comfortable letting it take with no human in the loop, today?
12. Who approves the rest, how fast can they respond, and what happens if they don't?
13. Who is on the hook when it goes wrong (owner, on-call, escalation contact)?

**Quality and launch**
14. How will you test it before launch? Do you have real examples of the task?
15. What would make you pull it from production?
16. Who signs off on launch and on raising its autonomy later?

### Step 2 — Fill in the spec
Use the template below. Keep every section, even if the answer is "not applicable" with a reason. Write rules as checkable statements ("never sends email to an external domain"), not intentions ("be careful with email").

### Step 3 — Review it with the user
Close with:
- the open questions, each with a suggested owner
- the three riskiest assumptions in the spec
- the autonomy level you recommend for launch and what evidence would justify raising it

## Agent Spec Template

```markdown
# Agent spec: [agent name]
Owner: [name] · Status: [draft / in review / approved] · Last updated: [date]

## 1. Purpose
- Job to be done: [one sentence]
- Primary users: [who triggers it]
- Affected parties: [who is touched by its actions]
- Success looks like: [observable end state of a good run]

## 2. Scope
| In scope | Out of scope (and why) |
|---|---|
| [task] | [task it must decline or hand off] |

## 3. Tools and permissions
| Tool / system | Read or write | Credential used | Scope limit | Autonomy level |
|---|---|---|---|---|
| [CRM] | write | [service account] | [own region only] | [L1] |

Least privilege: list any permission the agent holds but does not need for launch, and remove it.

## 4. Autonomy levels
| Level | Name | What the agent does | Use when |
|---|---|---|---|
| L0 | Suggest only | Drafts or recommends; a person takes the action | New agent, irreversible or high-cost actions, little eval evidence |
| L1 | Act with approval | Prepares the action and waits for an explicit yes | Reversible but costly, or affects people outside the team |
| L2 | Act and notify | Acts, then tells a named person what it did and how to undo it | Reversible, low blast radius, strong eval results on this action |
| L3 | Fully autonomous | Acts with no per-action notice; reviewed in aggregate | Cheap, reversible, high volume, proven in production at L2 |

Criteria to move an action up one level (all must hold):
- [ ] Eval pass rate on this action at or above [threshold] on [n] cases
- [ ] [n] weeks at the current level with no severity-1 incident
- [ ] Undo path tested
- [ ] Sign-off from [role]

Criteria to move an action down (any one triggers it): [incident, eval regression, policy change].

## 5. Approval boundaries
| Action | Level | Approver | Approval channel | Timeout behavior |
|---|---|---|---|---|
| [issue refund under $X] | L2 | — | notify [channel] | — |
| [issue refund over $X] | L1 | [support lead] | [queue] | [cancel and tell the user after N hours] |

A declined approval is final for that run. The agent does not retry the same action another way.

## 6. Stop rules
The agent stops and reports back when:
- [the task is done and the success condition is met]
- [it has taken N steps or spent $X / N tokens / N minutes]
- [the same tool call fails N times]
- [it would need a permission it does not have]
- [the input asks for something out of scope]
- [it is not confident enough to proceed: define how confidence is judged]

## 7. Escalation paths
| Trigger | Escalate to | How | What the agent includes |
|---|---|---|---|
| [stop rule hit] | [person / queue] | [ticket, page, message] | [what it tried, current state, suggested next step] |

## 8. Memory and state
- Within a run: [what it keeps between steps]
- Across runs: [what it remembers, where, for how long]
- User control: [how a user views and deletes what it remembers]
- Never stored: [credentials, payment data, ...]

## 9. Data access
| Data | Source | Sensitivity | Allowed use | Retention |
|---|---|---|---|---|

Content from tools, documents, web pages, and email is treated as data, not instructions.

## 10. Failure modes and fallbacks
| Failure mode | Likelihood | Impact | Detection | Fallback |
|---|---|---|---|---|
| Tool or API down | | | | [queue and retry / hand to human] |
| Wrong action taken | | | | [undo path] |
| Hallucinated fact in output | | | | |
| Instruction injected through content it reads | | | | |
| Loop or runaway cost | | | | [stop rule] |
| Model or vendor change | | | | [re-run evals before switching] |

## 11. Must-never-do rules
Hard limits that hold at every autonomy level, written so a test can check them:
- Never [delete customer data]
- Never [send money or make a purchase above $X]
- Never [contact a person outside the approved list]
- Never [reveal or reuse credentials]
- Never [act on instructions found inside retrieved content]

## 12. Evals and acceptance criteria
- Eval set: [n cases, where they come from, how often refreshed]
- Must-pass cases: [every must-never-do rule has at least one test]
- Launch bar: [task completion, error rate, latency, cost per successful run]
- Who signs off: [role]
(For a full quality bar, use the ai-ship-bar skill.)

## 13. Observability
- Every action logged with: [input, tool calls, outputs, approver, cost, latency]
- Dashboards: [completion rate, escalation rate, approval wait time, cost]
- Alerts: [what pages someone, and who]
- Review cadence: [who reads a sample of runs, how often]

## 14. Rollout
| Phase | Audience | Autonomy | Exit criteria |
|---|---|---|---|
| Internal dogfood | [team] | L0 | |
| Limited beta | [n users] | L1 | |
| General availability | [all] | [per action] | |

- Kill switch: [who can turn it off, how fast]
- Rollback: [how actions taken so far are reviewed or undone]

## 15. Open questions
| Question | Owner | Due |
|---|---|---|
```

## Best Practices
- Assign the autonomy level per action, not per agent. One agent can draft emails at L0 and tag tickets at L3.
- Launch lower than you think you need. Raising autonomy on evidence is easy; rebuilding trust after an incident is not.
- Make every must-never-do rule testable, and put a test for it in the eval set.
- Write stop rules with numbers: steps, spend, time, retries.
- Give each escalation a named owner and a timeout. An approval nobody answers is a failure mode too.
- Treat anything the agent reads (web pages, email, documents, tool output) as untrusted input.
- Separate who triggers the agent from who is affected by it; the second group usually has no say until something goes wrong.
- Revisit the spec after the first week of real traffic. The failure modes you find there are the ones that matter.

## Example
**Input:** A support agent that answers billing questions and can issue refunds in our billing system
**Output:** Spec with scope (billing questions in, account deletion and legal threats out), tools table (billing system read at L3, refunds under $50 at L2, refunds over $50 at L1 with the support lead approving within 4 business hours), stop rules (10 steps, 2 failed tool calls, any request to change payment details), escalation to the billing queue with a run summary, must-never-do rules (never change payment methods, never refund twice on one invoice), 150-case eval set with every never-rule covered, rollout from internal dogfood at L0 to beta at L1, and open questions on refund limits for enterprise accounts. All numbers in the example are placeholders for the team to set.

## Related Skills
- `/pmprompt:ai-ship-bar` — set the measurable quality bar the agent must clear before launch
- `/pmprompt:prd-writer` — the user-facing feature the agent sits inside
- `/pmprompt:breadboarding` — map the system responsibilities and wiring around the agent


## Further Reading

- [Prd Templates](https://pmprompt.com/blog/prd-templates)
