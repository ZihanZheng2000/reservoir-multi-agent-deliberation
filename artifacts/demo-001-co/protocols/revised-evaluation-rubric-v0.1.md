# Revised Evaluation Rubric v0.2

## Purpose

This rubric evaluates the three systems (multi-agent deliberation, single-agent baseline, MCDA baseline) across three separate quality layers. The layers are **never collapsed into a single combined score**. Each layer measures something distinct and is reported independently.

## Why Three Layers, Not One Score

A single combined score conflates two problems:

1. **Structural unfairness**: Layer 3 (Process Quality) dimensions like Role Fidelity and Audit/Revision are only meaningful for deliberative systems. MCDA and single-agent score near zero on these by design, not by failure. Collapsing Layer 3 into a total artificially inflates the multi-agent advantage.

2. **Claim dilution**: The paper makes two distinct claims — that multi-agent produces more useful recommendations (Outcome Quality) and that it represents deliberative structure (Process Quality). These are different claims that require separate evidence.

**Reporting rule:**
- Layer 1 and Layer 2: report for all three systems; use for cross-system comparison.
- Layer 3: report for multi-agent only as a descriptive quality metric; note explicitly that baselines are not designed for these dimensions.
- Do not add Layer 1 + Layer 2 + Layer 3 totals together.

---

## Layer 1: Outcome Quality /30

**What it measures:** Does the output help a human make a decision? Is the recommendation specific, calibrated, and within the evaluator-defined reasonable range?

**Applies to:** All three systems. Primary basis for cross-system comparison.

| Dimension | Points |
|---|---:|
| Decision-range fit | /5 |
| Recommendation specificity | /15 |
| Recommendation calibration | /10 |
| **Total** | **/30** |

### Decision-Range Fit /5

Measures whether the final recommendation falls within the evaluator-only reasonable decision range defined in the gold checklist.

| Score | Meaning |
|---:|---|
| 5 | Recommendation is within the reasonable range and the rationale explains why the alternative labels were not chosen. |
| 3 | Recommendation is adjacent to the reasonable range (one label away) with partial justification. |
| 1 | Recommendation is at the edge of suspicious territory but not clearly wrong. |
| 0 | Recommendation is outside the reasonable range (suspicious label) without adequate justification. |

Decision-range fit is a gate check, not a style check. A recommendation of "Build" when the evaluator-defined range is Defer/Redesign is a score of 0 regardless of how well-written the output is.

### Recommendation Specificity /15

Measures whether the recommendation is specific enough to act on.

| Score | Meaning |
|---|---|
| 13–15 | Case-specific recommendation; distinguishes construction-blocking conditions from commissioning conditions; specifies verifiable thresholds or timelines where relevant; a real decision-maker could act on this output without further interpretation. |
| 9–12 | Directionally correct but conditions are generic ("complete remaining studies" without specifying which or when); some case-specific detail present but not enough to act on directly. |
| 5–8 | Recommendation is underspecified or hedges across multiple labels; a generic "Defer" or "Redesign" that could apply to any case in the suite; missing what specifically needs to be resolved. |
| 0–4 | Recommendation direction is wrong, absent, or so vague as to be unusable. |

Note: a generic "Defer" on a case that warrants a time-conditioned "Build with conditions" (e.g., SRD-007) is a specificity failure. Score accordingly.

### Recommendation Calibration /10

Measures whether the recommendation is appropriately calibrated to the actual evidence in the scenario — not systematically over-conservative or over-permissive.

| Score | Meaning |
|---|---|
| 9–10 | Recommendation reflects the scenario's actual evidence level: approves when blockers are resolved (SRD-006), rejects when alternatives dominate and harm is irreversible (SRD-008), produces a conditioned pathway when evidence is genuinely ambiguous (SRD-007). No systematic conservative or permissive bias. |
| 6–8 | Recommendation is broadly appropriate but shows slight conservative or permissive lean that is not fully justified by scenario evidence. |
| 3–5 | Systematic miscalibration: adds unnecessary conditions to a clear-approval case, or fails to flag serious blockers in a high-risk case. |
| 0–2 | Clear miscalibration: recommends Build on a clear Do-not-build case, or Do-not-build on a clear Build case. |

---

## Layer 2: Evidence Quality /40

**What it measures:** Is the analysis grounded in scenario facts, complete in risk coverage, and appropriately calibrated on uncertainty?

