# Synthetic Case Suite v0.1

## Purpose

This suite defines 8 synthetic reservoir decision cases for evaluating the role-limited multi-agent deliberation system.

The goal is not to prove that any simulated recommendation is objectively correct. The goal is to test whether the system can produce acceptable, evidence-grounded, conflict-sensitive decision-support artifacts across different types of difficult reservoir decisions.

Each case should be evaluated with:

1. role-limited multi-agent deliberation;
2. single-agent decision analyst baseline;
3. weighted-score MCDA baseline;
4. three-layer evaluation rubric with sub-scores recorded per layer (see `artifacts/demo-001-co/protocols/revised-evaluation-rubric-v0.1.md`).

## Controlled Benchmark Rule

Each synthetic case is a controlled benchmark, not an open-ended story prompt.

For every case, create two layers:

1. **Agent-facing neutral scenario:** facts, variables, stakeholder statements, and uncertainties. This is the only case content agents can see.
2. **Evaluator-only hidden design layer:** gold risk checklist, expected issue clusters, reasonable decision range, and suspicious outputs. Agents must not see this layer.

The evaluation asks whether the system can recover the designed risk and conflict structure from neutral facts.

Required evaluator-only files for each case:

| File | Purpose |
|---|---|
| `protocols/evaluator-only-gold-checklist.md` | Lists the risks, benefits, conflicts, and missing-evidence items the case was designed to contain. |
| `protocols/reasonable-decision-range.md` | Defines acceptable recommendation labels and suspicious labels for the case. |

This design means we do not evaluate whether the system finds a single objectively correct policy answer. We evaluate whether it produces a recommendation that falls within the pre-specified reasonable decision range and whether it finds the risks that should be found.

See `artifacts/controlled-synthetic-benchmark-protocol-v0.1.md`.

## Shared Evaluation Records Required for Every Case

For each case, save:

- scenario packet;
- Round 1 agent assessments;
- Moderator conflict map;
- targeted deliberation;
- evidence audit;
- revised assessments;
- decision-authority recommendation;
- single-agent baseline;
- MCDA baseline;
- baseline comparison;
- deliberative acceptability evaluation;
- per-dimension score table;
- run log and run manifest.

## Required Score Tables

Every case must record three separate score tables. Do not sum across layers.

**Layer 1 — Outcome Quality /30** (all three systems; primary cross-system comparison):

| System | Decision-range fit /5 | Recommendation specificity /15 | Recommendation calibration /10 | Layer 1 total /30 | Final recommendation |
|---|---:|---:|---:|---:|---|
| Multi-agent |  |  |  |  |  |
| Single-agent |  |  |  |  |  |
| MCDA |  |  |  |  |  |

**Layer 2 — Evidence Quality /40** (all three systems; secondary comparison):

| System | Evidence grounding /10 | Risk coverage /20 | Uncertainty calibration /10 | Layer 2 total /40 |
|---|---:|---:|---:|---:|
| Multi-agent |  |  |  |  |
| Single-agent |  |  |  |  |
| MCDA |  |  |  |  |

**Layer 3 — Process Quality /55** (multi-agent only; descriptive; do not compare with baselines):

| Dimension | Score |
|---|---:|
| Stakeholder/conflict representation /15 |  |
| Role fidelity /15 |  |
| Objection-response quality /10 |  |
| Evidence audit and revision /10 |  |
| Minority preservation /5 |  |
| **Layer 3 total /55** |  |

Qualitative note: [1 paragraph describing where deliberation was strongest and weakest for this case]

## Required Controlled-Benchmark Table

Every case must also record this table:

| System | Must-detect recall | Should-detect recall | Decision-range fit /2 | False reassurance count | Unsupported blocker count |
|---|---:|---:|---:|---:|---:|
| Multi-agent |  |  |  |  |  |
| Single-agent |  |  |  |  |  |
| MCDA |  |  |  |  |  |

## Required Emergent Issue Discovery Table

Every case must also record additional issues proposed by each system but not included in the hidden checklist.

| System | Candidate emergent issues | Valid emergent issues | Weak-but-interesting | Duplicate/rephrasing | Unsupported/hallucinated | Emergent precision | Decision-relevant discoveries |
|---|---:|---:|---:|---:|---:|---:|---:|
| Multi-agent |  |  |  |  |  |  |  |
| Single-agent |  |  |  |  |  |  |  |
| MCDA |  |  |  |  |  |  |  |

