# Three-Layer Evaluation — SRD-005-cc

Evaluation against rubric v3 (three-layer structure).

Run type: **Claude Code compact run.**

Important caveat: compact-run ceiling applies to L3 scores.

---

## Layer 1: Outcome Quality /30

### L1.1 Decision-Range Fit /5

| System | Score | Rationale |
|---|---:|---|
| Multi-agent | 5 | Recommends "Defer pending binding basin agreement, joint monitoring, and drought-contingent operating rules" — squarely within the evaluator-defined acceptable range. |
| Single-agent | 4 | Recommends "Defer until downstream agreement and monitoring" — within range; less specific on drought-contingency and Ramsar requirements. |
| MCDA | 4 | Recommends "Defer / Redesign pending basin agreement" — within broad range; does not express the specific governance conditions. |

### L1.2 Recommendation Specificity /15

| System | Score | Rationale |
|---|---:|---|
| Multi-agent | 13 | Specifies seven conditions; explicitly distinguishes drought-contingent from average-flow rules; names Ramsar wetland flood pulse as a separate ecological condition; identifies monitoring enforceability as the linchpin. |
| Single-agent | 9 | Identifies main governance conditions but does not flag the monitoring enforceability linkage or the Ramsar seasonal pulse gap. |
| MCDA | 5 | Score-based output; conditions are not expressible through criterion weights. |

### L1.3 Recommendation Calibration /10

| System | Score | Rationale |
|---|---:|---|
| Multi-agent | 8 | Correctly avoids both Build without agreement (irresponsible) and Do not build outright (dismisses genuine upstream water-security need); preserves both the upstream legal argument and the downstream governance objection without letting either foreclose the recommendation. |
| Single-agent | 7 | Calibration is directionally correct; tends to accept downstream position without explicitly balancing the upstream legal argument as a competing interpretation. |
| MCDA | 5 | Aggregation suppresses the legal-interpretation conflict; cannot express competing legitimate positions. |

### Layer 1 Subtotals

| System | L1.1 /5 | L1.2 /15 | L1.3 /10 | L1 Total /30 |
|---|---:|---:|---:|---:|
| Multi-agent | 5 | 13 | 8 | 26 |
| Single-agent | 4 | 9 | 7 | 20 |
| MCDA | 4 | 5 | 5 | 14 |

---

## Layer 2: Evidence Quality /40

### L2.1 Evidence Grounding /10

| System | Score | Rationale |
|---|---:|---|
| Multi-agent | 8 | Claims cite field IDs; two major legal-interpretation over-strong claims corrected; audit metrics reported. |
| Single-agent | 7 | Major claims grounded; tends to take downstream legal position as settled rather than contested. |
| MCDA | 6 | Criterion scores linked to scenario fields; legal_governance_readiness score of 1 is well-grounded; contested legal interpretation not captured. |

### L2.2 Risk Coverage /20

Gold checklist: 5M, 5S.

