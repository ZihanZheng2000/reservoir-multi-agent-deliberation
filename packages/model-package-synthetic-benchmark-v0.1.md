# Model Package: Synthetic Benchmark v0.1

## Modeling Goal

- **goal statement:** Build and evaluate a controlled synthetic benchmark for a role-limited multi-agent deliberation system for reservoir construction decision support.
- **goal start trigger:** Planning Package approved and SRD-001 demo audit identified need for a stronger protocol.
- **execution mode:** synthetic benchmark with controlled case design.
- **goal stop condition:** synthetic cases have neutral scenario packets, hidden evaluator checklists, reasonable decision ranges, system/baseline outputs, and quantitative evaluation records, or a user decision is required.
- **first successful script/table/figure treated as final stop?** no.

## Modeling Contract

- **approved research question:** Can a role-limited multi-agent deliberation system produce more acceptable reservoir construction decision-support artifacts than single-agent and weighted-score baselines by recovering designed risk structures, preserving stakeholder conflict, and generating calibrated recommendations?
- **accepted claim level:** proof-of-concept synthetic benchmark.
- **not claimed:** objective correctness of real-world reservoir decisions.
- **allowed data sources:** synthetic scenario packets authored for controlled testing; later public real-case documents if separately approved.
- **allowed systems:** role-limited multi-agent deliberation, single-agent baseline, MCDA baseline.
- **required evaluation structure:** hidden gold checklist, reasonable decision range, blind agent run, risk recovery, decision-range fit, and deliberative acceptability scoring.
- **additional discovery structure:** extract non-checklist issues from outputs, classify them by human review, and report valid emergent issue discovery.

## Synthetic Benchmark Logic

Each synthetic case has two layers:

1. **Agent-facing neutral facts:** the system sees only case facts.
2. **Evaluator-only hidden expectations:** the evaluator records what risks should be found and what decision range is reasonable.

The system is evaluated by comparing its output against the hidden evaluation layer.

This tests whether the system can recover the designed risk/conflict structure without being shown the expected conclusion.

The benchmark also tests whether the system can discover valid additional issues beyond the checklist. These emergent issues are not counted as advantages unless they are supported by scenario facts or reasonable inference and pass human review.

## Required Per-Case Artifacts

| Artifact | Purpose | Required? |
|---|---|---|
| neutral scenario packet | Facts given to agents. | yes |
| hidden gold risk checklist | Designed issues evaluators expect systems to find. | yes |
| reasonable decision range | Acceptable and suspicious recommendation labels. | yes |
| multi-agent output | Main system result. | yes |
| single-agent baseline | Compact LLM baseline. | yes |
| MCDA baseline | Aggregation baseline. | yes |
| quantitative evidence audit | Claim-level evidence and overreach metrics. | yes for full runs |
| revised evaluation table | Shared and deliberative scoring. | yes |
| emergent issue discovery table | Candidate and validated additional issues beyond checklist. | yes |
| case run summary | Human-readable package. | yes |

## Current Case Status

