# Emergent Issue Discovery Protocol v0.1

## Purpose

This protocol evaluates whether a multi-agent deliberation system can discover decision-relevant issues that were **not** included in the designer-authored hidden checklist.

This is complementary to gold checklist recovery.

- **Recovery:** Did the system find the issues the case designer expected?
- **Discovery:** Did the system surface additional valid issues that the designer did not pre-specify?

## Why This Matters

If the system only recovers the hidden checklist, it is mainly reproducing the designer's known risk structure.

If it also identifies valid additional issues, then it may help researchers and decision-makers expand the risk space, notice overlooked stakeholder concerns, and improve the case design itself.

## Definitions

### Pre-Specified Issue

An issue listed in the evaluator-only gold checklist before the system run.

### Candidate Emergent Issue

An issue raised by the system that is not already listed in the gold checklist.

### Valid Emergent Issue

A candidate issue that:

1. is supported by scenario facts or a reasonable inference from those facts;
2. is not merely a duplicate or rewording of a checklist item;
3. has plausible decision relevance;
4. survives human evaluator review.

### Invalid Emergent Issue

A candidate issue that is:

- unsupported by the scenario;
- hallucinated;
- too generic;
- duplicate/rephrasing of a checklist item;
- not decision-relevant.

## Human Review Categories

Every candidate emergent issue must be classified by a human evaluator.

| Category | Meaning | Counted as valid? |
|---|---|---|
| valid_emergent | New, scenario-supported, decision-relevant issue. | yes |
| weak_but_interesting | Plausible but evidence is limited or decision relevance is uncertain. | partial / report separately |
| duplicate | Rephrasing or minor variant of checklist item. | no |
| unsupported | Not supported by scenario facts. | no |
| hallucinated | Contradicts or invents facts beyond scenario. | no |
| not_decision_relevant | Interesting but not relevant to project decision. | no |

## Required Extraction Process

1. Run the system without showing the hidden checklist.
2. Extract all substantive issues from the system output.
3. Remove all issues already covered by the hidden checklist.
4. The remaining issues become candidate emergent issues.
5. Human evaluator classifies each candidate issue.
6. Record metrics.

## Metrics

| Metric | Definition |
|---|---|
| candidate emergent issue count | Number of non-checklist issues proposed by the system. |
| valid emergent issue count | Number classified as `valid_emergent`. |
| weak-but-interesting count | Number classified as `weak_but_interesting`. |
| duplicate count | Number classified as `duplicate`. |
| unsupported/hallucinated count | Number classified as unsupported or hallucinated. |
| emergent issue precision | valid emergent / candidate emergent. |
| decision-relevant discovery count | valid emergent issues that affect recommendation, conditions, or stakeholder conflict. |

## Recommended Table

| Issue ID | Candidate emergent issue | Source agent/system | Scenario support | Human category | Decision relevance | Notes |
|---|---|---|---|---|---|---|

## Comparative Use

Compare:

- multi-agent deliberation;
- single-agent baseline;
- MCDA baseline.

Expected pattern:

- MCDA may have few emergent issues because it aggregates predefined criteria.
- Single-agent may discover some issues but usually without stakeholder interaction.
- Multi-agent may discover more valid emergent issues through role-specific perspectives and conflict generation.

## Reporting Rule

Do not count an issue as a system advantage unless it passes human review.

Use cautious language:

> The system surfaced candidate emergent issues. After human review, X were classified as valid, decision-relevant emergent issues.

Do not say:

> The system discovered new true risks.

## Relationship to Gold Checklist

Gold checklist recovery and emergent discovery should be reported together:

| System | Must-detect recall | Valid emergent issues | Unsupported/hallucinated issues | Interpretation |
|---|---:|---:|---:|---|

The best system is not the one that raises the most issues. It is the one that has high checklist recovery, useful valid emergent issues, and low unsupported/hallucinated issue count.
