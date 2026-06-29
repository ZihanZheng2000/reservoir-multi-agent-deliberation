# Project Overview

This project develops and evaluates a role-limited multi-agent deliberation workflow for reservoir construction decision support.

The central idea is to approximate the deliberative structure of a reservoir approval meeting rather than a single optimizing function. Different agents represent disciplinary experts and stakeholder groups. Their outputs are then synthesized by a moderator, audited for evidence quality, and turned into a decision-authority recommendation.

The method has an expert-specialization intuition similar in spirit to mixture-of-experts systems: it separates expertise across specialized components. Unlike a conventional neural MoE architecture, however, it does not rely on a hidden router that selects expert modules and aggregates their activations. It makes expert disagreement, stakeholder conflict, evidence gaps, and decision conditions visible as part of the decision-support artifact.

## Research Question

Can role-limited multi-agent deliberation produce reservoir construction recommendations that are more procedurally inspectable and decision-useful than single-agent analysis or MCDA-style weighted aggregation?

## Contribution Framing

The project makes a methodological contribution, not a claim of automated decision correctness. The system is intended to expose reasoning structure: conflicts, objections, uncertainties, role-specific judgments, and conditional pathways.

## Current Evidence Base

The current benchmark uses eight synthetic cases. These cases are controlled and useful for method development, but external validity requires real-world validation and independent human evaluation.