**Applies to:** All three systems. Secondary basis for cross-system comparison.

| Dimension | Points |
|---|---:|
| Evidence grounding | /10 |
| Risk coverage | /20 |
| Uncertainty calibration | /10 |
| **Total** | **/40** |

### Evidence Grounding /10

Measures whether substantive claims are traceable to scenario field IDs.

| Score | Meaning |
|---|---|
| 9–10 | Nearly all substantive claims cite specific field IDs; inferences explicitly labeled as `inference`; no material unsupported claim. |
| 6–8 | Most claims cited; some inferences unlabeled but not misleading; occasional unsupported claim. |
| 3–5 | Frequent uncited claims; inferences presented as fact; pattern of using general domain knowledge instead of scenario fields. |
| 0–2 | Claims routinely unsupported; scenario fields largely ignored. |

Note: Evidence grounding has low cross-system discrimination (all three systems tend to score similarly here). Weight reduced from prior versions accordingly.

### Risk Coverage /20

Measures whether the output identifies the risks and issues the case was designed to test.

Apply a must-detect penalty before assigning score:

- Start at 20.
- Subtract **4** for each missed must-detect risk from the evaluator-only gold checklist.
- Subtract **1** for each missed should-detect risk.
- Floor at 0.

**Compact run ceiling:** maximum 16/20 for a compact researcher-synthesized run unless a full verbatim transcript confirms coverage.

| Score (post-penalty) | Meaning |
|---:|---|
| 17–20 | All must-detect risks identified; most should-detect risks covered; no false reassurance. |
| 12–16 | Most must-detect risks identified; minor gaps or compact run ceiling applied. |
| 7–11 | One or two must-detect risks missed; meaningful gaps in coverage. |
| 0–6 | Multiple must-detect risks missed; systematic gaps. |

Risk coverage is the dimension most sensitive to case design quality. If the gold checklist was not designed carefully, this dimension may not discriminate well.

### Uncertainty Calibration /10

Measures whether the output treats uncertain findings as uncertain rather than settled.

| Score | Meaning |
|---|---|
| 9–10 | Missing evidence is consistently labeled as uncertainty; over-strong claims are avoided or explicitly hedged; the recommendation is not more confident than the evidence allows. |
| 6–8 | Most uncertainties labeled; occasional over-strong claim present but not pattern. |
| 3–5 | Frequent over-strong claims; evidence gaps treated as if resolved; uncertainty acknowledged only when forced. |
| 0–2 | Systematic overconfidence; output presents contested findings as settled. |

---

## Layer 3: Process Quality /55

**What it measures:** Does the deliberation exhibit structural properties of a good deliberative process?

**Applies to:** Multi-agent system only, as a descriptive quality metric. Do not report baselines on this layer. Do not compare baselines against multi-agent scores on Layer 3.

**Reporting convention:** Report Layer 3 dimensions for multi-agent with a one-paragraph qualitative note per case explaining where the deliberation was strongest and weakest. Do not use Layer 3 scores to claim multi-agent "beats" the baselines — they were not designed to deliberate.

| Dimension | Points |
|---|---:|
| Stakeholder/conflict representation | /15 |
| Role fidelity | /15 |
| Objection-response quality | /10 |
| Evidence audit and revision | /10 |
| Minority preservation | /5 |
| **Total** | **/55** |

### Stakeholder/Conflict Representation /15

| Score | Meaning |
|---|---|
| 13–15 | All major stakeholder groups appear as distinct voices; key conflicts named specifically (not collapsed into "pros and cons"); benefit-burden distribution made explicit; unresolved positions preserved. |
| 9–12 | Most stakeholders represented; main conflict identified; some compression of voices. |
| 5–8 | Stakeholders summarized rather than represented; conflict treated as narrative aside. |
| 0–4 | Stakeholder diversity absent. |

**Case-level calibration:** low-conflict cases (e.g., SRD-006) should naturally score 10–12 because there is less conflict to represent. This is appropriate, not inflated. Do not penalize a simple case for lacking complexity.

### Role Fidelity /15

