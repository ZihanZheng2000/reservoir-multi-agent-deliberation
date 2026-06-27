# Role-Limited Multi-Agent Deliberation for Reservoir Construction Decision Support: A Synthetic Benchmark Across Eight Cases

**Working Paper v0.1 — June 2026**

*Evidence basis: synthetic case artifacts and run manifests only. No external literature citations have been inserted in this version; a literature review should be added before formal submission.*

---

## Abstract

Reservoir construction decisions require simultaneous assessment of hydrological reliability, flood control, engineering safety, economic viability, ecological risk, resettlement impacts, legal readiness, climate robustness, and stakeholder legitimacy. Conventional decision-support methods, including weighted multi-criteria decision analysis (MCDA), aggregate these heterogeneous concerns into numerical scores [CITE], potentially obscuring veto conditions, sequencing logic, and the structure of expert disagreement. Single-agent large language model (LLM) analysis can produce more flexible written recommendations, but it typically collapses stakeholder conflict into a unified narrative [CITE].

This paper evaluates a role-limited multi-agent deliberation system designed to approximate the structure of a formal reservoir approval meeting. Expert and stakeholder agents hold bounded roles, cite scenario-specific evidence, and register disagreements; a decision authority then produces a final recommendation from the deliberation record. We test the system on eight purpose-built synthetic reservoir cases spanning the full decision space from unambiguous approval to unambiguous rejection, and evaluate all outputs using a three-layer rubric covering outcome quality, evidence quality, and deliberative process quality. Each case was run independently in two model environments — OpenAI Codex and Anthropic Claude Code — providing a cross-model consistency check.

The multi-agent system generated the full range of plausible decision outcomes across the eight cases, from Build to Do not build, without exhibiting systematic conservative bias. Its strongest advantages over the baselines emerged in procedurally complex cases requiring staged sequencing (SRD-004), governance-conditioned approval (SRD-005), and time-conditioned pathways (SRD-007). MCDA performed adequately on clear cases but could not express veto points, sequencing logic, or conditional approval pathways. Single-agent analysis typically identified the main decision direction but compressed stakeholder disagreement and minority positions. Decision directions were consistent across Codex and Claude Code for all eight cases, suggesting that the core deliberative logic is not an artifact of a single model environment.

The primary contribution of this study is methodological. Role-limited multi-agent deliberation produces a more inspectable and role-bounded decision-support artifact than the alternatives evaluated. The system should not be characterized as generating objectively correct reservoir decisions; it generates structured deliberation records in which the contributions of expert and stakeholder concerns are preserved and auditable. These findings support a restrained but substantive claim for the method's utility in contested infrastructure approval contexts.

**Keywords:** multi-agent deliberation; reservoir decision support; synthetic benchmark; stakeholder conflict; multi-criteria decision analysis; environmental governance; infrastructure approval

---

## 1. Introduction

Large reservoir projects rarely turn on a single technical criterion. A proposed dam may simultaneously improve urban water supply and flood protection while creating downstream flow deficits, irreversible habitat loss, resettlement obligations, public debt exposure, and safeguard compliance requirements. The analytical challenge is not merely dimensional: each concern belongs to a different epistemic domain and is evaluated by different professional communities operating under different evidentiary standards. A hydrologist quantifies firm yield and drought reliability. An ecologist may argue that irreversible species loss cannot be offset by generic mitigation commitments. A development financier treats an incomplete resettlement safeguard plan as a disbursement blocker rather than a risk to be averaged. Affected residents may refuse to treat sacred sites as items in a compensation table.

Standard decision-support methods respond to this complexity in different ways. MCDA tools reduce the multi-dimensional evaluation to a single weighted score, which provides comparability and criterion transparency but at the cost of compressing veto logic, sequencing, and the structure of disagreement [CITE]. A project may receive a moderate aggregate score even when it has one or two conditions that would make it unfinanceable or legally blocked. Single-agent LLM analysis can produce a more nuanced written recommendation, but because one model must simultaneously represent all disciplinary and stakeholder perspectives, it tends to synthesize disagreement into a coherent narrative rather than preserving it as a decision-relevant artifact [CITE].

The research design tested here is that role-limited multi-agent deliberation may better approximate the epistemic structure of an actual approval process. Rather than asking one model to be all experts simultaneously, the system assigns bounded roles to expert agents and stakeholder agents, forces each to cite evidence, registers conflicts and minority positions, and asks a decision authority to produce a final recommendation from the complete deliberation record. This design draws on deliberative governance frameworks that emphasize the procedural and legitimacy value of structured multi-party reasoning in contested decisions [CITE].

