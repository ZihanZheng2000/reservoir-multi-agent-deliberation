# Compact Run Summary — demo-004-cc

Case: SRD-004-cc — Lower Vale Flood Retention Reservoir
Run folder: `artifacts/demo-004-cc/`
Run type: Claude Code compact run
Rubric version: v3 (three-layer)
Gold checklist: 5M/5S (from `artifacts/demo-004/protocols/evaluator-only-gold-checklist.md`)

---

## Multi-Agent Deliberation Result

### Recommendation

**Phased emergency package now; defer final reservoir approval.**

### Final Build Approval Status

**Deferred.** Immediate non-structural protective measures are authorized now. Final reservoir approval is deferred pending climate-adjusted design, full geotechnical investigation, and complete safeguard review.

### Why This Result Emerged

The central tension was between the genuine and severe immediate flood risk (86,000 residents; two 1-in-50-year floods in five years) and the engineering and safeguard gaps that prevent safe reservoir approval. The Dam Safety agent established that concept-design-only engineering, variable foundation alluvium, and an emergency construction schedule are not sufficient bases for reservoir approval. The Social agent identified that 45-day emergency consultation for 180-household displacement does not meet standard safeguard requirements. The Moderator separated the immediate life-safety problem from the longer-term reservoir decision, producing the phased package as the resolution.

Key deliberative moments: (1) Dam Safety required that variable foundation alluvium must be resolved before any reservoir approval — not a minor issue; (2) Hydrologist flagged that the climate-adjusted flood estimate is incomplete and may change the design basis; (3) Emergency Agency stakeholder drew the distinction between downstream risk transfer from fast releases versus the risk of no reservoir; (4) Social agent raised the equity concern that low-income neighborhoods remain most exposed if only the reservoir is built without levee repair; (5) Moderator framed the recommendation as "act now on what is safe; defer what is not yet safe to approve."

### Expert Position Summary

| Agent | Position | Key evidence |
|---|---|---|
| Hydrologist | Flood risk is real and severe; climate-adjusted flood estimate is incomplete; downstream risk transfer from fast releases is a design dependency. | F2.1, F2.2, F2.3, F2.6, F3.3, F8.1 |
| Dam Safety / Engineer | Concept design with variable foundation alluvium and an emergency 3-year construction schedule is not approvable; dam safety standard requires full geotechnical and detailed design before construction authorization. | F3.1, F3.2, F3.5, F8.2 |
| Ecologist | No endemic species; seasonal bird habitat is affected; full EIA not complete; wetland restoration alternative (14 km²) should be included in the immediate package. | F4.2, F4.3, F4.4, F6.4 |
| Climate Risk | Climate-adjusted flood frequency may differ from the two 1-in-50-year events observed; design based on incomplete climate estimate is a long-term safety risk. | F3.3, F8.1 |
| Economist / Finance | Avoided damage estimate (USD 1.6B over 30 years) is directionally strong; climate-adjusted avoided damage is not yet estimated; emergency funding window (24 months) adds urgency. | F6.1, F6.2, F6.3, F6.5 |
| Social / Resettlement | 45-day emergency consultation for 180 displaced households is below standard safeguard requirements; low-income downstream neighborhoods remain exposed without levee repair; upstream landowner acquisition is legally contested. | F5.1, F5.3, F5.4, F5.5, F8.3 |
| Legal / Policy | Emergency review is allowed but full EIA is not complete; emergency acquisition under compressed timeline is legally contested; recommend phased approach that does not compromise legal standing. | F6.4, F5.3, F8.3 |

### Stakeholder Position Summary

| Stakeholder | Position | Key evidence |
|---|---|---|
| Flood-Hit Towns | Strongly support immediate action; cannot wait another decade for protection. | F7.1, F2.2 |
| Upstream Landowners | Oppose emergency land acquisition; argue emergency powers are being used to bypass adequate review. | F7.2, F5.3, F8.3 |
| Environmental Group | Wetland restoration and zoning should be part of the immediate package, not an afterthought; full EIA should be completed before final reservoir decision. | F7.3, F4.3, F6.4 |
| Emergency Agency / Government | Immediate risk reduction is necessary; operations must not transfer risk downstream; supports phased approach with immediate non-structural measures. | F7.4, F2.6, F8.4 |
| Developer / Constructor | Ready to mobilize on emergency schedule but requires clear scope before committing to 3-year compressed timeline. | F3.5 |
| Local Government | Supports urgent action; concerned that low-income neighborhoods are inadequately protected if only the reservoir is built without levee repair. | F5.5 |
| Financier | Emergency disaster recovery fund available for 24 months; full fund release requires legal land acquisition process and environmental review completion. | F6.5 |

