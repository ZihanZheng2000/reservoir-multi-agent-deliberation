# Cross-Case Score Summary v0.1

This file summarizes the current organized benchmark results for SRD-001 to SRD-008.

## Reporting Rule

Layer 1 and Layer 2 can be compared across multi-agent, single-agent, and MCDA systems. Layer 3 is reported only for the multi-agent system and should not be collapsed into a combined total with Layers 1 and 2.

## Decision Direction Summary

| Case | Codex multi-agent recommendation | Claude Code multi-agent recommendation | Agreement |
|---|---|---|---|
| SRD-001 | Redesign; defer final build approval | Redesign + Defer | High |
| SRD-002 | Build with conditions through phased approval | Build with conditions through phased approval | High |
| SRD-003 | Redesign toward the hybrid alternative | Redesign toward hybrid alternative | High |
| SRD-004 | Phased emergency package now; defer final reservoir approval | Phased emergency package now; defer final reservoir approval | High |
| SRD-005 | Defer pending basin agreement, joint monitoring, and drought rules | Defer pending binding basin agreement, joint monitoring, and drought-contingent rules | High |
| SRD-006 | Build; commissioning conditions attached | Build; commissioning conditions attached | High |
| SRD-007 | Build with conditions; approval lapses to Defer if livelihood plan is incomplete | Build with conditions; revert to Defer if livelihood plan is incomplete in 9 months | High |
| SRD-008 | Do not build; pursue wind portfolio alternative | Do not build; pursue wind portfolio alternative | High |

## Codex Scores

| Case | Multi-agent L1 /30 | Multi-agent L2 /40 | Multi-agent L3 /55 | Single-agent L1 /30 | Single-agent L2 /40 | MCDA L1 /30 | MCDA L2 /40 |
|---|---:|---:|---:|---:|---:|---:|---:|
| SRD-001 | 28 | 38 | 51 | 24 | 30 | 17 | 23 |
| SRD-002 | 27 | 33 | 39 | 26 | 30 | 23 | 27 |
| SRD-003 | 27 | 34 | 42 | 23 | 29 | 19 | 24 |
| SRD-004 | 28 | 34 | 43 | 26 | 30 | 20 | 25 |
| SRD-005 | 28 | 35 | 44 | 24 | 30 | 20 | 25 |
| SRD-006 | 29 | 34 | 35 | 28 | 31 | 28 | 30 |
| SRD-007 | 29 | 34 | 43 | 20 | 28 | 16 | 23 |
| SRD-008 | 29 | 35 | 40 | 27 | 31 | 25 | 28 |
| **Mean** | **28.1** | **34.6** | **42.1** | **24.8** | **29.9** | **21.0** | **25.6** |

## Claude Code Scores

| Case | Multi-agent L1 /30 | Multi-agent L2 /40 | Multi-agent L3 /55 | Single-agent L1 /30 | Single-agent L2 /40 | MCDA L1 /30 | MCDA L2 /40 |
|---|---:|---:|---:|---:|---:|---:|---:|
| SRD-001 | 26 | 36 | 49 | 16 | 22 | 13 | 18 |
| SRD-002 | 26 | 34 | 44 | 22 | 26 | 15 | 20 |
| SRD-003 | 26 | 34 | 43 | 19 | 26 | 13 | 18 |
| SRD-004 | 26 | 34 | 43 | 21 | 27 | 13 | 19 |
| SRD-005 | 26 | 34 | 45 | 20 | 27 | 14 | 20 |
| SRD-006 | 28 | 36 | 43 | 21 | 29 | 18 | 25 |
| SRD-007 | 27 | 34 | 45 | 16 | 26 | 11 | 18 |
| SRD-008 | 27 | 35 | 46 | 22 | 29 | 15 | 20 |
| **Mean** | **26.5** | **34.6** | **44.8** | **19.6** | **26.5** | **14.0** | **19.8** |

## Interpretation

The decision direction is stable across Codex and Claude Code. The largest substantive multi-agent advantage appears in procedurally complex cases, especially SRD-004 and SRD-007, where the output must distinguish immediate action, construction approval, commissioning conditions, and time-conditioned safeguards.

Codex tends to produce more direct decision-action summaries. Claude Code tends to preserve more process and audit detail. Both are useful: Codex is strong for reader-facing summaries, while Claude Code is strong for appendix-style process evidence.
