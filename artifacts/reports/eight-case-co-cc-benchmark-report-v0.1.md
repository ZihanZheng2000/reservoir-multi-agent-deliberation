# Multi-Agent Deliberation for Reservoir Construction Decision Support: Eight Synthetic Case Benchmark Report v0.1

## Material Status

- Project: reservoir multi-agent deliberation
- Report type: manuscript-style internal benchmark report
- Case set: SRD-001 to SRD-008
- Model runs compared: Codex (`co`) and Claude Code (`cc`)
- Run design: SRD-001 full run; SRD-002 to SRD-008 compact runs
- Date: 2026-06-26
- Evidence basis: local synthetic case artifacts and run manifests only
- Citation status: no external literature citations inserted in this version; literature review should be added before manuscript submission

## Abstract

Reservoir construction decisions require balancing hydrological reliability, flood control, engineering safety, economic viability, ecological risk, resettlement impacts, legal readiness, financing conditions, and stakeholder legitimacy. Conventional decision-support tools, including weighted multi-criteria decision analysis (MCDA), often compress these heterogeneous concerns into aggregate scores. Single-agent language-model analysis can produce more flexible written recommendations, but it tends to collapse expert disagreement and stakeholder conflict into a single narrative. This report evaluates a role-limited multi-agent deliberation system designed to simulate a reservoir approval meeting, in which different agents represent disciplinary experts and stakeholder positions.

We tested the system on eight synthetic reservoir decision cases. The cases were deliberately designed to cover a broad decision space: high-conflict multipurpose dam approval, low-conflict off-channel expansion, hydropower-dominant development, emergency flood-control infrastructure, transboundary downstream conflict, clean approval, near-tipping-point conditional approval, and a clear do-not-build case. Each case was evaluated using a three-layer rubric: Layer 1 Outcome Quality, Layer 2 Evidence Quality, and Layer 3 Process Quality. Layer 1 and Layer 2 apply to multi-agent, single-agent, and MCDA systems; Layer 3 applies only to multi-agent deliberation and is not used as a direct baseline comparison.

Both Codex and Claude Code runs produced broadly consistent decision directions across all eight cases. The multi-agent system generated recommendations ranging from Build to Do not build, indicating that it did not simply default to conservative deferral. Its strongest advantage appeared in ambiguous and procedurally complex cases, especially SRD-007, where it identified the livelihood restoration plan as the swing condition and produced a time-conditioned approval pathway. MCDA performed reasonably on clear cases but struggled to represent sequencing, veto points, and conditional pathways. Single-agent analysis usually captured the main direction but compressed stakeholder disagreement, minority reports, and role-specific objections. These findings support a restrained methodological claim: the multi-agent system should not be presented as producing objectively correct reservoir decisions, but as generating more inspectable, role-bounded, and procedurally useful decision-support reasoning.

Keywords: multi-agent deliberation; reservoir decision support; synthetic benchmark; stakeholder conflict; MCDA; environmental governance; infrastructure approval

## 1. Introduction

Large reservoir projects are rarely evaluated on a single technical dimension. A proposed dam may improve urban water supply and reduce moderate floods while simultaneously creating risks for downstream flows, endemic fish, cultural sites, public debt, resettlement, and financing safeguards. The difficulty is not merely that the decision contains many variables. The deeper difficulty is that those variables belong to different epistemic and political domains. A hydrologist may focus on firm yield and drought reliability; an ecologist may object that irreversible species loss cannot be offset by generic fish passage; a financier may treat incomplete safeguards as a disbursement blocker; affected residents may refuse to treat sacred sites as items in a compensation table.

A single objective function can aggregate such issues, but aggregation may hide the reason why a project is blocked. A single-agent analysis can write a more nuanced recommendation, but it often turns disagreement into a smooth summary. The research idea tested here is that a multi-agent system may better approximate the structure of an approval meeting. Instead of asking one model to be all experts simultaneously, the system assigns bounded roles to expert and stakeholder agents, forces them to cite scenario evidence, records disagreements, and asks a decision authority to produce a final recommendation from the meeting record.