The benchmark reported here is a first systematic test of this approach across a suite of eight synthetic reservoir cases. The cases were designed to cover the full range of decision outcomes and challenge types: high-conflict multipurpose dam approval, low-conflict off-channel expansion, hydropower-dominant development with hidden local burdens, emergency flood-control sequencing, transboundary governance conflict, unambiguous clean approval, near-tipping-point conditional approval, and an unambiguous do-not-build case. The evaluation uses a three-layer rubric covering outcome quality, evidence quality, and deliberative process quality, and each case was run in two independent model environments.

The study addresses four questions:

1. Can the multi-agent system generate a full range of decision labels rather than defaulting to conservative deferral or rejection?
2. Does the multi-agent system recover the designed risk structure in each case, as measured against evaluator-only gold checklists?
3. Where does multi-agent deliberation add the most value relative to single-agent and MCDA baselines?
4. Are results stable across two independent model-run environments?

The paper is organized as follows. Section 2 describes the methods, including case suite design, system architecture, evaluation rubric, and run protocol. Section 3 reports quantitative results across cases and model environments. Section 4 provides a case-level analysis of each of the eight cases. Section 5 discusses the findings, including baseline comparisons, the scope of the methodological contribution, limitations, and future directions. Section 6 concludes.

---

## 2. Methods

### 2.1 Case Suite

The benchmark contains eight synthetic cases, each representing a distinct reservoir approval problem. The suite was designed to include unambiguous approval, unambiguous rejection, and multiple forms of ambiguity, ensuring that any systematic bias in the system — toward caution, toward construction, or toward a particular recommendation type — would be detectable across the full suite.

**Table 1. Synthetic Case Suite**

| Case | Type | Designed decision challenge | Expected decision region |
|---|---|---|---|
| SRD-001 | High-conflict new multipurpose dam | Multiple substantial gaps across ecological, social, economic, safety, and safeguard domains. | Redesign and defer final approval |
| SRD-002 | Low-conflict off-channel expansion | Test whether the system can issue a construction approval when risks are manageable and bounded. | Build with conditions |
| SRD-003 | Hydropower-dominant project | Test whether renewable-energy framing obscures local ecological and livelihood burdens. | Redesign toward hybrid alternative |
| SRD-004 | Flood-control emergency | Test whether urgency drives premature irreversible approval of infrastructure. | Emergency action now; defer dam approval |
| SRD-005 | Transboundary and downstream conflict | Test whether governance legitimacy and downstream enforceability become decision-central. | Defer pending binding basin agreement |
| SRD-006 | Clean approval case | Test over-conservatism: the system must approve and avoid manufacturing objections. | Build, with commissioning conditions only |
| SRD-007 | Near-tipping-point case | Test whether the system identifies the specific swing condition rather than issuing a generic Defer. | Time-conditioned Build with conditions |
| SRD-008 | Do-not-build case | Test whether the system can reject a project and articulate why Redesign is also insufficient. | Do not build; pursue alternative |

SRD-001 was treated as a full-protocol demonstration case with separate expert assessments, stakeholder assessments, a moderator conflict map, a targeted deliberation round, an evidence audit, a decision-authority recommendation, and baseline outputs. SRD-002 through SRD-008 were run as compact cases that preserve the same logical components in condensed form without a full round-by-round transcript.

Each case scenario is a self-contained synthetic document providing project description, hydrological, ecological, economic, social, legal, and governance facts, with deliberately designed risk structures that agents were not directly told about. Evaluator-only gold checklists defined the set of must-detect and should-detect risks against which evidence recovery was assessed.

### 2.2 System Architecture

Three decision-support formats were compared within each run.

**Table 2. Systems Compared**

| System | Description | Intended strength | Expected limitation |
|---|---|---|---|
| Multi-agent deliberation | Role-limited expert and stakeholder agents deliberate; a decision authority produces the final recommendation from the meeting record. | Preserves role-specific reasoning, conflict, objections, minority positions, and decision sequencing. | More resource-intensive; process quality depends on prompt design and role-card fidelity. |
| Single-agent baseline | One integrated decision analyst reviews the same scenario and produces a written recommendation. | Efficient synthesis; generally coherent recommendation. | Compresses stakeholder conflict and role-specific objections into a unified narrative. |
| MCDA baseline | Weighted scoring across eleven decision criteria, producing a score on a 1–5 scale per criterion. | Transparent aggregation and easy cross-case comparison. | Cannot naturally represent veto points, sequencing conditions, or deliberative conflict. |

The multi-agent system assigns roles to seven expert agents (Hydrologist, Dam Safety Engineer, Ecologist, Climate Risk Analyst, Economist, Social/Resettlement Specialist, Legal/Policy Analyst) and between four and seven stakeholder agents per case. A Moderator agent produces a conflict map at the midpoint of the deliberation, and a Decision Authority agent produces the final recommendation following an evidence audit. Each expert and stakeholder agent is required to cite scenario field identifiers for any substantive factual claim.

