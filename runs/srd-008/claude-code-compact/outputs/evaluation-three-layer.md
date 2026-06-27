# Three-Layer Evaluation — SRD-008-cc

Evaluation against rubric v3 (three-layer structure).

Run type: **Claude Code compact run.**

Design note: SRD-008 tests whether the system produces the correct Do not build label AND articulates why Redesign is not the right path. A system that recommends Do not build but does not explain why a smaller dam still fails on fish passage, endemic species, and indigenous consent should score lower on L1.2 and L1.3 than one that explicitly addresses the redesign alternative and rules it out.

---

## Layer 1: Outcome Quality /30

### L1.1 Decision-Range Fit /5

| System | Score | Rationale |
|---|---:|---|
| Multi-agent | 5 | Recommends "Do not build; pursue wind portfolio alternative" — squarely within the evaluator-defined acceptable range. |
| Single-agent | 5 | Recommends "Do not build; pursue wind and storage alternatives" — within the acceptable range. |
| MCDA | 4 | Recommends "Do not build" at 1.64/5.0 — within range; does not express wind portfolio as the specific next step. |

### L1.2 Recommendation Specificity /15

| System | Score | Rationale |
|---|---:|---|
| Multi-agent | 13 | Articulates three independent grounds for rejection; explicitly rules out Redesign for each ground; recommends three specific next steps including wind portfolio grid adequacy study. |
| Single-agent | 10 | Recommends Do not build and mentions the wind portfolio; does not explicitly rule out Redesign by addressing each core objection. |
| MCDA | 5 | Correct direction; no explanation of why Redesign fails; no pathway to next steps. |

### L1.3 Recommendation Calibration /10

| System | Score | Rationale |
|---|---:|---|
| Multi-agent | 9 | Correctly avoids Redesign (which is the most common failure mode on this case); correctly does not Defer (the core problems are not resolvable by study time); correctly does not Build or Build with conditions; explicitly preserves the Energy Ministry's policy need while rejecting the project. |
| Single-agent | 7 | Correctly avoids Build; does not explicitly address why Redesign is not the path; calibration is directionally correct but incomplete. |
| MCDA | 6 | Low score drives correct Do not build recommendation; no indication of why conditions cannot fix the project; no Redesign discussion. |

### Layer 1 Subtotals

| System | L1.1 /5 | L1.2 /15 | L1.3 /10 | L1 Total /30 |
|---|---:|---:|---:|---:|
| Multi-agent | 5 | 13 | 9 | 27 |
| Single-agent | 5 | 10 | 7 | 22 |
| MCDA | 4 | 5 | 6 | 15 |

---

## Layer 2: Evidence Quality /40

### L2.1 Evidence Grounding /10

| System | Score | Rationale |
|---|---:|---|
| Multi-agent | 9 | All three grounds for rejection are cited with field IDs; audit corrections prevent revenue sharing from appearing as a consent path; all major claims cite scenario evidence. |
| Single-agent | 8 | Major claims grounded; does not cite the tourism livelihood exclusion from BCR (F7.4, F4.4). |
| MCDA | 6 | Criterion scores link to scenario; aggregation compresses three distinct grounds into one low score. |

### L2.2 Risk Coverage /20

Gold checklist: 5M, 5S.

Multi-agent coverage:
- R1 (BCR 0.94 base case fails; 0.71 downside) ✓M
- R2 (two endemic fish species; extinction certain; fish passage physically impossible at any height) ✓M
- R3 (indigenous FPIC formally withheld; no FPIC process; revenue offer formally rejected) ✓M
- R4 (wind portfolio BCR 1.68, 42% lower cost, no river impact) ✓M
- R5 (Redesign does not resolve any of the three core objections — explicitly ruled out) ✓M
- R6 (sedimentation 1.8%/yr reduces generation 25% over 30 years; true BCR worse than headline) ✓S
- R7 (no PPA signed; revenue based on forecast market prices) ✓S
- R8 (Ramsar wetland in inundation zone; reportable loss) ✓S
- R9 (EIA alternatives analysis excluded wind/solar; regulator criticism) ✓S
- R10 (1,800 tourism/recreation livelihoods excluded from economic impact study) ✓S

M_detected: 5/5; S_detected: 5/5; compact-run ceiling applied.

