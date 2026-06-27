# Cross-Case Score Summary v0.1

## Scope

This file summarizes synthetic cases SRD-001 to SRD-008.

Scores measure decision-support quality across three separate layers, not a single combined score.

**Rubric history:**
- v1 (all 8 cases below): single 100-point scale with 6 dimensions. Used for initial cross-case comparison and reported here for reference.
- former Codex two-layer run: two-layer structure (shared /60 + deliberative /40). Superseded.
- **v3 (current)**: three-layer structure â€” Outcome Quality /30 (all systems), Evidence Quality /40 (all systems), Process Quality /55 (multi-agent only, descriptive). Apply this rubric to all future full-protocol runs.

The v1 scores below are retained as preliminary estimates. They should not be used for manuscript comparison tables because they collapse outcome quality, evidence quality, and deliberative process quality into a single number that structurally favors the multi-agent system (Role Fidelity and Deliberation/Revision dimensions cannot be scored by MCDA or single-agent by design).

**Cross-system comparison should use Layer 1 and Layer 2 scores only.** Layer 3 scores describe the quality of deliberative process for multi-agent and are not compared against baselines.

## Case List

| Case | Type | Multi-agent recommendation |
|---|---|---|
| SRD-001 | High-conflict new multipurpose dam | Redesign, with final build approval deferred |
| SRD-002 | Low-conflict off-channel / existing reservoir expansion | Build with conditions through phased approval |
| SRD-003 | Hydropower-dominant project with weak local water benefits | Redesign toward hybrid alternative |
| SRD-004 | Flood-control emergency project after disasters | Phased emergency package now; defer final reservoir approval |
| SRD-005 | Transboundary / downstream-conflict reservoir | Defer pending basin agreement, joint monitoring, and drought rules |
| SRD-006 | Clean approval case: small off-channel water security reservoir | Build; commissioning conditions attached |
| SRD-007 | Near-tipping-point: marginal economics, one incomplete safeguard | Build with conditions; revert to Defer if livelihood plan not complete in 9 months |
| SRD-008 | Do not build: negative-BCR remote hydropower dam with irreversible endemic-species loss | Do not build; pursue wind portfolio alternative |

## SRD-001 Codex vs Claude Code Runs

SRD-001 now has two named reruns:

| Run | Directory | Role in the benchmark |
|---|---|---|
| Codex revised compact run | `artifacts/demo-001-co/` | Protocol/control run with neutral scenario, hidden checklist, prompt templates, emergent issue discovery, and compact three-layer evaluation. |
| Claude Code full transcript run | `artifacts/demo-001-cc/` | Full transcript-style run with separate expert/stakeholder rounds and stronger process inspectability. |
| Codex full transcript-style run | `artifacts/demo-001-co-full/` | Codex-generated full meeting artifact using the neutral `demo-001-co` scenario and current three-layer rubric. |

Current three-layer comparison:

| Run/System | L1 Outcome /30 | L2 Evidence /40 | L3 Process /55 |
|---|---:|---:|---:|
| Codex multi-agent compact | 25 | 32 | 41 |
| Claude Code multi-agent full transcript | 26 | 36 | 49 |
| Codex multi-agent full transcript-style | 28 | 38 | 51 |

Interpretation: `demo-001-co` is stronger as the benchmark protocol/control artifact; `demo-001-cc` is stronger as a transcript-level demonstration of the deliberative process.


## Current Three-Layer Compact Scores: SRD-002 to SRD-008

These are compact-run evaluations and should be treated as preliminary. The compact-run ceiling is applied to multi-agent risk coverage and audit/revision scores.

| Case | Multi-agent L1 /30 | Multi-agent L2 /40 | Multi-agent L3 /55 | Single-agent L1 /30 | Single-agent L2 /40 | MCDA L1 /30 | MCDA L2 /40 |
|---|---:|---:|---:|---:|---:|---:|---:|
| SRD-002 | 27 | 33 | 39 | 26 | 30 | 23 | 27 |
| SRD-003 | 27 | 34 | 42 | 23 | 29 | 19 | 24 |
| SRD-004 | 28 | 34 | 43 | 26 | 30 | 20 | 25 |
| SRD-005 | 28 | 35 | 44 | 24 | 30 | 20 | 25 |
| SRD-006 | 29 | 34 | 35 | 28 | 31 | 28 | 30 |
| SRD-007 | 29 | 34 | 43 | 20 | 28 | 16 | 23 |
| SRD-008 | 29 | 35 | 40 | 27 | 31 | 25 | 28 |