The purpose of this report is to summarize the first complete synthetic benchmark. The benchmark is not intended to prove that the system makes objectively correct water-infrastructure decisions. The cases are synthetic and researcher-designed. Instead, the benchmark evaluates whether the system produces recommendations that are decision-useful, evidence-grounded, procedurally calibrated, and inspectable as deliberation artifacts.

The report addresses four questions:

1. Can the multi-agent system generate a range of decision labels rather than defaulting to rejection or deferral?
2. Does the multi-agent system recover the designed risk structure in each case?
3. Where does multi-agent deliberation add value relative to single-agent and MCDA baselines?
4. Are the results stable across two independent model-run environments, Codex and Claude Code?

## 2. Benchmark Design

### 2.1 Case Suite

The benchmark contains eight synthetic cases. Each case represents a distinct reservoir approval problem. The suite was intentionally constructed to include clear approval, clear rejection, and ambiguous cases.

| Case | Case type | Designed decision challenge | Expected decision region |
|---|---|---|---|
| SRD-001 | High-conflict new multipurpose dam | Benefits are real, but ecological, social, economic, safety, and safeguard gaps are substantial. | Redesign and defer final approval |
| SRD-002 | Low-conflict off-channel expansion | Test whether the system can approve when risks are manageable. | Build with conditions |
| SRD-003 | Hydropower-dominant project | Test whether renewable-energy framing hides local ecological and livelihood burdens. | Redesign toward hybrid alternative |
| SRD-004 | Flood-control emergency | Test whether urgency leads to premature irreversible approval. | Emergency action now; defer dam approval |
| SRD-005 | Transboundary/downstream conflict | Test whether governance legitimacy and downstream enforceability become central. | Defer pending basin agreement |
| SRD-006 | Clean approval case | Test over-conservatism directly. | Build, with commissioning conditions only |
| SRD-007 | Near-tipping-point case | Test whether the system identifies the swing condition rather than issuing generic Defer. | Time-conditioned Build with conditions |
| SRD-008 | Do-not-build case | Test whether the system can reject and explain why Redesign is insufficient. | Do not build; pursue alternative |

SRD-001 was run as a full transcript-style case. SRD-002 to SRD-008 were run as compact cases. A full run contains separate expert assessments, stakeholder assessments, a moderator conflict map, targeted deliberation, evidence audit, decision-authority recommendation, baseline outputs, and evaluation. A compact run preserves the same logical components in compressed form but does not provide a full round-by-round transcript.

### 2.2 Systems Compared

The benchmark compares three decision-support formats inside each run:

| System | Description | Intended strength | Expected limitation |
|---|---|---|---|
| Multi-agent deliberation | Role-limited experts and stakeholders deliberate before a final decision authority recommendation. | Preserves role-specific reasoning, conflict, objections, minority positions, and sequencing. | More expensive and less compact; process quality depends on prompt design. |
| Single-agent baseline | One integrated decision analyst reviews the same scenario. | Efficient synthesis and generally coherent recommendation. | Compresses stakeholder conflict and role boundaries. |
| MCDA baseline | Weighted scoring across decision criteria. | Transparent aggregation and easy comparison. | Cannot naturally express veto points, sequencing, or deliberative conflict. |

The multi-agent system is not compared against baselines on Process Quality because MCDA and single-agent baselines are not designed to simulate deliberation. This is an important fairness constraint. A process score should describe the multi-agent artifact, not mechanically inflate its advantage over systems that lack process structure by design.

### 2.3 Evaluation Rubric

The current rubric has three layers.

**Layer 1: Outcome Quality /30** evaluates whether the recommendation is useful for a decision-maker. It includes decision-range fit, recommendation specificity, and recommendation calibration.

**Layer 2: Evidence Quality /40** evaluates whether the output is grounded in scenario facts, recovers the designed risks, and treats uncertainty appropriately. Risk coverage is checked against evaluator-only gold checklists.

