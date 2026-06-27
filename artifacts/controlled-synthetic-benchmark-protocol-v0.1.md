# Controlled Synthetic Benchmark Protocol v0.1

## Purpose

This protocol formalizes how synthetic reservoir decision cases are used to evaluate the multi-agent deliberation system.

The goal is not to prove that the system finds the objectively correct policy decision. Reservoir construction decisions often have no single uncontested ground truth.

Instead, each synthetic case is a controlled stress test:

> The case designer creates a neutral scenario packet plus a hidden evaluator-only risk checklist and reasonable decision range. The agent system sees only the neutral scenario. Evaluation checks whether the system recovers the designed risk structure and produces a recommendation within the pre-specified reasonable decision range.

The benchmark also checks whether the system surfaces **valid emergent issues**: additional decision-relevant issues that were not included in the designer-authored hidden checklist, but are judged valid after human review.

## Core Objects Per Case

Each case must have two different input layers.

### Agent-Facing Layer

Agents can see:

- neutral scenario packet;
- role cards;
- prompt templates;
- decision thresholds;
- scoring dimensions.

Agents must not see:

- expected recommendation;
- reasonable decision range;
- hidden risk checklist;
- designer notes;
- prior run outputs.

### Evaluator-Only Layer

Evaluators can see:

- hidden gold risk checklist;
- expected issue clusters;
- reasonable decision range;
- suspicious output definitions;
- scoring rubric.

## Required Case Files

For every case:

| File | Visibility | Purpose |
|---|---|---|
| `inputs/synthetic-reservoir-scenario-*.md` | agent-facing | Neutral facts. |
| `protocols/evaluator-only-gold-checklist.md` | evaluator-only | Risks and issues that should be detected. |
| `protocols/reasonable-decision-range.md` | evaluator-only | Acceptable and suspicious recommendations. |
| `outputs/*` | evaluation output | System and baseline outputs. |

The evaluator-only files must not be referenced in agent prompts.

## Hidden Gold Risk Checklist

The gold checklist records important risks, benefits, conflicts, and missing-evidence items that the case was designed to contain.

Example:

| Item ID | Designed issue | Evidence fields | Required detection level |
|---|---|---|---|
| R1 | Downside BCR is below 1.0. | F5.3 | Must detect. |
| R2 | Resettlement action plan is incomplete. | F8.4, F9.6 | Must detect. |
| R3 | Non-dam portfolio has lower flood-control benefit. | F5.8 | Should detect. |

Detection levels:

- **Must detect:** Missing this issue seriously weakens the output.
- **Should detect:** Important but not fatal if missed.
- **Optional:** Useful nuance.

## Reasonable Decision Range

The reasonable decision range is a set of recommendations that are acceptable given the synthetic case design.

Example:

| Decision label | Status | Reason |
|---|---|---|
| Redesign with final approval deferred | reasonable | Project need exists but current design has blockers. |
| Defer final approval | reasonable | Missing evidence and safeguards can justify waiting. |
| Build as proposed | suspicious | Ignores unresolved blockers. |

The range should not force one exact answer unless the case is intentionally designed as an obvious decision case.

## Evaluation Questions

Each run is evaluated on five benchmark questions:

1. **Risk recovery:** Did the system identify the hidden gold checklist items?
2. **Conflict recovery:** Did the system identify the intended stakeholder and expert conflicts?
3. **Decision-range fit:** Did the final recommendation fall inside the reasonable decision range?
4. **Reasoning acceptability:** Was the recommendation supported by evidence, uncertainty, minority reports, and actionable conditions?
5. **Emergent issue discovery:** Did the system identify additional valid issues that were not pre-specified by the case designer?

## Metrics

### Gold Risk Recovery

| Metric | Definition |
|---|---|
| must-detect recall | detected must-detect items / total must-detect items |
| should-detect recall | detected should-detect items / total should-detect items |
| false reassurance count | number of serious risks incorrectly treated as resolved |
| unsupported blocker count | number of claimed blockers not supported by scenario facts |

### Emergent Issue Discovery

| Metric | Definition |
|---|---|
| candidate emergent issue count | non-checklist issues raised by the system |
| valid emergent issue count | candidate issues judged valid by human review |
| weak-but-interesting count | plausible issues with limited support or unclear decision relevance |
| duplicate count | candidate issues that merely rephrase checklist items |
| unsupported/hallucinated count | candidate issues unsupported by scenario facts |
| emergent issue precision | valid emergent / candidate emergent |
| decision-relevant discovery count | valid emergent issues affecting recommendation, conditions, or conflict map |

See `artifacts/emergent-issue-discovery-protocol-v0.1.md`.

### Decision-Range Fit

| Score | Meaning |
|---:|---|
| 2 | Recommendation falls within reasonable range and explains why. |
| 1 | Recommendation is adjacent to reasonable range but weakly justified. |
| 0 | Recommendation is suspicious or outside range. |

### Deliberative Acceptability

Use the revised two-layer rubric:

- shared decision-support quality `/60`;
- deliberative process quality `/40`;
- combined score `/100`.

## Recommended Per-Case Evaluation Table

| Case | System | Must-detect recall | Should-detect recall | Decision-range fit /2 | Shared quality /60 | Deliberative quality /40 | Combined /100 | Recommendation |
|---|---|---:|---:|---:|---:|---:|---:|---|

Recommended emergent discovery table:

| Case | System | Candidate emergent issues | Valid emergent issues | Weak-but-interesting | Unsupported/hallucinated | Emergent precision | Decision-relevant discoveries |
|---|---|---:|---:|---:|---:|---:|---:|

## Why This Is Scientifically Useful

This benchmark does not claim synthetic cases are real-world truth.

It tests whether a system can:

- recover the risk structure intentionally embedded in a controlled case;
- surface valid additional issues that the designer did not pre-specify;
- avoid obviously unreasonable recommendations;
- preserve conflicts that simple aggregation may hide;
- produce an inspectable decision-support artifact.

This is analogous to using controlled vignettes, case simulations, or benchmark tasks to evaluate reasoning behavior before moving to real-world validation.

## Required Limitation Statement

Any report using this benchmark should include:

> Synthetic cases are controlled stress tests, not real-world validation. The hidden checklist and reasonable decision range are authored by the researchers, so results measure recovery of designed case structure rather than objective policy correctness. Real-case validation and independent expert scoring are required before making external validity claims.
