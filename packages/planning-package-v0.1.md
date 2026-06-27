# Planning Package v0.1

## Project

**Working title:** Role-Limited Multi-Agent Deliberation for Reservoir Construction Decision Support

**Gate status:** Draft for Planning Gate review. Not yet approved for Modeling.

## User-Need Profile

- **Research area:** LLM-based multi-agent systems, environmental decision support, reservoir/hydropower project assessment, stakeholder deliberation.
- **Intended output:** A research prototype and manuscript-ready evidence package.
- **Workflow mode:** Demo-first research workflow.
- **Idea maturity:** Partly formed idea.
- **Planning depth:** Light-to-full calibration. A focused scoping literature review is required before strong novelty claims.
- **Intended research product:** Method framework + synthetic benchmark + decision-support prototype.
- **Research purpose:** Build and evaluate a role-limited multi-agent deliberation system for reservoir construction decisions.
- **Practical success criterion:** The system can process a structured reservoir scenario, produce expert/stakeholder assessments, expose conflicts, audit evidence, generate multi-dimensional scores, and issue a Build / Do not build / Defer / Redesign recommendation.
- **Target audience or venue:** AI for decision support, environmental informatics, water resources management, or AI governance venues. Exact venue undecided.
- **Venue/output status:** Provisional.
- **Preferred citation or formatting style:** To be selected after target venue calibration.
- **Available data:** No real project dataset yet. Start with synthetic scenario packets.
- **Public data needed:** Later phase may use public EIA documents, hydropower sustainability reports, government project documents, or case-study materials.
- **Time/tooling constraints:** First priority is a small runnable demo, not a full real-world validation.
- **Runtime or API/token constraints:** Keep demo small enough to run with a bounded number of agent calls.
- **Method-complexity limit:** Use a transparent orchestration workflow before complex learning or fine-tuning.
- **Novelty expectation:** Moderate to high if the role-limited expert/stakeholder architecture, evidence audit, and evaluation metrics are clearly specified.
- **Topics, methods, or data types to avoid:** Avoid pretending that synthetic cases prove real-world policy validity. Avoid unsupported claims of expert equivalence.
- **Gate mode:** Real user gates.

## Planning Depth Decision

| Item | Decision | Reason | Downstream implication |
|---|---|---|---|
| idea maturity | partly formed | The system concept is clear, but literature position, benchmark design, and evaluation metrics need refinement. | Proceed with a focused planning package and then a demo. |
| literature/prior-work scan depth | focused scoping review | Need to verify related work in MCDA/optimization, hydropower sustainability assessment, stakeholder participation, and LLM multi-agent deliberation. | Required before manuscript novelty claims. |
| novelty assessment depth | light now, deeper before writing | Current gap is plausible but not yet fully validated. | Demo can proceed with provisional claim level. |
| venue/output calibration depth | deferred | No target venue yet. | Revisit before Writing. |
| revisit trigger | before real-case validation and before manuscript drafting | Stronger literature and venue scan needed for paper. | Planning addendum likely needed. |

## Clarifications Before Planning

| Question or ambiguity | Resolution | Effect on plan |
|---|---|---|
| Real case or synthetic case first? | Start with an idealized synthetic case; real case becomes later validation. | Modeling begins with a synthetic benchmark/demo. |
| Should agents represent experts or stakeholders? | Use both, plus governance agents. | Architecture has three groups: expert agents, stakeholder agents, governance agents. |
| Who gives final decision? | Simulate a decision authority, but keep human final approval. | System outputs recommendation, not binding policy decision. |
| Is yes/no enough? | No. Need yes/no plus scores, debate report, evidence traceability, and risk list. | Output schema must include all four. |
| What is the main contribution? | AI method contribution applied to realistic reservoir decision deliberation. | Paper framing should lead with framework/method, not only tool demo. |

## Prior Work, Skill Patterns, and Gaps

This is a provisional scoping summary, not a completed literature review.