**Layer 3: Process Quality /55** evaluates the quality of multi-agent deliberation: stakeholder/conflict representation, role fidelity, objection-response quality, evidence audit/revision, and minority preservation. This layer is reported only for multi-agent outputs.

The key reporting rule is that Layer 1 and Layer 2 are valid for cross-system comparison, while Layer 3 is a descriptive process-quality measure for multi-agent deliberation only.

## 3. Run Structure and Artifact Coverage

The current workspace contains both Codex and Claude Code runs for all eight cases.

| Case | Codex artifact | Claude Code artifact | Run type |
|---|---|---|---|
| SRD-001 | `artifacts/demo-001-co-full/` | `artifacts/demo-001-cc-full/` | Full transcript-style |
| SRD-002 | `artifacts/demo-002/` | `artifacts/demo-002-cc/` | Compact |
| SRD-003 | `artifacts/demo-003/` | `artifacts/demo-003-cc/` | Compact |
| SRD-004 | `artifacts/demo-004/` | `artifacts/demo-004-cc/` | Compact |
| SRD-005 | `artifacts/demo-005/` | `artifacts/demo-005-cc/` | Compact |
| SRD-006 | `artifacts/demo-006/` | `artifacts/demo-006-cc/` | Compact |
| SRD-007 | `artifacts/demo-007/` | `artifacts/demo-007-cc/` | Compact |
| SRD-008 | `artifacts/demo-008/` | `artifacts/demo-008-cc/` | Compact |

SRD-001 full runs are used primarily to demonstrate the deliberation mechanism. SRD-002 to SRD-008 compact runs are used primarily for cross-case pattern testing.

## 4. Results

### 4.1 Decision Direction Across Cases

The most important result is that the multi-agent system generated the full range of plausible decision outcomes. It did not simply recommend Defer or Do not build. Across the eight cases, the multi-agent recommendations covered Build, Build with conditions, Redesign, Defer, emergency sequencing, and Do not build.

| Case | Codex multi-agent recommendation | Claude Code multi-agent recommendation | Agreement |
|---|---|---|---|
| SRD-001 | Redesign; defer final build approval | Redesign + Defer | High |
| SRD-002 | Build with conditions through phased approval | Build with conditions through phased approval | High |
| SRD-003 | Redesign toward the hybrid alternative | Redesign toward hybrid alternative | High |
| SRD-004 | Phased emergency package now; defer final reservoir approval | Phased emergency package now; defer final reservoir approval | High |
| SRD-005 | Defer pending basin agreement, joint monitoring, and drought rules | Defer pending binding basin agreement, joint monitoring, and drought-contingent rules | High |
| SRD-006 | Build; commissioning conditions attached | Build; commissioning conditions attached | High |
| SRD-007 | Build with conditions; approval lapses to Defer if livelihood plan is incomplete | Build with conditions; revert to Defer if livelihood plan is incomplete in 9 months | High |
| SRD-008 | Do not build; pursue wind portfolio alternative | Do not build; pursue wind portfolio alternative | High |

This agreement is substantively important. It suggests that the decision logic is not an artifact of one model environment. The wording differs, but the decision structure is stable.

### 4.2 Codex Score Summary

| Case | Multi-agent L1 /30 | Multi-agent L2 /40 | Multi-agent L3 /55 | Single-agent L1 /30 | Single-agent L2 /40 | MCDA L1 /30 | MCDA L2 /40 |
|---|---:|---:|---:|---:|---:|---:|---:|
| SRD-001 | 28 | 38 | 51 | 24 | 30 | 17 | 23 |
| SRD-002 | 27 | 33 | 39 | 26 | 30 | 23 | 27 |
| SRD-003 | 27 | 34 | 42 | 23 | 29 | 19 | 24 |
| SRD-004 | 28 | 34 | 43 | 26 | 30 | 20 | 25 |
| SRD-005 | 28 | 35 | 44 | 24 | 30 | 20 | 25 |
| SRD-006 | 29 | 34 | 35 | 28 | 31 | 28 | 30 |
| SRD-007 | 29 | 34 | 43 | 20 | 28 | 16 | 23 |
| SRD-008 | 29 | 35 | 40 | 27 | 31 | 25 | 28 |
| **Mean** | **28.1** | **34.6** | **42.1** | **24.8** | **29.9** | **21.0** | **25.6** |