The MCDA baseline evaluates eleven criteria: water supply benefit, flood control benefit, energy benefit, economic viability, engineering feasibility, ecological impact acceptability, social impact acceptability, legal/governance readiness, climate robustness, stakeholder support, and evidence confidence. Equal weights are applied across criteria. Because the MCDA score is deterministic given the same scenario input, scores are consistent across Codex and Claude Code runs for each case.

The multi-agent system is not compared against baselines on Process Quality, because MCDA and single-agent formats are not designed to simulate deliberation. Applying a process-quality rubric to these baselines would mechanically inflate the multi-agent advantage without providing meaningful comparison.

### 2.3 Evaluation Rubric

The evaluation uses a three-layer rubric (v3).

**Layer 1 — Outcome Quality (/30)** assesses whether the recommendation is decision-useful. Subscores evaluate decision-range fit (whether the final recommendation falls within the expected region), recommendation specificity (whether conditions and sequencing are articulated), and calibration (whether confidence expressed in the recommendation matches the evidence base).

**Layer 2 — Evidence Quality (/40)** assesses whether outputs are grounded in scenario evidence, recover the designed risk structure, and treat uncertainty appropriately. The risk-coverage subscore (L2.2) is checked against evaluator-only gold checklists with must-detect (M) and should-detect (S) tiers. Missing an M-tier risk incurs a −4 penalty; missing an S-tier risk incurs a −1 penalty. Compact runs are subject to a ceiling adjustment on L2.2 reflecting that risk recovery in compact artifacts is inherently less complete than in full transcript runs.

**Layer 3 — Process Quality (/55)** assesses the quality of multi-agent deliberation across five dimensions: stakeholder and conflict representation, agent role fidelity, objection-response quality, evidence audit rigor and revision, and preservation of minority positions. This layer is reported for multi-agent outputs only and is not used as a direct baseline comparison (see Appendix C).

### 2.4 Run Protocol and Artifact Coverage

Each case was run twice: once in a Codex environment (designated `co`) and once in a Claude Code environment (designated `cc`). Both environments operated on identical scenario inputs and were subject to the same evaluation rubric and gold checklists. The co and cc runs were conducted independently.

All Codex compact runs (SRD-002 to SRD-008) were evaluated under the v1 rubric; three-layer evaluations were not produced for those runs. All Claude Code compact runs (SRD-002 to SRD-008) were evaluated under the full v3 three-layer rubric. The scores reported for Codex compact cases are therefore not directly comparable to the v3 scores from the Claude Code compact cases; cross-run score comparisons should be interpreted with this asymmetry in mind.

---

## 3. Results

### 3.1 Decision Direction Across Cases

The most substantively important result is that the multi-agent system generated the full range of plausible decision outcomes. Across eight cases it recommended Build (SRD-006), Build with conditions (SRD-002, SRD-007), Redesign (SRD-001, SRD-003), staged emergency action followed by deferred approval (SRD-004), Defer pending governance conditions (SRD-005), and Do not build (SRD-008). The system did not default to conservative deferral.

Codex and Claude Code produced the same decision direction for every case. Wording differs — most notably in whether time-conditioned recommendations are framed as gateway conditions or revert triggers — but the underlying decision structure is identical across environments. This cross-model agreement is a meaningful robustness signal: it suggests that the decision logic is driven by case design and system structure, not by idiosyncratic model behavior.

**Table 3. Multi-Agent Decision Directions Across Cases and Environments**

| Case | Codex multi-agent recommendation | Claude Code multi-agent recommendation | Agreement |
|---|---|---|---|
| SRD-001 | Redesign; defer final build approval | Redesign + Defer | High |
| SRD-002 | Build with conditions through phased approval | Build with conditions through phased approval | High |
| SRD-003 | Redesign toward the hybrid alternative | Redesign toward hybrid alternative | High |
| SRD-004 | Phased emergency package now; defer final reservoir approval | Phased emergency package now; defer final reservoir approval | High |
| SRD-005 | Defer pending basin agreement, joint monitoring, and drought rules | Defer pending binding basin agreement, joint monitoring, and drought-contingent rules | High |
| SRD-006 | Build; commissioning conditions attached | Build; commissioning conditions attached | High |
| SRD-007 | Build with conditions; approval lapses to Defer if livelihood plan is incomplete | Build with conditions; revert to Defer if livelihood plan is incomplete within 9 months | High |
| SRD-008 | Do not build; pursue wind portfolio alternative | Do not build; pursue wind portfolio alternative | High |

