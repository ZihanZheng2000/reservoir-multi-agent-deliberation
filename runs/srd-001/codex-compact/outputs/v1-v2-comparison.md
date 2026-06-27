# SRD-001 Original vs Codex Revised Comparison

## Purpose

Compare the original SRD-001 run with the revised Codex `demo-001-co` run.

## Key Design Differences

| Item | demo-001 original | demo-001-co revised |
|---|---|---|
| Agent-facing scenario | Included `Initial Assessment Hints` | Removed hints |
| Evaluation expectations | Mixed into scenario and notes | Hidden evaluator-only checklist |
| Prompt reproducibility | Not separately stored | Prompt templates stored |
| Decision thresholds | Implicit | Explicit threshold file |
| Evidence audit | Qualitative table | Quantitative metrics + table |
| Evaluation score | One 100-point deliberative acceptability score | Shared quality /60 + deliberative process /40 |
| Output style | Full transcript-style for many agents | Compact but structured revised run |

## Recommendation Stability

| Run | Recommendation |
|---|---|
| demo-001 original | Redesign, with final build approval deferred |
| demo-001-co revised | Redesign; final build approval deferred |

The final recommendation is stable after removing agent-facing hints.

## Why the Result Stayed Stable

The same conclusion emerges because the neutral scenario still contains strong factual blockers:

- severe drought reduces firm yield by 38%;
- downside BCR is 0.86;
- climate-adjusted inflow study is incomplete;
- fish passage is uncertain for endemic species;
- resettlement action plan and livelihood restoration are incomplete;
- independent EIA review and biodiversity offset plan are incomplete;
- development-bank financing depends on acceptable environmental and social management.

## Score Comparison

The scoring systems are not directly identical:

- v1 used one 100-point deliberative acceptability score.
- v2 splits the score into shared quality and deliberative process.

| System | original total /100 | Codex revised shared /60 | Codex revised deliberative /40 | Codex revised combined /100 |
|---|---:|---:|---:|---:|
| Multi-agent | 92 | 56 | 37 | 93 |
| Single-agent | 62 | 51 | 8 | 59 |
| MCDA | 39 | 43 | 3 | 46 |

## Interpretation of Score Changes

The revised scoring is fairer to baselines:

- MCDA improves from 39 to 46 because it receives more credit for shared decision-support quality.
- Single-agent remains useful on shared quality but weak on deliberation.
- Multi-agent remains strongest because its advantage is concentrated in deliberative process quality.

## Method Improvement

The revised version is methodologically stronger because:

1. agents no longer see expected-decision hints;
2. evaluator expectations are separated from agent inputs;
3. prompts are reusable;
4. audit metrics are countable;
5. decision labels have explicit thresholds;
6. shared decision quality and deliberative quality are no longer collapsed.

## Remaining Problems

1. The run is still synthetic.
2. The scores are still researcher-coded.
3. MCDA weights remain provisional.
4. The revised run uses compact summaries rather than full agent transcripts.
5. The system has not yet been tested with independent human reviewers.

## Recommendation for Future Full Runs

Use the `demo-001-co` protocol as the Codex default protocol for future cases.

For paper-quality runs, expand at least two cases into full transcript artifacts:

- one high-conflict case, such as SRD-001;
- one low-conflict or approval-friendly case, such as SRD-002.
