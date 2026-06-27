# Run Log: demo-001-co

## Purpose

Revise and rerun SRD-001 after method audit.

## Changes Implemented

- Removed agent-facing `Initial Assessment Hints`.
- Added evaluator-only gold checklist.
- Added decision thresholds.
- Added revised two-layer evaluation rubric.
- Added quantitative evidence audit template.
- Added reusable prompt templates.
- Reran compact multi-agent, single-agent, and MCDA comparison.
- Added emergent issue discovery evaluation.
- Added current three-layer evaluation under `outputs/evaluation-three-layer.md`.
- Added Codex vs Claude Code comparison under `outputs/codex-vs-claude-code-comparison.md`.
- Renamed references from the former v2 placeholder directory to `demo-001-co`.

## Result

Recommendation: **Redesign; final build approval deferred.**

Scores:

| System | Shared /60 | Deliberative /40 | Combined /100 |
|---|---:|---:|---:|
| Multi-agent | 56 | 37 | 93 |
| Single-agent | 51 | 8 | 59 |
| MCDA | 43 | 3 | 46 |

Emergent issue discovery:

| System | Candidate | Valid | Weak | Unsupported/hallucinated |
|---|---:|---:|---:|---:|
| Multi-agent | 7 | 4 | 1 | 0 |
| Single-agent | 3 | 1 | 1 | 0 |
| MCDA | 1 | 0 | 1 | 0 |

## Status

Complete.

## Next Recommendation

Use the demo-001-co protocol as the Codex default for future full runs.