| Case | Status | Notes |
|---|---|---|
| SRD-001 | full original run complete; revised v2 complete; gold checklist complete | v2 removes hints; checklist updated with must-detect/should-detect tiers (7M/8S). |
| SRD-001 Codex vs Claude Code comparison | complete | `demo-001-co` is the Codex revised compact/control run; `demo-001-cc` is the Claude Code full transcript run. Current comparison stored in `demo-001-co/outputs/codex-vs-claude-code-comparison.md`. |
| SRD-002 | Codex + Claude Code compact runs complete; gold checklist complete | Seismic clarified as routine retrofit. Checklist: 3M/4S. cc run in `demo-002-cc/`; v3 three-layer scores: L1=26, L2=34, L3=44. Needs full-protocol transcript run before manuscript use. |
| SRD-003 | Codex + Claude Code compact runs complete; gold checklist complete | Hybrid alternative quantified (F5.6-F5.9). Checklist: 5M/5S. cc run in `demo-003-cc/`; v3 three-layer scores: L1=26, L2=34, L3=43. Candidate appendix case. |
| SRD-004 | Codex + Claude Code compact runs complete; gold checklist complete | Checklist: 5M/5S. cc run in `demo-004-cc/`; v3 three-layer scores: L1=26, L2=34, L3=43. Needs full-protocol transcript run if selected for main paper. |
| SRD-005 | Codex + Claude Code compact runs complete; gold checklist complete | Legal advocate added; governance conflict sharpened. Checklist: 5M/5S. cc run in `demo-005-cc/`; v3 three-layer scores: L1=26, L2=34, L3=45. Needs full-protocol run if selected. |
| SRD-006 | Codex + Claude Code compact runs complete; gold checklist complete | Clean approval case. Checklist: 4M/4S (commissioning-vs-blocker characterization test). cc run in `demo-006-cc/`; v3 three-layer scores: L1=28, L2=36, L3=43. Needs full-protocol run. |
| SRD-007 | Codex + Claude Code compact runs complete; gold checklist complete | Near-tipping-point. Checklist: 4M/6S; swing condition is livelihood plan (R1). cc run in `demo-007-cc/`; v3 three-layer scores: L1=27, L2=34, L3=45. Needs full-protocol run. |
| SRD-008 | Codex + Claude Code compact runs complete; gold checklist complete | Do not build case. Checklist: 5M/5S; R5 explicitly tests Why-not-Redesign reasoning. cc run in `demo-008-cc/`; v3 three-layer scores: L1=27, L2=35, L3=46. Needs full-protocol run. |

## Evaluation Metrics

### Gold Risk Recovery

| Metric | Definition |
|---|---|
| must-detect recall | detected must-detect risks / total must-detect risks |
| should-detect recall | detected should-detect risks / total should-detect risks |
| false reassurance count | serious risks incorrectly treated as resolved |
| unsupported blocker count | claimed blockers not supported by scenario facts |

### Emergent Issue Discovery

| Metric | Definition |
|---|---|
| candidate emergent issue count | non-checklist issues raised by the system |
| valid emergent issue count | candidate issues classified as valid by human review |
| weak-but-interesting count | plausible but not fully supported or not clearly decision-changing |
| unsupported/hallucinated count | invalid additional issues |
| emergent issue precision | valid emergent / candidate emergent |
| decision-relevant discovery count | valid issues affecting recommendation, conditions, or conflicts |

**Minimum precision threshold:** A precision at or above 0.50 is the minimum bar for claiming useful non-checklist discovery. Below 0.50, the system produces more noise than signal and emergent discovery results should not be highlighted as a system advantage. Precision should be reported alongside candidate counts so readers can assess noise level independently.

### Decision-Range Fit

| Score | Meaning |
|---:|---|
| 2 | Recommendation falls within reasonable range and explains why. |
| 1 | Recommendation is adjacent to reasonable range but weakly justified. |
| 0 | Recommendation is suspicious or outside range. |

### Three-Layer Rubric

Scores are reported in three layers that are **never collapsed into a single combined score**.

**Layer 1 — Outcome Quality /30** (all systems; primary comparison):

- decision-range fit `/5`;
- recommendation specificity `/15`;
- recommendation calibration `/10`.

**Layer 2 — Evidence Quality /40** (all systems; secondary comparison):

- evidence grounding `/10`;
- risk coverage `/20` (with must-detect penalty: −4 per missed must-detect, −1 per missed should-detect);
- uncertainty calibration `/10`.

**Layer 3 — Process Quality /55** (multi-agent only; descriptive):

- stakeholder/conflict representation `/15`;
- role fidelity `/15`;
- objection-response quality `/10`;
- evidence audit and revision `/10`;
- minority preservation `/5`.

