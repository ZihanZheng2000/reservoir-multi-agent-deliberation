# Case Run Summary: SRD-006

## Case Focus

Clean approval case: small off-channel water security reservoir.

This case tests whether the system can produce a Build recommendation when no structural blockers remain. It exposes over-conservatism if the system defaults to Defer or adds unnecessary conditions that apply to construction rather than commissioning.

## Multi-Agent Deliberation Result

### Recommendation

**Build; attach three operating conditions before first commissioning.**

### Final Build Approval Status

**Granted, subject to commissioning conditions.**

### Reasoning Structure

All expert and stakeholder agents agreed the project is construction-ready. No agent identified a structural, safety, social, or ecological blocker. The three remaining items (sediment management plan, low-flow diversion cutoff, habitat monitoring protocol) are administrative conditions that apply to first operation, not to construction approval.

The deliberation centered not on whether to build but on which conditions belong to the construction permit versus the operating license. The key deliberative contribution was explicitly separating these two categories to prevent unnecessary delay.

Key agent positions:

| Agent | Position | Key evidence |
|---|---|---|
| Hydrologist | Firm yield exceeds deficit in all scenarios including 1-in-30 drought; off-channel design preserves river flows. | F2.2, F2.3, F2.4, F2.6 |
| Engineering / Dam Safety | Final design complete; geotechnical, spillway, and EAP all clear; no blocker. | F6.1–F6.7 |
| Ecologist | No critical habitat or protected species; offset plan funded; monitoring condition sufficient. | F3.2–F3.5, F6.5 |
| Climate Risk | Climate-adjusted spillway reviewed; dry-year yield still covers projected deficit. | F2.4, F6.4 |
| Economist / Finance | BCR positive in base and P90 combined scenario; financing confirmed; no economic blocker. | F5.3, F5.4 |
| Social / Resettlement | Resettlement complete; all objections resolved; grievance mechanism operational. | F4.3, F4.4, F4.5 |
| Legal / Policy | Permits at final administrative stage; all EIA and safeguard requirements met. | F6.5, F6.6 |

### Stakeholder Position Summary

| Stakeholder | Position | Key evidence |
|---|---|---|
| Water utility | Full support; project closes water gap cost-effectively. | F2.2, F2.3, F5.3 |
| Local government | Support with operating pricing condition for smallholder farms. | F7.2 |
| Affected households | No objections; relocation agreements finalized. | F4.3, F7.3 |
| Downstream farmers | Support; require low-flow diversion cutoff in operating license before first fill. | F7.4, F8.2 |
| Environmental group | Support; require annual habitat monitoring reports. | F7.5, F8.3 |
| Funder | Ready to disburse; all safeguard conditions satisfied. | F7.6 |

### Decisive Evidence

| Evidence | Fields | Effect |
|---|---|---|
| Firm yield exceeds projected deficit in all modeled scenarios. | F2.2, F2.3, F2.4 | Removes water supply uncertainty as a blocker. |
| Off-channel design; no mainstem blockage. | F2.6, F3.1 | Removes river ecology conflict. |
| No endemic or protected species; EIA independently reviewed positively. | F3.3, F6.5 | Removes ecological blocker. |
| Resettlement complete; all affected households agreed. | F4.3, F4.4 | Removes social blocker. |
| BCR positive under P90 cost and dry-climate scenario. | F5.3 | Removes economic blocker. |
| Final design, geotechnical, spillway, and EAP all complete. | F6.1–F6.7 | Removes engineering and safety blocker. |

### Commissioning Conditions (not construction blockers)

| Condition | Fields | Required by |
|---|---|---|
| Formally adopt sediment management plan | F6.8, F8.1 | Water authority, before first operation |
| Include low-flow diversion cutoff in operating license | F8.2 | Operating permit, before first fill |
| Finalize annual habitat offset monitoring protocol | F8.3, F3.5 | EIA compliance, before first operation |

### Minority Reports

None. All agents and stakeholders support the project or have operational conditions only. This absence of minority reports is itself a result — it distinguishes this case from SRD-001 through SRD-005 where unresolved dissent is expected.

### Evidence Confidence

**High.**

## Baseline Outputs

### Single-Agent Baseline

Recommendation: **Build with conditions.**

The single-agent baseline correctly identified the project as approvable. It listed conditions similar to the multi-agent output. On a simple case, the single-agent result is largely aligned with the multi-agent recommendation. The main limitation: it compressed downstream farmer and environmental group positions into generic conditions rather than preserving them as distinct stakeholder voices.

### MCDA Baseline

| Criterion | Score 1-5 |
|---|---:|
| water_supply_benefit | 5 |
| flood_control_benefit | 2 |
| energy_benefit | 1 |
| economic_viability | 5 |
| engineering_feasibility | 5 |
| ecological_impact_acceptability | 5 |
| social_impact_acceptability | 5 |
| legal_governance_readiness | 5 |
| climate_robustness | 4 |
| stakeholder_support | 4 |
| evidence_confidence | 5 |

Weighted score: **4.41 / 5.00**

Recommendation: **Build.**

MCDA performs well on this case because no dimension has a blocker-level concern. The compressed score aggregation is less misleading when all dimensions point in the same direction.

## Deliberative Acceptability Scores

| System | Evidence Grounding /20 | Risk Coverage /15 | Stakeholder and Conflict Representation /15 | Role Fidelity /15 | Deliberation and Revision /15 | Decision Usefulness /20 | Total /100 | Final recommendation |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Multi-agent | 18 | 14 | 11 | 13 | 10 | 19 | 85 | Build; commissioning conditions attached |
| Single-agent | 15 | 13 | 9 | 5 | 4 | 18 | 64 | Build with conditions |
| MCDA | 13 | 13 | 6 | 2 | 1 | 18 | 53 | Build |

## Case Interpretation

SRD-006 demonstrates two things:

**1. The system is not unconditionally conservative.** When structural blockers are resolved, the multi-agent system recommends Build. This directly addresses the over-conservatism concern raised by the five-case conservative-bias check.

**2. Score gaps narrow on a low-conflict case.** The multi-agent total (85) is lower than its SRD-001 to SRD-005 range (89–92). MCDA reaches 53 (vs. 39–44 in complex cases) and single-agent reaches 64 (roughly consistent). The narrowing at the top — multi-agent 85 vs. MCDA 53 vs. single-agent 64 — reflects a meaningful pattern: the multi-agent advantage is specifically in stakeholder conflict representation and deliberation quality, both of which are naturally lower when there is little conflict to represent. This is expected behavior, not a performance failure. The score ceiling problem is partly a case-selection artifact — the system scores similarly high on all difficult cases because they all require the same deliberative capacity.

**Decision diversity update:** SRD-006 produces the first clean Build (or near-Build) recommendation in the benchmark suite, completing the decision space.
