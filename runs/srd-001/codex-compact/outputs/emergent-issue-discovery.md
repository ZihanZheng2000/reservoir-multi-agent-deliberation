# Emergent Issue Discovery: SRD-001-co

## Purpose

This file evaluates whether the systems raised additional decision-relevant issues beyond the evaluator-only gold checklist.

Gold checklist used:

- `protocols/evaluator-only-gold-checklist.md`

Protocol:

- `artifacts/emergent-issue-discovery-protocol-v0.1.md`

## Summary Table

| System | Candidate emergent issues | Valid emergent issues | Weak-but-interesting | Duplicate/rephrasing | Unsupported/hallucinated | Emergent precision | Decision-relevant discoveries |
|---|---:|---:|---:|---:|---:|---:|---:|
| Multi-agent | 7 | 4 | 1 | 2 | 0 | 0.57 | 4 |
| Single-agent | 3 | 1 | 1 | 1 | 0 | 0.33 | 1 |
| MCDA | 1 | 0 | 1 | 0 | 0 | 0.00 | 0 |

## Multi-Agent Candidate Emergent Issues

| Issue ID | Candidate emergent issue | Source agent/system | Scenario support | Human category | Decision relevance | Notes |
|---|---|---|---|---|---|---|
| E1 | Flood-control pre-release rules may conflict with hydropower revenue and storage objectives. | Hydrologist / Moderator | F3.5, F4.3 | valid_emergent | high | Checklist mentions flood limits but not this operational incentive conflict explicitly. |
| E2 | Late delivery of technical documents may reduce trust, not just formal consultation adequacy. | Upstream residents / Legal / Moderator | F8.5, F9.4 | valid_emergent | high | Adds legitimacy/trust mechanism beyond checklist consultation item. |
| E3 | Lower-fertility replacement land may make cash compensation insufficient for livelihood restoration. | Social expert / Upstream residents | F8.4, F8.7 | valid_emergent | high | Checklist mentions livelihood restoration, but not this compensation-quality mechanism. |
| E4 | Financing safeguard failure is also a project delivery risk, not only an ethical/legal issue. | Financier / Developer | F9.8, F10.7, F5.4 | valid_emergent | high | Connects safeguards to bankability and implementation feasibility. |
| E5 | Redesign without affected-community bargaining power may become pre-committed approval under another name. | Upstream residents / NGO | F8.5, F8.8, F10.4 | weak_but_interesting | medium | Plausible governance concern, but scenario does not directly describe bargaining institutions. |
| E6 | Non-dam portfolio may lower ecological harm but has weaker flood-control benefit and higher coordination burden. | Economist / NGO | F0.6, F5.8 | duplicate | medium | Mostly covered by checklist R3 in the benchmark protocol example and scenario facts. |
| E7 | Downstream fishery protections need monitoring and compensation mechanisms. | Downstream users | F7.6, F10.5 | duplicate | medium | Mostly rephrases downstream flow/fisheries and environmental flow checklist items. |

## Single-Agent Candidate Emergent Issues

| Issue ID | Candidate emergent issue | Source agent/system | Scenario support | Human category | Decision relevance | Notes |
|---|---|---|---|---|---|---|
| S-E1 | Non-dam alternatives need consistent comparison rather than being listed as a fallback. | Single-agent baseline | F0.6, F5.8 | valid_emergent | high | Useful comparison-design issue. |
| S-E2 | Project sequencing matters: studies should precede final approval and financing close. | Single-agent baseline | F9.3, F9.6, F9.8 | duplicate | medium | Mostly covered by safeguard-readiness checklist. |
| S-E3 | Public debt exposure could become a governance issue. | Single-agent baseline | F5.4, F5.3 | weak_but_interesting | medium | Plausible but scenario does not specify fiscal stress. |

## MCDA Candidate Emergent Issues

| Issue ID | Candidate emergent issue | Source agent/system | Scenario support | Human category | Decision relevance | Notes |
|---|---|---|---|---|---|---|
| M-E1 | Sensitivity analysis could change recommendation under different weights. | MCDA baseline | MCDA method, not scenario field | weak_but_interesting | medium | Useful methodological issue, but not a case-specific reservoir risk. |

## Interpretation

The multi-agent system produced more candidate and valid emergent issues than the baselines. The strongest discoveries were not new facts, but new connections among facts:

1. operational conflict between flood control, hydropower, and storage;
2. consultation delay as a trust problem;
3. replacement-land quality as a compensation adequacy problem;
4. safeguards as project delivery and financing risk.

These issues are valuable because they help a human evaluator improve the original case checklist and decision conditions.

## Caution

The emergent issues were classified by the researcher/assistant, not by independent reviewers. Future runs should use blind human review.