---

## Moderator Conflict Map

| Conflict | Why it matters | Evidence |
|---|---|---|
| Urgency vs. engineering readiness | Flood risk is real and severe, but concept-design-only with variable alluvium is not safe to approve; fast-tracking could create a dam safety incident. | F3.1, F3.2, F3.5 |
| Emergency schedule vs. standard safety timeline | 3-year emergency schedule vs. standard 6-year timeline increases quality-control risk; compressed timelines have historically contributed to construction defects. | F3.5 |
| Emergency powers vs. safeguard requirements | 45-day consultation for 180 displaced households and contested land acquisition may not meet standard requirements; legal challenge risk. | F5.3, F5.4, F8.3 |
| Downstream risk transfer vs. flood reduction benefit | Fast reservoir releases could concentrate flood peaks downstream if operations fail; risk is transferred, not eliminated. | F2.6, F8.4 |
| Reservoir-only protection vs. equity | Low-income downstream neighborhoods remain exposed if levee repair and non-structural measures are not included in the package. | F5.5, F2.5 |

---

## Quantitative Evidence Audit

### Claim Audit Metrics

| Metric | Value |
|---|---:|
| Total substantive claims audited | 55 |
| Claims with field citations | 51 |
| Claims explicitly labeled inference/assumption | 8 |
| Claims explicitly labeled uncertainty | 9 |
| Unsupported claims | 1 |
| Role-overreach claims | 1 |
| Over-strong claims | 3 |
| Claims corrected after audit | 4 |
| Unresolved audit blockers | 0 |

### Main Audit Findings

| Claim ID | Agent | Claim | Issue type | Severity | Correction |
|---|---|---|---|---|---|
| A1 | Hydrologist | Climate-adjusted flood estimate confirms current design is adequate. | unsupported | major | Revised to "climate-adjusted estimate is not yet complete; design adequacy under future conditions cannot be confirmed." |
| A2 | Dam Safety | Variable alluvium means the dam cannot be safely built at this location. | over-strong | minor | Revised to "variable alluvium requires full geotechnical investigation before foundation design can be confirmed; this is not yet done." |
| A3 | Flood Towns | Emergency approval now will not create safety issues. | over-strong | minor | Revised to "emergency approval may be achievable with appropriate conditions, but current engineering gaps create unresolved safety risk." |
| A4 | Developer | Standard 6-year timeline is too long given the emergency. | inference | minor | Marked as inference; whether a compressed timeline can maintain quality control depends on scope and resourcing not yet defined. |

### Audit Decision

**Pass with revisions.**

No unresolved audit blocker remains. The key correction (A1) prevents an unsupported claim from appearing in the deliberation as a factual basis for approval.

---

## Decision Authority Recommendation

### Recommendation

**Phased emergency package now; defer final reservoir approval.**

### Final Build Approval Status

**Deferred for final reservoir.** Immediate non-structural protective measures authorized.

### One-Sentence Rationale

The immediate life-safety risk to 86,000 residents justifies urgent protective action, but final reservoir approval is premature given concept-design-only engineering, incomplete climate adjustment, variable foundation alluvium, and compressed safeguard processes that do not yet meet standard requirements.

### Immediate Package (authorized now)

| Action | Basis | Effect |
|---|---|---|
| Emergency levee repair for low-income downstream neighborhoods. | F5.5, F2.5 | Reduces immediate flood exposure for most vulnerable communities. |
| Early warning system deployment. | F2.5 | Reduces fatality risk for current flood season. |
| Floodplain zoning emergency order. | F2.5 | Limits new construction exposure. |
| Wetland restoration feasibility study. | F4.3, F7.3 | Begins longer-term risk reduction without construction risk. |

### Conditions for Final Reservoir Approval