### 3.2 Quantitative Scores: Codex Runs

Table 4 reports L1 and L2 scores for multi-agent, single-agent, and MCDA outputs, and L3 for multi-agent outputs only, across the Codex runs. For SRD-001 the full transcript-style run is reported; for SRD-002–SRD-008 the compact runs are reported.

**Table 4. Codex Run Scores by Layer and System**

| Case | MA L1 /30 | MA L2 /40 | MA L3 /55 | SA L1 /30 | SA L2 /40 | MCDA L1 /30 | MCDA L2 /40 |
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

*MA = multi-agent; SA = single-agent. L3 is not scored for SA or MCDA.*

Three patterns are evident. First, multi-agent L1 Outcome Quality is consistently high, with the strongest scores in SRD-006, SRD-007, and SRD-008 — cases where a clear and specific decision label was required. Second, multi-agent L2 Evidence Quality is stable across cases, suggesting reliable recovery of the designed risk structure. Third, L3 Process Quality varies meaningfully: it is lower in SRD-006 because the clean approval case has limited conflict to represent, and higher in high-conflict or governance-heavy cases such as SRD-001, SRD-004, and SRD-005.

### 3.3 Quantitative Scores: Claude Code Runs

Table 5 reports scores for the Claude Code runs, evaluated under the v3 three-layer rubric for all cases.

**Table 5. Claude Code Run Scores by Layer and System**

| Case | MA L1 /30 | MA L2 /40 | MA L3 /55 | SA L1 /30 | SA L2 /40 | MCDA L1 /30 | MCDA L2 /40 |
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

The Claude Code profile differs from Codex in three respects. Multi-agent L2 Evidence Quality means are identical across environments (34.6 in both), while multi-agent L3 Process Quality is higher in the Claude Code runs (44.8 vs. 42.1). This is consistent with the qualitative observation that Claude Code compact artifacts tend to preserve more audit-explicit detail, including claim correction records and deliberative trace information. Codex scores higher on L1 Outcome Quality (28.1 vs. 26.5), partly because Codex recommendations are more directly phrased as action pathways.

Single-agent and MCDA baselines score more severely in the Claude Code runs. Because the baseline prompts are identical across environments, this difference likely reflects stricter rubric application in the Claude Code evaluations rather than genuine performance differences between the baseline systems. Cross-environment comparison of baseline scores should therefore be treated cautiously.

### 3.4 Cross-Model Comparison

Table 6 summarizes the main qualitative differences between Codex and Claude Code run profiles.

**Table 6. Cross-Environment Run Profile Comparison**

| Dimension | Codex tendency | Claude Code tendency | Interpretation |
|---|---|---|---|
| Final recommendation | More direct and action-oriented phrasing | Slightly more conditional framing in some cases | Both reach the same decision region |
| Evidence scoring | Stable and concise | Stable; more audit-explicit | Similar evidence recovery overall |
| Process artifact | Cleaner summary format | Richer audit and deliberative trace | Claude Code stronger for process inspection |
| Baseline scoring stringency | More generous | More severe | Baseline comparison should be reported cautiously |
| Manuscript use case | Compact result tables; reader-facing summary | Appendix-style process evidence | Both runs should be retained |

The most defensible manuscript strategy is to use one harmonized table for decision direction and risk recovery, and to treat co/cc score differences as a cross-model robustness check. The productive cross-environment claim is that the multi-agent method produces consistent decision structures across two independent model environments, not that one environment is objectively superior.

---

## 4. Case-Level Analysis

### 4.1 SRD-001: High-Conflict New Multipurpose Dam

SRD-001 is the flagship full-run case and the primary demonstration of the deliberative mechanism. The project has credible public benefits — urban water yield, irrigation reliability, flood reduction, and hydropower — but both Codex and Claude Code identify multiple concurrent blockers: incomplete climate-adjusted hydrology, uncertain fish passage effectiveness, endemic fish spawning habitat at risk, large-scale displacement, sacred sites, incomplete livelihood restoration, incomplete EIA review, incomplete safeguard plans, conditional financing, marginal downside economics, and dam-safety gaps.

The final recommendation in both environments is Redesign combined with deferred final approval. SRD-001 is best used as the process demonstration case in a manuscript, because the full-run artifact allows a reader to trace the chain from role-specific expert assessment through targeted deliberation, evidence audit, and decision-authority recommendation. The multi-agent output does not merely enumerate risks; it shows how different agents convert the same factual inputs into qualitatively different forms of concern — a financing condition, a legal blocker, a safety boundary, an ecological uncertainty, a social legitimacy objection, an economic downside scenario — each traceable to the agent and field evidence that produced it.