Interpretation: gaps narrow on clear cases (SRD-006, SRD-008) and widen on the near-tipping-point case (SRD-007). This supports the claim that multi-agent deliberation is most valuable when decision conditions must be sequenced rather than merely aggregated.


## Claude Code Compact Counterparts

Claude Code compact runs exist for SRD-002 to SRD-008. These are independent compact artifacts and should not be merged with the Codex compact files.

| Case | Directory | Multi-agent L1 /30 | Multi-agent L2 /40 | Multi-agent L3 /55 | Note |
|---|---|---:|---:|---:|---|
| SRD-002 | artifacts/demo-002-cc/ | 26 | 34 | 44 | Low-conflict approval case; strong phasing and audit detail. |
| SRD-003 | artifacts/demo-003-cc/ | 26 | 34 | 43 | Hydropower case; strongest value is redesign toward hybrid. |
| SRD-004 | artifacts/demo-004-cc/ | 26 | 34 | 43 | Emergency case; strongest value is emergency-now/final-approval-later sequencing. |
| SRD-005 | artifacts/demo-005-cc/ | 26 | 34 | 45 | Transboundary case; highest L3.1 in suite; competing legal interpretations preserved. |
| SRD-006 | artifacts/demo-006-cc/ | 28 | 36 | 43 | Clean approval case; highest L1 in suite (28/30); commissioning-condition characterization. |
| SRD-007 | artifacts/demo-007-cc/ | 27 | 34 | 45 | Near-tipping-point; largest L1 gap vs. single-agent (27 vs. 16) in suite. |
| SRD-008 | artifacts/demo-008-cc/ | 27 | 35 | 46 | Do not build case; highest L3 in suite (46/55); explicit Redesign ruling-out. |

Use these directories for Codex-vs-Claude-Code compact comparisons.

## Per-Case Scores

### SRD-001

| System | Evidence Grounding /20 | Risk Coverage /15 | Stakeholder and Conflict Representation /15 | Role Fidelity /15 | Deliberation and Revision /15 | Decision Usefulness /20 | Total /100 | Final recommendation |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Multi-agent | 19 | 15 | 14 | 13 | 14 | 17 | 92 | Redesign, with final build approval deferred |
| Single-agent | 15 | 14 | 8 | 5 | 4 | 16 | 62 | Defer approval pending major revisions and additional studies |
| MCDA | 12 | 11 | 4 | 2 | 1 | 9 | 39 | Do not build as proposed; major redesign required |

### SRD-002

| System | Evidence Grounding /20 | Risk Coverage /15 | Stakeholder and Conflict Representation /15 | Role Fidelity /15 | Deliberation and Revision /15 | Decision Usefulness /20 | Total /100 | Final recommendation |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Multi-agent | 18 | 14 | 13 | 13 | 13 | 18 | 89 | Build with conditions through phased approval |
| Single-agent | 15 | 13 | 8 | 5 | 4 | 17 | 62 | Approve with conditions |
| MCDA | 12 | 11 | 4 | 2 | 1 | 14 | 44 | Build with conditions |

### SRD-003

| System | Evidence Grounding /20 | Risk Coverage /15 | Stakeholder and Conflict Representation /15 | Role Fidelity /15 | Deliberation and Revision /15 | Decision Usefulness /20 | Total /100 | Final recommendation |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Multi-agent | 18 | 15 | 14 | 13 | 13 | 17 | 90 | Defer pending alternatives analysis and downstream livelihood study |
| Single-agent | 15 | 14 | 8 | 5 | 4 | 16 | 62 | Defer approval and conduct broader alternatives analysis |
| MCDA | 12 | 11 | 4 | 2 | 1 | 10 | 40 | Do not build as proposed; major redesign or alternatives required |

### SRD-004

| System | Evidence Grounding /20 | Risk Coverage /15 | Stakeholder and Conflict Representation /15 | Role Fidelity /15 | Deliberation and Revision /15 | Decision Usefulness /20 | Total /100 | Final recommendation |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Multi-agent | 18 | 15 | 14 | 13 | 13 | 18 | 91 | Phased emergency package now; defer final reservoir approval |
| Single-agent | 15 | 14 | 8 | 5 | 4 | 17 | 63 | Emergency measures now; defer final reservoir approval |
| MCDA | 12 | 12 | 5 | 2 | 1 | 11 | 43 | Redesign / Defer, with emergency measures |