| Condition | Type | Field IDs | Required action |
|---|---|---|---|
| Climate-adjusted flood estimate | Engineering/safety | F3.3, F8.1 | Complete and use climate-adjusted design flood before finalizing reservoir and spillway dimensions. |
| Full geotechnical investigation | Engineering/safety | F3.2, F8.2 | Complete foundation investigation and confirm treatment before detailed design authorization. |
| Revised construction schedule | Engineering/safety | F3.5 | Develop a construction timeline with realistic quality-control standards; 3-year emergency schedule requires independent safety review. |
| Complete safeguard review | Social/legal | F5.1, F5.4, F8.3 | Complete full consultation process for 180 displaced households; resolve land acquisition legal challenge. |
| Downstream risk transfer assessment | Engineering | F2.6, F8.4 | Complete operating-rule analysis to confirm releases will not create downstream peak amplification. |
| Full EIA completion | Environmental/governance | F6.4 | Complete EIA including bird habitat and wetland restoration options. |

### Score Matrix

| Dimension | Score 1–5 | Dissent range | Confidence | Main evidence |
|---|---:|---|---|---|
| water_supply_benefit | 1 | 1 | high | no water supply component |
| flood_control_benefit | 4 | 3–4 | medium | F2.3: 38% reduction for 1-in-50 event; climate adjustment pending |
| energy_benefit | 1 | 1 | high | no hydropower |
| economic_viability | 3 | 3–4 | medium | F6.2: USD 1.6B avoided damage; climate-adjusted not estimated |
| engineering_feasibility | 2 | 1–2 | medium | F3.1, F3.2, F3.5: concept design, alluvium, compressed schedule |
| ecological_impact_acceptability | 3 | 3 | medium-high | F4.4: no endemic; seasonal bird habitat affected |
| social_impact_acceptability | 2 | 2–3 | medium | F5.1, F5.4, F5.5: contested acquisition, shortened consultation, equity gap |
| legal_governance_readiness | 2 | 2 | medium | F6.4, F8.3: EIA incomplete, acquisition contested |
| climate_robustness | 2 | 2–3 | low | F3.3: climate-adjusted design not complete |
| stakeholder_support | 3 | 2–4 | medium | F7.1: strong from flood towns; opposed by landowners |
| evidence_confidence | 2 | 2–3 | medium | F8.1–F8.4: several key uncertainties unresolved |

### Minority Reports

| Agent/stakeholder | Dissenting concern | Status |
|---|---|---|
| Dam Safety | Even the phased immediate package carries risk if it is interpreted as implying reservoir approval in 24 months regardless of study outcomes; studies must complete before any approval commitment. | Incorporated: recommendation defers final reservoir without timeline commitment. |
| Upstream Landowners | Emergency acquisition process remains legally contested; phased approach does not resolve their land rights concern. | Noted; legal resolution required as a condition for final approval. |
| Environmental Group | Wetland restoration and zoning should be implemented before final reservoir decision is even considered, not as parallel tracks. | Partially incorporated: restoration feasibility study is in immediate package. |

### Evidence Confidence

**Medium-low for reservoir design readiness; medium-high for flood risk justification.**

---

## Baseline Outputs

### Single-Agent Baseline

**Recommendation: Emergency measures now; defer final reservoir approval.**

The single-agent output correctly identifies the phased approach and lists the key gaps (climate-adjusted design, geotechnical investigation, safeguard review). It does not separately identify the downstream risk transfer concern or the low-income equity gap. It does not flag the legal basis of the land acquisition contest as a separate risk. Recommendation direction is correct but less specific on immediate-package content.

### MCDA Baseline

**Weighted score: approximately 2.51 / 5.00**

**Recommendation: Redesign / Defer, with emergency measures.**

| Criterion | Score 1–5 |
|---|---:|
| water_supply_benefit | 1 |
| flood_control_benefit | 4 |
| energy_benefit | 1 |
| economic_viability | 3 |
| engineering_feasibility | 2 |
| ecological_impact_acceptability | 3 |
| social_impact_acceptability | 2 |
| legal_governance_readiness | 2 |
| climate_robustness | 2 |
| stakeholder_support | 3 |
| evidence_confidence | 2 |

MCDA scores emergency context as a higher flood-control score but cannot express the immediate-vs-deferred-reservoir sequencing. Recommendation direction is broadly correct; phased package structure is not captured.
