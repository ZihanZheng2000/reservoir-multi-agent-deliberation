# Decision Thresholds v0.1

## Purpose

These thresholds guide the Decision Authority. They reduce arbitrary final recommendations and make cross-case decisions more consistent.

## Allowed Labels

| Label | Use when |
|---|---|
| Build | Benefits are strong, evidence is mature, and no unresolved blocker remains. |
| Build with conditions | Benefits are strong and no critical blocker remains, but implementable conditions must be satisfied before construction or operation. |
| Redesign | Project need is credible, but current design creates avoidable harms or unacceptable tradeoffs that may be reduced by design changes. |
| Defer | Key evidence, legal readiness, safeguard readiness, or financing readiness is missing; decision should wait for resolution. |
| Do not build | Benefits are weak, or severe harms appear non-mitigable, or alternatives dominate. |

## Compound Labels

A recommendation may combine two adjacent labels when separate conditions apply simultaneously:

| Compound label | Use when |
|---|---|
| Redesign + Defer | The current design must be changed before build approval (Redesign), AND key evidence or safeguard readiness is also missing such that even a redesigned project cannot be approved yet (Defer). Final build approval is deferred pending both redesign completion and evidence resolution. |

When using a compound label, state each component separately in the recommendation output and list conditions under the relevant component.

## Blocker Definitions

| Blocker type | Meaning |
|---|---|
| Evidence blocker | Missing information could materially change the decision. |
| Legal/governance blocker | Approval, EIA, consultation, safeguard, or permit readiness is incomplete. |
| Social blocker | Displacement, livelihood, cultural, consent, or grievance issues are unresolved at a level that undermines legitimacy. |
| Ecological blocker | Irreversible or high-severity ecological harm is likely and mitigation is unproven. |
| Financial blocker | Project cannot be financed or has weak downside economic viability. |
| Safety blocker | Engineering, spillway, geotechnical, or emergency-preparedness issue prevents responsible approval. |

## Decision Logic

1. If any critical blocker is unresolved and cannot be addressed by conditions before construction, do not issue `Build`.
2. If blockers are mostly about missing evidence or procedural readiness, prefer `Defer`.
3. If blockers are caused by the current design but the project need remains credible, prefer `Redesign`.
4. If redesign is recommended, state whether final build approval is deferred.
5. If immediate action is needed but irreversible construction is not ready, recommend phased or emergency non-structural action where applicable.
6. If benefits are weak or harms appear non-mitigable, recommend `Do not build`.

## Required Final Recommendation Fields

- recommendation label;
- whether final build approval is granted or deferred;
- decisive benefits;
- unresolved blockers;
- conditions;
- minority reports;
- evidence confidence.