### SRD-005

| System | Evidence Grounding /20 | Risk Coverage /15 | Stakeholder and Conflict Representation /15 | Role Fidelity /15 | Deliberation and Revision /15 | Decision Usefulness /20 | Total /100 | Final recommendation |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Multi-agent | 18 | 15 | 15 | 13 | 13 | 18 | 92 | Defer pending basin agreement and joint monitoring |
| Single-agent | 15 | 14 | 9 | 5 | 4 | 16 | 63 | Defer until downstream agreement and monitoring |
| MCDA | 12 | 12 | 5 | 2 | 1 | 11 | 43 | Defer / Redesign pending basin agreement |

### SRD-006

| System | Evidence Grounding /20 | Risk Coverage /15 | Stakeholder and Conflict Representation /15 | Role Fidelity /15 | Deliberation and Revision /15 | Decision Usefulness /20 | Total /100 | Final recommendation |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Multi-agent | 18 | 14 | 11 | 13 | 10 | 19 | 85 | Build; commissioning conditions attached |
| Single-agent | 15 | 13 | 9 | 5 | 4 | 18 | 64 | Build with conditions |
| MCDA | 13 | 13 | 6 | 2 | 1 | 18 | 53 | Build |

### SRD-007

| System | Evidence Grounding /20 | Risk Coverage /15 | Stakeholder and Conflict Representation /15 | Role Fidelity /15 | Deliberation and Revision /15 | Decision Usefulness /20 | Total /100 | Final recommendation |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Multi-agent | 18 | 14 | 14 | 13 | 13 | 18 | 90 | Build with conditions; revert to Defer if livelihood plan not complete in 9 months |
| Single-agent | 15 | 13 | 8 | 5 | 4 | 12 | 57 | Defer until livelihood plan and economic review complete |
| MCDA | 12 | 11 | 5 | 2 | 1 | 8 | 39 | Redesign or Defer; marginally viable |

### SRD-008

| System | Evidence Grounding /20 | Risk Coverage /15 | Stakeholder and Conflict Representation /15 | Role Fidelity /15 | Deliberation and Revision /15 | Decision Usefulness /20 | Total /100 | Final recommendation |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Multi-agent | 18 | 15 | 13 | 13 | 13 | 17 | 89 | Do not build; pursue wind portfolio alternative |
| Single-agent | 15 | 14 | 8 | 5 | 4 | 17 | 63 | Do not build; pursue wind and storage alternatives |
| MCDA | 12 | 12 | 5 | 2 | 1 | 14 | 46 | Do not build |

## Mean Scores Across All Eight Synthetic Cases

| System | Mean total /100 | Evidence Grounding | Risk Coverage | Stakeholder/Conflict | Role Fidelity | Deliberation/Revision | Decision Usefulness |
|---|---:|---:|---:|---:|---:|---:|---:|
| Multi-agent | 89.4 | 18.1 | 14.4 | 13.1 | 13.0 | 12.4 | 17.9 |
| Single-agent | 61.5 | 15.0 | 13.5 | 8.3 | 5.0 | 4.0 | 15.9 |
| MCDA | 44.1 | 12.3 | 11.9 | 4.6 | 2.0 | 1.0 | 12.3 |

**Score ceiling note (SRD-001 to SRD-005 pattern):** Multi-agent scores ranged from 89â€“93 across the first five cases â€” a band too narrow to reflect genuine case-level variation. SRD-006 (multi-agent: 85) shows the band is now wider with the simple case included. SRD-007 single-agent Decision Usefulness (12/20) shows meaningful divergence on a near-tipping-point case. Going forward, apply the v2 rubric scoring anchors (must-detect penalty in Risk Coverage; decision precision tiers in Decision Usefulness; compact run ceilings) to prevent the scores from functioning as a pass/fail checklist rather than a quality gradient.

## Decision Diversity Check

