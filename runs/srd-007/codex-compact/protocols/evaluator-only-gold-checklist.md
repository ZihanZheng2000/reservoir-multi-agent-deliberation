# Evaluator-Only Gold Checklist: SRD-007

Do not provide this file to agents. It is for evaluation only.

## Design Note for Evaluators

SRD-007 is the near-tipping-point case. The core test is whether the system identifies the **livelihood restoration gap** as the swing condition and produces a **specific, time-conditioned recommendation** rather than a generic Defer. A system that correctly identifies all must-detect items but produces a generic Defer without specifying the swing condition and a resolution pathway should score lower on Recommendation Specificity. A system that produces a time-conditioned Build-with-conditions tied to livelihood plan completion should score higher.

## Expected Risk and Issue Checklist

Tier key: **M** = must-detect (miss penalty: −4 per item on Risk Coverage /20); **S** = should-detect (miss penalty: −1 per item)

| Risk ID | Tier | Issue that should be identified | Fields |
|---|---|---|---|
| R1 | M | Livelihood restoration section of the resettlement action plan is incomplete; identified as the key gap by the independent reviewer; the development lender will not disburse until this section is complete; this is the **swing condition** for the recommendation. | F5.4, F9.1, F7.4, F8.6 |
| R2 | M | BCR falls to 0.97 below 1.0 under P90 cost and dry-climate combined scenario; economic viability is marginally confirmed under the base case only; the project does not clear the standard 1.0 threshold under downside assumptions. | F6.3, F9.2 |
| R3 | M | Emergency Action Plan is at outline stage only; a full EAP is required before construction can begin; this is a dam safety standard requirement, not a discretionary condition. | F3.6 |
| R4 | M | Fish passage is technically feasible for the species of concern but effectiveness has not been assessed; mitigation credibility depends on a completed effectiveness study. | F4.4, F9.3 |
| R5 | S | Geotechnical investigation is 85% complete; one abutment zone requires additional borings before detailed design can begin; not a blocker for feasibility approval but must be resolved before detailed design. | F3.3, F9.6 |
| R6 | S | Climate-adjusted spillway estimate has not been updated; the current spillway design uses historical inflow data; update required before detailed design. | F3.5, F9.4 |
| R7 | S | Environmental flow minimum of 20% natural flow is contested by the downstream ecology assessment; adequacy under low-flow conditions is not confirmed. | F2.5 |
| R8 | S | Downstream wetland flow significance under altered seasonal pattern is unclear; preliminary study suggests manageable but full assessment is not complete. | F4.5, F9.5 |
| R9 | S | Long-term sedimentation management (0.5%/yr storage loss) has not been costed or planned. | F2.6 |
| R10 | S | Non-dam alternative (irrigation efficiency + groundwater) covers 55% of irrigation gap at lower capital cost; this is a partial alternative that does not replace the project but establishes that the marginal irrigation gap this project closes is 45% of the total deficit. | F6.6 |

## Reasonable Decision Range

**Acceptable outputs:**
- Build with conditions: issue construction approval contingent on the livelihood restoration plan being completed within a defined period (approximately 9 months is defensible); if not completed within that period, revert to Defer; other gaps (EAP, fish passage effectiveness, geotechnical borings, spillway update) addressed before detailed design or construction as appropriate.
- Defer until the livelihood plan is complete: acceptable, but should specify the livelihood plan as the condition, not a generic list of all gaps.

**Suspicious outputs:**
- Unconditional Build without resolving the livelihood restoration plan; this ignores the development lender's explicit blocking condition and the independent reviewer's identified key gap.
- Do not build without recognizing that the irrigation need is credible, the project is near-complete on safeguards, and the remaining gap is resolvable — the project is not fundamentally flawed, only near-complete.
- Redesign: the identified gaps are safeguard and assessment completion issues, not design flaws; recommending redesign confuses an incomplete safeguard with a structural problem.
- Generic Defer without identifying the livelihood plan as the specific swing condition and without suggesting a time-conditioned pathway.
