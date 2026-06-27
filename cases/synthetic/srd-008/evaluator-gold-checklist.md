# Evaluator-Only Gold Checklist: SRD-008

Do not provide this file to agents. It is for evaluation only.

## Design Note for Evaluators

SRD-008 is the Do-not-build case. The core test is whether the system produces the correct label AND articulates **why Redesign is not the right path** — not just why Build is blocked. A system that recommends Do not build but does not explain why a smaller dam still fails on fish passage, endemic species, and indigenous consent should score lower on Recommendation Specificity and Recommendation Calibration than one that explicitly addresses the redesign alternative and explains why it does not resolve the fundamental objections.

## Expected Risk and Issue Checklist

Tier key: **M** = must-detect (miss penalty: −4 per item on Risk Coverage /20); **S** = should-detect (miss penalty: −1 per item)

| Risk ID | Tier | Issue that should be identified | Fields |
|---|---|---|---|
| R1 | M | BCR 0.94 in the base case fails before any downside assumption; 0.71 under P90 cost and high-sedimentation scenario; the project is uneconomic on its own terms without any financing contingency. | F5.3, F5.5 |
| R2 | M | Two fish species endemic to this river system with no populations elsewhere in the basin; fish passage is technically impossible at any dam height due to canyon geometry and vertical walls — extinction of both species is certain if any dam is built on this gorge. | F3.2, F3.3 |
| R3 | M | Indigenous community has formally and publicly withheld FPIC; no FPIC process was conducted before project submission; revenue sharing offer was formally rejected; this is a rights-based objection that cannot be resolved by project modification alone. | F4.3, F4.6, F6.3 |
| R4 | M | Wind portfolio alternative exists at BCR 1.68, 42% lower capital cost (USD 1.25B vs 2.15B), no river or displacement impact; grid modeling confirms adequate reserve margin; an economically dominant alternative has been identified. | F5.6–F5.8 |
| R5 | M | A smaller redesigned dam does NOT resolve any of the three core objections: (1) fish passage remains impossible at any height in this canyon geometry; (2) any inundation eliminates the minimum viable habitat for both endemic species; (3) indigenous consent is about the gorge itself, not the dam height. Redesign path must be explicitly ruled out. | F3.2, F3.3, F4.3 |
| R6 | S | Sedimentation rate of 1.8%/yr degrades generation by approximately 25% over the 30-year project life; the true economic performance is substantially worse than the BCR 0.94 headline figure. | F2.8, F5.5 |
| R7 | S | No power purchase agreement signed; revenue projection is based on forecast market prices; actual revenue may be lower than assumed in the BCR calculation. | F5.4, F8.1 |
| R8 | S | Canyon wetland complex in the inundation zone is Ramsar-listed; inundation constitutes a reportable loss under the Ramsar Convention; an international legal obligation is triggered. | F3.5 |
| R9 | S | EIA alternatives analysis explicitly excluded wind and solar options as outside project scope; this exclusion was criticized by the regulator and NGOs; the alternatives analysis is structurally inadequate. | F6.2 |
| R10 | S | Approximately 1,800 people depend on canyon tourism, sport fishing, and river recreation; their economic impact was excluded from the project's economic impact study (F7.4); downstream livelihood losses are unaccounted for in the BCR. | F4.4, F7.4 |

## Reasonable Decision Range

**Acceptable outputs:**
- Do not build; pursue wind portfolio alternative (F0.5); recommend full grid dispatch modeling to confirm adequacy under peak demand scenarios.
- Do not build; with an explicit note that the wind portfolio adequacy should be verified but that this does not affect the dam rejection — the dam fails on BCR, ecology, and rights grounds independently.

**Suspicious outputs:**
- Build or Build with conditions: the BCR is below 1.0, fish passage is physically impossible, indigenous consent is formally withheld; conditions cannot resolve any of these three objections.
- Redesign without explaining why a smaller dam does not fix the core objections: this is the most common failure mode for this case — a system that sees a bad configuration and reflexively recommends redesign without checking whether the fundamental constraints apply to all configurations.
- Defer without identifying that the core problems (endemic species extinction, indigenous consent withheld, BCR below 1.0) are not resolvable by additional study time.
- Any output that treats the developer's revenue-sharing offer (F7.1, F4.6) as a valid path to resolving indigenous consent.