| System | Score | Rationale |
|---|---:|---|
| Multi-agent | 18 | All 5M and 5S detected; compact ceiling (-2) applied. |
| Single-agent | 14 | 5/5M detected; 3/5S (misses Ramsar Convention obligation, sedimentation economic impact explicitly, and tourism exclusion from BCR). |
| MCDA | 9 | 3/5M well-characterized through scores; S items compressed. |

### L2.3 Uncertainty Calibration /10

| System | Score | Rationale |
|---|---:|---|
| Multi-agent | 8 | The three grounds for rejection are labeled as confirmed facts, not uncertain estimates; wind portfolio grid adequacy is correctly labeled as requiring further study; no uncertainty inflation on the core rejection grounds. |
| Single-agent | 7 | Uncertainty acknowledged for wind portfolio adequacy; rejection grounds not explicitly labeled as confirmed. |
| MCDA | 5 | Uncertainty not propagated; certainty of rejection is implicit in very low score. |

### Layer 2 Subtotals

| System | L2.1 /10 | L2.2 /20 | L2.3 /10 | L2 Total /40 |
|---|---:|---:|---:|---:|
| Multi-agent | 9 | 18 | 8 | 35 |
| Single-agent | 8 | 14 | 7 | 29 |
| MCDA | 6 | 9 | 5 | 20 |

---

## Layer 3: Process Quality /55

Multi-agent only. Descriptive; do not compare against baselines.

### L3.1 Stakeholder and Conflict Representation /15

Score: **13 / 15**

All seven stakeholder positions represented including the indigenous community's explicit territorial consent position and the tourism association's exclusion-from-BCR concern. Five conflicts are mapped. The moderator's direct question to the Developer about revenue sharing and consent is preserved. The indigenous community's position is presented verbatim from the scenario (F7.3).

### L3.2 Role Fidelity /15

Score: **13 / 15**

Ecologist correctly limits to canyon-specific ecology; does not generalize beyond this gorge segment. Economist correctly limits to BCR analysis without deciding consent. Legal agent correctly limits to permit and FPIC status without deciding ecological acceptability. The audit corrections A1 and A2 protect role fidelity by preventing the Developer and Energy Ministry from overstating their positions.

### L3.3 Objection-Response Quality /10

Score: **8 / 10**

Five-item conflict map produces explicit Redesign-ruling-out for each of the three core objections. The moderator's intervention on revenue sharing and consent is the most important process element: it prevents a common failure mode (treating revenue sharing as a path to consent) before it enters the deliberation record. Full transcripts not preserved.

### L3.4 Evidence Audit and Revision /10

Score: **8 / 10**

58 claims audited; 4 corrections including two major corrections (A1 on revenue sharing, A2 on Energy Ministry authorization). The A1 correction is the most important in the benchmark suite for this type of case: it prevents an unsupported claim from creating a consent path that does not exist in the evidence.

### L3.5 Minority Preservation /5

Score: **4 / 5**

Two minority positions preserved (Developer transition support request, Energy Ministry policy priority). Both are noted; the Energy Ministry position is explicitly incorporated into the recommendation through the wind portfolio pathway.

### Layer 3 Total

| Dimension | Score | Max |
|---|---:|---:|
| Stakeholder/conflict representation | 13 | 15 |
| Role fidelity | 13 | 15 |
| Objection-response quality | 8 | 10 |
| Evidence audit and revision | 8 | 10 |
| Minority preservation | 4 | 5 |
| **Layer 3 total** | **46** | **55** |

---

## Summary Scorecard

| System | L1 Outcome /30 | L2 Evidence /40 | L3 Process /55 |
|---|---:|---:|---:|
| Multi-agent | 27 | 35 | 46 |
| Single-agent | 22 | 29 | n/a |
| MCDA | 15 | 20 | n/a |

---

## Interpretation

SRD-008's distinctive contribution is the explicit Redesign-ruling-out. The gold checklist defines R5 (Redesign does not resolve any of the three core objections) as a must-detect item precisely because the most common failure mode on a clear Do not build case is a reflexive recommendation to redesign without checking whether the fundamental constraints apply to all configurations. The multi-agent system correctly identifies this trap through the Ecologist + Legal + Moderator exchange, producing explicit justification for each objection that Redesign does not resolve.

The L3 scores (46/55) are among the highest in the benchmark suite because the deliberative work is substantive: the moderator's revenue-sharing challenge, the Redesign ruling-out structure, and the audit correction preventing a consent path based on unsupported evidence are all meaningful process contributions. The audit correction A1 is arguably the single most important audit action in the full demo suite for a Do not build case.
