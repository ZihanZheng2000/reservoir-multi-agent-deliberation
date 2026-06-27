# Evaluator-Only Gold Checklist: SRD-006

Do not provide this file to agents. It is for evaluation only.

## Design Note for Evaluators

SRD-006 is the benchmark's clean-approval case. The gold checklist here differs from high-conflict cases: it tests whether the system correctly **characterizes** the nature of remaining items (commissioning conditions vs. construction blockers), not just whether it identifies risks. A system that correctly identifies all three remaining items AND correctly labels them as commissioning conditions should score well. A system that identifies them but treats them as construction blockers should score lower on Recommendation Calibration.

## Expected Findings Checklist

Tier key: **M** = must correctly identify and characterize (miss penalty: −4 per item); **S** = should note (miss penalty: −1 per item)

| Risk ID | Tier | Finding that should be identified and correctly characterized | Fields |
|---|---|---|---|
| R1 | M | Long-term sediment management plan is drafted but not formally adopted; correctly characterized as a **commissioning condition** (affects long-term yield management, not construction safety); construction approval should not be withheld for this alone. | F6.8, F8.1 |
| R2 | M | BCR 1.31 under P90 cost and 1-in-30 dry-climate combined scenario; system must **cite this as positive approval-enabling evidence**, not dismiss or ignore it. Economics are robust across all modeled scenarios. | F5.3 |
| R3 | M | Resettlement plan complete, independently reviewed, all 12 affected households have signed agreements; no unresolved formal objection; system must recognize this as a completed safeguard, not a pending blocker. | F4.3, F4.4 |
| R4 | M | Financing confirmed (60% grant + 40% bond); funder has confirmed safeguard conditions are satisfied and funds will be released on construction permit; system must cite this as approval-enabling, not flag it as uncertain. | F5.4, F7.6 |
| R5 | S | Low-flow diversion cutoff rule should be written into the operating license before first fill, not before construction; correctly identified as a first-operation condition. | F8.2, F7.4 |
| R6 | S | Small farm water pricing protection should be included in operating rules; this is a legitimate operating condition raised by local government, not a construction blocker. | F7.2 |
| R7 | S | Annual habitat offset monitoring protocol is a commissioning condition; it must be finalized before commissioning, not before construction. | F8.3, F7.5 |
| R8 | S | Non-dam alternatives (demand management, managed aquifer recharge) cover approximately 50% of deficit; project is justified because they cannot close the full gap — the system should note this distinction, not treat partial alternatives as a reason to reject. | F5.6 |

## Reasonable Decision Range

**Acceptable outputs:**
- Build: all construction-blocking conditions are resolved; commissioning conditions are legitimate to attach but must not be framed as construction blockers.
- Build with commissioning conditions: attach the three remaining administrative items as pre-commissioning operating requirements, not pre-construction blockers.

**Suspicious outputs:**
- Defer pending the sediment management plan, the diversion cutoff rule, or the habitat monitoring protocol: these are administrative operating items, not safety or safeguard gaps that block construction.
- Do not build despite resolved resettlement, completed EIA, confirmed financing, no endemic species, and BCR 1.31 under worst case — this is the strongest indicator of over-conservatism in the benchmark.
- Redesign: no structural, ecological, or social design flaw has been identified that warrants redesign.
- Any output that treats the three commissioning items as equivalent in gravity to unresolved safeguard or engineering gaps in SRD-001 or SRD-007.
