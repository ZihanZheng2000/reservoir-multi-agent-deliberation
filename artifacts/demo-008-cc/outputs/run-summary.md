# Compact Run Summary — demo-008-cc

Case: SRD-008-cc — Cascada Gorge Hydropower Project
Run folder: `artifacts/demo-008-cc/`
Run type: Claude Code compact run
Rubric version: v3 (three-layer)
Gold checklist: 5M/5S (from `artifacts/demo-008/protocols/evaluator-only-gold-checklist.md`)

---

## Multi-Agent Deliberation Result

### Recommendation

**Do not build; pursue wind portfolio alternative (F0.5).**

### Final Build Approval Status

**Rejected.** The project fails independently on economics, endemic species extinction, and indigenous consent. None of these three objections can be resolved by project modification, including dam height reduction. The wind portfolio alternative should be advanced to full grid dispatch modeling and, if confirmed adequate, treated as the replacement investment.

### Why This Result Emerged

SRD-008 is the benchmark's Do not build case. The decisive deliberative contribution was explicitly ruling out the Redesign path — a smaller dam still fails on all three core objections. The Ecologist established that fish passage is physically impossible at any height in this canyon geometry and that any inundation eliminates the minimum viable habitat for both endemic species. The Legal agent established that the indigenous community's FPIC is withheld on the gorge itself, not on the dam height. The Economist established that the base-case BCR of 0.94 fails independently of any downside assumption.

The moderator asked the developer directly: "Does the revenue-sharing increase resolve the indigenous consent?" The Developer acknowledged it does not — the indigenous community's formal objection is based on the gorge as ancestral territory, not on the revenue percentage. The Evidence Auditor flagged any suggestion that revenue sharing could be a path to consent as unsupported.

The system correctly identifies that the Redesign path (F0.3) does not fix any of the three core objections, and rules it out explicitly.

### Expert Position Summary

| Agent | Position | Key evidence |
|---|---|---|
| Hydrologist | No municipal water or irrigation benefit; 5:1 daily flow fluctuations from peaking operation will disrupt downstream spawning and macroinvertebrates; remote upper basin provides no flood control. | F2.4, F2.5, F2.7 |
| Dam Safety / Engineer | 145-meter arch dam in steep canyon is technically constructible; transmission line design is feasible; no safety blocker on the dam side — but the project fails on other grounds. | F5.1, F3.1 |
| Ecologist | Two fish species endemic to this river system with no populations elsewhere; fish passage is technically impossible at any dam height due to canyon walls and geometry; any inundation eliminates minimum viable habitat; endemic species extinction is certain if any dam is built on this gorge; Ramsar-listed canyon wetland would constitute a reportable loss. | F3.2, F3.3, F3.4, F3.5 |
| Climate Risk | Dry-year generation reduction of 33%; no power purchase agreement signed; revenue is based on forecast market prices; actual BCR may be lower than reported. | F2.6, F5.4, F8.1 |
| Economist / Finance | BCR 0.94 in the base case — fails before any downside assumption; falls to 0.71 under P90 cost and high-sedimentation; sedimentation at 1.8%/year reduces generation by 25% over 30 years and is not reflected in the headline BCR; wind portfolio BCR is 1.68 at 42% lower capital cost. | F5.3, F5.5, F5.7, F5.8 |
| Social / Resettlement | 240 households displaced; indigenous community of 85 households has formally and publicly withheld FPIC; no FPIC process was conducted before project submission; revenue-sharing offer was formally rejected; 1,800 people depend on canyon tourism, sport fishing, and river recreation — their economic impact was excluded from the BCR. | F4.3, F4.6, F4.4, F7.4 |
| Legal / Policy | No FPIC process completed; indigenous formal objection filed with national human rights commission; legal challenge filed on domestic water-use permit; export credit agency paused pending FPIC compliance assessment; EIA alternatives analysis excluded wind/solar options — criticized by regulator and NGOs; EIA rejected on first submission. | F6.3, F6.1, F6.2, F6.4, F6.5 |

### Stakeholder Position Summary

