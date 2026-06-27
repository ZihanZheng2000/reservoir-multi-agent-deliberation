# Compact Run Summary — demo-003-cc

Case: SRD-003-cc — Gorge Peak Hydropower Project
Run folder: `artifacts/demo-003-cc/`
Run type: Claude Code compact run
Rubric version: v3 (three-layer)
Gold checklist: 5M/5S (from `artifacts/demo-003/protocols/evaluator-only-gold-checklist.md`)

---

## Multi-Agent Deliberation Result

### Recommendation

**Redesign toward the hybrid alternative (F0.5): run-of-river plus solar/storage.**

### Final Build Approval Status

**Deferred.** The project as proposed is not approvable. Approval could proceed only for the redesigned hybrid configuration after a full alternatives analysis confirms the hybrid's grid adequacy.

### Why This Result Emerged

The central conflict was not whether the grid needed peaking capacity — both energy and developer agents agreed it did — but whether this specific high-dam configuration on the last free-flowing gorge was justified given the existence of the hybrid alternative. The Ecologist and Environmental NGO required a formal alternatives analysis. The Climate Risk and Economist agents identified that the BCR drops below 1.0 under dry-climate and mitigation-cost conditions, removing the economic basis for approving the full dam. The hybrid alternative data in F5.6–F5.9 provided sufficient information for the Decision Authority to recommend Redesign toward the hybrid rather than a generic Defer.

Key deliberative moments: (1) Ecologist challenged whether fish passage was technically feasible given gorge geometry — the answer was no; (2) Economist identified that the downside BCR (0.92) fails the 1.0 threshold; (3) Moderator framed the conflict as "same grid need, lower river impact, lower cost" using the hybrid data; (4) Developer acknowledged the hybrid addresses grid need but requested transition credit for permitting investments.

### Expert Position Summary

| Agent | Position | Key evidence |
|---|---|---|
| Hydrologist | Hydropeaking creates 4:1 daily flow fluctuations that affect spawning and macroinvertebrates; impact not yet assessed for this species. | F2.7, F3.5, F8.1 |
| Dam Safety / Engineer | Technically feasible dam design; gorge geometry makes effective fish passage practically impossible; no structural blocker to construction but ecological design is unresolved. | F3.4 |
| Ecologist | The gorge is the last free-flowing segment in the basin; fish passage is technically difficult due to height and geometry; habitat loss is irreversible; requires full alternatives analysis. | F3.1, F3.2, F3.3, F3.4 |
| Climate Risk | Dry-year generation reduction of 28% under climate scenarios weakens the peaking reliability argument; carbon benefit is real but does not offset ecological costs on its own. | F2.6, F5.5, F8.4 |
| Economist / Finance | Base BCR 1.25 appears viable; downside BCR 0.92 falls below 1.0 under dry-climate and fish-mitigation constraints; hybrid alternative at USD 2.1B vs. USD 2.8B has a better cost profile. | F5.2, F5.7, F5.8 |
| Social / Resettlement | 620 households displaced; 8,400 downstream people depend on fisheries and tourism; benefit-sharing at 1.5% is insufficient to compensate for likely fishery and tourism losses. | F4.1, F4.2, F4.3 |
| Legal / Policy | Draft EIA submitted with narrow alternatives analysis criticized by regulator; downstream flow license not finalized; legal readiness is blocked. | F6.1, F6.3 |

### Stakeholder Position Summary

| Stakeholder | Position | Key evidence |
|---|---|---|
| Developer | Supports full dam; willing to discuss hybrid as a fallback if the regulatory process is blocked; requests permitting transition credit. | F7.1, F0.5 |
| Energy Ministry | Grid needs dispatchable renewable capacity; has not committed to this specific project or configuration. | F7.2 |
| Downstream Fishers | Strongly opposed; hydropeaking would destroy the fishery supporting their income; requests binding hydropeaking assessment before any approval. | F7.3, F4.2, F2.7 |
| Environmental NGO | Opposed to current design; the gorge is the last free-flowing segment; requests formal alternatives analysis including the hybrid option before any approval. | F7.4, F3.1, F3.2 |
| Local Government | Revenue sharing at 1.5% is too small if local tourism and fisheries decline; conditionally accepts the hybrid if local benefit-sharing is improved. | F7.5, F4.3 |
| Export Credit Agency / Financier | Will not finance without credible alternatives analysis and downstream livelihood protection. | F6.2, F8.2 |
| Upstream Affected Residents | 620 households displaced; requests livelihood restoration commitments regardless of which project configuration proceeds. | F4.1 |