### 4.2 SRD-002: Low-Conflict Off-Channel Expansion

SRD-002 tests conservative bias. The project expands off-channel or existing storage, avoids blocking the main river, involves limited displacement, and rests on a stronger governance basis. Both systems recommend Build with conditions.

This case is important to the benchmark because it demonstrates that the multi-agent system does not automatically convert every uncertainty into a construction blocker. Remaining concerns — drought refill performance, tariff protection, wetland buffer enforceability, seismic retrofit, and grazing access — are treated as conditions rather than grounds for deferral. SRD-002 directly addresses the concern that a multi-agent setup might simply accumulate expert objections and systematically recommend delay regardless of whether the case warrants it.

### 4.3 SRD-003: Hydropower-Dominant Project

SRD-003 tests whether renewable energy framing causes the system to underweight local ecological and livelihood burdens. Both Codex and Claude Code recommend redesign toward a hybrid alternative. The important result is not merely that the proposed dam is rejected as designed, but that the system identifies a specific alternative pathway.

The multi-agent contribution is visible in the structure of the recommendation: energy benefit is preserved as a policy goal, but it is analytically separated from the local ecological and livelihood burden imposed by the current design. The hybrid alternative becomes decision-actionable because different agents connect grid-system need, river-specific ecological harm, comparative cost, and local benefit-burden mismatch into a coherent redesign case. MCDA can show that the current project scores poorly, but it cannot naturally explain why a hybrid alternative constitutes the appropriate redesign direction.

### 4.4 SRD-004: Flood-Control Emergency

SRD-004 tests whether emergency conditions lead the system toward premature approval of irreversible infrastructure. Both environments produce a phased recommendation: implement immediate emergency protective measures now, defer final reservoir approval pending further investigation.

This case demonstrates the multi-agent system's capacity for decision sequencing. A simple Build or Defer label is structurally inadequate for this scenario. The correct policy logic requires acting immediately on non-controversial protective measures — early-warning systems, temporary flood barriers, channel clearing — while withholding irreversible construction approval until climate-adjusted flood estimates, geotechnical investigation, land acquisition legitimacy, and downstream operation safety are resolved. The multi-agent output converts an apparent binary choice into a staged governance pathway, which is the appropriate decision-support form for scenarios where urgency and irreversibility are in tension.

### 4.5 SRD-005: Transboundary and Downstream Conflict

SRD-005 is governance-heavy. The upstream project benefits are real, but downstream dry-season flow reduction, wetland impacts, basin compact ambiguity, absence of trusted joint monitoring mechanisms, and lender requirements make unilateral approval questionable under international water law and financing conditions [CITE]. Both systems recommend deferral pending a binding basin agreement, joint monitoring arrangement, and binding drought operating rules.

The most significant deliberative contribution in this case is the preservation of legal disagreement. The upstream domestic legal position and the downstream no-significant-harm argument are not collapsed into a single legal conclusion. The system treats the unresolved legal conflict itself as a decision-relevant blocking condition. This is precisely the type of issue that a weighted MCDA score can conceal: a moderate legal-readiness criterion score does not reveal that the governing compact is subject to competing interpretations between treaty parties.

### 4.6 SRD-006: Clean Approval Case

SRD-006 is the clean approval case. Both systems recommend Build with only commissioning conditions attached. This case is central to the conservative-bias check: the multi-agent system must distinguish construction blockers from operational commissioning requirements. Sediment management protocols, low-flow diversion cutoff triggers, and habitat monitoring plans are correctly characterized as conditions for the operational phase rather than reasons to withhold construction authorization.

The lower Layer 3 Process Quality score in the Codex run for this case is not a failure. It reflects that there is less conflict to represent and preserve in a low-conflict scenario. A well-calibrated deliberative system should not manufacture controversy from thin evidence. SRD-006 therefore serves a secondary calibration function for the process rubric: low-conflict cases should naturally receive lower stakeholder-conflict scores, and rubric calibration that produces artificially high L3 scores for clean cases would misrepresent what the process layer is measuring.

### 4.7 SRD-007: Near-Tipping-Point Case

SRD-007 is the strongest evidence case for multi-agent added value. The project has credible irrigation benefits and most safeguards are substantially complete, but the livelihood restoration section of the resettlement action plan remains unfinalized. A generic Defer is defensible but not maximally decision-useful.

