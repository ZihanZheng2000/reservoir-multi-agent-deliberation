# Reservoir Multi-Agent Deliberation Benchmark

This repository contains a research prototype and synthetic benchmark for evaluating role-limited multi-agent deliberation in reservoir construction decision support.

The project asks a practical question: can a multi-agent system simulate the structure of a reservoir approval meeting better than a single-agent analysis or a weighted MCDA baseline? The system assigns different roles to hydrologists, dam-safety engineers, ecologists, economists, legal/policy experts, affected communities, financiers, and decision authorities. The goal is not to claim that AI can make objectively correct infrastructure decisions. The goal is to test whether multi-agent deliberation produces more inspectable, role-bounded, and procedurally useful decision-support reasoning.

## Current Status

- Synthetic benchmark cases: 8
- Full transcript-style cases: SRD-001, run with Codex and Claude Code
- Compact cases: SRD-002 to SRD-008, run with Codex and Claude Code
- Baselines: single-agent decision analyst and MCDA
- Evaluation: three-layer rubric covering Outcome Quality, Evidence Quality, and Process Quality
- Real-world validation: not yet included

## Case Suite

| Case | Decision challenge | Multi-agent decision direction |
|---|---|---|
| SRD-001 | High-conflict multipurpose dam | Redesign and defer final approval |
| SRD-002 | Low-conflict off-channel expansion | Build with conditions |
| SRD-003 | Hydropower-dominant project with weak local benefits | Redesign toward hybrid alternative |
| SRD-004 | Emergency flood-control project | Emergency package now; defer reservoir approval |
| SRD-005 | Transboundary/downstream conflict | Defer pending basin agreement |
| SRD-006 | Clean approval case | Build with commissioning conditions |
| SRD-007 | Near-tipping-point conditional approval | Build with time-limited conditions |
| SRD-008 | Clear do-not-build case | Do not build; pursue alternative |

## Repository Structure

```text
cases/          Synthetic scenario packets and evaluator-only gold checklists
runs/           Codex and Claude Code outputs for each case
protocols/      Benchmark protocol, emergent issue protocol, and evaluation rubric
reports/        Cross-case reports and benchmark summaries
docs/           Method, repository, evaluation, and limitation notes
packages/       Planning/modeling packages from the research workflow
artifacts/      Original working artifacts retained for traceability
archive/        Reserved for older or superseded material
scripts/        Reserved for future reproducibility utilities
```

## Systems Compared

| System | Role in benchmark |
|---|---|
| Multi-agent deliberation | Main method; simulates expert/stakeholder approval meeting |
| Single-agent baseline | One integrated decision analyst reviewing the same scenario |
| MCDA baseline | Weighted multi-criteria scoring baseline |

## Evaluation Rubric

The current rubric has three layers:

1. **Outcome Quality /30**: decision-range fit, recommendation specificity, recommendation calibration.
2. **Evidence Quality /40**: evidence grounding, risk coverage, uncertainty calibration.
3. **Process Quality /55**: stakeholder/conflict representation, role fidelity, objection-response quality, evidence audit/revision, minority preservation.

Layer 1 and Layer 2 are used for cross-system comparison. Layer 3 is reported only for the multi-agent system because single-agent and MCDA baselines are not designed to simulate deliberation.

## Key Report

The main current report is:

- [`reports/eight-case-co-cc-benchmark-report-v0.1.md`](reports/eight-case-co-cc-benchmark-report-v0.1.md)

## Main Finding

Across eight synthetic cases and two model-run environments, the multi-agent system produced stable decision directions and covered the full decision range from Build to Do not build. Its strongest advantage appears in cases where a decision requires sequencing, stakeholder conflict preservation, or conditional approval logic rather than a single aggregate score.

## Important Limitations

This is a research prototype. The current benchmark is synthetic and researcher-scored. It should not be interpreted as a validated reservoir approval system. Manuscript-ready validation will require independent blinded evaluation, MCDA weight calibration, and one or more real-world reservoir cases.

## Suggested Citation

A formal citation file is provided in `CITATION.cff`, but author and release metadata should be updated before public release.
