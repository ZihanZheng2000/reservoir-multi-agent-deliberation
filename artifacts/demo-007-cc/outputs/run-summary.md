# Compact Run Summary — demo-007-cc

Case: SRD-007-cc — Mara Bend Irrigation Reservoir
Run folder: `artifacts/demo-007-cc/`
Run type: Claude Code compact run
Rubric version: v3 (three-layer)
Gold checklist: 4M/6S (from `artifacts/demo-007/protocols/evaluator-only-gold-checklist.md`)

---

## Multi-Agent Deliberation Result

### Recommendation

**Build with conditions; revert to Defer if livelihood restoration plan is not complete within 9 months.**

### Final Build Approval Status

**Conditional construction approval issued.** The livelihood restoration section of the resettlement action plan must be completed and approved within 9 months; if not, approval reverts to Defer pending completion.

### Why This Result Emerged

SRD-007 is the near-tipping-point case. The system's central task was to distinguish the livelihood restoration gap — which is near-complete and resolvable within months — from the EAP, fish passage, geotechnical, and spillway gaps, which are pre-construction and pre-detailed-design requirements but not approval blockers at feasibility stage.

The decisive deliberative structure: (1) the Development Lender stakeholder identified the livelihood plan as the single financing block; (2) the Social agent confirmed that the resettlement housing section is complete and the livelihood section is near-complete, not fundamentally absent; (3) the Dam Safety agent established that the EAP at outline stage means a full EAP must be completed before construction can start, not before feasibility approval; (4) the Ecologist confirmed that fish passage is technically feasible and the effectiveness assessment can be completed in parallel with construction design; (5) the Moderator framed the swing condition: livelihood plan is the only financing blocker; the rest are pre-construction or pre-design conditions, not pre-approval blockers.

The system produced a time-conditioned recommendation rather than a generic Defer, demonstrating that it can distinguish a near-complete safeguard gap from a fundamental project flaw.

### Expert Position Summary

| Agent | Position | Key evidence |
|---|---|---|
| Hydrologist | Irrigation reliability improves from 55% to 79%; falls to 61% in 1-in-20-year drought — modest but real improvement; environmental flow adequacy at 20% is contested. | F2.2, F2.4, F2.5 |
| Dam Safety / Engineer | Feasibility design complete; geotechnical 85% complete with one abutment zone outstanding — this must be resolved before detailed design, not before feasibility approval; EAP is at outline stage and a full EAP is required before construction can begin (dam safety standard requirement). | F3.2, F3.3, F3.6, F9.6 |
| Ecologist | Fish passage is technically feasible for the species of concern; effectiveness assessment not yet complete — this is a mitigation credibility issue, not a design blocker; downstream wetland preliminary study suggests manageable. | F4.2, F4.4, F4.5, F9.3 |
| Climate Risk | Spillway design uses historical inflow data; climate-adjusted update is required before detailed design; this is a future precondition, not a feasibility-stage blocker. | F3.5, F9.4 |
| Economist / Finance | BCR 1.08 base case; 0.97 under P90 and dry-climate combined — falls below 1.0 under downside; economic viability is marginally confirmed at base case; the margin is thin and the livelihood plan gap adds cost uncertainty. | F6.3, F9.2 |
| Social / Resettlement | Resettlement housing and compensation are complete and independently reviewed; livelihood restoration budget and timeline are not finalized — this is the key identified gap; near-complete, not fundamentally absent. | F5.3, F5.4, F9.1 |
| Legal / Policy | Final EIA 85% complete; preliminary conclusion positive with livelihood gap noted; construction permit pending EIA completion; financing explicitly conditioned on complete resettlement action plan including livelihood section. | F7.1, F7.2, F7.4 |

### Stakeholder Position Summary

| Stakeholder | Position | Key evidence |
|---|---|---|
| Irrigation Association | Irrigation reliability is critical; project is needed and technically sound; support for construction approval. | F8.1 |
| Urban Water Authority | Supplemental urban supply benefit is real but modest; supportive but not critical for urban supply alone. | F8.2 |
| Upstream-Affected Households | Conditionally supportive — will only accept if the livelihood restoration plan specifies what they will receive, when, and how disputes will be resolved. | F8.3, F5.7 |
| Downstream Farmers | Require binding environmental flow rules before accepting changes to seasonal flood patterns. | F8.4 |
| Environmental Group | Fish species and wetland risks are manageable with proposed mitigation; effectiveness assessments must be completed before construction starts. | F8.5 |
| Development Lender | Project is nearly financeable; the remaining blocker is the incomplete livelihood restoration section; will disburse when this section is complete. | F8.6, F7.4 |
| Local Government | Aligns with national irrigation policy; supports approval with the understanding that affected households' livelihoods are addressed. | F7.3 |

