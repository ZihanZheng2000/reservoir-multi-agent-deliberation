# Run Summary — demo-001-cc

Case: SRD-001-cc — North Fork Multipurpose Reservoir
Run folder: `artifacts/demo-001-cc/`
Rubric version: v3 (three-layer)
Gold checklist: 7M/8S (from `artifacts/demo-001/protocols/evaluator-only-gold-checklist.md`)

---

## Final Recommendation

**Multi-agent deliberation:** Redesign + Defer
**Single-agent baseline:** Defer
**MCDA baseline:** Redesign (score 2.15/5.0)

Expected decision range for SRD-001: Redesign or Build with conditions.

Multi-agent recommendation is squarely within range. Single-agent is adjacent (Defer is acceptable but underspecific). MCDA is correct direction.

---

## Scorecard

| System | L1 Outcome /30 | L2 Evidence /40 | L3 Process /55 |
|---|---:|---:|---|
| Multi-agent | 26 | 36 | 49 |
| Single-agent | 16 | 22 | n/a |
| MCDA | 13 | 18 | n/a |

L1 + L2 gap (multi-agent vs. single-agent): +24 points (26+36=62 vs. 16+22=38).
L1 + L2 gap (multi-agent vs. MCDA): +37 points (62 vs. 13+18=31).

---

## Risk Coverage

| System | M detected /7 | S detected /8 | L2.2 /20 |
|---|---:|---:|---:|
| Multi-agent | 7/7 | 7/8 | 19 |
| Single-agent | ~5/7 | ~5/8 | 13 |
| MCDA | ~3/7 | ~5/8 | 9 |

Key missed risks by baseline:
- Single-agent: R14 (sacred sites as separate process), R15 (USD 355–512M financing gap quantification) partially; R8 (hydropower/flood conflict) missed entirely; R13 (combined downside BCR estimate) missed.
- MCDA: R14, R15 missed; R8 missed; R10 (consultation legal risk) partial; R4 (F7.8 specifically) partial.

---

## Unique Contributions of Multi-Agent Deliberation

1. **Combined downside BCR estimate (0.65–0.80):** Produced via joint Climate Risk + Economist R2 exchange. Neither baseline produced this.
2. **Sacred sites as requiring separate consent, not resettlement plan item:** Produced by Upstream Residents required challenge (F8.3). Not distinguished in either baseline.
3. **R8 — hydropower/flood pre-release conflict:** Produced by Downstream Users stakeholder and Moderator conflict map (F3.5). Not detected by either baseline.
4. **USD 355–512M financing gap quantified:** Produced by Financier R2 clarification. Single-agent noted the condition; did not quantify it.
5. **"Do not build if passage fails" trigger preserved:** Produced by Ecologist minority position. No baseline preserved a conditional trigger.

---

## Agent Performance Highlights

| Agent | Required challenge | Executed? | Impact |
|---|---|---|---|
| Hydrologist | Challenge 22% env. flow (F2.10) | Yes | Triggered joint ecological flow exchange with Ecologist |
| Dam Safety | Flag EAP as safety blocker | Yes | Established clear dam construction boundary |
| Ecologist | Require species-specific study, not just feasibility | Yes | Elevated R4 to full M detection; triggered Developer acknowledgment |
| Climate Risk | Flag BCR test doesn't combine stressors | Yes | Triggered combined downside BCR estimation in R2 |
| Economist | Challenge BCR not including full safeguard costs | Yes | Quantified combined downside range |
| Social | Challenge cash compensation vs. livelihood continuity | Yes | Distinguished livelihood budget gap from general compensation |
| Legal | State EIA gap is financing-blocking | Yes | Connected EIA status to development bank tranche condition |

All 7 required challenges executed.

---

## Process Quality Highlights (Layer 3)

- 4 minority reports explicitly preserved in Decision Authority recommendation
- 78 claims audited; 7 corrected
- 4 substantive Round 2 exchanges with resolution outcomes
- 0 unresolved audit blockers
- 0 role-overreach violations confirmed
- Alternatives analysis (F0.6 non-dam portfolio) remained unresolved as an open gap — Environmental NGO minority position preserved

---

## Comparison with demo-001 Original Run

*Note: The original demo-001 run used a compact format. Direct claim-level comparison is approximate.*

| Dimension | demo-001 (compact) | demo-001-cc (full transcript) |
|---|---|---|
| Decision | Redesign + conditions | Redesign + Defer |
| Condition count | ~8 conditions | 14 specific conditions |
| Minority positions documented | Informal notes | 4 formal minority reports |
| Evidence audit | Not conducted | Full audit, 78 claims |
| Financing gap quantified | Not in compact output | Yes — USD 355–512M |
| Sacred sites as separate process | Noted | Explicitly distinguished from resettlement plan item |
| Combined downside BCR | Not calculated | 0.65–0.80 (inference) |

---

## Files in This Run

| File | Purpose |
|---|---|
| `agents/role-cards-v0.1.md` | Role definitions for all 17 agents |
| `inputs/` | Scenario input files |
| `outputs/round-1-expert-assessments.md` | Round 1: 7 expert agents |
| `outputs/round-1-stakeholder-assessments.md` | Round 1: 7 stakeholder agents |
| `outputs/moderator-conflict-map.md` | Issue clusters, conflicts, targeted questions |
| `outputs/round-2-deliberation.md` | 5 targeted exchanges |
| `outputs/evidence-audit.md` | 78 claims audited, 7 corrected |
| `outputs/decision-authority-recommendation.md` | Final recommendation |
| `outputs/baseline-single-agent.md` | Single-agent baseline |
| `outputs/baseline-mcda.md` | MCDA baseline |
| `outputs/evaluation-three-layer.md` | Three-layer rubric evaluation |
| `outputs/run-summary.md` | This file |