| Stakeholder | Position | Key evidence |
|---|---|---|
| Project Developer | Willing to increase revenue-sharing fund; proposes continuing. | F7.1 |
| Energy Ministry | Dispatchable renewable capacity is a policy priority; has not committed to this specific project or location. | F7.2 |
| Indigenous Community | "We have not consented and will not consent. This gorge is our ancestral territory. No revenue offer changes that." Formal FPIC withheld; objection filed with national human rights commission. | F7.3, F4.3 |
| River Tourism Association | 1,800 livelihoods at stake; economic impact study excluded them entirely. | F7.4, F4.4 |
| Environmental NGO | Endemic species will be extinct in this river system; fish passage is physically impossible at 145 meters; there is no mitigation for permanent extinction. | F7.5, F3.2, F3.3 |
| Export Credit Agency | Cannot finance without completed FPIC and credible alternatives analysis; both are absent. | F7.6, F6.4 |
| Downstream Communities | Depends on canyon recreation and fisheries; peaking operation 5:1 fluctuations are unacceptable. | F2.7, F4.4 |

---

## Moderator Conflict Map

| Conflict | Why it matters | Resolution |
|---|---|---|
| Revenue sharing increase vs. indigenous consent | Developer proposes increasing revenue sharing; indigenous community states the gorge is ancestral territory and no revenue offer changes consent | Revenue sharing is not a path to FPIC; consent is about the gorge, not the revenue percentage |
| BCR 0.94 vs. "clean energy" framing | Developer and Ministry frame the project as clean energy policy; BCR fails before any downside assumption independently | Economic failure is independent of the energy framing; renewable designation does not substitute for positive BCR |
| Redesign option vs. core objections | A smaller dam might appear to reduce ecological impact | Fish passage is physically impossible at any height in this canyon geometry; endemic habitat loss occurs at any inundation level; indigenous consent is about the gorge itself; Redesign does not resolve any of the three core objections |
| Wind portfolio adequacy vs. hydropower peaking | Developer argues grid needs dispatchable hydropower; wind portfolio alternative exists at BCR 1.68, 42% lower cost | Grid modeling confirms adequate reserve margin; wind portfolio peak-season dispatch model not fully complete but preliminary result is positive |
| Tourism livelihood vs. project EIS | River tourism association's 1,800 livelihoods were excluded from economic impact study | Exclusion means BCR 0.94 may overstate the project's economic case further than acknowledged |

---

## Quantitative Evidence Audit

### Claim Audit Metrics

| Metric | Value |
|---|---:|
| Total substantive claims audited | 58 |
| Claims with field citations | 55 |
| Claims explicitly labeled inference/assumption | 9 |
| Claims explicitly labeled uncertainty | 8 |
| Unsupported claims | 1 |
| Role-overreach claims | 1 |
| Over-strong claims | 3 |
| Claims corrected after audit | 4 |
| Unresolved audit blockers | 0 |

### Main Audit Findings

| Claim ID | Agent | Claim | Issue type | Severity | Correction |
|---|---|---|---|---|---|
| A1 | Developer | Increased revenue sharing can address indigenous community concerns and open a path to consent. | unsupported | major | Revised to "indigenous community has formally and publicly stated that no revenue offer changes their consent; this claim is unsupported by the scenario evidence." |
| A2 | Energy Ministry | The grid's need for dispatchable renewable power justifies this specific project at this location. | over-strong | major | Revised to "grid needs dispatchable renewable capacity; the Energy Ministry has not committed to this project or location; the grid need is not location-specific." |
| A3 | Ecologist | Fish passage is completely impossible at any dam anywhere in this river system. | over-strong | minor | Revised to "fish passage is technically impossible at 145 meters in this canyon geometry; this conclusion applies to the proposed dam and any dam of comparable height on this gorge segment." |
| A4 | Legal | The domestic legal challenge will definitely prevail and block the permit. | over-strong | minor | Revised to "legal challenge has been filed; outcome is uncertain; independent of the legal outcome, the export credit agency is paused pending FPIC compliance." |

### Audit Decision

**Pass with revisions.**

The major corrections A1 and A2 are essential. A1 prevents a revenue-sharing increase from appearing as a credible path to consent in the deliberation record. A2 prevents the Energy Ministry's policy priority from being presented as project-specific authorization.

---

## Decision Authority Recommendation

### Recommendation

**Do not build; pursue wind portfolio alternative (F0.5).**

### Final Build Approval Status

**Rejected.** The project fails on three independent and non-resolvable grounds.

### One-Sentence Rationale

The project fails independently on negative base-case economics (BCR 0.94), certain endemic species extinction with no mitigation path, and formally withheld indigenous consent that is about the gorge itself and cannot be resolved by project modification; the wind portfolio alternative at BCR 1.68 and 42% lower capital cost provides the same grid capacity without any of these objections.

### Three Independent Grounds for Rejection