---

## Moderator Conflict Map

| Conflict | Why it matters | Resolution |
|---|---|---|
| Livelihood plan gap: financing blocker vs. near-complete | Lender will not disburse; affected households withhold conditional support — but the plan is near-complete, not fundamentally absent | Time-conditioned approval: 9-month completion window; revert to Defer if not met |
| EAP at outline stage: construction condition vs. feasibility blocker | Dam safety standard requires full EAP before construction, not before feasibility approval; this is a real condition but not a pre-approval blocker | EAP completion as pre-construction condition, not as a reason to defer feasibility approval |
| BCR 0.97 under downside: failing threshold vs. marginal case | BCR falls below 1.0 under P90 + dry climate; thin margin, but base case (1.08) is above threshold; project is marginal, not failing | Approve base case; note downside limitation as condition on livelihood plan cost integration |
| Fish passage effectiveness: mitigation gap vs. construction blocker | Effectiveness not assessed for species of concern; feasibility is confirmed; this is a credibility condition, not a design blocker | Effectiveness assessment before construction start, not before feasibility approval |
| Environmental flow adequacy: contested vs. confirmed | 20% minimum flow is contested by downstream ecology assessment; preliminary wetland study is manageable | Binding environmental flow rules as a condition before commissioning |

---

## Quantitative Evidence Audit

### Claim Audit Metrics

| Metric | Value |
|---|---:|
| Total substantive claims audited | 62 |
| Claims with field citations | 58 |
| Claims explicitly labeled inference/assumption | 10 |
| Claims explicitly labeled uncertainty | 12 |
| Unsupported claims | 0 |
| Role-overreach claims | 1 |
| Over-strong claims | 4 |
| Claims corrected after audit | 5 |
| Unresolved audit blockers | 0 |

### Main Audit Findings

| Claim ID | Agent | Claim | Issue type | Severity | Correction |
|---|---|---|---|---|---|
| A1 | Irrigation Association | Project is financially sound and will clearly deliver returns. | over-strong | major | Revised to "BCR 1.08 base case; 0.97 under downside; financially marginal, not clearly sound." |
| A2 | Economist | BCR below 1.0 under downside means the project should not proceed. | over-strong | minor | Revised to "BCR falling below 1.0 under downside is a concern to note and monitor, not a standalone blocker given that base-case BCR is above 1.0." |
| A3 | Dam Safety | EAP outline is sufficient for approval purposes. | over-strong | major | Revised to "full EAP is required before construction; outline is acceptable for feasibility review but not for construction authorization." |
| A4 | Social | Livelihood plan is complete. | over-strong | major | Revised to "livelihood restoration section is not complete; housing and compensation sections are complete and reviewed." |
| A5 | Environmental Group | Fish passage effectiveness can be assumed as adequate given feasibility confirmation. | role-overreach / over-strong | minor | Revised to "feasibility confirmed for the species of concern; effectiveness requires assessment before construction." |

### Audit Decision

**Pass with revisions.**

The three major corrections (A1, A3, A4) are essential: A4 corrects an over-strong claim that mischaracterizes the status of the key swing condition; A3 prevents a safety gap from being inadvertently closed by a premature assertion; A1 prevents the BCR from being overstated. No unresolved blocker remains.

---

## Decision Authority Recommendation

### Recommendation

**Build with conditions; revert to Defer if livelihood restoration plan is not complete within 9 months.**

### Final Build Approval Status

**Conditional construction approval.** The construction permit may be issued; first disbursement requires the complete resettlement action plan including livelihood section.

### One-Sentence Rationale

The project addresses a credible irrigation need with most safeguards substantially complete, and the remaining blocker — the livelihood restoration section — is near-complete and resolvable within months; a time-conditioned Build-with-conditions is more specific than a generic Defer and prevents the project from being held indefinitely on a near-complete gap.

### Decisive Benefits

| Benefit | Field IDs | Effect |
|---|---|---|
| Irrigation reliability improvement from 55% to 79% in normal years. | F2.2 | Addresses credible agricultural need. |
| Dry-year improvement from 44% to 61% — meaningful even if modest. | F2.4 | Real benefit even in stress conditions. |
| BCR 1.08 in base case; above 1.0. | F6.3 | Economic viability confirmed at base case. |
| Resettlement housing and compensation sections complete and independently reviewed. | F5.3 | Most of the safeguard is already done. |
| Development lender states project is "nearly financeable." | F8.6 | Financing is conditionally available. |