Candidate emergent issues must be reviewed by a human evaluator using `artifacts/emergent-issue-discovery-protocol-v0.1.md`.

## Case SRD-001: High-Conflict New Multipurpose Dam

**Status:** completed first run.

**Scenario type:** new mainstem/upper-valley multipurpose reservoir.

**Core tension:** real water, flood, and energy benefits vs severe ecological, social, safeguard, climate, and downside-economic risks.

**Why this is realistic and difficult:**

- Many real dam controversies are not about zero benefits; they are about whether benefits justify concentrated displacement, river fragmentation, and procedural risk.
- Public benefits and local burdens are distributed unevenly.
- Project promoters may argue mitigation is possible while affected communities and NGOs argue risks are irreversible.

**Stress-test purpose:**

- Can the system block premature approval while preserving the fact that the project has legitimate public benefits?
- Can it represent affected residents, NGO concerns, financing safeguards, and technical experts without collapsing them into a single pro/con list?

**Expected reasonable decision range:**

- Redesign with final approval deferred.
- Defer.
- Do not build as proposed.

**Suspicious output:**

- Immediate Build.
- Simple Do not build without recognizing water-security and flood-control benefits.

## Case SRD-002: Low-Conflict Off-Channel Storage / Existing Reservoir Expansion

**Scenario type:** expansion of an existing reservoir or off-channel storage that does not block the main river.

**Core tension:** high water-security benefit and relatively mature governance vs cost, climate uncertainty, and opportunity cost.

**Why this is realistic and difficult:**

- Some water projects are not dramatic mega-dams but incremental storage expansions.
- These projects may have lower displacement and ecological disruption, but still face cost, climate, and alternative-investment questions.
- A good system should not be biased toward Defer/Reject when evidence and safeguards are comparatively strong.

**Stress-test purpose:**

- Test whether the system can recommend Build with conditions or phased approval.
- Test whether stakeholder and ecological agents can give qualified support when risks are low.
- Test over-conservatism.

**Expected reasonable decision range:**

- Build with conditions.
- Phased approval.
- Redesign minor components.

**Suspicious output:**

- Automatic Defer or Do not build despite low social/ecological risk.
- Ignoring remaining climate or cost uncertainties.

**Key scenario ingredients to include:**

- Existing dam or off-channel basin.
- Minimal physical displacement.
- No endemic species or critical habitat inundation.
- Completed EIA with manageable mitigation.
- Strong municipal drought need.
- Moderate cost overrun risk.
- Public concern over tariffs or debt.
- Non-dam alternatives partially useful but insufficient alone.

## Case SRD-003: Hydropower-Dominant Project With Weak Local Water Benefits

**Scenario type:** hydropower-oriented dam proposed mainly for energy generation and revenue.

**Core tension:** renewable energy and grid flexibility vs river ecology, downstream livelihoods, and limited local water-supply benefit.

**Why this is realistic and difficult:**

- Hydropower is often framed as clean energy, but ecological and social costs may be severe.
- Benefits may accrue to national grids or urban consumers while local communities bear impacts.
- Climate variability can reduce hydropower reliability.

**Stress-test purpose:**

- Test whether energy benefits are overvalued relative to local ecological/social costs.
- Test whether the system can distinguish renewable energy value from overall public-interest justification.
- Test whether downstream users and ecological agents can force alternatives analysis.

**Expected reasonable decision range:**

- Defer pending alternatives analysis.
- Redesign.
- Do not build as proposed.

**Suspicious output:**

- Build simply because hydropower is renewable.
- Ignore local benefit-burden mismatch.

**Key scenario ingredients to include:**

- High installed capacity and grid value.
- Limited water-supply or flood-control benefit.
- Fish migration and downstream sediment impacts.
- Few but politically marginalized affected communities.
- Competing solar/wind/storage alternative.
- Power-purchase agreement pressure.

## Case SRD-004: Flood-Control Emergency Project After Disasters

**Scenario type:** dam or flood-retention reservoir proposed after repeated severe floods.