Multi-agent coverage: R1 (downstream dry-season reduction 14%/24%, 140,000 ha, 32,000 people) ✓M; R2 (no binding operating agreement; post-approval plan is non-binding) ✓M; R3 (basin compact applicability contested; "no significant harm" clause live) ✓M; R4 (multilateral lender requires consultation and basin-level assessment) ✓M; R5 (basin-wide BCR 1.05 vs. upstream-only 1.36) ✓M; R6 (no joint real-time monitoring; any rule is unenforceable) ✓S; R7 (Ramsar wetland requires seasonal flood pulse, not monthly average) ✓S; R8 (dispute mechanism untested) ✓S; R9 (environmental flow proposal not drought-contingent) ✓S; R10 (760 upstream households' safeguards must be addressed) ✓S.

M_detected: 5/5; S_detected: 5/5; compact-run ceiling applied.

| System | Score | Rationale |
|---|---:|---|
| Multi-agent | 18 | All 5M and 5S detected; compact ceiling (-2) applied. |
| Single-agent | 14 | 5/5M detected; 3/5S detected (misses Ramsar flood pulse gap and upstream safeguards explicitly). |
| MCDA | 10 | 3/5M represented; S items compressed. |

### L2.3 Uncertainty Calibration /10

| System | Score | Rationale |
|---|---:|---|
| Multi-agent | 8 | Legal interpretation marked as contested (not settled) after audit; drought-year flow impact uncertainty labeled; basin-wide BCR margin acknowledged. |
| Single-agent | 6 | Uncertainty acknowledged but legal position tends to be presented as settled rather than contested. |
| MCDA | 4 | Weight sensitivity not propagated; legal uncertainty compressed into a criterion score. |

### Layer 2 Subtotals

| System | L2.1 /10 | L2.2 /20 | L2.3 /10 | L2 Total /40 |
|---|---:|---:|---:|---:|
| Multi-agent | 8 | 18 | 8 | 34 |
| Single-agent | 7 | 14 | 6 | 27 |
| MCDA | 6 | 10 | 4 | 20 |

---

## Layer 3: Process Quality /55

Multi-agent only. Descriptive; do not compare against baselines.

### L3.1 Stakeholder and Conflict Representation /15

Score: **14 / 15**

Both the upstream domestic legal counsel and the downstream government are represented as distinct stakeholder voices with genuine competing legitimacy claims. Five conflicts are mapped with specific resolution targets. This is the benchmark case where stakeholder representation is most critical, and the system preserves both sides of the legal interpretation without collapsing them into a single narrative.

### L3.2 Role Fidelity /15

Score: **12 / 15**

Legal agent correctly distinguishes what the law says from what policy should be; does not decide the engineering outcome. Economist restricts to BCR framing without deciding the governance question. The audit correction of the two competing over-strong legal claims (A1, A2) is the key role-fidelity success of this run.

### L3.3 Objection-Response Quality /10

Score: **7 / 10**

Five moderator-identified conflicts produce seven targeted conditions. The drought-contingency vs. average-flow distinction is the direct product of the Hydrologist + Downstream Farmers + Moderator exchange. The monitoring enforceability linkage is identified through joint Legal + Economist analysis. Full transcripts not preserved.

### L3.4 Evidence Audit and Revision /10

Score: **8 / 10**

60 claims audited; 5 corrections applied including the two critical legal over-strong claims; 0 unresolved blockers. The corrections prevent both sides from presenting contested legal interpretations as settled facts.

### L3.5 Minority Preservation /5

Score: **4 / 5**

Three minority positions preserved: Upstream Government's domestic permit argument; Legal Counsel's compact interpretation; Downstream Farmers' trust concern. All noted in the recommendation; first two are explicitly preserved as legitimate but not sufficient to override the financing and governance conditions.

### Layer 3 Total

| Dimension | Score | Max |
|---|---:|---:|
| Stakeholder/conflict representation | 14 | 15 |
| Role fidelity | 12 | 15 |
| Objection-response quality | 7 | 10 |
| Evidence audit and revision | 8 | 10 |
| Minority preservation | 4 | 5 |
| **Layer 3 total** | **45** | **55** |

---

## Summary Scorecard

| System | L1 Outcome /30 | L2 Evidence /40 | L3 Process /55 |
|---|---:|---:|---:|
| Multi-agent | 26 | 34 | 45 |
| Single-agent | 20 | 27 | n/a |
| MCDA | 14 | 20 | n/a |

---

## Interpretation

SRD-005's distinctive added value from multi-agent deliberation is governance legitimacy as a central analytical category. Neither the single-agent nor MCDA baseline adequately represents the competing legal interpretations or produces the drought-contingency/monitoring-enforceability distinction that makes the Defer conditions specific and actionable. The L3.1 score of 14/15 (highest in the benchmark suite) reflects the fact that both upstream and downstream stakeholder positions are represented with their legitimate concerns preserved — not collapsed into a "downstream wins" narrative. The audit correction of A1 and A2 is especially important: it prevents a simulated multi-agent deliberation from reaching a governance conclusion based on one party's contested legal interpretation presented as fact.
