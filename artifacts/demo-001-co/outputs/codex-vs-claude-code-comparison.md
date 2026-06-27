# SRD-001 Codex vs Claude Code Comparison

## Compared Runs

| Run | Directory | Character |
|---|---|---|
| Codex revised compact run | `artifacts/demo-001-co/` | Neutral scenario, hidden checklist, reusable prompts, compact synthesized outputs |
| Claude Code full transcript run | `artifacts/demo-001-cc/` | Full transcript-style multi-agent outputs with separate expert/stakeholder rounds |

## Recommendation Comparison

| Run | Recommendation |
|---|---|
| Codex revised compact run | Redesign; final build approval deferred |
| Claude Code full transcript run | Redesign + Defer / final build approval deferred |

The recommendation direction is stable across both runs.

## Three-Layer Score Comparison

| Run/System | L1 Outcome /30 | L2 Evidence /40 | L3 Process /55 | Notes |
|---|---:|---:|---:|---|
| Codex multi-agent compact | 25 | 32 | 41 | Compact-run ceiling applied; strong protocol clarity, weaker transcript inspectability. |
| Claude Code multi-agent full transcript | 26 | 36 | 49 | Better full-process evidence and richer claim-level audit trail. |
| Codex single-agent baseline | 22 | 26 | n/a | Stronger compact baseline than Claude Code single-agent on L1/L2 under current coding. |
| Claude Code single-agent baseline | 16 | 22 | n/a | More conservative scoring due to weaker field citation and specificity. |
| Codex MCDA baseline | 15 | 20 | n/a | Transparent but still limited by aggregation. |
| Claude Code MCDA baseline | 13 | 18 | n/a | Similar pattern; weaker specificity. |

## What Codex Did Better

- Cleaner controlled-benchmark structure.
- Neutral scenario and evaluator-only checklist are explicit.
- Prompt templates are stored.
- Compact summary is easier to read and reuse.
- Emergent issue discovery is included.

## What Claude Code Did Better

- Stronger transcript-level inspectability.
- Separate expert and stakeholder first-round outputs.
- More detailed Round 2 objection-response.
- Stronger Layer 3 Process Quality score.
- Better evidence for role fidelity and audit/revision because the artifacts are more granular.

## Research Interpretation

The two runs are complementary rather than redundant:

- `demo-001-co` is stronger as a **protocol/control run**.
- `demo-001-cc` is stronger as a **full transcript demonstration**.

For a manuscript, use the Codex run to define the benchmark protocol and use the Claude Code run as evidence that the protocol can produce inspectable full deliberation artifacts.

## Recommended Cleanup / Next Step

Use these names consistently:

- `demo-001-co`: Codex revised compact run.
- `demo-001-cc`: Claude Code full transcript run.

Do not refer to the former v2 placeholder as a directory.