**Core tension:** urgent disaster-risk reduction vs rushed process, safety, environmental review, and maladaptation risk.

**Why this is realistic and difficult:**

- Post-disaster politics can create pressure for rapid infrastructure approval.
- Flood-control projects may have strong public support but can create false security or downstream risk transfer.
- Emergency framing can weaken consultation and alternatives analysis.

**Stress-test purpose:**

- Test whether the system handles urgency without abandoning safeguards.
- Test whether the decision authority can recommend emergency/temporary measures while deferring irreversible construction.
- Test climate, dam safety, and downstream risk reasoning.

**Expected reasonable decision range:**

- Phased emergency measures plus Defer final dam approval.
- Redesign.
- Build with strict conditions only if evidence is unusually strong.

**Suspicious output:**

- Immediate Build because floods are severe.
- Do not build without offering emergency risk-reduction alternatives.

**Key scenario ingredients to include:**

- Recent catastrophic floods.
- High political pressure.
- Incomplete long-term hydrology.
- Potential downstream risk transfer.
- Strong public support in flood-hit towns.
- Ecological and land-acquisition concerns.
- Alternative levee, wetland, early-warning, zoning measures.

## Case SRD-005: Transboundary / Downstream-Conflict Reservoir

**Scenario type:** upstream reservoir with cross-jurisdictional or cross-border downstream impacts.

**Core tension:** upstream water and energy security vs downstream water rights, treaty obligations, fisheries, agriculture, and regional conflict.

**Why this is realistic and difficult:**

- Many reservoir decisions are not only local; they affect downstream jurisdictions.
- The most important issue may be governance legitimacy, data sharing, and binding operating rules rather than engineering feasibility.
- Stakeholders may distrust each other even when technical mitigation is possible.

**Stress-test purpose:**

- Test whether the system can represent institutional trust and downstream rights.
- Test whether legal/policy and governance agents become central.
- Test whether the system identifies data-sharing and operating-rule commitments as decision conditions.

**Expected reasonable decision range:**

- Defer pending basin agreement.
- Redesign with binding operating rules.
- Build only after treaty/compact conditions.

**Suspicious output:**

- Build based only on upstream benefits.
- Ignore downstream legal or political legitimacy.

**Key scenario ingredients to include:**

- Upstream region receives storage and hydropower benefits.
- Downstream region depends on seasonal flows.
- Existing water-sharing compact or treaty is ambiguous.
- No trusted joint monitoring system.
- Downstream government or communities object.
- Climate change increases dry-season scarcity.

## Case SRD-006: Clean Approval Case

**Status:** scenario complete; run summary complete.

**Scenario type:** small off-channel water security reservoir with no structural blockers.

**Core tension:** no major conflict. Remaining items are administrative commissioning conditions, not construction blockers. Tests over-conservatism directly.

**Why this is realistic and difficult:**

- Real projects do reach a state where all blockers are resolved. A good system should be able to say Build when that state is reached, not add unnecessary deferral.
- The challenge is separating commissioning conditions (sediment plan, operating rule, monitoring) from construction-blocking conditions. A system that conflates these will add unnecessary delay.

**Stress-test purpose:**

- Test whether the system produces Build or near-Build when blockers are resolved.
- Test whether MCDA and single-agent also perform reasonably on simple cases (expected: score gaps narrow).

**Expected reasonable decision range:**

- Build.
- Build with minor commissioning conditions.

**Suspicious output:**

- Defer due to incomplete sediment plan or operating rule (these are administrative, not blocking).
- Do not build despite strong economics, complete EIA, and resolved resettlement.

## Case SRD-007: Near-Tipping-Point Case

**Status:** scenario complete; run summary complete.

**Scenario type:** medium-scale irrigation dam with marginal economics and one incomplete safeguard as the swing condition.

**Core tension:** project need is credible and most safeguards are complete, but economics are marginal under downside assumptions and the livelihood restoration section of the resettlement plan is incomplete. The decision genuinely could go either way.

**Why this is realistic and difficult:**

- Many real reservoir decisions are neither clear-Build nor clear-Reject; they sit on a threshold where one remaining gap determines the recommendation.
- Single-agent and MCDA baselines tend to default to generic Defer on ambiguous cases; multi-agent deliberation can identify the specific swing condition and produce a time-conditioned pathway.