| Cluster or source | What has been done | Reusable skill or method pattern | Gap or opportunity | Relevance to this plan |
|---|---|---|---|---|
| Hydropower Sustainability Assessment Protocol / hydropower sustainability standards | Provides multi-dimensional sustainability assessment across social, environmental, business, and technical topics. | Use as a domain-grounded source for assessment dimensions and agent responsibilities. | Existing protocols structure assessment but do not provide LLM-based role-limited deliberation. | Strong basis for scenario dimensions and scoring rubrics. |
| World Commission on Dams and stakeholder governance literature | Frames dam decisions as multi-stakeholder governance problems with environmental, social, economic, and political conflict. | Use to justify stakeholder and decision-authority simulation. | Does not offer executable multi-agent AI workflow. | Supports the decision-meeting framing. |
| MCDA / multi-objective optimization for water and hydropower decisions | Converts multiple objectives into weights, scores, tradeoffs, or optimization objectives. | Use as baseline: weighted scoring or MCDA-style aggregation. | Often compresses conflict into weights and may not preserve deliberation, objections, or role-specific reasoning. | Provides a clear non-LLM baseline. |
| LLM multi-agent decision-making and debate | Uses multiple agents for debate, negotiation, simulation, or decision improvement. | Use role profiles, deliberation rounds, moderator, and judge/auditor patterns. | Often lacks domain-specific evidence audit and realistic infrastructure governance structure. | Provides AI-method baseline and vocabulary. |
| Environmental decision-support systems | Support ecological or infrastructure planning using GIS, rules, decision models, or workflows. | Use evidence inventory and decision-support output conventions. | Less focused on LLM role boundaries and stakeholder debate. | Useful for tool-output design. |

## Proposed Gap

Existing reservoir and hydropower decision methods commonly use sustainability protocols, environmental and social impact assessment, MCDA, or optimization. These methods can structure decision criteria, but they tend to compress disagreements into weights, scores, or expert reports.

Existing LLM-based multi-agent systems can simulate debate, negotiation, and decision-making, but they often lack domain-specific evidence discipline, explicit stakeholder governance structure, and mechanisms that prevent each agent from becoming a generic all-knowing consultant.

This project targets the gap between these two traditions:

> A reservoir construction decision-support framework that models both domain expertise and stakeholder conflict through role-limited agents, evidence auditing, and simulated decision authority.

## Approved Research Question

Draft, not yet final:

> Can a role-limited multi-agent deliberation system improve reservoir construction decision support by identifying risks, exposing stakeholder conflicts, preserving evidence traceability, and producing transparent Build / Do not build / Defer / Redesign recommendations compared with single-agent and weighted-score baselines?

## Working Title

`Role-Limited Multi-Agent Deliberation for Reservoir Construction Decision Support`

## Hypotheses or Expected Claims

- A role-limited multi-agent system will identify a broader and more diverse set of reservoir project risks than a single-agent LLM baseline.
- Separating expert agents from stakeholder agents will make value conflicts more explicit than a weighted-score baseline.
- Evidence auditing will reduce unsupported claims and make final recommendations more inspectable.
- A decision-authority layer can generate more realistic recommendations than simple voting among agents.
- The system's strongest contribution is not replacing human decision-makers, but producing a transparent, auditable deliberation package.

## System Architecture

### Expert Agents

These agents represent technical knowledge boundaries.

| Agent | Main responsibility | Role boundary |
|---|---|---|
| Hydrologist | Water availability, flood control, hydrological variability, drought risk. | Should not decide social acceptability or financial viability. |
| Dam Safety / Civil Engineer | Structural feasibility, geology, construction and maintenance risks, dam safety. | Should not override ecological or resettlement concerns. |
| Ecologist | Biodiversity, aquatic ecosystems, downstream flows, water quality, habitat fragmentation. | Should not decide project finance. |
| Climate Risk Expert | Future precipitation, extreme events, climate robustness, long-term uncertainty. | Should not replace hydrologist or engineer but can challenge assumptions. |
| Economist / Finance Expert | Cost-benefit, economic viability, opportunity cost, project financing. | Should not reduce non-market harms to money without caveats. |
| Social Impact / Resettlement Expert | Displacement, livelihoods, compensation, cultural heritage, vulnerable groups. | Should not decide technical hydrology. |
| Legal / Policy Expert | EIA requirements, permits, compliance, water rights, public participation, cross-border issues if relevant. | Should not create policy claims without evidence. |

