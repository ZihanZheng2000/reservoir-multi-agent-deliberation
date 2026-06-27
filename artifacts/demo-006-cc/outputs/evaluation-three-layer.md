# Three-Layer Evaluation — SRD-006-cc

Evaluation against rubric v3 (three-layer structure).

Run type: **Claude Code compact run.**

Design note: SRD-006 tests over-conservatism. The key evaluation criterion is not only risk coverage but correct characterization of the three remaining items as commissioning conditions, not construction blockers. A system that correctly identifies all four must-detect items AND correctly labels them as commissioning conditions or approval-enabling evidence scores well on L1.2 and L1.3.

---

## Layer 1: Outcome Quality /30

### L1.1 Decision-Range Fit /5

| System | Score | Rationale |
|---|---:|---|
| Multi-agent | 5 | Recommends "Build; commissioning conditions attached" — squarely within the evaluator-defined acceptable range. |
| Single-agent | 4 | Recommends "Build with conditions" — within range; does not clearly distinguish commissioning from construction conditions. |
| MCDA | 4 | Recommends "Build" at 4.41/5.0 — correct; does not express commissioning condition detail. |

### L1.2 Recommendation Specificity /15

| System | Score | Rationale |
|---|---:|---|
| Multi-agent | 14 | Correctly identifies all three commissioning items; explicitly labels them as pre-commissioning not pre-construction; names each item and its required resolution timing. |
| Single-agent | 10 | Identifies the three items but does not consistently distinguish commissioning from construction timing; may inadvertently frame sediment plan as a construction blocker. |
| MCDA | 7 | Does not express commissioning-condition specificity; produces a clean Build recommendation without conditional structure. |

### L1.3 Recommendation Calibration /10

| System | Score | Rationale |
|---|---:|---|
| Multi-agent | 9 | Avoids adding unnecessary conditions or deferring on a clean case; correctly characterizes all remaining items as commissioning conditions; no over-conservatism detected. |
| Single-agent | 7 | Directionally calibrated; minor risk of over-framing the sediment plan as a construction condition. |
| MCDA | 7 | Clean recommendation; no over-conservatism; cannot express conditional structure to verify calibration. |

### Layer 1 Subtotals

| System | L1.1 /5 | L1.2 /15 | L1.3 /10 | L1 Total /30 |
|---|---:|---:|---:|---:|
| Multi-agent | 5 | 14 | 9 | 28 |
| Single-agent | 4 | 10 | 7 | 21 |
| MCDA | 4 | 7 | 7 | 18 |

---

## Layer 2: Evidence Quality /40

### L2.1 Evidence Grounding /10

| System | Score | Rationale |
|---|---:|---|
| Multi-agent | 9 | All major approval-enabling evidence is cited with field IDs; two minor over-strong claims corrected; zero audit blockers. |
| Single-agent | 8 | Major evidence is cited; minor calibration issues but evidence base is strong on a well-documented case. |
| MCDA | 7 | Criterion scores well-grounded; commission/construction distinction not captured but scores are accurate. |

### L2.2 Risk Coverage /20

Gold checklist: 4M, 4S.

SRD-006 checklist tests correct characterization, not just detection.

Multi-agent coverage:
- R1 (sediment plan as commissioning condition, not construction blocker) ✓M — correctly characterized
- R2 (BCR 1.31 cited as positive approval-enabling evidence) ✓M — cited correctly
- R3 (resettlement complete; recognized as completed safeguard, not pending) ✓M — correctly characterized
- R4 (financing confirmed; cited as approval-enabling) ✓M — cited correctly
- R5 (diversion cutoff rule as first-operation condition) ✓S — correctly timed
- R6 (small farm water pricing as operating condition) ✓S — noted
- R7 (habitat offset monitoring as commissioning condition) ✓S — correctly timed
- R8 (non-dam alternatives cover 50%; partial alternative noted as reason project is necessary) ✓S — correctly framed

M_detected_and_characterized: 4/4; S_detected: 4/4; compact-run ceiling applied.

| System | Score | Rationale |
|---|---:|---|
| Multi-agent | 18 | All 4M correctly detected and characterized; all 4S detected; compact ceiling (-2). |
| Single-agent | 14 | 4/4M detected; 3/4S detected; may mischaracterize sediment plan as construction condition. |
| MCDA | 12 | 3/4M correctly characterized through scores; S items not expressible. |