---

## Moderator Conflict Map

| Conflict | Why it matters | Evidence |
|---|---|---|
| National grid need vs. location-specific harm | Grid needs peaking capacity, but the specific gorge site causes irreversible ecological harm; the hybrid provides comparable capacity at lower cost without the gorge. | F2.1–F2.3, F3.1, F5.6–F5.9 |
| BCR viability vs. downside conditions | Base BCR 1.25 supports study; downside BCR 0.92 falls below 1.0; the economic case depends on base-case assumptions holding. | F5.2, F8.4 |
| Benefit-burden mismatch | Urban grid benefits accrue nationally; 8,400 downstream people bear fishery and tourism costs; local electricity benefit is minimal. | F4.2, F4.4, F2.4 |
| Hydropeaking vs. downstream livelihoods | 4:1 daily flow fluctuations are the central operational threat to fishery livelihoods; impact has not been assessed for this river. | F2.7, F7.3, F8.1 |
| Narrow alternatives analysis vs. regulatory requirement | EIA alternatives analysis was criticized by the regulator as too narrow; approval without correcting this is a legal blocker. | F6.1 |

---

## Quantitative Evidence Audit

### Claim Audit Metrics

| Metric | Value |
|---|---:|
| Total substantive claims audited | 57 |
| Claims with field citations | 53 |
| Claims explicitly labeled inference/assumption | 9 |
| Claims explicitly labeled uncertainty | 10 |
| Unsupported claims | 1 |
| Role-overreach claims | 2 |
| Over-strong claims | 4 |
| Claims corrected after audit | 5 |
| Unresolved audit blockers | 0 |

### Main Audit Findings

| Claim ID | Agent | Claim | Issue type | Severity | Correction |
|---|---|---|---|---|---|
| A1 | Developer | Fish passage at dam height is feasible if designed properly. | over-strong | major | Revised to "technically difficult due to dam height and gorge geometry; feasibility is not confirmed." |
| A2 | Ecologist | The gorge fish passage is physically impossible. | over-strong | minor | Revised to "technically difficult; effectiveness for migratory species at this dam height is not demonstrated." |
| A3 | Economist | The hybrid alternative is economically superior in all scenarios. | inference | minor | Marked as inference; seasonal dispatch modeling not complete. |
| A4 | Social | 1.5% revenue sharing is inadequate to compensate fishery losses. | over-strong | minor | Revised to "likely inadequate given scale of fishery and tourism dependence; quantification is pending livelihood study." |
| A5 | Developer | Developer acknowledges gorge ecology risk. | role-overreach: developer accepted ecological conclusion without qualifying | minor | Corrected to: "Developer acknowledges regulatory concern; does not accept that fish passage is impossible." |

### Audit Decision

**Pass with revisions.**

The one unsupported claim (A1 after correction) is now a labeled inference. No unresolved audit blocker remains.

---

## Decision Authority Recommendation

### Recommendation

**Redesign toward hybrid alternative (F0.5).**

### Final Build Approval Status

**Deferred.** The project as proposed is not approvable. The hybrid configuration requires a full grid adequacy study before a Redesign approval can be issued.

### One-Sentence Rationale

The project addresses a genuine grid need, but the high-dam design fails on downside economics, irreversible ecological harm in the last gorge segment, and inadequate alternatives analysis; the hybrid alternative in F0.5 is a credibly superior option at lower cost and with no river impact that must be formally evaluated before any approval is issued.

### Decisive Benefits (retained)

| Benefit | Field IDs | Effect |
|---|---|---|
| 640 MW peaking capacity; 1,920 GWh annual generation. | F2.1, F2.2 | Addresses genuine grid peaking need. |
| Carbon benefit of 1.1 Mt CO2e/year vs. fossil peakers. | F5.5 | Real environmental benefit, but not location-specific. |
| Government-backed 25-year PPA proposed. | F5.3 | Revenue security if project proceeds in any configuration. |

### Unresolved Blockers (for current design)

