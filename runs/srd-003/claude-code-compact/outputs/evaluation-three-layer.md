# Three-Layer Evaluation — SRD-003-cc

Evaluation against rubric v3 (three-layer structure).

Run type: **Claude Code compact run.**

Important caveat: compact-run ceiling applies to L3 scores. Deliberation is synthesized rather than preserved as a full transcript.

---

## Layer 1: Outcome Quality /30

### L1.1 Decision-Range Fit /5

| System | Score | Rationale |
|---|---:|---|
| Multi-agent | 5 | Recommends "Redesign toward hybrid alternative" — squarely within the evaluator-defined acceptable range. |
| Single-agent | 4 | Recommends Defer without specifying the hybrid alternative direction — adjacent but underspecific. |
| MCDA | 3 | Recommends "Do not build as proposed" — correct direction but does not express Redesign-toward-hybrid pathway. |

### L1.2 Recommendation Specificity /15

| System | Score | Rationale |
|---|---:|---|
| Multi-agent | 13 | Specifies five conditions for the hybrid approval path; identifies the hybrid alternative explicitly; names the downstream livelihood study as a required precondition. |
| Single-agent | 9 | Conditions are broadly correct (alternatives analysis, livelihood study) but do not point to the hybrid as the specific path. |
| MCDA | 5 | Score-based output; no actionable pathway to approval; does not identify hybrid. |

### L1.3 Recommendation Calibration /10

| System | Score | Rationale |
|---|---:|---|
| Multi-agent | 8 | Correctly avoids Do not build (the grid need is real); correctly does not approve the current design; preserves minority positions. |
| Single-agent | 6 | Defer is directionally correct but does not distinguish resolvable from unresolvable blockers. |
| MCDA | 5 | Aggregation compresses the difference between Redesign-toward-hybrid (preferred) and Do not build (too strong). |

### Layer 1 Subtotals

| System | L1.1 /5 | L1.2 /15 | L1.3 /10 | L1 Total /30 |
|---|---:|---:|---:|---:|
| Multi-agent | 5 | 13 | 8 | 26 |
| Single-agent | 4 | 9 | 6 | 19 |
| MCDA | 3 | 5 | 5 | 13 |

---

## Layer 2: Evidence Quality /40

### L2.1 Evidence Grounding /10

| System | Score | Rationale |
|---|---:|---|
| Multi-agent | 8 | Claims cite field IDs; audit metrics reported; 5 corrections applied; compact-run ceiling. |
| Single-agent | 7 | Major claims are grounded; no claim-level audit. |
| MCDA | 5 | Criterion scores link to scenario fields; hybrid alternative data not systematically used. |

### L2.2 Risk Coverage /20

Gold checklist: 5M, 5S.

Multi-agent coverage: R1 (BCR 0.92 downside) ✓M; R2 (irreversible gorge habitat, fish passage not confirmed) ✓M; R3 (benefit-burden mismatch, 8,400 people) ✓M; R4 (hybrid alternative, full alternatives analysis required) ✓M; R5 (hydropeaking 4:1 flow fluctuations) ✓M; R6 (narrow EIA alternatives analysis) ✓S; R7 (revenue sharing inadequate) ✓S; R8 (dry-year generation 28% reduction) ✓S; R9 (downstream flow license not finalized) ✓S; R10 (carbon benefit real but does not override local costs) ✓S.

M_detected: 5/5; S_detected: 5/5; compact-run ceiling applied.

| System | Score | Rationale |
|---|---:|---|
| Multi-agent | 18 | All 5M and 5S detected; compact ceiling (-2) applied; detection is comprehensive. |
| Single-agent | 13 | 4/5M detected (R4 hybrid path not explicitly identified); 3/5S detected. |
| MCDA | 9 | 3/5M represented through scores; S items compressed. |

### L2.3 Uncertainty Calibration /10

| System | Score | Rationale |
|---|---:|---|
| Multi-agent | 8 | Uncertainty labels appear in audit and recommendation; hybrid adequacy study noted as inference-based pending grid model. |
| Single-agent | 6 | Uncertainty acknowledged for BCR and livelihood estimate; not systematically labeled. |
| MCDA | 4 | Weight sensitivity not propagated into recommendation. |

### Layer 2 Subtotals

| System | L2.1 /10 | L2.2 /20 | L2.3 /10 | L2 Total /40 |
|---|---:|---:|---:|---:|
| Multi-agent | 8 | 18 | 8 | 34 |
| Single-agent | 7 | 13 | 6 | 26 |
| MCDA | 5 | 9 | 4 | 18 |

---

## Layer 3: Process Quality /55

Multi-agent only. Descriptive; do not compare against baselines.

### L3.1 Stakeholder and Conflict Representation /15

Score: **13 / 15**

All seven expert and stakeholder positions are represented in separate summary tables. Five conflicts are mapped with targeted interventions. The downstream fisher position is explicitly preserved and drives the hydropeaking impact condition. Compact ceiling applied.

### L3.2 Role Fidelity /15

Score: **12 / 15**

Domain separation is maintained: Engineer correctly limits to structural feasibility and does not decide ecological acceptability; Ecologist does not decide economic viability; Developer acknowledges regulatory concern without conceding the ecological conclusion. Compact format makes per-claim boundary verification harder.

### L3.3 Objection-Response Quality /10

Score: **7 / 10**

Conflict map produces four targeted exchanges leading to the hybrid Redesign recommendation. The moderator's framing of "same grid need, lower river impact, lower cost" is a direct product of objection-response structure. Full transcript exchanges not preserved.

### L3.4 Evidence Audit and Revision /10

Score: **7 / 10**

57 claims audited; 5 corrections applied; 0 unresolved blockers. The fish-passage claim correction (A1/A2) is a substantive revision that prevents over-strong ecological conclusions in either direction.

### L3.5 Minority Preservation /5

Score: **4 / 5**

Three minority positions preserved (Developer transition credit, Energy Ministry non-commitment, NGO hybrid EIA requirement). All noted; one incorporated as a condition.

### Layer 3 Total

| Dimension | Score | Max |
|---|---:|---:|
| Stakeholder/conflict representation | 13 | 15 |
| Role fidelity | 12 | 15 |
| Objection-response quality | 7 | 10 |
| Evidence audit and revision | 7 | 10 |
| Minority preservation | 4 | 5 |
| **Layer 3 total** | **43** | **55** |

---

## Summary Scorecard

| System | L1 Outcome /30 | L2 Evidence /40 | L3 Process /55 |
|---|---:|---:|---:|
| Multi-agent | 26 | 34 | 43 |
| Single-agent | 19 | 26 | n/a |
| MCDA | 13 | 18 | n/a |

---

## Interpretation

SRD-003's strongest added value from multi-agent deliberation is the shift from a generic Defer to a specific Redesign-toward-hybrid recommendation. The hybrid alternative data (F5.6–F5.9) is present in the scenario but only becomes decision-actionable when the Ecologist, Economist, and Moderator jointly identify that the gorge is irreplaceable, the BCR fails under downside conditions, and the hybrid closes the same grid gap at lower cost and zero river impact. Neither the single-agent nor the MCDA baseline produces this specific pathway. The L1 gap between multi-agent (26) and single-agent (19) on this case reflects this specificity advantage.