Both Codex and Claude Code identify the livelihood restoration plan as the specific swing condition and produce a time-conditioned approval pathway: Build with conditions, with a revert trigger if the livelihood restoration section is not completed within nine months. The critical deliberative contribution is the distinction between a near-complete, resolvable safeguard gap and a fundamental project flaw. The system achieves this by combining evidence from multiple agents: the Development Lender's identification of the livelihood plan as the single financing block; the Social Agent's confirmation that the housing and compensation sections are already complete and independently reviewed; the Dam Safety Agent's clarification that the emergency action plan outline is acceptable for feasibility approval but not for construction authorization; and the Moderator's synthesis of these inputs into a hierarchically ordered condition structure.

The single-agent baseline in this case recommends Defer until the livelihood plan and economic review are complete — a defensible but less specific response that does not produce a time-conditioned pathway or distinguish the livelihood plan from the other outstanding items. MCDA reads the incomplete social safeguard and marginal economic case (BCR 1.08 base, 0.97 downside) as low criterion scores and produces a Redesign or Defer output. Neither baseline generates the conditional-approval-with-revert structure that the case design identifies as the decision-useful target. The score gap between multi-agent and baselines is larger in SRD-007 than in any other case, which is consistent with the case design: near-tipping-point conditions are precisely where granular condition logic matters most.

### 4.8 SRD-008: Do-Not-Build Case

SRD-008 tests whether the system can reject a project and explicitly rule out the Redesign alternative. Both environments recommend Do not build and pursue the wind portfolio alternative. The important feature is that the multi-agent output does not merely note that the current design is deficient; it provides independent grounds for ruling out each alternative disposition label — smaller dam, redesign, and defer — and identifies a wind portfolio as a policy-compatible substitute with a materially higher benefit-cost ratio (1.68 versus 0.94 for the proposed project).

MCDA performs relatively well in this case because all major criteria point in the same direction, producing an aggregate score (approximately 1.73/5.0) that clearly signals non-viability. However, MCDA still lacks the explanatory structure to articulate why Redesign is insufficient. It cannot express that the project fails simultaneously on economics, irreversible endemic species extinction, and withheld indigenous consent, and that no resolvable pathway through those three independent objections exists. The multi-agent output makes each line of reasoning traceable to a specific agent's assessment and the scenario evidence that supports it.

---

## 5. Discussion

### 5.1 When Multi-Agent Deliberation Adds Most Value

Three findings from this benchmark characterize the conditions under which multi-agent deliberation generates the greatest decision-support value relative to the baselines.

First, multi-agent advantage is most pronounced in cases where the decision requires structured sequencing rather than a single label. SRD-004 is the clearest example: the correct response combines immediate protective action with deferred final approval, and neither MCDA nor single-agent analysis generates this structure. SRD-007 exhibits the same pattern: the conditional-approval-with-revert-trigger format emerges specifically from the multi-agent deliberative process, in which the Moderator synthesizes agent-specific testimony about which conditions are pre-approval blockers and which are pre-construction requirements.

Second, multi-agent deliberation adds the most visible value when the decision logic turns on a condition that does not reduce easily to a criterion score. In SRD-005, the basin-compact legal disagreement between treaty parties is irreducible to a single legal-readiness score; it requires representation as an unresolved conflict between two defensible legal positions. In SRD-007, the distinction between a near-complete safeguard gap and a fundamental project flaw requires agent-level testimony that would be invisible inside a criterion average. The multi-agent format provides a natural structure for this kind of condition-specific reasoning.

Third, the method's advantage is weakest in clear cases. SRD-006 demonstrates that when the scenario is unambiguous and the decision is straightforward, the single-agent output is already close to adequate, and the multi-agent output adds limited decision content. This expected pattern is important for positioning the method correctly: role-limited multi-agent deliberation should not be described as always superior to single-agent analysis, but as providing the largest gain when decision complexity warrants the added structure.

### 5.2 Baseline Performance Comparison

The single-agent baseline is not weak in a trivial sense. It identifies major risks across all eight cases and typically reaches an adjacent or correct decision region. Its structural limitation is that it produces a unified narrative rather than a deliberation record: it does not preserve who disagreed, what role-specific objection was raised, whether the objection was answered, or which minority positions remain on the record. In contested infrastructure governance, the acceptability of a recommendation often depends not only on its content but on the visible procedural process through which concerns were heard and handled [CITE].

MCDA performs reasonably on clear cases (SRD-006, SRD-008) where all major criteria align. Three recurring limitations appear across the benchmark:

1. **Veto compression**: A legal or safeguard condition that would block financing or construction can be partially offset by high scores on other criteria, producing a moderate aggregate that obscures the blocking condition.
2. **Sequencing incapacity**: MCDA cannot express emergency action now combined with deferred approval later. It outputs a single score for the proposed action, not a staged governance pathway.
3. **Conditional-pathway incapacity**: MCDA cannot generate a time-conditioned approval of the form produced in SRD-007, because such approvals depend on conditional logic rather than aggregation.

