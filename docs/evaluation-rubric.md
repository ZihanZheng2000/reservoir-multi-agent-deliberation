# Evaluation Rubric Summary

The benchmark uses a three-layer rubric.

## Layer 1: Outcome Quality /30

Measures whether the recommendation is useful for decision-making.

- Decision-range fit /5
- Recommendation specificity /15
- Recommendation calibration /10

## Layer 2: Evidence Quality /40

Measures whether the output is grounded in case facts and recovers the designed risk structure.

- Evidence grounding /10
- Risk coverage /20
- Uncertainty calibration /10

## Layer 3: Process Quality /55

Measures deliberative process quality for multi-agent runs only.

- Stakeholder/conflict representation /15
- Role fidelity /15
- Objection-response quality /10
- Evidence audit and revision /10
- Minority preservation /5

## Reporting Rule

Layer 1 and Layer 2 can be compared across multi-agent, single-agent, and MCDA outputs. Layer 3 should be reported only for multi-agent deliberation. Do not add all three layers into one combined score.

The detailed rubric is in `protocols/revised-evaluation-rubric-v0.2.md`.