The Codex results show three patterns. First, multi-agent L1 Outcome Quality is consistently high, with the strongest cases being SRD-006, SRD-007, and SRD-008. Second, Layer 2 Evidence Quality is stable across cases, suggesting that the system generally recovered the designed risk structure. Third, Layer 3 Process Quality varies meaningfully: it is lower in SRD-006 because the clean approval case has little conflict to preserve, and higher in high-conflict or governance-heavy cases.

### 4.3 Claude Code Score Summary

| Case | Multi-agent L1 /30 | Multi-agent L2 /40 | Multi-agent L3 /55 | Single-agent L1 /30 | Single-agent L2 /40 | MCDA L1 /30 | MCDA L2 /40 |
|---|---:|---:|---:|---:|---:|---:|---:|
| SRD-001 | 26 | 36 | 49 | 16 | 22 | 13 | 18 |
| SRD-002 | 26 | 34 | 44 | 22 | 26 | 15 | 20 |
| SRD-003 | 26 | 34 | 43 | 19 | 26 | 13 | 18 |
| SRD-004 | 26 | 34 | 43 | 21 | 27 | 13 | 19 |
| SRD-005 | 26 | 34 | 45 | 20 | 27 | 14 | 20 |
| SRD-006 | 28 | 36 | 43 | 21 | 29 | 18 | 25 |
| SRD-007 | 27 | 34 | 45 | 16 | 26 | 11 | 18 |
| SRD-008 | 27 | 35 | 46 | 22 | 29 | 15 | 20 |
| **Mean** | **26.5** | **34.6** | **44.8** | **19.6** | **26.5** | **14.0** | **19.8** |

Claude Code shows a slightly different profile. Its multi-agent Evidence Quality mean is identical to Codex's mean, while Process Quality is higher. This matches the qualitative observation that Claude Code compact artifacts tend to preserve more audit metrics, claim corrections, and deliberative process details. Codex scores higher on Outcome Quality in this set, partly because its recommendations are often more directly phrased as action pathways.

### 4.4 Cross-Model Interpretation

The co/cc comparison is not a competition in the simple sense. Both runs support the same methodological story. Codex and Claude Code agree on the final decision direction for every case. This is stronger evidence than a single run because it reduces the risk that the benchmark conclusion depends on one model's idiosyncratic wording.

The main differences are stylistic and process-oriented:

| Dimension | Codex tendency | Claude Code tendency | Interpretation |
|---|---|---|---|
| Final recommendation | More direct and decision-action oriented | Slightly more conservative wording in some cases | Both reach same decision region |
| Evidence scoring | Stable and concise | Stable and often more audit-explicit | Similar evidence recovery |
| Process artifact | Cleaner summary | Richer audit/process trace | Claude Code stronger for process inspection |
| Baseline scoring | More generous to baselines | More severe toward baselines | Baseline comparison should be reported carefully |
| Use in manuscript | Good for compact tables and reader-facing summary | Good for appendix-style process evidence | Both should be retained |

The most defensible manuscript strategy is therefore to use one harmonized result table for decision direction and risk recovery, while treating co/cc differences as a robustness check. The paper should not overclaim that one model is objectively superior. The useful claim is that the multi-agent method produces stable decision structures across two independent model-run environments.

## 5. Case-Level Interpretation

### 5.1 SRD-001: High-Conflict New Multipurpose Dam