MCDA is useful as a baseline precisely because these limitations illustrate what is lost when multi-party deliberation is reduced to weighted aggregation. The gap between the multi-agent and MCDA outputs is itself informative about the nature of each case's decision complexity.

### 5.3 The Central Contribution: Process Inspectability

This study advances a methodological claim rather than an empirical claim about decision correctness. The cases are synthetic and were constructed by the same researchers who designed the evaluation rubric and ran the scoring. The benchmark cannot establish that the multi-agent system makes better reservoir decisions in any externally validated sense.

What the benchmark establishes is that the multi-agent system produces a qualitatively different kind of decision-support artifact. That artifact is inspectable at the level of individual roles: a reader can identify which expert or stakeholder concern produced a given condition, which objection was raised and answered, and which minority position remains unresolved. This structure is useful not only for the quality of the final recommendation but for the process of institutional review and accountability that accompanies contested infrastructure decisions [CITE].

This is a restrained but substantive claim. It positions the method as a decision-support tool rather than a decision oracle, which is the appropriate framing for a system evaluated on synthetic cases without real-world outcomes. More ambitious claims — that the system makes objectively better decisions, or that its recommendations would survive independent expert review — require evidence that the present benchmark cannot provide.

### 5.4 Limitations

Several limitations constrain the conclusions that can be drawn from this benchmark.

**Synthetic cases and researcher involvement.** All eight cases are synthetic and were constructed by the same researchers who designed the evaluation rubric and conducted the scoring. This provides experimental control over the risk structure, but creates the possibility that the evaluation reflects the designer's expectations rather than an independent assessment. The evaluator-only gold checklists reduce direct leakage to the agents, but they do not eliminate researcher involvement in case construction and scoring. Independent blinded evaluation by water-resource experts, environmental assessment specialists, or infrastructure governance scholars would be required before making strong empirical claims.

**Researcher-coded scoring.** All L1, L2, and L3 scores were assigned by members of the research team. Inter-rater reliability has not been assessed and should be established before submission to a peer-reviewed venue.

**Compact run limitations.** SRD-002 through SRD-008 are compact runs rather than full-protocol runs. Compact runs provide useful evidence of deliberative structure and decision direction, but do not support the same depth of process-quality inference as a full run. The v3 rubric applies a ceiling adjustment to L2.2 risk-coverage scores for compact artifacts to account for this; nonetheless, compact scores should not be treated as equivalent to full-run scores.

**Rubric asymmetry across environments.** Codex compact runs were evaluated under the v1 rubric; Claude Code compact runs were evaluated under the full v3 three-layer rubric. Direct score comparison between co and cc compact runs is not fully valid. Scores should be interpreted as within-environment patterns.

**MCDA weights are provisional.** Equal weights across eleven criteria are a reasonable starting assumption but should not be treated as validated. A mature study should either justify weights from the water-resources decision-analysis literature or report sensitivity analysis across alternative weight structures.

**No real-world cases.** The benchmark includes no real reservoir cases. Real cases introduce missing documentation, political ambiguity, conflicting historical data, and observable outcomes against which recommendations can be checked. Synthetic results support method development; external validity requires real-case validation.

### 5.5 Future Work

The following steps would most substantially strengthen a manuscript built on this benchmark.

**Full-protocol transcript run for SRD-007.** SRD-007 is the strongest candidate for a second full run because it demonstrates the most distinctive multi-agent capability — identifying a swing condition and producing a time-conditioned pathway. A full run would allow more granular process-quality evaluation of how that pathway was constructed across agent exchanges, and would support higher L3 scores than the current compact run permits.

**Independent blinded evaluation.** At least one wave of independent scoring — by evaluators who did not construct the cases and who do not see the run-environment label — is required for claims about recommendation quality to have external standing.

**MCDA calibration and sensitivity analysis.** Either justify equal weights from the decision-analysis literature [CITE] or present sensitivity analysis showing whether the reported multi-agent versus MCDA score gap holds under alternative weight structures.

**Real-world case validation.** One or two cases using publicly available EIA reports, financing appraisal documents, resettlement plans, or basin management agreements would test whether the framework performs outside synthetic conditions and whether the deliberative contributions identified here are reproducible in less controlled settings.

**Literature integration.** A manuscript-ready version requires a full literature review covering: MCDA in water-infrastructure planning [CITE]; participatory and deliberative governance frameworks for contested infrastructure decisions [CITE]; LLM-based multi-agent reasoning systems [CITE]; and environmental decision support tools [CITE].

---

## 6. Conclusion