| Decision type | Produced by multi-agent? | Case |
|---|---|---|
| Build (or near-Build with commissioning conditions only) | yes | SRD-006 |
| Build with conditions (time-conditioned, specific) | yes | SRD-007 |
| Build with conditions / phased approval | yes | SRD-002 |
| Redesign toward specific evaluated alternative | yes | SRD-003 |
| Redesign with final approval deferred | yes | SRD-001 |
| Emergency action plus defer final dam approval | yes | SRD-004 |
| Defer pending governance/legal resolution | yes | SRD-005 |
| Do not build | yes | SRD-008 |

## Conservative-Bias Check

The multi-agent system demonstrated a range from Build (SRD-006) to Defer (SRD-005) across seven cases. With the addition of SRD-006, the over-conservatism concern is directly addressed: the system recommends Build when blockers are genuinely resolved.

Key patterns across the suite:
- **SRD-006** (clean case): multi-agent recommends Build; MCDA and single-agent also recommend Build or near-Build. Gaps narrow on simple cases.
- **SRD-007** (tipping-point): the most pronounced multi-agent advantage is on Decision Usefulness â€” the system produces a time-conditioned pathway; single-agent defaults to generic Defer.
- **SRD-003** (updated): with hybrid alternative performance data, the recommendation shifts from generic Defer to specific Redesign toward hybrid â€” showing that richer scenario data produces more actionable outputs.
- **SRD-005** (updated): with domestic legal advocate added, the legal dispute is now internal to the deliberation rather than assumed, making the governance legitimacy argument more earned.

The system now covers the full decision space from Build (SRD-006) to Do not build (SRD-008). The system still never produces a simple unconditional Build without any conditions attached. This may be appropriate â€” the benchmark does not include a case so clean that zero operating conditions are reasonable â€” but reviewers should note that SRD-006's three commissioning conditions are minor administrative items, not substantive blockers.

## Where Multi-Agent Adds the Most Value

| Case | Strongest added value |
|---|---|
| SRD-001 | Preserving high-conflict stakeholder and safeguard issues. |
| SRD-002 | Showing conditional support rather than blanket conservatism. |
| SRD-003 | Separating renewable-energy benefits from local ecological/social costs. |
| SRD-004 | Separating urgent emergency measures from irreversible infrastructure approval. |
| SRD-005 | Making governance legitimacy and downstream trust central. |

## What Single-Agent Consistently Compresses

- Stakeholder voices become a general analytical narrative.
- Role boundaries disappear.
- Minority reports are usually not preserved.
- Objection-response structure is absent.
- It remains useful for compact summaries, but weaker as a simulated meeting artifact.

## What MCDA Consistently Compresses

- Stakeholder conflict becomes scores.
- Legal or safeguard blockers can be hidden inside weighted averages.
- It cannot naturally express procedural sequencing such as "emergency action now, final approval later."
- It is transparent and useful as an aggregation baseline, but weak as a deliberative artifact.

## Preliminary Cross-Case Claims

These are preliminary estimates from compressed runs and v1 scoring. Full three-layer scores require full-protocol transcript runs. Two separate claims are supported at different levels of confidence:

**Claim 1 â€” Outcome Quality**: Multi-agent produces more specific and calibrated recommendations than single-agent on genuinely ambiguous cases. Evidence: SRD-007 Decision Usefulness gap (multi-agent 18/20, single-agent 12/20). On clear cases (SRD-006, SRD-008), the gap narrows and both systems recommend the correct direction. MCDA Decision Usefulness is consistently lower on complex cases because aggregation cannot express conditioned pathways.

**Claim 2 â€” Process Quality**: Multi-agent preserves role-specific reasoning, stakeholder conflict, evidence audit, and minority concerns that single-agent and MCDA compress. This is a structural property of the method, not a performance advantage over systems that were not designed to deliberate. Report this claim separately and do not compare baselines on Process Quality dimensions.

Neither claim supports:

> The multi-agent method makes objectively correct reservoir construction decisions.

## Manuscript Use Notes

These scores are not yet enough for a mature manuscript unless the limitations are clear:

1. Synthetic cases were authored by the research team.
2. Scores were researcher/assistant-coded.
3. MCDA weights are provisional.
4. No real-world case or expert blind review has been completed.

Manuscript-ready next steps:

1. Create a scoring appendix with the rubric.
2. Ask independent human evaluators to score outputs blindly.
3. Add 1-2 real cases with public documentation.
4. Calibrate MCDA criteria and weights from literature or expert elicitation.