| Blocker | Type | Field IDs | Required resolution |
|---|---|---|---|
| BCR falls to 0.92 under dry-climate and fish-mitigation constraints | Economic | F5.2, F8.4 | Full cost model including fish-mitigation and downside climate. |
| Irreversible habitat loss of last gorge segment; fish passage not confirmed | Ecological | F3.1, F3.2, F3.4 | Resolve through redesign to run-of-river configuration. |
| Benefit-burden mismatch: 8,400 downstream people bear costs, no local electricity benefit | Social | F4.2, F4.4 | Downstream livelihood assessment and benefit-sharing redesign. |
| EIA alternatives analysis too narrow; regulator criticism outstanding | Legal/governance | F6.1 | Full alternatives analysis including hybrid before any approval. |
| Downstream flow license not finalized | Legal | F6.3 | Finalize license for any project configuration. |

### Conditions for Redesign Approval (hybrid path)

1. Commission full grid adequacy study to confirm hybrid (120 MW run-of-river + 200 MW solar/storage) provides adequate seasonal dispatch capacity.
2. Complete downstream livelihood and hydropeaking impact study for current proposal as a reference baseline.
3. Redesign benefit-sharing to address fishery and tourism livelihood losses if hybrid proceeds.
4. Finalize downstream flow license under run-of-river operating rules.
5. Complete full EIA for the hybrid configuration with a proper alternatives analysis.

### Score Matrix (current high-dam proposal)

| Dimension | Score 1–5 | Dissent range | Confidence | Main evidence |
|---|---:|---|---|---|
| water_supply_benefit | 1 | 1 | high | F2.4, F2.5: no municipal or irrigation benefit |
| flood_control_benefit | 1 | 1 | high | F2.5: limited due to peaking operation |
| energy_benefit | 4 | 3–4 | medium | F2.1, F2.2, F5.3 |
| economic_viability | 2 | 2–3 | medium | F5.2: downside BCR 0.92 |
| engineering_feasibility | 3 | 3 | medium | F3.4: fish passage difficult |
| ecological_impact_acceptability | 1 | 1–2 | high | F3.1, F3.2, F3.3 |
| social_impact_acceptability | 1 | 1–2 | high | F4.2, F4.3: 8,400 people bear cost |
| legal_governance_readiness | 2 | 2 | high | F6.1, F6.3 |
| climate_robustness | 2 | 2–3 | medium | F2.6, F8.4 |
| stakeholder_support | 1 | 1–2 | high | F7.3, F7.4: opposed |
| evidence_confidence | 3 | 2–3 | medium | F8.1, F8.2 |

### Minority Reports

| Agent/stakeholder | Dissenting concern | Status |
|---|---|---|
| Developer | Redesign toward hybrid should credit permitting investment; transition support needed. | Noted; not incorporated as a decision condition. |
| Energy Ministry | Has not committed to this project or configuration; grid need is affirmed, not the specific project. | Incorporated: recommendation preserves the grid need while requiring configuration change. |
| Environmental NGO | Even the hybrid run-of-river component may affect the gorge; requires full EIA for hybrid before any approval. | Incorporated as condition 5. |

---

## Baseline Outputs

### Single-Agent Baseline

**Recommendation: Defer pending full alternatives analysis and downstream livelihood study.**

The single-agent output identifies the main problems (narrow EIA, downside BCR, hydropeaking threat) and recommends Defer. It does not produce a specific Redesign-toward-hybrid recommendation even though F5.6–F5.9 provide sufficient data to do so. It compresses stakeholder positions and does not separately identify the benefit-burden mismatch as a decision-critical issue.

### MCDA Baseline

**Weighted score: approximately 2.15 / 5.00**

**Recommendation: Do not build as proposed; major redesign or alternatives required.**

| Criterion | Score 1–5 |
|---|---:|
| water_supply_benefit | 1 |
| flood_control_benefit | 1 |
| energy_benefit | 5 |
| economic_viability | 2 |
| engineering_feasibility | 3 |
| ecological_impact_acceptability | 1 |
| social_impact_acceptability | 1 |
| legal_governance_readiness | 2 |
| climate_robustness | 2 |
| stakeholder_support | 2 |
| evidence_confidence | 3 |

MCDA reaches the correct direction. Limitations: does not identify the hybrid alternative specifically; does not express the Redesign-toward-hybrid pathway; compresses downstream livelihood concerns into social_impact_acceptability.