### Stakeholder Agents

These agents represent interests, lived impacts, institutional goals, and legitimacy concerns.

| Agent | Main interest | Typical stance |
|---|---|---|
| Project Developer / Utility | Construction feasibility, power generation, revenue, project delivery. | Usually supportive if financial/technical risks are manageable. |
| Central or Regional Government | Public welfare, energy/water security, development goals, legal legitimacy. | Conditional support if public-interest case is strong. |
| Local Government | Jobs, tax base, local infrastructure, social stability. | May support benefits but worry about local conflict. |
| Upstream Affected Residents | Land loss, resettlement, compensation, cultural and livelihood disruption. | Often concerned or opposed unless compensation and consent are credible. |
| Downstream Users / Farmers / Fishers | Flow changes, irrigation, fisheries, flood/drought exposure. | Conditional or opposed depending on downstream flow guarantees. |
| Environmental NGO | Biodiversity, river connectivity, irreversible ecological harm, alternatives. | Often critical unless mitigation and alternatives are strong. |
| Financier / Development Bank | Investment risk, ESG compliance, safeguards, reputational risk. | Conditional on evidence, safeguards, and stakeholder support. |

### Governance Agents

These agents control deliberation and recommendation.

| Agent | Function | Output |
|---|---|---|
| Moderator | Runs deliberation rounds, asks agents to respond to objections, prevents repetition. | Structured debate log. |
| Evidence Auditor | Checks whether claims cite scenario facts, data fields, rules, or assumptions. | Evidence audit table and unsupported-claim flags. |
| Decision Authority | Simulates government/regulatory decision logic. | Build / Do not build / Defer / Redesign recommendation with rationale. |
| Human Final Approver | User/researcher gatekeeper. | Accepts, rejects, or revises the system recommendation. |

## Synthetic Benchmark Design

### Demo Scenario

Create one idealized reservoir proposal with structured facts:

- medium-sized reservoir on a river basin;
- intended benefits: urban water supply, flood control, hydropower, irrigation reliability;
- expected harms: habitat loss, fish migration disruption, altered downstream flow, resettlement, cultural heritage risk;
- uncertain conditions: climate change, sedimentation, cost overrun, compensation credibility;
- alternatives: smaller reservoir, demand management, watershed restoration, solar/wind plus water conservation, redesign with environmental flow guarantees.

### Scenario Packet Schema

The synthetic scenario should include:

- project description;
- location and basin context;
- hydrological assumptions;
- expected storage and yield;
- flood-control benefits;
- hydropower output if relevant;
- cost and financing assumptions;
- affected population and resettlement details;
- ecological indicators;
- downstream user dependencies;
- legal and permitting status;
- mitigation measures;
- known uncertainties;
- stakeholder statements;
- decision alternatives.

### Output Schema

The system must produce:

1. agent-specific assessment;
2. multi-dimensional score matrix;
3. stakeholder conflict map;
4. debate transcript or structured deliberation log;
5. evidence audit table;
6. risk register;
7. final recommendation: Build / Do not build / Defer / Redesign;
8. recommendation rationale and minority reports.

## Scoring Dimensions

Draft dimensions:

| Dimension | Meaning |
|---|---|
| Water supply benefit | Contribution to reliable water availability. |
| Flood-control benefit | Expected reduction in flood risk. |
| Energy benefit | Hydropower generation or grid value, if applicable. |
| Economic viability | Cost-benefit, financing, opportunity cost, cost-overrun risk. |
| Engineering feasibility | Construction, geological, safety, and maintenance feasibility. |
| Ecological impact | Biodiversity, flow regime, habitat, water quality, cumulative impacts. |
| Social impact | Resettlement, livelihoods, cultural heritage, distributive justice. |
| Legal and governance risk | Permits, EIA adequacy, public participation, compliance. |
| Climate robustness | Performance under future climate uncertainty and extremes. |
| Stakeholder support | Degree and distribution of support/opposition among directly affected groups. |
| Evidence confidence | Whether claims are supported, uncertain, or unsupported. |

