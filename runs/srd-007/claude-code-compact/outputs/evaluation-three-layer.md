# Three-Layer Evaluation — SRD-007-cc

Evaluation against rubric v3 (three-layer structure).

Run type: **Claude Code compact run.**

Design note: SRD-007 tests whether the system produces a **specific, time-conditioned** recommendation on a genuinely ambiguous case, rather than defaulting to a generic Defer. A system that correctly identifies all must-detect items but produces generic Defer without the swing condition and revert trigger should score lower on L1.2 and L1.3.

---

## Layer 1: Outcome Quality /30

### L1.1 Decision-Range Fit /5

| System | Score | Rationale |
|---|---:|---|
| Multi-agent | 5 | Recommends "Build with conditions; revert to Defer if livelihood plan not complete in 9 months" — squarely within the evaluator-defined acceptable range (time-conditioned Build-with-conditions). |
| Single-agent | 3 | Recommends generic Defer — within the broad acceptable range but misses the time-conditioned pathway that distinguishes a near-complete gap from a fundamental flaw. |
| MCDA | 3 | Recommends Redesign or Defer — Redesign is a suspicious output on this case (the gaps are safeguard completion issues, not design flaws); Defer is acceptable but is produced for the wrong reason. |

### L1.2 Recommendation Specificity /15

| System | Score | Rationale |
|---|---:|---|
| Multi-agent | 13 | Specifies six conditions; distinguishes livelihood plan as the swing condition with a 9-month revert trigger; correctly separates pre-construction conditions from pre-approval conditions. |
| Single-agent | 8 | Identifies the livelihood plan gap and economic review; does not specify a time-conditioned pathway or distinguish pre-construction from pre-approval requirements. |
| MCDA | 4 | Cannot express condition hierarchy or time-conditioned pathway. |

### L1.3 Recommendation Calibration /10

| System | Score | Rationale |
|---|---:|---|
| Multi-agent | 9 | Correctly avoids unconditional Build (livelihood plan is unfinished); correctly avoids Do not build (the project is not fundamentally flawed); correctly avoids generic Defer (the gap is resolvable in months); correctly avoids Redesign (the gaps are safeguard completion, not design errors). |
| Single-agent | 5 | Generic Defer is defensible but misses the time-conditioned calibration that distinguishes this case. |
| MCDA | 4 | Redesign recommendation is miscalibrated for this case; gaps are not design flaws. |

### Layer 1 Subtotals

| System | L1.1 /5 | L1.2 /15 | L1.3 /10 | L1 Total /30 |
|---|---:|---:|---:|---:|
| Multi-agent | 5 | 13 | 9 | 27 |
| Single-agent | 3 | 8 | 5 | 16 |
| MCDA | 3 | 4 | 4 | 11 |

---

## Layer 2: Evidence Quality /40

### L2.1 Evidence Grounding /10

| System | Score | Rationale |
|---|---:|---|
| Multi-agent | 8 | Claims cite field IDs; five corrections applied; three major corrections prevent over-strong claims on the key swing condition, EAP status, and livelihood plan status. |
| Single-agent | 7 | Major claims grounded; does not distinguish pre-approval from pre-construction conditions at a granular level. |
| MCDA | 5 | Criterion scores linked to scenario; cannot express near-complete vs. fundamentally-absent distinction. |

### L2.2 Risk Coverage /20

Gold checklist: 4M, 6S.

Multi-agent coverage: R1 (livelihood restoration incomplete; swing condition; lender block) ✓M; R2 (BCR 0.97 under P90 + dry climate; below 1.0) ✓M; R3 (EAP at outline; full EAP required before construction) ✓M; R4 (fish passage feasible; effectiveness not assessed) ✓M; R5 (geotechnical borings 85% complete; abutment zone outstanding) ✓S; R6 (climate-adjusted spillway not updated) ✓S; R7 (environmental flow 20% contested by downstream ecology) ✓S; R8 (downstream wetland significance unclear) ✓S; R9 (sedimentation management not costed) ✓S; R10 (non-dam alternative covers 55%; project closes remaining 45%) ✓S.