Reporting rule: Layer 1 and Layer 2 scores are reported for all three systems and used for cross-system comparison. Layer 3 is reported for multi-agent only and described qualitatively; baselines are not compared on Layer 3.

See `artifacts/demo-001-co/protocols/revised-evaluation-rubric-v0.1.md` for full scoring anchors and guidance.

## SRD-001 Codex Revised Current Result

The table below uses pre-transition v1 scores and is retained for historical reference. Re-evaluate under the three-layer rubric when a full transcript run is completed.

| System | Shared quality /60 | Deliberative process /40 | Combined /100 | Recommendation |
|---|---:|---:|---:|---|
| Multi-agent v2 | 56 | 37 | 93 | Redesign; final build approval deferred |
| Single-agent baseline | 51 | 8 | 59 | Defer final approval pending revisions |
| MCDA baseline | 43 | 3 | 46 | Do not build as proposed; major redesign required |

**Note:** the combined /100 figure above conflates outcome/evidence quality (available to all systems) with deliberative process quality (structural multi-agent advantage). Under the three-layer rubric, these are reported separately. Do not use the combined figure for cross-system comparison.

## Interpretation of SRD-001 Codex Revised Run

After removing agent-facing hints, the recommendation remained stable:

> Redesign; final build approval deferred.

This supports the idea that the conclusion was driven by the neutral scenario facts rather than explicit hints.

The key benchmark result is not that the multi-agent output is objectively correct. The key result is that it recovered the designed high-risk structure and produced a recommendation within the evaluator-defined reasonable decision range.

## Risks and Limitations

| Risk | Severity | Mitigation |
|---|---|---|
| Case designer bias | high | Use hidden checklist but later add independent human-designed cases. |
| Researcher-coded scores | high | Add blind human expert scoring. |
| Compounded researcher bias | high | Entire evaluation chain (case design, hidden checklist authorship, system run, and score coding) is performed by one researcher; this compounds the case-designer and scorer biases into a stronger confound than either alone implies. Prioritize blind human expert scoring over expanding the synthetic case count. Consider independent case design for at least one case before reporting benchmark results. |
| MCDA weights provisional | medium | Weights are not yet sourced from literature or expert elicitation; document the provisional weight values and their assumed source before reporting. Calibrate from published infrastructure MCDA studies or structured expert elicitation. |
| Synthetic external validity limited | high | Add 1-2 real public cases after synthetic benchmark. |
| Agent outputs generated in compact form | medium | Expand selected cases into full transcript runs. |

## Next Modeling Queue

| Next action | Purpose | Priority |
|---|---|---|
| Run SRD-002 full transcript under three-layer rubric | Test approval-friendly case with full agent outputs; this is the highest-priority full run because it demonstrates the Build direction. | high |
| Run SRD-007 full transcript under three-layer rubric | Near-tipping-point case; produces largest single-agent Decision Usefulness gap; strongest demonstration of multi-agent value. | high |
| Build cross-case three-layer score table | Replace compressed v1 scores with controlled benchmark scores using the new Layer 1/2/3 structure. | high |
| Add emergent issue discovery tables for full transcript runs | Measure whether multi-agent finds useful non-checklist issues beyond the gold checklist. | high |
| Document provisional MCDA weight values and sources | Required before cross-case reporting; weights are currently undocumented. | high |
| Confirm SRD-003 as appendix case or drop from scope | SRD-003 is a candidate appendix case; selection decision is needed before allocating full-run effort. | medium |
| Choose SRD-004 or SRD-005 for full transcript run | Add either urgency or governance case to main evidence. | medium |
| Search/select real cases | Prepare external validation. | medium |

**Sequencing note:** SRD-002 v2 rerun should precede the cross-case score table. MCDA weight documentation should precede any cross-case MCDA comparison. At least one v2 case should be expanded to full transcript before submission to a manuscript venue.

## Model Gate Status

The synthetic benchmark is not yet ready for Reporting as a mature result. It is ready for continued Modeling under the revised controlled benchmark protocol.
