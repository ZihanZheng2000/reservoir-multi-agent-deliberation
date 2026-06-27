# MCDA Baseline — SRD-001-cc

Multi-Criteria Decision Analysis applied to the SRD-001-cc scenario. Criteria weights are provisional and documented in `packages/model-package-synthetic-benchmark-v0.1.md`.

---

## Criteria and Weights (Provisional)

| Criterion | Weight | Sub-criteria included |
|---|---:|---|
| Water supply benefit | 0.20 | Firm yield vs. demand gap, drought reliability |
| Flood control benefit | 0.10 | Peak reduction, design event coverage |
| Energy benefit | 0.05 | Installed capacity, annual generation, grid role |
| Economic viability | 0.15 | BCR base and downside, cost overrun risk, financing |
| Ecological impact | 0.15 | Species risk, habitat loss, mitigation credibility |
| Social impact | 0.15 | Displacement scale, livelihood restoration, sacred sites, community support |
| Legal/governance readiness | 0.10 | EIA status, consultation, RAP completeness, bank conditions |
| Climate robustness | 0.10 | Adjusted yield, downside scenario coverage, spillway adequacy |
| **Total** | **1.00** | |

---

## Criterion Scores (1–5 scale)

| Criterion | Raw score | Weight | Weighted score | Evidence basis |
|---|---:|---:|---:|---|
| Water supply benefit | 4 | 0.20 | 0.80 | F2.4, F2.5, F2.7 |
| Flood control benefit | 3 | 0.10 | 0.30 | F3.2, F3.3, F3.5 |
| Energy benefit | 3 | 0.05 | 0.15 | F4.1–4.4 |
| Economic viability | 2 | 0.15 | 0.30 | F5.2, F5.3 |
| Ecological impact | 1 | 0.15 | 0.15 | F7.2, F7.3, F7.7, F7.8 |
| Social impact | 1 | 0.15 | 0.15 | F8.1–F8.8 |
| Legal/governance readiness | 1 | 0.10 | 0.10 | F9.3, F9.4, F9.6, F9.8 |
| Climate robustness | 2 | 0.10 | 0.20 | F11.1, F2.7 |
| **Weighted total** | | **1.00** | **2.15** | |

---

## MCDA Decision

**Weighted composite score: 2.15 / 5.0**

Decision threshold for approval: 3.0+ (provisionally).
Decision threshold for Redesign: 2.0–3.0.
Decision threshold for Defer / Do not build: below 2.0.

**MCDA recommendation: Redesign** (score falls in 2.0–3.0 range).

---

## Sensitivity Analysis

| Scenario | What changes | Direction of score | MCDA outcome |
|---|---|---|---|
| Higher ecological weight (0.25 vs. 0.15) | Larger penalty for endemic species risk | Decreases to ~1.90 | Defer |
| Lower ecological + social weight, higher water supply | If policy frames water security as primary | Increases to ~2.45 | Redesign (stronger) |
| Ecological score drops to 0 (irreversible harm confirmed) | Species-specific study finds no viable passage | Decreases substantially (< 1.5) | Do not build |
| All safeguards completed, governance score rises to 4 | Complete legal and RAP readiness | Increases to ~2.60 | Redesign (firmer) |

---

## MCDA Limitations for This Case

1. The weighted-sum MCDA method does not capture irreversibility. A score of 1 in Ecological Impact could represent either a recoverable impact or an irreversible species loss — the number is identical. The multi-agent deliberation explicitly preserves the Ecologist's minority position that irreversibility may make Redesign insufficient even if the score improves. MCDA cannot represent this distinction.

2. Criterion independence is violated in this case: Economic Viability and Climate Robustness share inputs (yield projections). MCDA treats them as independent, overstating the apparent precision of the composite score.

3. The weights are provisional and have not been validated against stakeholder preferences. Downstream user fishery interests and upstream sacred site concerns are subsumed into Social Impact (weight 0.15) rather than treated as potentially categorical conditions.

4. MCDA produces a single composite number (2.15) that aggregates across criteria; this paper trail does not survive the aggregation. The multi-agent deliberation preserves the reasoning behind each score, the dissenting positions, and the specific conditions required for the recommendation to change.