## Baselines

| Baseline | Purpose |
|---|---|
| Single-agent LLM decision analyst | Tests whether multi-agent structure adds value beyond one strong generalist model. |
| Weighted-score MCDA baseline | Tests whether deliberation adds value beyond fixed criteria and weights. |
| Expert-only multi-agent system | Tests whether stakeholder agents add conflict and legitimacy insight. |
| Stakeholder-only multi-agent system | Tests whether technical expert agents improve evidence and feasibility quality. |
| Multi-agent without evidence auditor | Tests whether audit layer improves traceability and reduces unsupported claims. |

## Evaluation Metrics

### Risk Discovery

- number of unique risks identified;
- coverage across technical, ecological, social, economic, legal, and climate categories;
- number of high-severity risks missed by each baseline.

### Conflict Articulation

- number of explicit stakeholder conflicts identified;
- clarity of who benefits, who bears cost, and why;
- whether conflicts are linked to evidence rather than generic statements.

### Role Fidelity

- percentage of claims within each agent's role boundary;
- number of overreach violations;
- whether agents preserve domain-specific blind spots instead of becoming generic consultants.

### Evidence Traceability

- percentage of claims linked to scenario facts, assumptions, source fields, or explicit uncertainty;
- number of unsupported claims;
- number of claims corrected or softened after evidence audit.

### Decision Quality

- recommendation includes yes/no/defer/redesign logic;
- recommendation explains decisive evidence and decisive uncertainty;
- minority or dissenting views are preserved;
- decision is stable under prompt/order perturbation.

### Deliberation Quality

- debate produces new risks, reframings, or conditions;
- agents respond to objections instead of repeating initial positions;
- final recommendation reflects conflicts rather than hiding them.

## Data Plan

- **Primary data source:** Synthetic structured scenario generated by the research team.
- **Backup data source:** A second synthetic scenario with different tradeoffs.
- **Exact raw data host:** Local project files in a later `artifacts/` directory.
- **Official data source:** Not applicable for synthetic demo.
- **Documentation source:** Scenario-generation notes and rubric.
- **Data version or access date:** To be recorded during Modeling.
- **License/access status:** Internal research artifact.
- **Acquisition success rule:** Scenario packet counts as usable only if it contains all fields required by the agent prompts and scoring rubric.
- **Minimum viable data scale:** One synthetic scenario.
- **Full-study data scale:** 5-10 synthetic scenarios plus 1-2 real cases if public data are accessible.
- **Key variables:** Benefits, harms, risks, uncertainties, stakeholders, mitigation, alternatives.
- **Unit of analysis:** Reservoir project proposal.
- **Time/spatial coverage:** Synthetic; later real-case coverage depends on selected case.
- **Access or licensing concerns:** Low for synthetic demo; real cases require source and license review.

## Method Blueprint

1. Build one structured synthetic reservoir scenario packet.
2. Create role cards for expert, stakeholder, and governance agents.
3. Run independent first-round assessments from expert and stakeholder agents.
4. Convert assessments into a preliminary score matrix and risk register.
5. Run a moderated deliberation round where agents challenge each other's assumptions.
6. Run evidence audit on claims, scores, and objections.
7. Ask agents to revise or defend claims flagged by the auditor.
8. Decision authority generates Build / Do not build / Defer / Redesign recommendation.
9. Compare outputs against baselines.
10. Evaluate risk discovery, conflict articulation, role fidelity, evidence traceability, and decision quality.

## Expected Manuscript Package

- **Figures:**
  - system architecture diagram;
  - deliberation workflow diagram;
  - role-boundary design diagram;
  - risk/conflict heatmap;
  - evidence-traceability comparison across baselines.