### Conditions

| Condition | Type | Field IDs | Required before | Revert trigger |
|---|---|---|---|---|
| Complete livelihood restoration section of resettlement action plan | Social / financing | F5.4, F9.1 | First disbursement; within 9 months | Yes — if not complete in 9 months, approval reverts to Defer |
| Complete full EAP | Dam safety standard | F3.6 | Construction start | No — if EAP is delayed, construction start is delayed, not the approval |
| Complete geotechnical borings for one abutment zone | Engineering | F3.3, F9.6 | Detailed design start | No — pre-detailed-design condition |
| Complete fish passage effectiveness assessment | Ecological | F4.4, F9.3 | Construction start | No — construction start condition |
| Write binding environmental flow rules into operating license | Ecological/governance | F2.5, F8.4 | Commissioning | No — commissioning condition |
| Update climate-adjusted spillway estimate | Engineering | F3.5, F9.4 | Detailed design start | No — pre-detailed-design condition |

### Score Matrix

| Dimension | Score 1–5 | Dissent range | Confidence | Main evidence |
|---|---:|---|---|---|
| water_supply_benefit | 3 | 3–4 | medium | F2.2, F2.3: irrigation + urban supply |
| flood_control_benefit | 1 | 1 | high | no flood control component |
| energy_benefit | 2 | 1–2 | medium | F1: small hydropower secondary benefit |
| economic_viability | 3 | 2–3 | medium | F6.3: 1.08 base; 0.97 downside |
| engineering_feasibility | 3 | 3 | medium | F3.3, F3.5: mostly complete with two pre-design gaps |
| ecological_impact_acceptability | 3 | 3 | medium | F4.2, F4.4: manageable; effectiveness assessment pending |
| social_impact_acceptability | 3 | 2–3 | medium | F5.3, F5.4: housing complete; livelihood incomplete |
| legal_governance_readiness | 3 | 3 | medium | F7.1, F7.4: EIA 85%; lender condition unmet |
| climate_robustness | 3 | 2–3 | medium | F9.4: spillway update pending |
| stakeholder_support | 3 | 3 | medium | F5.7: 61% support; conditional upstream |
| evidence_confidence | 3 | 3 | medium | F9.1–F9.6: several conditions near-complete |

Weighted score (provisional): **2.82 / 5.00** (marginal viable; consistent with tipping-point case)

### Minority Reports

| Agent/stakeholder | Dissenting concern | Status |
|---|---|---|
| Upstream-Affected Households | Construction approval before livelihood plan is final is premature regardless of the 9-month window; the plan should be complete before any construction activity near the displacement zone. | Noted; incorporated as requirement that disbursement is conditioned on livelihood plan completion. |
| Downstream Farmers | Binding environmental flow rules must be agreed before approval, not before commissioning. | Noted; recommendation preserves this as a commissioning condition but does not require it before construction approval. |
| Environmental Group | Fish passage effectiveness assessment should be required before construction start, not during construction design phase. | Incorporated as a pre-construction-start condition. |

### Evidence Confidence

**Medium.** Near-complete safeguards mean the evidence base is substantial; the residual uncertainty is the livelihood plan and BCR downside margin.

---

## Baseline Outputs

### Single-Agent Baseline

**Recommendation: Defer until livelihood plan and economic review are complete.**

The single-agent result correctly identifies the livelihood plan as the key gap and recommends Defer. However, it produces a generic Defer without specifying the 9-month window, the revert trigger, or the hierarchy of conditions (which are pre-construction vs. pre-commissioning vs. pre-design). It does not produce the time-conditioned Build-with-conditions pathway that the gold checklist identifies as the preferred output. This is the case where the multi-agent added value on Decision Usefulness is most pronounced.

### MCDA Baseline

**Weighted score: approximately 2.52 / 5.00**

**Recommendation: Redesign or Defer; marginally viable.**

| Criterion | Score 1–5 |
|---|---:|
| water_supply_benefit | 3 |
| flood_control_benefit | 1 |
| energy_benefit | 2 |
| economic_viability | 2 |
| engineering_feasibility | 3 |
| ecological_impact_acceptability | 3 |
| social_impact_acceptability | 2 |
| legal_governance_readiness | 3 |
| climate_robustness | 2 |
| stakeholder_support | 3 |
| evidence_confidence | 3 |

MCDA produces a Redesign/Defer output because low social_impact_acceptability (livelihood gap) drives the score down. It cannot express the time-conditioned Build-with-conditions path. Limitation: the score compresses the near-complete vs. fundamentally-absent distinction into a single criterion value.
