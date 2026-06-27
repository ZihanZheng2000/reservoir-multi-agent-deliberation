# Case Run Summary: SRD-008

## Case Focus

Do not build case: remote hydropower dam with negative base-case economics, irreversible endemic-species loss, and a clearly dominant alternative.

This case tests whether the system can produce a Do not build recommendation when the evidence converges clearly in one direction. It also tests whether the system articulates *why* Do not build is the right label rather than Defer or Redesign — specifically, whether it identifies that the fundamental problems are location-specific and not resolvable by conditions or redesign.

## Multi-Agent Deliberation Result

### Recommendation

**Do not build. Pursue the wind portfolio alternative (F0.5) and conduct full grid dispatch modeling to confirm adequacy.**

### Final Build Approval Status

**Rejected.**

### Reasoning Structure

The deliberation produced unusually high inter-agent agreement on the direction of the recommendation. The developer argued for a revenue-sharing increase and additional conditions; all other agents identified problems that conditions cannot resolve.

The decisive deliberative contribution was distinguishing "Do not build" from "Defer" and "Redesign":

- **Why not Defer**: the fundamental problems — BCR below 1.0, endemic species extinction, indigenous consent withheld, EIA alternatives analysis invalidated — are not resolvable with more study time. Additional studies would confirm these problems, not solve them.
- **Why not Redesign**: reducing dam height reduces inundation extent but does not restore fish passage (still technically impossible at any height in this canyon geometry), does not restore the endemic species habitat (already the minimum viable range), and does not resolve indigenous consent. A smaller dam worsens the economics further without changing the fundamental objections.

Key agent positions:

| Agent | Position | Key evidence |
|---|---|---|
| Hydrologist | No water supply or flood control benefit; sedimentation degrades power output over project life. | F2.4, F2.5, F2.8, F5.5 |
| Engineering / Dam Safety | Engineering is technically feasible; fish passage is not. Canyon geometry precludes all known designs at 145m. | F3.3 |
| Ecologist | Endemic species extinction is irreversible. Ramsar inundation is a reportable international obligation. Fish passage is impossible. No redesign changes this. | F3.2, F3.3, F3.5 |
| Climate Risk | Dry-year generation loss of 33% and sedimentation compound economic weakness under climate uncertainty. | F2.6, F2.8, F5.3 |
| Economist / Finance | BCR 0.94 in base case fails before any downside assumption. Wind alternative BCR 1.68 at 42% lower cost. No PPA signed. | F5.3, F5.7, F5.8 |
| Social / Resettlement | Indigenous consent formally withheld; FPIC process not conducted. Revenue sharing rejected. | F4.2, F4.3, F4.6 |
| Legal / Policy | FPIC obligation exists under international standards regardless of domestic permit authority. Legal challenge filed. Export credit agency has paused. | F6.3, F6.4, F6.5 |

### Stakeholder Position Summary

| Stakeholder | Position | Key evidence |
|---|---|---|
| Developer | Build; willing to increase revenue-sharing fund. | F7.1 |
| Energy ministry | Policy priority for dispatchable renewables, but no commitment to this project or location. | F7.2 |
| Indigenous community | Formally withholds consent; non-negotiable. | F7.3, F4.3 |
| River tourism association | Opposes; economic impact study excluded their livelihoods. | F7.4, F4.4 |
| Environmental NGO | Opposes; endemic species loss is permanent and fish passage is physically impossible. | F7.5, F3.2, F3.3 |
| Export credit agency | Will not finance without FPIC and independent alternatives analysis; both absent. | F7.6, F6.4 |

### Decisive Evidence

| Evidence | Fields | Effect |
|---|---|---|
| BCR 0.94 in base case; fails before any downside assumption. | F5.3 | Project is uneconomic on its own terms. |
| Wind portfolio BCR 1.68 at 42% lower capital cost. | F5.7, F5.8 | Dominant alternative exists; dam cannot be justified on least-cost grounds. |
| Two endemic species; fish passage physically impossible at any dam height in this canyon. | F3.2, F3.3 | Ecological harm is irreversible and non-mitigable regardless of design. |
| Indigenous community has formally withheld FPIC. | F4.3, F6.3 | Legal and ethical blocker that cannot be resolved by redesign or conditions. |
| No water supply or flood control benefit. | F2.4, F2.5 | No public-interest justification beyond power revenue. |
| Ramsar inundation is a reportable obligation. | F3.5 | International legal constraint. |
| Sedimentation at 1.8%/year degrades generation by ~25% over 30 years. | F2.8, F5.5 | True economic viability is worse than BCR 0.94 headline figure. |

