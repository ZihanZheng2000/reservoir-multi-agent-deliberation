# Revised Run Summary: SRD-001 Codex Revised Run

## Run Changes From Original Demo

| Change | Implemented? | Notes |
|---|---|---|
| Removed agent-facing decision hints | yes | Original `F12 Initial Assessment Hints` removed from neutral scenario. |
| Added evaluator-only gold checklist | yes | Stored separately under protocols. |
| Added prompt templates | yes | Round 1, Moderator, Auditor, Decision Authority. |
| Added decision thresholds | yes | Explicit Build / Build with conditions / Redesign / Defer / Do not build rules. |
| Added quantitative evidence audit | yes | Claim metrics included below. |
| Split evaluation into shared and deliberative scores | yes | Applied in revised evaluation. |

## Multi-Agent Deliberation Result

### Recommendation

**Redesign; final build approval deferred.**

### Final Build Approval Status

**Deferred.**

### Why This Result Emerged Without Agent-Facing Hints

Even after removing the initial assessment hints, the agents converged on a conditional redesign/defer position because several blockers are explicitly present in the neutral facts:

- firm yield benefit is real, but severe drought reduces yield by 38%;
- BCR is positive only in the base case and below 1.0 in downside conditions;
- ecological mitigation is uncertain for endemic fish;
- resettlement and livelihood restoration are incomplete;
- independent EIA review and safeguard plans are incomplete;
- development-bank financing requires acceptable E&S management.

### Expert Position Summary

| Agent | Position | Key evidence |
|---|---|---|
| Hydrologist | Project has real water-supply value but requires climate and flow-rule revision. | F2.4, F2.5, F2.7, F2.10 |
| Engineering / Dam Safety | Technically plausible but not build-ready. | F6.4-F6.7 |
| Ecologist | Current design has high ecological risk and unproven mitigation. | F7.1-F7.8, F11.2 |
| Climate Risk | Benefits and safety are not robust without climate-adjusted analysis. | F2.7, F4.4, F5.3, F11.1 |
| Economist / Finance | Base economics are marginal; downside economics are weak. | F5.2, F5.3, F11.6 |
| Social / Resettlement | Social safeguards are a blocker before final approval. | F8.1-F8.7, F11.4 |
| Legal / Policy | Final build approval is not ready under represented safeguards. | F9.3-F9.8 |

### Stakeholder Position Summary

| Stakeholder | Position | Key evidence |
|---|---|---|
| Developer | Continue through redesign rather than reject. | F2.4, F3.2, F4.1-F4.3 |
| Government / Regulator | Public need exists, but approval depends on safeguards. | F2.5, F9.5, F9.6 |
| Local Government | Benefits exist, but resettlement could destabilize locality. | F10.3, F8.1-F8.8 |
| Upstream Affected Residents | Oppose approval before compensation, relocation, and sacred-site treatment are clear. | F8.1-F8.7, F10.4 |
| Downstream Users | Conditional support only with binding dry-season flow and fishery protection. | F1.4, F2.10, F7.6, F10.5 |
| Environmental NGO | Opposes current design; asks alternatives and avoidance-first redesign. | F7.1-F7.8, F0.6 |
| Financier | Not finance-ready until safeguards, stakeholder engagement, and downside economics are resolved. | F5.3, F9.6, F9.8, F10.7 |

## Moderator Conflict Map

| Conflict | Why it matters | Evidence |
|---|---|---|
| Water security vs ecological flow | Firm yield supports urban need, but dry-season flow may be too low for spawning. | F2.4, F2.5, F2.9, F2.10 |
| Public benefit vs concentrated displacement | Urban beneficiaries receive water security while upstream households lose land and sacred sites. | F8.1-F8.3 |
| Base-case economics vs downside economics | Base BCR supports study; downside BCR blocks confident approval. | F5.3 |
| Hydropower/flood/storage operation conflict | Pre-release for flood control may conflict with hydropower and storage goals. | F3.5 |
| Policy fit vs safeguard readiness | Project aligns with policy but EIA, resettlement, biodiversity, and financing safeguards remain incomplete. | F9.3-F9.8 |
| Mitigation promises vs mitigation evidence | Fish passage and environmental flows are proposed but uncertain. | F7.7, F7.8, F11.2 |

## Quantitative Evidence Audit

### Claim Audit Metrics

| Metric | Value |
|---|---:|
| total substantive claims audited | 64 |
| claims with field citations | 59 |
| claims explicitly labeled inference/assumption | 9 |
| claims explicitly labeled uncertainty | 11 |
| unsupported claims | 1 |
| role-overreach claims | 2 |
| over-strong claims | 4 |
| claims corrected after audit | 6 |
| unresolved audit blockers | 0 |

### Main Audit Findings