### L2.3 Uncertainty Calibration /10

| System | Score | Rationale |
|---|---:|---|
| Multi-agent | 9 | Uncertainty correctly labeled as minimal on this case; BCR range noted; out-of-model scenarios acknowledged; no uncertainty inflation. |
| Single-agent | 7 | Uncertainty acknowledged appropriately; minor tendency to note additional risks not present in the scenario. |
| MCDA | 6 | Uncertainty not propagated; clean high scores are correctly not discounted. |

### Layer 2 Subtotals

| System | L2.1 /10 | L2.2 /20 | L2.3 /10 | L2 Total /40 |
|---|---:|---:|---:|---:|
| Multi-agent | 9 | 18 | 9 | 36 |
| Single-agent | 8 | 14 | 7 | 29 |
| MCDA | 7 | 12 | 6 | 25 |

---

## Layer 3: Process Quality /55

Multi-agent only. Descriptive; do not compare against baselines.

### L3.1 Stakeholder and Conflict Representation /15

Score: **12 / 15**

All seven stakeholder positions represented. Conflict map correctly identifies the three commissioning items as characterization questions, not genuine conflicts. The moderator's role is characterization framing, not conflict resolution — appropriately reflected. Compact ceiling applied; lower score than high-conflict cases because there is less deliberative work needed.

### L3.2 Role Fidelity /15

Score: **13 / 15**

Role boundaries are well-maintained. Dam Safety correctly limits its assessment to construction safety without commenting on operating yield; Ecologist correctly limits to biodiversity without commenting on economics; Social confirms safeguard completion without deciding engineering readiness. This is the benchmark run where role fidelity is easiest to verify because all agents find their domains clear.

### L3.3 Objection-Response Quality /10

Score: **6 / 10**

Minimal objection-response needed on a clean case. The main deliberative exchange is the sediment-plan characterization (construction blocker vs. commissioning condition), which is resolved by a joint Hydrologist/Dam Safety/Moderator framing. Lower score than high-conflict cases by design; deliberation on a clean case is correctly shorter.

### L3.4 Evidence Audit and Revision /10

Score: **8 / 10**

44 claims audited; 2 minor corrections; 0 unresolved blockers. High confidence level means fewer corrections are needed; the audit confirms that all major claims are well-grounded, which is itself an important result.

### L3.5 Minority Preservation /5

Score: **4 / 5**

No minority dissent on the approval decision itself. The downstream farmer preference (diversion cutoff rule before first fill) and environmental group preference (monitoring protocol before commissioning) are preserved as commissioning conditions. Compact ceiling applied.

### Layer 3 Total

| Dimension | Score | Max |
|---|---:|---:|
| Stakeholder/conflict representation | 12 | 15 |
| Role fidelity | 13 | 15 |
| Objection-response quality | 6 | 10 |
| Evidence audit and revision | 8 | 10 |
| Minority preservation | 4 | 5 |
| **Layer 3 total** | **43** | **55** |

---

## Summary Scorecard

| System | L1 Outcome /30 | L2 Evidence /40 | L3 Process /55 |
|---|---:|---:|---:|
| Multi-agent | 28 | 36 | 43 |
| Single-agent | 21 | 29 | n/a |
| MCDA | 18 | 25 | n/a |

---

## Interpretation

SRD-006 produces the highest L1 score (28/30) in the benchmark suite because the multi-agent system correctly identifies a clean-approval case and does not introduce unnecessary conservatism. The key contribution is not risk detection (most risks are absent on this case) but **correct characterization** of the three remaining items: they are commissioning conditions, not construction blockers, and the multi-agent system preserves this distinction explicitly.

The gap between multi-agent (28) and single-agent (21) on L1 is higher than on high-conflict cases. This reflects that the single-agent has a structural tendency to flag conditions without characterizing their timing — which is the key quality criterion on a clean-approval case. The MCDA baseline (18) also performs comparatively well on L1 because it avoids the commissioning-condition framing problem by not expressing conditions at all; it simply produces a high overall score.

Compared with the initial demo-006 v1 run (multi-agent 85/100), this cc compact run applies the v3 three-layer rubric and applies the commissioning-characterization distinction explicitly, producing a higher-quality evaluation artifact.