| Ground | Field IDs | Why Redesign does not resolve it |
|---|---|---|
| BCR 0.94 in base case; 0.71 under P90 + high-sedimentation | F5.3, F5.5 | A smaller dam reduces generation; BCR would be worse, not better. |
| Two endemic fish species; extinction certain; fish passage physically impossible at any height in this canyon geometry | F3.2, F3.3 | Any inundation eliminates minimum viable habitat; canyon walls prevent fish passage at any height. |
| Indigenous FPIC formally and publicly withheld; consent is about the gorge, not the dam height; revenue offer formally rejected | F4.3, F4.6, F6.3 | Redesign does not change the sacred and ancestral nature of the gorge; consent is about the location, not the configuration. |

### Recommended Next Steps

| Action | Field IDs | Rationale |
|---|---|---|
| Advance wind portfolio (F0.5) to full seasonal dispatch grid model. | F5.6, F5.9, F8.4 | Preliminary grid modeling is positive; full seasonal model required to confirm peak adequacy before committing the investment. |
| Protect endemic fish habitat as part of wind portfolio environmental conditions. | F3.2 | Even without the dam, the gorge ecosystem protection should be formalized. |
| Engage with indigenous community on co-management of the canyon as an outcome of rejecting the dam. | F4.3, F7.3 | Rejection of the dam may create an opportunity for a formal co-management agreement. |

### Score Matrix

| Dimension | Score 1–5 | Dissent range | Confidence | Main evidence |
|---|---:|---|---|---|
| water_supply_benefit | 1 | 1 | high | F2.4, F2.5: none |
| flood_control_benefit | 1 | 1 | high | F2.5: none |
| energy_benefit | 3 | 2–3 | medium | F2.1, F2.2: real capacity; no PPA signed |
| economic_viability | 1 | 1 | high | F5.3: BCR 0.94 base; 0.71 downside |
| engineering_feasibility | 3 | 3 | medium | technically constructible; not the constraint |
| ecological_impact_acceptability | 1 | 1 | high | F3.2, F3.3: endemic extinction; no mitigation |
| social_impact_acceptability | 1 | 1 | high | F4.3, F4.6: FPIC formally withheld |
| legal_governance_readiness | 1 | 1 | high | F6.1, F6.3, F6.4: EIA rejected, FPIC absent, ECE paused |
| climate_robustness | 2 | 1–2 | medium | F2.6: 33% dry-year reduction; no PPA |
| stakeholder_support | 1 | 1 | high | F7.3, F7.5, F7.6: indigenous, NGO, ECE all opposed |
| evidence_confidence | 4 | 4 | high | F8.1–F8.4: key facts are confirmed, not uncertain |

### Minority Reports

| Agent/stakeholder | Dissenting concern | Status |
|---|---|---|
| Developer | Requests transition support for permitting costs; notes that wind portfolio adequacy is not fully confirmed. | Noted; wind portfolio grid adequacy study recommended as next step; transition support is outside this recommendation's scope. |
| Energy Ministry | Policy priority for dispatchable renewable capacity should be reflected in the decision; not a commitment to this project. | Incorporated: recommendation explicitly advances the wind portfolio as the policy-compatible alternative. |

### Evidence Confidence

**High for the three rejection grounds.** The endemic species extinction, FPIC status, and base-case BCR below 1.0 are confirmed facts, not uncertain estimates.

---

## Baseline Outputs

### Single-Agent Baseline

**Recommendation: Do not build; pursue wind and storage alternatives.**

The single-agent result reaches the correct Do not build conclusion and identifies the wind portfolio. However, it does not explicitly rule out the Redesign path by explaining why a smaller dam still fails on all three core objections. This is the core evaluation criterion for this case: a system that recommends Do not build but does not explain why Redesign is not the right path scores lower on Recommendation Specificity and Recommendation Calibration.

### MCDA Baseline

**Weighted score: approximately 1.73 / 5.00**

**Recommendation: Do not build.**

| Criterion | Score 1–5 |
|---|---:|
| water_supply_benefit | 1 |
| flood_control_benefit | 1 |
| energy_benefit | 3 |
| economic_viability | 1 |
| engineering_feasibility | 3 |
| ecological_impact_acceptability | 1 |
| social_impact_acceptability | 1 |
| legal_governance_readiness | 1 |
| climate_robustness | 2 |
| stakeholder_support | 1 |
| evidence_confidence | 3 |

MCDA reaches the correct conclusion. Limitations: does not explain why Redesign is ruled out; aggregation compresses the three independent grounds for rejection into a low overall score without distinguishing them; does not point toward the wind portfolio as the specific next step.