| Claim ID | Agent | Claim | Issue type | Severity | Correction |
|---|---|---|---|---|---|
| A1 | Developer | Redesign can resolve safeguard and ecological risks. | over-strong | major | Revised to "redesign can attempt to reduce risks, pending evidence." |
| A2 | Legal / Policy | Project is legally not approvable. | over-strong | minor | Revised to "not ready for final build approval under represented safeguards." |
| A3 | Government | Final approval must wait for regulatory requirements. | inference labeling | minor | Marked as governance inference. |
| A4 | Moderator | Environmental-flow proposal is inadequate. | over-strong | minor | Revised to "not sufficiently justified for approval as proposed." |
| A5 | Upstream Residents | Approval before resettlement is coercive. | inference labeling | minor | Marked as stakeholder-position inference. |
| A6 | Developer | Engineering issues are manageable. | unsupported as stated | major | Revised to "potentially manageable if studies resolve gaps." |

### Audit Decision

**Pass with revisions.**

No unresolved audit blocker remains after correction.

## Decision Authority Recommendation

### Recommendation

**Redesign.**

### Final Build Approval Status

**Deferred.**

### One-Sentence Rationale

The project addresses credible water-security, flood-control, irrigation, and energy needs, but final build approval should be deferred because ecological mitigation, resettlement, safeguard compliance, climate robustness, and downside economics remain unresolved.

### Decisive Benefits

| Benefit | Field IDs | Effect |
|---|---|---|
| Expected firm yield exceeds projected urban water gap. | F2.4, F2.5 | Supports continued consideration. |
| Flood peak reduction is meaningful for 1-in-20-year events. | F3.2 | Supports public benefit. |
| Hydropower provides flexible peaking energy. | F4.1-F4.3 | Adds benefit but is drought-sensitive. |
| Policy fit exists. | F9.5 | Supports government interest. |

### Unresolved Blockers

| Blocker | Type | Field IDs | Required resolution |
|---|---|---|---|
| Climate-adjusted hydrology incomplete | Evidence / safety | F6.5, F11.1 | Climate stress test for inflow, flood safety, yield, and BCR. |
| Fish passage and ecological flow uncertain | Ecological | F2.10, F7.8, F11.2 | Species-specific fish and flow assessment. |
| Resettlement and livelihood restoration incomplete | Social | F8.1-F8.7, F11.4 | Complete resettlement action and livelihood plan. |
| Independent EIA and safeguards incomplete | Legal/governance | F9.3, F9.6, F9.8 | Complete independent review and E&S management plan. |
| Downside economics weak | Financial | F5.2, F5.3, F11.6 | Update economics with P90, dry climate, sedimentation, and safeguards. |

### Score Matrix

| Dimension | Score 1-5 | Dissent range | Confidence | Main evidence |
|---|---:|---|---|---|
| water_supply_benefit | 4 | 3-4 | medium | F2.4, F2.5, F2.7 |
| flood_control_benefit | 3 | 3 | medium | F3.2-F3.5 |
| energy_benefit | 3 | 3-4 | medium | F4.1-F4.4 |
| economic_viability | 2 | 2-3 | medium | F5.2, F5.3 |
| engineering_feasibility | 3 | 2-3 | medium | F6.4-F6.7 |
| ecological_impact_acceptability | 1 | 1-2 | medium-high | F7.1-F7.8 |
| social_impact_acceptability | 1 | 1-2 | high | F8.1-F8.8 |
| legal_governance_readiness | 2 | 2 | high | F9.3-F9.8 |
| climate_robustness | 2 | 2 | medium | F2.7, F4.4, F11.1 |
| stakeholder_support | 2 | 1-3 | medium | F8.8, F10.1-F10.7 |
| evidence_confidence | 3 | 2-4 | medium | F11.1-F11.6 |

### Conditions

1. Complete climate-adjusted hydrology, flood-safety, drought-yield, and economic stress tests.
2. Redesign environmental-flow rules with species-specific ecological thresholds.
3. Complete independent fish-passage and spawning-habitat assessment.
4. Complete resettlement action plan, livelihood restoration budget, cultural-site treatment, and grievance mechanism.
5. Complete independent EIA review, biodiversity offset plan, and E&S management plan.
6. Update economic model with P90 cost, sedimentation, safeguards, and dry-climate assumptions.
7. Compare redesigned dam with non-dam portfolio under consistent assumptions.

### Minority Reports

| Agent/stakeholder | Dissenting concern | Status |
|---|---|---|
| Environmental NGO | Ecological harm may remain non-mitigable even after redesign. | unresolved |
| Upstream Affected Residents | Redesign without negotiated consent may still be unacceptable. | unresolved |
| Financier | Project is not finance-ready until safeguards and downside economics are resolved. | incorporated as condition |
| Legal / Policy | Final build approval should remain deferred until procedural readiness is achieved. | incorporated |

### Evidence Confidence

**Medium.**

## Baseline Outputs

### Single-Agent Baseline

Recommendation: **Defer final approval pending major revisions and additional studies.**

The single-agent output covers most major risks and gives a useful concise recommendation, but it compresses stakeholder conflict and does not include an audit/revision loop.

### MCDA Baseline

Recommendation: **Do not build as proposed; major redesign required.**

Weighted score: **2.34 / 5.00** using provisional weights.

The MCDA output is transparent but compresses safeguard, stakeholder, and ecological blockers into low scores.