SRD-001 is the flagship full-run case. The project has credible public benefits: urban water yield, irrigation reliability, flood reduction, and hydropower. However, both Codex and Claude Code identify multiple blockers: incomplete climate-adjusted hydrology, uncertain fish passage, endemic fish spawning habitat, large displacement, sacred sites, incomplete livelihood restoration, incomplete EIA review, incomplete safeguard plans, conditional financing, marginal downside economics, and dam-safety gaps.

The final recommendation is Redesign + Defer final approval. This case demonstrates the main value of a full run. The multi-agent process does not merely list risks. It shows how different agents convert facts into different forms of concern: a financing condition, a legal blocker, a safety boundary, an ecological uncertainty, a social legitimacy problem, or an economic downside scenario.

SRD-001 is therefore best used in the paper as the process demonstration case. The reader can inspect the chain from role-specific assessment to targeted deliberation, evidence audit, and decision-authority recommendation.

### 5.2 SRD-002: Low-Conflict Off-Channel Expansion

SRD-002 tests over-conservatism. The project is lower conflict because it expands off-channel or existing storage, avoids blocking the main river, has limited displacement, and has a stronger governance basis. Both systems recommend Build with conditions.

This case is important because it shows the multi-agent system does not automatically inflate every uncertainty into a construction blocker. The remaining issues are treated as conditions around drought refill performance, tariff protection, wetland buffer enforceability, seismic retrofit, and grazing access. In manuscript terms, SRD-002 helps answer the reviewer concern that a multi-agent setup might simply produce more objections and therefore always recommend delay.

### 5.3 SRD-003: Hydropower-Dominant Project

SRD-003 tests whether renewable-energy value causes the system to underweight local impacts. Both Codex and Claude Code recommend redesign toward a hybrid alternative. The important feature is not merely that the current dam is rejected as proposed, but that the system identifies a specific alternative path.

The case shows a strong multi-agent contribution: the energy benefit is preserved, but it is separated from the local ecological and livelihood burden. The hybrid alternative becomes decision-actionable because the agents connect grid need, river-specific ecological harm, cost comparison, and local benefit-burden mismatch. MCDA can show that the current project scores poorly, but it cannot as naturally explain why the hybrid alternative is the correct redesign direction.

### 5.4 SRD-004: Flood-Control Emergency

SRD-004 tests whether emergency conditions lead the system to approve irreversible infrastructure prematurely. Both runs produce a phased recommendation: implement emergency measures now, but defer final reservoir approval.

This case is methodologically useful because it shows sequencing. A simple Build/Defer label is inadequate. The correct policy logic is to act immediately on non-controversial emergency measures while withholding irreversible dam approval until climate-adjusted flood estimates, geotechnical investigation, land acquisition legitimacy, and downstream operation safety are resolved. The multi-agent system is useful because it turns an apparent binary decision into a staged governance pathway.

### 5.5 SRD-005: Transboundary and Downstream Conflict

SRD-005 is governance-heavy. The upstream benefits are real, but downstream dry-season flow reduction, wetland impacts, compact ambiguity, lack of trusted monitoring, and lender requirements make unilateral approval illegitimate. Both systems recommend deferral pending basin agreement, joint monitoring, and binding drought operating rules.

The strongest deliberative contribution is preservation of legal disagreement. The upstream domestic legal position and downstream/no-significant-harm position are not collapsed into a single legal conclusion. The system treats the legal conflict itself as a decision-relevant unresolved condition. This is exactly the kind of issue that a weighted score can obscure.

### 5.6 SRD-006: Clean Approval Case

SRD-006 is the clean approval case. Both systems recommend Build, with only commissioning conditions attached. This case is central to the conservative-bias check. The multi-agent system correctly distinguishes construction blockers from commissioning requirements. Sediment management, low-flow diversion cutoff, and habitat monitoring are not treated as reasons to defer construction.

The lower Layer 3 process score in Codex is not a failure. It reflects that there is less conflict to represent. A good deliberative system should not manufacture controversy. This case therefore helps calibrate the process rubric: low-conflict cases should naturally have lower stakeholder-conflict scores.

### 5.7 SRD-007: Near-Tipping-Point Case