This paper reports the first systematic synthetic benchmark of role-limited multi-agent deliberation for reservoir construction decision support, covering eight cases in two model environments. The system produced decision outcomes spanning the full range from Build to Do not build without systematic conservative bias. Single-agent and MCDA baselines produced shorter, less structured outputs that consistently compressed the deliberative complexity that the multi-agent format preserved.

The clearest evidence for multi-agent added value comes from cases requiring staged sequencing, governance-specific blocking conditions, or time-conditioned approval pathways — decision structures that neither single-agent analysis nor weighted aggregation can naturally produce. Cross-model consistency between Codex and Claude Code environments for all eight cases supports the conclusion that the observed decision logic is driven by case design and system structure rather than model-specific behavior.

The central methodological contribution is that role-limited multi-agent deliberation generates an inspectable, role-bounded decision-support artifact. The system's value does not lie in producing objectively correct reservoir decisions — a claim that synthetic evaluation cannot support — but in structuring the reasoning process so that expert disagreement, stakeholder conflict, minority positions, and the chain from evidence to recommendation are preserved and auditable. For contested infrastructure decisions where the legitimacy of the review process matters alongside the quality of the final recommendation, this structure is itself decision-relevant.

The present benchmark supports a method-and-benchmark manuscript draft, provided limitations are stated clearly. The study will become substantially stronger after at least one additional full-protocol run, independent blinded scoring, MCDA sensitivity analysis, and real-world case validation.

---

## References

*Literature review not yet completed. This section should cover: MCDA in water-resources and infrastructure planning; participatory and deliberative governance frameworks; LLM-based multi-agent systems; and environmental decision support tools. Citation placeholders marked [CITE] throughout the text indicate where specific references should be inserted.*

---

## Appendix A: Evaluation Rubric Summary

**Layer 1 — Outcome Quality (/30)**

| Subscore | Description | Max |
|---|---|---|
| L1.1 Decision-range fit | Whether the recommendation falls within the expected decision region | /12 |
| L1.2 Recommendation specificity | Whether conditions, sequencing, and pathways are articulated | /10 |
| L1.3 Calibration | Whether expressed confidence matches the evidence base | /8 |

**Layer 2 — Evidence Quality (/40)**

| Subscore | Description | Max |
|---|---|---|
| L2.1 Factual grounding | Whether factual claims are cited to scenario field identifiers | /10 |
| L2.2 Risk coverage | Whether must-detect and should-detect risks from the gold checklist are recovered | /20 |
| L2.3 Uncertainty treatment | Whether inference, assumption, and uncertainty are labeled appropriately | /10 |

*L2.2 penalty structure: −4 per missed M-tier risk; −1 per missed S-tier risk. Compact runs subject to a ceiling adjustment.*

**Layer 3 — Process Quality (/55)** *(multi-agent outputs only)*

| Subscore | Description | Max |
|---|---|---|
| L3.1 Stakeholder and conflict representation | Whether relevant stakeholders and conflict types are present and faithfully represented | /12 |
| L3.2 Role fidelity | Whether agents remain within their assigned expert or stakeholder boundaries | /10 |
| L3.3 Objection-response quality | Whether raised objections are acknowledged and addressed, or explicitly preserved as unresolved | /12 |
| L3.4 Evidence audit rigor | Whether substantive claims are audited, labeled, and corrected where necessary | /13 |
| L3.5 Minority preservation | Whether minority positions are recorded in the final output rather than absorbed into consensus | /8 |

---

## Appendix B: Key Artifact Paths

| Artifact | Path in workspace |
|---|---|
| SRD-001 Codex revised compact run | `artifacts/demo-001-co/` |
| SRD-001 Claude Code full transcript run | `artifacts/demo-001-cc/` |
| SRD-001 Codex full transcript-style run | `artifacts/demo-001-co-full/` |
| SRD-002–SRD-008 Codex compact runs | `artifacts/demo-002/` through `artifacts/demo-008/` |
| SRD-002–SRD-008 Claude Code compact runs | `artifacts/demo-002-cc/` through `artifacts/demo-008-cc/` |
| Cross-case score summary | `artifacts/cross-case-score-summary-v0.1.md` |
| Case run index | `artifacts/synthetic-case-run-index.md` |
| Benchmark protocol | `artifacts/controlled-synthetic-benchmark-protocol-v0.1.md` |
| Model package and case status | `packages/model-package-synthetic-benchmark-v0.1.md` |

---

## Appendix C: Reporting Rule for Layer Scores

Layer 1 and Layer 2 scores are valid for cross-system comparison (multi-agent, single-agent, MCDA). Layer 3 scores should be reported only for multi-agent deliberation outputs. A combined L1+L2+L3 total should not be reported, because it would reward multi-agent systems for having deliberative structure that MCDA and single-agent formats were not designed to provide.