- **Tables:**
  - agent roles and boundaries;
  - scenario packet schema;
  - scoring rubric;
  - baseline comparison;
  - evaluation metrics;
  - example decision recommendation output.
- **Likely method/conceptual visuals:**
  - expert/stakeholder/governance three-layer architecture;
  - evidence-audited deliberation loop.
- **Claim-evidence map:**
  - method claims supported by demo outputs;
  - domain claims supported by hydropower sustainability and stakeholder governance literature;
  - AI claims supported by multi-agent decision-making literature.
- **Limitations to acknowledge:**
  - synthetic scenarios cannot prove real-world policy validity;
  - LLM agents are not actual experts or stakeholders;
  - role prompts may encode researcher assumptions;
  - evaluation of deliberation quality remains partly judgment-based;
  - real-world validation requires public case data and possibly domain expert review.
- **Reproducibility artifacts:**
  - scenario packet;
  - agent role cards;
  - orchestration script or notebook;
  - prompts;
  - raw outputs;
  - scoring/evaluation rubric;
  - run log.

## External Tool and Skill Scan

| Candidate tool, package, template, or skill | Workflow task | Maturity or reason to trust | Output to bring back | Cost/access/limits | Decision |
|---|---|---|---|---|---|
| Hydropower Sustainability Assessment Protocol / related sustainability standards | domain rubric | Internationally recognized hydropower sustainability framework | assessment dimensions and topic coverage | may require careful source verification | reuse as domain basis |
| MCDA methods | baseline | mature decision-analysis tradition | weighted score baseline | weights may be subjective | reuse as baseline |
| LLM multi-agent frameworks | orchestration | active AI research area | agent orchestration patterns | implementation complexity varies | adapt selectively |
| Academic Research Suite | planning/lit review/review | available workflow skill | scoping review and critique notes | must verify citations | reuse |
| CCF-Figure or diagram tool | conceptual figures | useful for AI/CS paper figures | architecture diagrams | not empirical evidence | defer to Writing/Reporting |

## Skill Construction Decision

| Skill need | External alternative checked | Why external option is sufficient or insufficient | Decision | Promotion status |
|---|---|---|---|---|
| Reservoir deliberation role-card generation | General LLM prompting, hydropower protocols | Existing tools do not encode project-specific role boundaries and overreach rules. | create project-specific role cards during Modeling | project-specific |
| Evidence-audited deliberation loop | Generic multi-agent debate | Debate alone does not enforce evidence traceability. | create project-specific orchestration protocol | project-specific |
| Synthetic scenario generator | Manual writing, benchmark templates | Manual scenario is enough for demo; generator can come later. | no skill needed now | none |

## Research Opportunities Considered

| Opportunity | Prior-work basis | Feasibility | Novelty | Decision |
|---|---|---|---|---|
| Synthetic role-limited multi-agent reservoir deliberation benchmark | LLM multi-agent + hydropower sustainability + stakeholder governance | high | moderate/high | selected |
| Real-world dam case validation | EIA and public case-study documents | uncertain | high | backup / phase 2 |
| Fine-tuning agents for negotiation | LLM negotiation literature | low for first demo | moderate | future work |
| Pure MCDA reservoir decision model | MCDA literature | high | low | baseline only |

## Feasibility and Cost Check

| Item | Assessment | Evidence or test | Fallback |
|---|---|---|---|
| data access | feasible for synthetic, uncertain for real cases | synthetic scenario can be locally authored | use synthetic-only demo |
| text/table/image/API extractability | feasible for synthetic | structured scenario packet | no extraction needed in demo |
| candidate sources vs usable acquired data | candidate literature exists; usable real case not acquired | focused scoping scan only | do not claim real-case validation yet |
| demo scale | one scenario, all agents, one deliberation loop | manageable | reduce number of agents if cost is high |
| full-study scale | 5-10 synthetic scenarios + 1-2 real cases | later phase | synthetic benchmark only |
| runtime/storage burden | low to moderate | mostly text outputs | batch runs can be capped |
| API/token cost | uncertain but controllable | limit turns and output schema | use fewer baselines |
| external tool or skill feasibility | feasible | existing skills and simple scripts | manual orchestration |
| licensing/privacy/ethics | low for synthetic; real cases require review | synthetic data has no privacy risk | postpone real-case data |