M_detected: 4/4; S_detected: 6/6; compact-run ceiling applied.

| System | Score | Rationale |
|---|---:|---|
| Multi-agent | 18 | All 4M and 6S detected; compact ceiling (-2). |
| Single-agent | 13 | 4/4M detected; 3/6S detected (misses sedimentation, spillway update, and wetland significance explicitly). |
| MCDA | 9 | 2/4M well-characterized through scores; S items compressed. |

### L2.3 Uncertainty Calibration /10

| System | Score | Rationale |
|---|---:|---|
| Multi-agent | 8 | Uncertainty labels in audit; BCR margin acknowledged; downside acknowledged without overstating it as a blocker. |
| Single-agent | 6 | Uncertainty acknowledged; BCR downside flagged but does not distinguish it from the livelihood plan as the primary swing condition. |
| MCDA | 4 | Weight sensitivity not propagated; uncertainty compressed into criterion scores. |

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

All stakeholder positions represented. Five conflicts are mapped with targeted resolution framing. The upstream-affected households' conditional support and the development lender's near-approval signal are both preserved as separate deliberative inputs that inform the 9-month revert trigger structure.

### L3.2 Role Fidelity /15

Score: **13 / 15**

The three major audit corrections protect role fidelity: Dam Safety does not misrepresent EAP outline as sufficient; Social agent does not misrepresent the livelihood plan as complete; Irrigation Association stakeholder does not misrepresent the BCR as "clearly sound." These corrections demonstrate that role-specific positions are maintained and not conflated into a general approval narrative.

### L3.3 Objection-Response Quality /10

Score: **7 / 10**

The five-item conflict map produces a structured recommendation with a clear distinction between the swing condition (livelihood plan, 9-month trigger) and the non-swing conditions (pre-construction and pre-design requirements). This structure is a direct product of the Moderator + Development Lender + Social agent exchange. Full transcripts not preserved.

### L3.4 Evidence Audit and Revision /10

Score: **8 / 10**

62 claims audited; 5 corrections including three major substantive corrections (A1, A3, A4). The three major corrections prevent the recommendation from being built on mischaracterized evidence about the key swing condition.

### L3.5 Minority Preservation /5

Score: **4 / 5**

Three minority positions preserved (upstream households on pre-construction priority, downstream farmers on operating rules, environmental group on effectiveness assessment timing). All three are incorporated as conditions at the appropriate level.

### Layer 3 Total

| Dimension | Score | Max |
|---|---:|---:|
| Stakeholder/conflict representation | 13 | 15 |
| Role fidelity | 13 | 15 |
| Objection-response quality | 7 | 10 |
| Evidence audit and revision | 8 | 10 |
| Minority preservation | 4 | 5 |
| **Layer 3 total** | **45** | **55** |

---

## Summary Scorecard

| System | L1 Outcome /30 | L2 Evidence /40 | L3 Process /55 |
|---|---:|---:|---:|
| Multi-agent | 27 | 34 | 45 |
| Single-agent | 16 | 26 | n/a |
| MCDA | 11 | 18 | n/a |

---

## Interpretation

SRD-007 produces the largest L1 gap between multi-agent (27) and single-agent (16) in the benchmark suite. The reason is specific to this case type: the correct output is not a generic Defer but a time-conditioned Build-with-conditions that distinguishes a near-complete safeguard gap from a fundamental project flaw. The multi-agent system produces this distinction through the Moderator + Development Lender + Social agent exchange; the single-agent compresses all gaps into a Defer recommendation without the swing-condition specificity.

The L3 scores (45/55) are higher than simpler cases because the deliberative work is more substantial: five conflicts require targeted resolution, three major audit corrections are needed, and the stakeholder separation (upstream households conditional vs. downstream farmers conditional vs. lender "nearly financeable") directly informs the revert trigger structure.