| Score | Meaning |
|---|---|
| 13–15 | Expert agents stay within assigned domain; stakeholder agents reflect interests without becoming generic analysts; role-specific "Required challenge" is addressed; overreach is self-identified. |
| 9–12 | Most agents appropriately bounded; occasional cross-role claim not corrected. |
| 5–8 | Frequent role overreach; agents make claims outside their domain without labeling them. |
| 0–4 | Role boundaries consistently violated; outputs are indistinguishable from a single summarizing agent. |

### Objection-Response Quality /10

| Score | Meaning |
|---|---|
| 8–10 | Agents respond to specific objections raised by other agents; responses engage with the actual argument, not a weaker version; unresolved objections are preserved as minority reports. |
| 5–7 | Some objection-response structure present; partial engagement; some objections dropped without resolution. |
| 2–4 | Objections acknowledged but not engaged; responses are generic reassurances. |
| 0–1 | No objection-response structure; agents present independent summaries. |

### Evidence Audit and Revision /10

| Score | Meaning |
|---|---|
| 8–10 | Explicit audit process; specific claims challenged and either revised, softened, or labeled; audit decision documented; corrections traceable. |
| 5–7 | Some revision occurred; audit trail incomplete; not all over-strong claims caught. |
| 2–4 | Revision mentioned but no specific claim changes documented. |
| 0–1 | No audit process. |

**Compact run ceiling:** maximum 7/10 for a compact run unless a full verbatim audit transcript is provided.

### Minority Preservation /5

| Score | Meaning |
|---|---|
| 5 | All unresolved dissenting positions explicitly listed with the agent/stakeholder and the specific concern; reader can identify who disagrees and why without reading the full transcript. |
| 3–4 | Most minority positions preserved; one or two compressed or dropped. |
| 1–2 | Minority positions mentioned in passing but not clearly attributed or preserved. |
| 0 | Minority positions absent or converted into consensus. |

---

## Cross-Case Reporting Format

For each case, report:

```
Case: [ID]
Layer 1 — Outcome Quality
  Decision-range fit:       [score /5]
  Recommendation specificity: [score /15]
  Recommendation calibration: [score /10]
  Layer 1 total:            [score /30]

Layer 2 — Evidence Quality
  Evidence grounding:       [score /10]  (all systems)
  Risk coverage:            [score /20]  (all systems, penalty applied)
  Uncertainty calibration:  [score /10]  (all systems)
  Layer 2 total:            [score /40]

Layer 3 — Process Quality (multi-agent only)
  Stakeholder/conflict:     [score /15]
  Role fidelity:            [score /15]
  Objection-response:       [score /10]
  Audit and revision:       [score /10]
  Minority preservation:    [score /5]
  Layer 3 total:            [score /55]
  Qualitative note:         [1 paragraph]
```

For cross-case comparison figures:
- **Figure A**: Layer 1 scores (all three systems, all 8 cases) — primary comparative figure
- **Figure B**: Layer 2 scores (all three systems, all 8 cases) — supporting analysis
- **Figure C**: Layer 3 scores (multi-agent only, all 8 cases) — deliberation quality profile

---

## Score Ceiling Guidance

If multi-agent scores consistently near maximum on Layer 3 across all cases, check whether the rubric is distinguishing quality or simply confirming the system has deliberative structure. The scoring anchors above are calibrated to produce variation:

- Low-conflict cases (SRD-006) should score lower on Stakeholder/Conflict and Audit/Revision than high-conflict cases — less to represent and fewer claims to revise.
- Cases with weak or vague agent outputs should score lower on Role Fidelity and Objection-Response even if the system type is multi-agent.
- The must-detect penalty in Risk Coverage should cause Layer 2 scores to fall meaningfully when the system misses designed risks.

---

## Relationship to Controlled Benchmark Metrics

The rubric above measures quality dimensions. The controlled benchmark protocol produces separate outcome metrics that are reported alongside but not combined with the rubric scores:

| Outcome metric | Layer it informs | Where reported |
|---|---|---|
| Must-detect recall | Layer 2 (Risk Coverage penalty) | Gold checklist evaluation |
| Should-detect recall | Layer 2 (Risk Coverage penalty) | Gold checklist evaluation |
| Decision-range fit /5 | Layer 1 | Rubric (above) |
| False reassurance count | Layer 1 (calibration) | Gold checklist evaluation |
| Emergent issue precision | Supplement only | Emergent issue discovery table |

Decision-range fit is the one controlled benchmark metric explicitly incorporated into the rubric score (Layer 1). The others remain as supplementary reporting.
