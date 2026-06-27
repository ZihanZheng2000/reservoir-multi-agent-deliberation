# Three-Layer Evaluation — SRD-004-cc

Evaluation against rubric v3 (three-layer structure).

Run type: **Claude Code compact run.**

Important caveat: compact-run ceiling applies to L3 scores.

---

## Layer 1: Outcome Quality /30

### L1.1 Decision-Range Fit /5

| System | Score | Rationale |
|---|---:|---|
| Multi-agent | 5 | Recommends "Phased emergency package now; defer final reservoir approval" — squarely within the evaluator-defined acceptable range. |
| Single-agent | 4 | Recommends "Emergency measures now; defer final reservoir approval" — within range; less specific on immediate-package content. |
| MCDA | 3 | Recommends "Redesign / Defer with emergency measures" — directionally correct but does not express the authorized-now vs. deferred structure. |

### L1.2 Recommendation Specificity /15

| System | Score | Rationale |
|---|---:|---|
| Multi-agent | 13 | Specifies four immediate-package items; six conditions for final reservoir approval; separates what is authorized now from what is deferred. |
| Single-agent | 10 | Identifies main gaps but does not specify immediate-package content or separate phasing explicitly. |
| MCDA | 5 | Score-based output; cannot express authorized-now vs. deferred-approval sequencing. |

### L1.3 Recommendation Calibration /10

| System | Score | Rationale |
|---|---:|---|
| Multi-agent | 8 | Correctly avoids both "Emergency Build as proposed" (unsafe) and "Standard Defer without near-term action" (irresponsible given 86,000 people at risk). |
| Single-agent | 7 | Direction is calibrated; immediate-vs-deferred distinction is present but compressed. |
| MCDA | 5 | Aggregation cannot preserve the urgency-vs-safety tension; recommendation appears more generic than warranted. |

### Layer 1 Subtotals

| System | L1.1 /5 | L1.2 /15 | L1.3 /10 | L1 Total /30 |
|---|---:|---:|---:|---:|
| Multi-agent | 5 | 13 | 8 | 26 |
| Single-agent | 4 | 10 | 7 | 21 |
| MCDA | 3 | 5 | 5 | 13 |

---

## Layer 2: Evidence Quality /40

### L2.1 Evidence Grounding /10

| System | Score | Rationale |
|---|---:|---|
| Multi-agent | 8 | Claims cite field IDs; audit metrics reported; 4 corrections applied; compact-run ceiling applied. |
| Single-agent | 7 | Major claims grounded; no claim-level audit; downstream risk transfer less explicitly cited. |
| MCDA | 5 | Criterion scores linked to scenario fields; emergency context is compressed into flood_control_benefit score. |

### L2.2 Risk Coverage /20

Gold checklist: 5M, 5S.

Multi-agent coverage: R1 (climate-adjusted flood estimate incomplete) ✓M; R2 (downstream risk transfer from fast releases) ✓M; R3 (concept-design-only, variable foundation alluvium) ✓M; R4 (emergency consultation shortened to 45 days, 180 households) ✓M; R5 (3-year emergency schedule quality-control risk) ✓M; R6 (non-structural measures in immediate package) ✓S; R7 (climate-adjusted avoided damage not estimated) ✓S; R8 (upstream acquisition legally contested) ✓S; R9 (emergency EIA incomplete, bird habitat) ✓S; R10 (equity: low-income neighborhoods still exposed without levee repair) ✓S.

M_detected: 5/5; S_detected: 5/5; compact-run ceiling applied.

| System | Score | Rationale |
|---|---:|---|
| Multi-agent | 18 | All 5M and 5S detected; compact ceiling (-2) applied. |
| Single-agent | 14 | 5/5M detected; 3/5S detected (misses downstream risk transfer equity and acquisition legal basis explicitly). |
| MCDA | 10 | 3/5M represented through scores; S items compressed. |

### L2.3 Uncertainty Calibration /10

| System | Score | Rationale |
|---|---:|---|
| Multi-agent | 8 | Uncertainty labels in audit; climate confidence rated low; foundation uncertainty carried forward explicitly. |
| Single-agent | 6 | Uncertainty acknowledged for climate and engineering gaps; not systematically labeled. |
| MCDA | 4 | Weight sensitivity not propagated; urgency context compressed into one criterion. |

### Layer 2 Subtotals

| System | L2.1 /10 | L2.2 /20 | L2.3 /10 | L2 Total /40 |
|---|---:|---:|---:|---:|
| Multi-agent | 8 | 18 | 8 | 34 |
| Single-agent | 7 | 14 | 6 | 27 |
| MCDA | 5 | 10 | 4 | 19 |

---

## Layer 3: Process Quality /55

Multi-agent only. Descriptive; do not compare against baselines.

### L3.1 Stakeholder and Conflict Representation /15

Score: **13 / 15**

Seven stakeholder positions represented including the upstream landowner legal objection and the low-income equity concern. Five conflicts are mapped. Moderator explicitly separates the immediate-risk problem from the long-term reservoir decision.

### L3.2 Role Fidelity /15

Score: **12 / 15**

Dam Safety correctly limits itself to engineering readiness without deciding social acceptability. Social agent does not decide engineering feasibility. Economist does not prescribe resettlement. Compact format limits per-claim verification.

### L3.3 Objection-Response Quality /10

Score: **7 / 10**

The phased-package structure is a direct product of the Dam Safety–Social–Moderator exchange: Dam Safety establishes reservoir cannot be approved as proposed; Social establishes non-structural measures can proceed now; Moderator frames the recommendation as "act on what is safe now, defer what is not." Full transcripts not preserved.

### L3.4 Evidence Audit and Revision /10

Score: **7 / 10**

55 claims audited; 4 corrections applied; 0 unresolved blockers. The climate-adjusted design claim correction (A1) is substantive and prevents an unsupported basis for approval.

### L3.5 Minority Preservation /5

Score: **4 / 5**

Three minority positions preserved (Dam Safety on timeline ambiguity, landowner legal concern, Environmental Group on sequencing). All noted and incorporated or preserved as conditions.

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
| Single-agent | 21 | 27 | n/a |
| MCDA | 13 | 19 | n/a |

---

## Interpretation

SRD-004's core test is whether the system can separate urgent near-term risk reduction from a premature reservoir approval — handling urgency without abandoning safety and safeguard standards. The multi-agent system's added value here is the immediate-package specification (levees, warning systems, wetland study) that provides near-term protection while allowing the reservoir decision to complete proper engineering and social review. Neither the single-agent nor MCDA baseline produces this explicit separation with actionable immediate-package content. The L1 advantage (multi-agent 26 vs. single-agent 21) reflects the specificity of the phased structure; the L2 gap is modest because single-agent also catches most technical risks.