SRD-007 is probably the strongest evidence for the multi-agent method. The project has real irrigation benefits and most safeguards are near completion, but the livelihood restoration plan remains incomplete. A generic Defer is defensible but not maximally useful. The multi-agent system identifies the livelihood plan as the swing condition and recommends a time-conditioned approval pathway: Build with conditions, but approval lapses or reverts to Defer if the livelihood plan is not completed within nine months.

This is the clearest example of multi-agent value over both baselines. Single-agent analysis tends to recommend Defer until the livelihood plan and economic review are complete. MCDA reads the marginal economics and incomplete safeguard as low scores and cannot express a time-conditioned pathway. The multi-agent system distinguishes a nearly resolved blocker from systemic non-viability.

### 5.8 SRD-008: Do-Not-Build Case

SRD-008 tests whether the system can reject a project and explain why redesign is insufficient. Both systems recommend Do not build and pursue the wind portfolio alternative. The important feature is that the multi-agent output does not merely say the current design is bad. It explains why a smaller dam or redesign does not solve the core objections: negative economics, irreversible endemic species loss, indigenous consent withheld, and a superior alternative.

This case shows that MCDA can work reasonably well when all major dimensions point in the same direction. However, MCDA still has less explanatory power. It can say the project scores poorly; it cannot as naturally articulate why Redesign is not the right label.

## 6. Baseline Comparison

### 6.1 Single-Agent Baseline

Single-agent analysis is not weak in the trivial sense. It usually identifies major risks and often reaches an adjacent or correct decision region. Its limitation is structural. Because it speaks as one integrated analyst, it tends to compress conflict into a coherent narrative. It usually does not preserve who disagrees, what role-specific objection they raised, whether the objection was answered, or which minority positions remain unresolved.

This matters because reservoir approval is not only about reaching a final recommendation. The acceptability of the recommendation depends on whether affected groups, financiers, regulators, and technical experts can see how their concerns were handled. Multi-agent deliberation provides a more inspectable record of that process.

### 6.2 MCDA Baseline

MCDA is transparent and useful when dimensions broadly align. It performs relatively better in SRD-006 and SRD-008 because those cases are clear: the project is either broadly approvable or broadly non-viable. However, MCDA struggles in cases where decision quality depends on sequencing or veto logic.

Three recurring MCDA limitations appear:

1. **Blocker compression:** a legal or safeguard veto can be hidden inside an average score.
2. **Sequencing failure:** MCDA cannot naturally express emergency action now but final approval later.
3. **Conditional-pathway failure:** MCDA cannot naturally produce a time-conditioned approval such as SRD-007.

This does not mean MCDA is useless. Rather, MCDA is a useful baseline precisely because it shows what is lost when deliberation is reduced to weighted aggregation.

## 7. Main Claims Supported by the Benchmark

The current benchmark supports three restrained claims.

**Claim 1: The multi-agent system can represent decision diversity.** The system recommends Build in SRD-006, Build with conditions in SRD-002 and SRD-007, Redesign in SRD-001 and SRD-003, Defer in SRD-005, staged emergency action in SRD-004, and Do not build in SRD-008. This directly addresses the concern that multi-agent deliberation may simply accumulate objections and become systematically conservative.

**Claim 2: Multi-agent advantage is strongest in procedurally complex cases.** The clearest examples are SRD-004 and SRD-007. These cases cannot be handled well by a single label. They require staging, timing, and condition precedence. The multi-agent system generates decision pathways, not just recommendations.

**Claim 3: The main contribution is process inspectability, not objective correctness.** The system should not be described as discovering the true decision. Instead, it produces a structured deliberation artifact: role-bounded reasoning, stakeholder conflict, objection-response structure, evidence audit, and preserved minority positions.

## 8. Limitations

The benchmark has several important limitations.

First, all eight cases are synthetic and researcher-designed. This gives experimental control but creates a risk that the evaluation reflects the designer's expectations. The hidden checklists reduce direct leakage to agents, but they do not eliminate researcher involvement in case construction and scoring.

