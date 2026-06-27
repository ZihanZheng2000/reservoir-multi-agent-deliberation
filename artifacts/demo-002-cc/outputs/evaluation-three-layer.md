# Three-Layer Evaluation — SRD-002-cc

Evaluation against rubric v3 (three-layer structure).

Run type: **Claude Code compact run.**

Important caveat: compact-run ceiling applies to L3 scores. Stakeholder position tables and conflict map are included, but agent deliberation is synthesized rather than preserved as a full transcript. Risk coverage scores are reported with this caveat.

---

## Layer 1: Outcome Quality /30

Applied to all three systems.

### L1.1 Decision-Range Fit /5

| System | Score | Rationale |
|---|---:|---|
| Multi-agent | 5 | Recommends "Build with conditions through phased approval" — squarely within the evaluator-defined acceptable range. |
| Single-agent | 5 | Recommends "Approve with conditions" — within the acceptable range; slightly less specific on phasing. |
| MCDA | 4 | Recommends "Build with conditions" at 3.94/5.0 — correct direction; does not distinguish commissioning from construction conditions. |

### L1.2 Recommendation Specificity /15

| System | Score | Rationale |
|---|---:|---|
| Multi-agent | 13 | Identifies five specific conditions, distinguishes commissioning from construction conditions, and specifies phased approval milestones. |
| Single-agent | 10 | Conditions are correct but compressed; does not distinguish commissioning vs. construction timing; misses grazing access route gap. |
| MCDA | 6 | Score-driven conditions lack sequencing and enforceability specificity. |

### L1.3 Recommendation Calibration /10

| System | Score | Rationale |
|---|---:|---|
| Multi-agent | 8 | Appropriately avoids unnecessary Defer on a low-conflict project; minor positions are preserved but not allowed to inflate the recommendation toward rejection. |
| Single-agent | 7 | Calibration is reasonable; uncertainty is acknowledged but less systematically labeled. |
| MCDA | 5 | Aggregation compresses dissent and uncertainty into a single score without expressing the phasing logic. |

### Layer 1 Subtotals

| System | L1.1 /5 | L1.2 /15 | L1.3 /10 | L1 Total /30 |
|---|---:|---:|---:|---:|
| Multi-agent | 5 | 13 | 8 | 26 |
| Single-agent | 5 | 10 | 7 | 22 |
| MCDA | 4 | 6 | 5 | 15 |

---

## Layer 2: Evidence Quality /40

Applied to all three systems.

### L2.1 Evidence Grounding /10

| System | Score | Rationale |
|---|---:|---|
| Multi-agent | 9 | All major claims cite field IDs; audit metrics reported; 4 minor corrections applied; no unresolved blockers. |
| Single-agent | 7 | Major claims are grounded in scenario facts; no systematic claim-level audit. |
| MCDA | 6 | Criterion scores link to scenario fields; weights are provisional; tariff and enforceability interpretation is implicit. |

### L2.2 Risk Coverage /20

Gold checklist: 3M, 4S.

Multi-agent coverage: R1 (BCR 1.16 under combined downside) ✓M; R2 (two-year drought refill not tested) ✓M; R3 (low-income tariff increase 6–9%) ✓M; R4 (seismic retrofit scheduling) ✓S; R5 (climate refill rule untested) ✓S; R6 (wetland buffer enforceability) ✓S; R7 (grazing access routes not finalized) ✓S.

M_detected: 3/3; S_detected: 4/4; compact-run ceiling applied.

| System | Score | Rationale |
|---|---:|---|
| Multi-agent | 17 | All 3M and all 4S detected; compact ceiling (-1) applied; strong but summarized rather than full transcript. |
| Single-agent | 13 | 3M detected; 2/4 S detected (misses grazing access and refill rule distinction explicitly). |
| MCDA | 10 | 3M represented through scores; S items partially compressed; enforceability distinction not captured. |

### L2.3 Uncertainty Calibration /10

| System | Score | Rationale |
|---|---:|---|
| Multi-agent | 8 | Uncertainty labels appear in audit metrics and recommendation; confidence levels assigned to each score dimension. |
| Single-agent | 6 | Uncertainty acknowledged but less systematically labeled across claims. |
| MCDA | 4 | Sensitivity of scores to weights not propagated into recommendation statement. |

### Layer 2 Subtotals

| System | L2.1 /10 | L2.2 /20 | L2.3 /10 | L2 Total /40 |
|---|---:|---:|---:|---:|
| Multi-agent | 9 | 17 | 8 | 34 |
| Single-agent | 7 | 13 | 6 | 26 |
| MCDA | 6 | 10 | 4 | 20 |

---

## Layer 3: Process Quality /55

Multi-agent only. Descriptive; do not compare against baselines.

### L3.1 Stakeholder and Conflict Representation /15

Score: **13 / 15**

All seven expert and seven stakeholder positions are represented in summary tables. Conflict map identifies four genuine disagreements. Compact format loses two points because positions are synthesized, not transcript-level.

### L3.2 Role Fidelity /15

Score: **12 / 15**

Role-specific positions are separated and domain-appropriate. Dam Safety correctly limits itself to retrofit classification, not ecological or social conclusions. Social agent does not decide tariff policy. Compact format makes individual role-boundary checks harder to verify.

### L3.3 Objection-Response Quality /10

Score: **7 / 10**

Conflict map identifies four conflicts with targeted responses. Phased approval sequencing is the direct product of the moderator's intervention on the tariff/commissioning distinction. Full exchange transcripts are not preserved.

### L3.4 Evidence Audit and Revision /10

Score: **8 / 10**

49 claims audited; 4 corrections applied; 0 unresolved blockers. Audit metrics are robust for a compact run. Revised claim text is summarized rather than fully preserved.

### L3.5 Minority Preservation /5

Score: **4 / 5**

Two minority positions are preserved (NGO enforceability preference, Climate Risk commissioning timing). Both are noted as incorporated or noted in the recommendation. Full transcript would make dissent stronger and more inspectable.

### Layer 3 Total

| Dimension | Score | Max |
|---|---:|---:|
| Stakeholder/conflict representation | 13 | 15 |
| Role fidelity | 12 | 15 |
| Objection-response quality | 7 | 10 |
| Evidence audit and revision | 8 | 10 |
| Minority preservation | 4 | 5 |
| **Layer 3 total** | **44** | **55** |

---

## Summary Scorecard

| System | L1 Outcome /30 | L2 Evidence /40 | L3 Process /55 |
|---|---:|---:|---:|
| Multi-agent | 26 | 34 | 44 |
| Single-agent | 22 | 26 | n/a |
| MCDA | 15 | 20 | n/a |

Reporting rule: L1 and L2 support cross-system comparison. L3 is descriptive for multi-agent only.

---

## Interpretation

SRD-002 is the benchmark's low-conflict case. The multi-agent system correctly avoids unnecessary conservatism: it does not default to Defer or Redesign on a project where the blockers are genuinely manageable conditions. The key added value is the enforceability/phasing distinction — the system identifies that the tariff and wetland buffer gaps require operating license action before commissioning, not before construction, and that the phased approval path avoids the cost of unnecessary delay.

Compared with demo-001-co (SRD-001, compact run: L1=25, L2=32, L3=41), SRD-002-cc scores higher on evidence grounding and minority handling because the case is lower conflict and the deliberative output is cleaner. L3 is higher because role fidelity is easier to maintain when positions are more compatible.