## Data Source Identity

| Role | Source name or URL | Version/date/access date | License/access status | Notes |
|---|---|---|---|---|
| raw data host | local synthetic scenario packet | TBD | internal | Not real-world data. |
| official data source | none for synthetic demo | N/A | N/A | Real-case phase will need official source identity. |
| documentation source | scenario design notes | TBD | internal | Must record assumptions. |
| citation source | hydropower sustainability and stakeholder governance literature | TBD | public/varied | Must verify before manuscript use. |

## Venue or Output Calibration

| Candidate venue/output | Why it fits | Tradeoffs | Decision |
|---|---|---|---|
| AI decision-support workshop/conference paper | Method contribution and baseline comparison fit. | Needs clear AI novelty and evaluation. | candidate |
| Environmental informatics / water resources journal | Domain application fit. | Requires stronger real-case validation and domain literature. | candidate |
| Demo/prototype technical report | Fast and feasible. | Lower publication value. | backup |
| Preprint | Can document framework and demo early. | Needs careful claim limitation. | possible |

Official venue requirements and exemplar scan are deferred until after demo feasibility is established.

## Candidate Research Plans Considered

| Plan | RQ | Data | Method | Venue/output fit | Decision |
|---|---|---|---|---|---|
| Synthetic benchmark first | Can role-limited multi-agent deliberation improve reservoir decision support on controlled scenarios? | synthetic scenario packets | multi-agent orchestration + baselines | AI methods / prototype paper | selected |
| Real case first | Can the system evaluate a real reservoir project? | public EIA/project documents | document extraction + multi-agent deliberation | water resources / environmental informatics | backup |
| Tool-only prototype | Can we build a useful reservoir decision tool? | synthetic or user-provided | UI/tool workflow | internal/demo | future |

## Risks and Gate Notes

| Risk | Severity | Mitigation |
|---|---|---|
| Project becomes a prompt demo without research contribution. | high | Define baselines, metrics, and role-boundary evaluation before demo. |
| Synthetic case lacks realism. | medium | Ground scenario fields in hydropower sustainability and EIA categories. |
| Agents become generic all-knowing advisors. | high | Use strict role boundaries and role-fidelity scoring. |
| Final yes/no hides uncertainty. | high | Include Defer and Redesign recommendations plus uncertainty and minority reports. |
| Evidence audit is too shallow. | medium | Require every claim to link to scenario field, assumption, or cited source. |
| Evaluation metrics are subjective. | medium | Use rubric-based human review plus countable indicators where possible. |
| Real-case validation data unavailable. | medium | Treat real case as phase 2, not required for demo success. |

## Acceptance Rubric for Model Stage

The Model stage can begin when:

- the user approves synthetic benchmark first;
- the research question and claim level are accepted as provisional;
- the three-layer agent architecture is accepted;
- the minimum synthetic scenario fields are defined;
- the output schema is accepted;
- baselines are accepted;
- evaluation metrics are accepted;
- the demo is explicitly labeled as a proof-of-concept, not real-world policy validation.

## Recommended Next Step

Proceed to Modeling demo after Planning Gate approval:

1. create the synthetic reservoir scenario packet;
2. write role cards for all agents;
3. write the evidence-audited deliberation protocol;
4. run one complete demo;
5. produce a Modeling Package with outputs, limitations, and baseline comparison plan.

## Planning Gate Prompt

This Planning Package proposes a demo-first route for a role-limited multi-agent reservoir construction decision-support system.

If approved, Modeling should start with one synthetic reservoir scenario and pause at a Demo Gate after the first complete run. Alternative routes are:

- revise the research question;
- reduce the number of agents;
- add a focused literature review before demo;
- search for a real case before synthetic demo;
- terminate or archive the idea.