Second, the scoring is still researcher-coded. Independent blinded scoring by water-resource experts, environmental assessment specialists, or infrastructure governance scholars would be needed before making strong empirical claims.

Third, MCDA weights and thresholds remain provisional. A mature manuscript should either justify these weights from literature, elicit them from experts, or report sensitivity analysis.

Fourth, compact runs are not equivalent to full transcript runs. SRD-002 to SRD-008 are useful for cross-case pattern testing, but they provide weaker evidence of deliberative process than SRD-001. At least one additional full run, ideally SRD-007 or SRD-008, would strengthen the paper.

Fifth, the benchmark does not yet include real-world reservoir cases. Real cases would introduce messy documentation, missing data, political ambiguity, and historical outcomes. Synthetic results are valuable for method development, but real-case validation is needed for external validity.

## 9. Recommended Next Steps

The next stage should focus on turning the benchmark into a manuscript-ready study.

1. **Create a clean manuscript table package.** Consolidate co/cc results into one table for decision direction, one table for Layer 1 and Layer 2 scores, and one table for Layer 3 process quality.
2. **Run one more full case.** SRD-007 is the best candidate because it demonstrates the strongest multi-agent advantage: identifying a swing condition and producing a time-conditioned pathway.
3. **Add blinded human evaluation.** Ask independent evaluators to rate recommendation acceptability, risk coverage, and reasoning transparency without knowing which system produced each output.
4. **Calibrate MCDA.** Either justify weights from decision-analysis literature or run sensitivity analysis showing whether conclusions depend on weight choices.
5. **Add one or two real cases.** Use public EIA, financing, resettlement, or basin-management documents to test whether the framework works outside synthetic examples.
6. **Write the literature review.** The literature review should cover MCDA in water infrastructure, participatory environmental decision-making, LLM multi-agent systems, and deliberative decision support.

## 10. Conclusion

The eight-case benchmark provides a coherent first demonstration of role-limited multi-agent deliberation for reservoir construction decision support. Across two model-run environments, Codex and Claude Code, the system produced stable decision directions across the full range of reservoir approval outcomes. It approved clean cases, rejected clearly non-viable cases, and produced staged or conditional pathways for ambiguous cases.

The most important contribution is not that the multi-agent system is objectively correct. The stronger and more defensible claim is that it creates a better decision-support artifact for contested infrastructure approval. It preserves the structure of disagreement. It shows how technical, ecological, social, financial, legal, and stakeholder concerns interact. It identifies when a problem is a construction blocker, a commissioning condition, a redesign requirement, or a reason for rejection.

For a paper, the current results are sufficient to support a method-and-benchmark manuscript draft, provided the limitations are clearly stated. The work will become substantially stronger after one additional full transcript case, independent human scoring, MCDA calibration, and one or two real-world validation cases.

## Appendix A: Key Artifact Paths

| Artifact | Path |
|---|---|
| Codex SRD-001 full run | `artifacts/demo-001-co-full/` |
| Claude Code SRD-001 full run | `artifacts/demo-001-cc-full/` |
| Codex compact runs | `artifacts/demo-002/` to `artifacts/demo-008/` |
| Claude Code compact runs | `artifacts/demo-002-cc/` to `artifacts/demo-008-cc/` |
| Codex compact evaluations | `artifacts/demo-00X/outputs/evaluation-three-layer-compact.md` |
| Claude Code compact evaluations | `artifacts/demo-00X-cc/outputs/evaluation-three-layer.md` |
| Existing cross-case summary | `artifacts/cross-case-score-summary-v0.1.md` |

## Appendix B: Reporting Rule for Scores

Layer 1 and Layer 2 can be compared across multi-agent, single-agent, and MCDA systems. Layer 3 should be reported only for multi-agent deliberation. A combined total across all three layers should not be reported because it would unfairly reward multi-agent systems for having a deliberative process that the baselines were not designed to provide.