**Stress-test purpose:**

- Test whether the system can produce a specific, time-conditioned recommendation ("Build with conditions; revert to Defer in 9 months if condition not met") rather than generic Defer.
- Test whether the system distinguishes a near-complete safeguard gap from a fundamental project flaw.
- Show the largest single-agent Decision Usefulness gap in the benchmark.

**Expected reasonable decision range:**

- Build with conditions contingent on livelihood plan completion.
- Defer until livelihood plan is complete.

**Suspicious output:**

- Unconditional Build without resolving the livelihood plan.
- Do not build without recognizing that irrigation need is credible and most safeguards are in place.

## Case SRD-008: Do Not Build Case

**Status:** scenario complete; run summary complete.

**Scenario type:** remote hydropower dam with negative base-case BCR, irreversible endemic-species loss, indigenous consent formally withheld, and a clearly dominant wind alternative.

**Core tension:** developer argues for dispatchable clean energy and increased revenue sharing; all other agents identify problems that conditions and redesign cannot resolve.

**Why this is realistic and difficult:**

- Real "Do not build" decisions are politically difficult even when the evidence is clear. A system should be able to produce this label and defend it — not default to Defer or Redesign when those labels are inappropriate.
- The challenge is distinguishing Do not build from Redesign: the system must articulate why a smaller dam does not resolve the fundamental objections, not just score the current configuration poorly.

**Stress-test purpose:**

- Test whether the system produces Do not build rather than a reflexive Defer or an unwarranted Redesign recommendation.
- Test whether the system explicitly addresses why redesign is not a viable path, not just why Build is blocked.
- Test MCDA performance on a case where multiple dimensions are low — expected to perform better than on complex mixed cases.

**Expected reasonable decision range:**

- Do not build.
- Do not build; pursue wind/solar portfolio.

**Suspicious output:**

- Build or Build with conditions despite BCR below 1.0, fish passage technically impossible, and indigenous consent formally withheld.
- Redesign without explaining why fish passage and endemic species loss are not resolved by a smaller dam.
- Defer without identifying that the core problems are not resolvable by additional study.

## Proposed Case Execution Order

1. SRD-001: high-conflict new dam. Completed first.
2. SRD-002: low-conflict off-channel / expansion. Tests over-conservatism.
3. SRD-004: flood emergency. Tests urgency vs safeguards.
4. SRD-003: hydropower-dominant. Tests renewable-energy framing and local burden.
5. SRD-005: transboundary/downstream conflict. Tests governance and legal legitimacy.
6. SRD-006: clean approval. Tests over-conservatism directly; produces Build.
7. SRD-007: near-tipping-point. Tests decision specificity under genuine ambiguity.
8. SRD-008: Do not build. Completes full decision-space coverage.

## Real-Case Validation After Synthetic Suite

After at least four synthetic cases are completed, select 1-2 public real cases with enough documentation:

- official project documents or EIA;
- stakeholder or NGO comments;
- financing/safeguard documents if available;
- government decision or approval status;
- media or public consultation records.

Real cases should not be treated as ground truth. They are used to test whether the system can process messy real-world evidence and whether its concerns align with documented expert/stakeholder issues.

## Cross-Case Analysis Plan

After all synthetic cases:

| Analysis | Purpose |
|---|---|
| Score comparison across systems | Does multi-agent consistently score higher on deliberative acceptability? |
| Decision diversity check | Does the system produce Build, Redesign, Defer, and Reject when scenario conditions differ? |
| Conservative-bias check | Does the system overuse Defer/Redesign? |
| Role-fidelity trend | Which agents most often overreach? |
| Evidence-audit trend | Which claim types most often lack support? |
| Conflict coverage trend | Which conflicts are best/worst represented? |
| Baseline loss analysis | What does single-agent or MCDA consistently compress or miss? |

## Minimum Manuscript-Ready Synthetic Evidence

The synthetic suite is manuscript-ready only if:

1. at least 4 cases are completed;
2. every case has all three systems evaluated;
3. every case includes per-dimension scores;
4. the system produces different recommendations under different scenario conditions;
5. at least one case plausibly supports Build with conditions or phased approval;
6. limitations are explicit that synthetic cases do not validate real policy correctness.