### Why Redesign Does Not Work

| Objection | Why redesign does not resolve it |
|---|---|
| Fish passage impossible | Canyon geometry constraint applies at any dam height; shorter dam reduces power but does not enable passage |
| Endemic species extinction | Any inundation of the 28 km gorge eliminates the minimum viable habitat; there is no partial solution |
| Indigenous consent withheld | Consent is about the gorge itself; a smaller dam inundating fewer sites does not change the foundational objection |
| BCR already below 1.0 | Smaller dam produces less revenue while transmission costs are largely fixed; economics worsen with redesign |

### Minority Report

| Agent/stakeholder | Dissenting position | Status |
|---|---|---|
| Developer | Revenue-sharing increase and improved compensation could achieve social acceptance. | Not adopted; indigenous community explicitly stated consent is not contingent on compensation level |
| Energy ministry | Dispatchable renewable capacity is a genuine policy need. | Incorporated as a reason to pursue the wind alternative, not a reason to approve this project |

### Evidence Confidence

**High** for the Do not build direction. The wind portfolio adequacy (F8.4) remains to be confirmed by full grid dispatch modeling, but this does not affect the dam rejection — it only affects the pace and specification of the alternative.

## Baseline Outputs

### Single-Agent Baseline

Recommendation: **Do not build; pursue wind and storage alternatives.**

The single-agent baseline correctly identified the project as non-viable on economic, ecological, and rights grounds. It recommended Do not build. On a case where the direction is clear, the single-agent output is largely aligned with multi-agent on recommendation, though it compressed the indigenous rights argument and did not distinguish why Redesign fails separately from why Build fails.

### MCDA Baseline

| Criterion | Score 1-5 |
|---|---:|
| water_supply_benefit | 1 |
| flood_control_benefit | 1 |
| energy_benefit | 3 |
| economic_viability | 1 |
| engineering_feasibility | 3 |
| ecological_impact_acceptability | 1 |
| social_impact_acceptability | 1 |
| legal_governance_readiness | 1 |
| climate_robustness | 2 |
| stakeholder_support | 1 |
| evidence_confidence | 3 |

Weighted score: **1.73 / 5.00**

Recommendation: **Do not build.**

MCDA performs relatively well on this case because the low scores across economic, ecological, social, and governance dimensions all converge clearly. When all blocking dimensions score at or near 1, the weighted average leaves little room for ambiguity. This illustrates both MCDA's strength (transparent aggregation on clear cases) and its limitation (it cannot explain why redesign is specifically inadequate, only that the current configuration scores poorly).

## Deliberative Acceptability Scores

| System | Evidence Grounding /20 | Risk Coverage /15 | Stakeholder and Conflict Representation /15 | Role Fidelity /15 | Deliberation and Revision /15 | Decision Usefulness /20 | Total /100 | Final recommendation |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Multi-agent | 18 | 15 | 13 | 13 | 13 | 17 | 89 | Do not build; pursue wind portfolio |
| Single-agent | 15 | 14 | 8 | 5 | 4 | 17 | 63 | Do not build; pursue wind and storage alternatives |
| MCDA | 12 | 12 | 5 | 2 | 1 | 14 | 46 | Do not build |

## Case Interpretation

SRD-008 completes the benchmark decision space by producing the first Do not build recommendation in the suite.

Three patterns are worth noting for the cross-case analysis:

**1. Score gaps on clear cases.** On cases where the direction is unambiguous (SRD-006: Build; SRD-008: Do not build), the multi-agent advantage on Decision Usefulness is moderate (17/20 for both systems on SRD-008). The large gap appears on ambiguous cases (SRD-007: multi-agent 18, single-agent 12). This suggests multi-agent adds the most decision-usefulness value when the evidence is genuinely mixed.

**2. MCDA performs better on extreme cases.** MCDA scores 46 on SRD-008 vs. 39–43 on the moderate-complexity cases. When all dimensions score low, the weighted average is unambiguous. MCDA is weakest when a project is good on some dimensions and blocked on others — its aggregation mechanism hides the blocker.

**3. The "Why not Redesign" argument is a multi-agent contribution.** Single-agent also recommends Do not build but does not systematically separate "Do not build" from "Redesign." The multi-agent deliberation forces each agent to explicitly evaluate whether redesign resolves their objection, producing a more robust and defensible rejection.
