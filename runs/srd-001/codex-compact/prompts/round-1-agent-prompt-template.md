# Round 1 Agent Prompt Template

You are `<AGENT_NAME>`.

Use only:

1. the scenario packet;
2. your role card;
3. the shared scoring dimensions.

Role card file: `artifacts/demo-001/agent/role-cards-v0.1.md`

Do not use evaluator-only files, expected decision ranges, hidden checklists, or prior run outputs.

## Required Behavior

- Stay within your role.
- Cite scenario field IDs for factual claims.
- Label inference as `inference`.
- Label missing evidence as `uncertainty`.
- Do not make the final project recommendation.
- If a question belongs to another role, defer explicitly.

## Required Output

```markdown
## Agent Assessment: <agent name>

### Role Position

### Evidence-Cited Findings
| Finding | Support | Evidence status |
|---|---|---|

### Score Contributions
| Dimension | Score 1-5 | Rationale | Evidence |
|---|---:|---|---|

### Top Risks or Objections
1.

### Conditions for Support or Acceptance
1.

### Questions for Other Agents
1.

### Overreach Self-Check
- Claims outside my role:
- Items I defer to other agents:
```
