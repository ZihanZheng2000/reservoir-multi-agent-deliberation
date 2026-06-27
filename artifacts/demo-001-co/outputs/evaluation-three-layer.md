# Three-Layer Evaluation - SRD-001-co

Evaluation against the revised rubric v0.2 / current three-layer structure.

Run type: **Codex compact revised run**.

Important caveat: this is not a full transcript run. The scores below apply the compact-run caution from the rubric. In particular, risk coverage and audit/revision process scores should not be treated as equivalent to a full transcript evaluation.

## Layer 1: Outcome Quality /30

Applied to all three systems.

### L1.1 Decision-Range Fit /5

| System | Score | Rationale |
|---|---:|---|
| Multi-agent deliberation | 5 | Recommends "Redesign; final build approval deferred", which is inside the evaluator-defined reasonable range. |
| Single-agent baseline | 5 | Recommends deferring final approval pending major revisions and studies, also inside the reasonable range. |
| MCDA baseline | 4 | Recommends "Do not build as proposed; major redesign required", inside the broad acceptable range but less precise about approval sequencing. |

### L1.2 Recommendation Specificity /15

| System | Score | Rationale |
|---|---:|---|
| Multi-agent deliberation | 12 | Lists case-specific blockers and seven concrete conditions, but the compact summary does not preserve the full condition-by-agent derivation. |
| Single-agent baseline | 10 | Gives useful conditions but compresses stakeholder conflict and safeguard sequencing. |
| MCDA baseline | 6 | Identifies the poor approval status through a score, but conditions are threshold-driven and less actionable. |

### L1.3 Recommendation Calibration /10

| System | Score | Rationale |
|---|---:|---|
| Multi-agent deliberation | 8 | Appropriately avoids immediate Build and preserves medium confidence and minority concerns. |
| Single-agent baseline | 7 | Deferral is calibrated, but uncertainty and dissent are less explicit. |
| MCDA baseline | 5 | The numeric score is directionally useful, but provisional weights and aggregation make the recommendation appear more precise than warranted. |

### Layer 1 Subtotals

| System | L1.1 /5 | L1.2 /15 | L1.3 /10 | L1 Total /30 |
|---|---:|---:|---:|---:|
| Multi-agent | 5 | 12 | 8 | 25 |
| Single-agent | 5 | 10 | 7 | 22 |
| MCDA | 4 | 6 | 5 | 15 |

## Layer 2: Evidence Quality /40

Applied to all three systems.

### L2.1 Evidence Grounding /10

| System | Score | Rationale |
|---|---:|---|
| Multi-agent deliberation | 8 | Compact run cites field IDs extensively and reports audit metrics, but claim-level transcript evidence is not fully preserved. |
| Single-agent baseline | 7 | Major risks are grounded in scenario facts, but there is no claim-level audit. |
| MCDA baseline | 6 | Criterion scores are linked to scenario fields, but weights and threshold interpretation remain provisional. |

### L2.2 Risk Coverage /20

The hidden checklist contains 7 must-detect and 8 should-detect issues. The compact revised evaluation reports:

- multi-agent: 15/15 expected risks identified;
- single-agent: 13/15 expected risks identified;
- MCDA: 10/15 expected risks represented explicitly or implicitly.

Compact-run ceiling applied to multi-agent risk coverage.

| System | Score | Rationale |
|---|---:|---|
| Multi-agent deliberation | 16 | Full checklist recovery reported, capped because this is a compact run rather than a full transcript. |
| Single-agent baseline | 13 | Most major risks identified; stakeholder/process-specific risks are weaker. |
| MCDA baseline | 10 | Represents several risks through scores but misses or compresses specific safeguards and conflicts. |

### L2.3 Uncertainty Calibration /10

| System | Score | Rationale |
|---|---:|---|
| Multi-agent deliberation | 8 | Explicit uncertainty and inference labels appear in the audit metrics and recommendation. |
| Single-agent baseline | 6 | Recognizes missing evidence but less systematically labels uncertainty. |
| MCDA baseline | 4 | Sensitivity and weights are not fully propagated into the decision statement. |

### Layer 2 Subtotals

| System | L2.1 /10 | L2.2 /20 | L2.3 /10 | L2 Total /40 |
|---|---:|---:|---:|---:|
| Multi-agent | 8 | 16 | 8 | 32 |
| Single-agent | 7 | 13 | 6 | 26 |
| MCDA | 6 | 10 | 4 | 20 |

## Layer 3: Process Quality /55

Multi-agent only. Descriptive; do not compare this layer with baselines.

### L3.1 Stakeholder and Conflict Representation /15

Score: **12 / 15**

The compact run represents all major expert and stakeholder positions and includes a conflict map. It loses points because the record is synthesized rather than full transcript.

### L3.2 Role Fidelity /15

Score: **12 / 15**

Role boundaries are visible and role-specific positions are separated. The compact format makes it harder to verify every role boundary and required challenge.

### L3.3 Objection-Response Quality /10

Score: **6 / 10**

The run reports conflict resolution and conditions, but it does not preserve full objection-response exchanges in transcript form.

### L3.4 Evidence Audit and Revision /10

Score: **7 / 10**

The quantitative audit reports 64 claims, 1 unsupported claim, 2 role-overreach claims, 4 over-strong claims, and 6 corrections. Compact-run ceiling applied because revised claim text is summarized rather than fully preserved.

### L3.5 Minority Preservation /5

Score: **4 / 5**

Minority reports are preserved for NGO, affected residents, financier, and legal/policy perspectives. Full transcript would make dissent stronger and easier to inspect.

### Layer 3 Total

| Dimension | Score | Max |
|---|---:|---:|
| Stakeholder/conflict representation | 12 | 15 |
| Role fidelity | 12 | 15 |
| Objection-response quality | 6 | 10 |
| Evidence audit and revision | 7 | 10 |
| Minority preservation | 4 | 5 |
| Layer 3 total | 41 | 55 |

## Summary Scorecard

| System | L1 Outcome /30 | L2 Evidence /40 | L3 Process /55 |
|---|---:|---:|---:|
| Multi-agent deliberation | 25 | 32 | 41 |
| Single-agent baseline | 22 | 26 | n/a |
| MCDA baseline | 15 | 20 | n/a |

Reporting rule: Layer 1 and Layer 2 support cross-system comparison. Layer 3 is descriptive for multi-agent only.

## Interpretation

The Codex compact run is methodologically cleaner than the original SRD-001 because it removes agent-facing hints and uses hidden evaluator checklists. It supports the same recommendation as the original run.

Compared with the Claude Code full transcript run, this Codex run is less inspectable at the process level because it summarizes deliberation rather than preserving full agent transcripts. Its main value is protocol clarity and compact reproducibility; its main limitation is weaker transcript evidence.
