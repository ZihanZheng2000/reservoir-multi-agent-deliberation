# SRD-001 Method Audit v0.1

## Audit Scope

Reviewed:

- `artifacts/demo-001/inputs/synthetic-reservoir-scenario-v0.1.md`
- `artifacts/demo-001/agent/role-cards-v0.1.md`
- `artifacts/demo-001/protocols/evidence-audited-deliberation-protocol-v0.1.md`
- `artifacts/demo-001/outputs/round-1-agent-assessments.md`
- `artifacts/demo-001/outputs/evidence-audit.md`
- `artifacts/demo-001/outputs/deliberative-acceptability-evaluation.md`

## Overall Judgment

The SRD-001 setup is coherent as a first proof-of-concept. It successfully demonstrates a simulated approval meeting with expert agents, stakeholder agents, moderator, evidence auditor, and decision authority.

However, before using this as a mature paper method, several issues should be fixed:

1. the scenario is too decision-leading;
2. the agent set is large and may be costly;
3. agent scoring is not yet standardized enough;
4. the evidence audit is still too soft;
5. the evaluation rubric currently favors the multi-agent system by design;
6. there is no full reproducible prompt/execution format yet.

## Strengths

### 1. Scenario Has Realistic Multi-Dimensional Tension

SRD-001 is not a simple bad project. It has real benefits:

- water supply benefit;
- flood-control benefit;
- hydropower benefit;
- national policy fit.

But it also has serious blockers:

- ecology;
- resettlement;
- incomplete EIA;
- financing safeguards;
- climate uncertainty;
- cost downside.

This makes it a good high-conflict test case.

### 2. Expert and Stakeholder Separation Is Valuable

The role design separates:

- technical expertise;
- stakeholder interests;
- governance and decision authority.

This is the core methodological contribution.

### 3. Evidence Field IDs Work Well

The F-field system makes outputs auditable. Agents can be required to cite `F2.4`, `F8.1`, etc. This is much better than asking agents to reason from prose alone.

### 4. Evidence Auditor Adds Real Value

The auditor caught over-strong language such as:

- redesign "can resolve" risks;
- legal readiness claims stronger than available law;
- stakeholder interpretation presented too strongly.

This is a real mechanism, not just decorative.

## Main Weaknesses and Recommended Fixes

### Weakness 1: Scenario Is Somewhat Decision-Leading

The scenario itself includes a section called `Initial Assessment Hints`, which says redesign or defer may be more defensible. This risks making the case too easy and biasing the system toward `Redesign/Defer`.

**Fix:**

For future formal runs, remove `F12. Initial Assessment Hints` from the agent-facing packet.

Keep an internal `gold-risk-checklist.md` for evaluation, but do not show it to agents.

### Weakness 2: Too Many Agents for Full Runs

SRD-001 uses:

- 7 expert agents;
- 7 stakeholder agents;
- 3 governance agents.

This is realistic but expensive and verbose.

**Fix:**

Use a two-tier design:

- Full mode: all agents, used for 1-2 representative cases.
- Compact mode: 5 expert agents + 5 stakeholder agents + 3 governance agents, used for most synthetic cases.

Recommended compact set:

- Hydrologist / Water Resources
- Engineering / Dam Safety
- Ecology / Environment
- Economics / Finance
- Social / Legal Safeguards
- Developer
- Government / Regulator
- Affected Upstream Communities
- Downstream Users
- Environmental NGO or Financier, selected by case
- Moderator
- Evidence Auditor
- Decision Authority

### Weakness 3: Agent Score Contributions Are Not Fully Standardized

Different agents score different dimensions, which is reasonable, but there is no rule for aggregating or comparing scores.

**Fix:**

Add a score aggregation protocol:

1. agents only score assigned dimensions;
2. decision authority builds final score matrix;
3. final score matrix must list:
   - median score if multiple agents score a dimension;
   - dissent range;
   - confidence;
   - decisive evidence.

### Weakness 4: Evidence Audit Is Too Soft

The audit mostly flags wording issues, not all claim-level failures. It does not compute:

- total number of claims;
- claim citation rate;
- unsupported claim rate;
- inference-label compliance;
- role-overreach rate.

**Fix:**

Turn audit into a semi-quantitative table:

| Metric | Value |
|---|---:|
| total substantive claims |  |
| claims with field citation |  |
| claims labeled inference |  |
| unsupported claims |  |
| role-overreach claims |  |
| over-strong claims corrected |  |
| unresolved audit blockers |  |

### Weakness 5: Evaluation Rubric Favors Multi-Agent by Design

The rubric includes dimensions such as role fidelity and deliberation quality. Single-agent and MCDA are structurally unable to score highly there.

This is acceptable if the research question is about deliberative acceptability, but it must be disclosed clearly.

**Fix:**

Use two evaluation layers:

1. **Shared decision-support quality score** for all systems:
   - evidence grounding;
   - risk coverage;
   - decision usefulness;
   - uncertainty calibration.

2. **Deliberative process score** only for systems that claim to support deliberation:
   - conflict representation;
   - role fidelity;
   - objection-response;
   - minority preservation;
   - audit/revision.

This avoids unfairly saying MCDA is bad at something it was never designed to do.

### Weakness 6: No Reproducible Prompt/Execution Format Yet

The current outputs are plausible, but the exact prompts used to generate each agent are not separately stored.

**Fix:**

Create a reusable run protocol:

- `prompts/round-1-agent-prompt-template.md`
- `prompts/moderator-prompt.md`
- `prompts/evidence-auditor-prompt.md`
- `prompts/decision-authority-prompt.md`
- `outputs/run_metadata.json`

This matters for reproducibility.

### Weakness 7: Decision Authority May Be Too Conservative

Current decision logic says not to issue `Build` when safeguard blockers remain unresolved. This is sensible for SRD-001, but across cases it may bias toward conditional approval or deferral.

**Fix:**

Add explicit decision thresholds:

- `Build`: no unresolved blocker, benefits strong, mitigation mature.
- `Build with conditions`: no critical blocker, conditions are implementable before construction.
- `Redesign`: project need credible, but design creates avoidable harms.
- `Defer`: key evidence missing or legal/safeguard readiness incomplete.
- `Do not build`: benefits weak or harms cannot plausibly be mitigated.

### Weakness 8: Stakeholder Agents Need Decision-Power Modeling

Stakeholders currently express positions, but their formal power is not modeled.

In real meetings:

- affected residents may not have veto power but can create legitimacy/legal risk;
- financiers can block money;
- regulators can block permits;
- developers can redesign or withdraw;
- NGOs can create legal/reputational pressure.

**Fix:**

Add a stakeholder influence table:

| Stakeholder | Formal power | Informal power | What they can block |
|---|---|---|---|

Decision Authority should consider this table.

## Recommended Revised Workflow

### Agent-Facing Inputs

Use:

1. neutral scenario packet;
2. role card;
3. output schema.

Do not show:

1. initial assessment hints;
2. expected decision range;
3. gold-risk checklist.

### Internal Evaluation Inputs

Use:

1. gold risk checklist;
2. expected reasonable decision range;
3. scoring rubric;
4. audit metrics.

### Revised Round Structure

1. Round 0: Preflight.
2. Round 1: Independent role assessments.
3. Round 2: Moderator conflict map.
4. Round 3: Targeted challenge-response.
5. Round 4: Evidence audit with quantitative metrics.
6. Round 5: Agent corrections.
7. Round 6: Decision authority recommendation.
8. Round 7: Evaluator scoring, separated into shared quality and deliberative process scores.

## What Should Be Changed Before Full Case Runs

High priority:

1. remove initial assessment hints from agent-facing scenario packets;
2. split scoring into shared quality score and deliberative process score;
3. add quantitative audit metrics;
4. create reusable prompt templates;
5. define decision thresholds.

Medium priority:

1. reduce agent count for compact runs;
2. add stakeholder power/influence table;
3. add final score aggregation rules;
4. create hidden gold-risk checklist for each case.

Low priority:

1. expand all cases into full transcripts;
2. calibrate MCDA weights from literature;
3. add human expert blind evaluation.

## Bottom Line

SRD-001 is a strong first demo, but it is not yet a mature experimental protocol.

The most important correction is methodological: separate what agents see from what evaluators use. Agents should receive neutral case facts; evaluators can use hidden expected-risk checklists and scoring rubrics.
