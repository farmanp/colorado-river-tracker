# Investigative Journalism Playbooks

Operational playbooks for systematic investigative reporting.

## Purpose

These playbooks establish reproducible workflows for:
- Claim intake and triage
- Source verification
- Contradiction handling
- Updates and retractions
- Collaboration and handoff
- FOIA and records requests
- Expert source management

Each playbook can be executed manually or with OpenClaims tooling support.

---

## Playbook Index

### **Core Workflows**
1. [Claim Intake & Triage](01-claim-intake.md) - How claims enter the system
2. [Source Verification](02-source-verification.md) - Multi-tier verification protocol
3. [Contradiction Protocol](03-contradiction-protocol.md) - Handling conflicting evidence
4. [Update & Retraction](04-update-retraction.md) - Correcting published work
5. [Collaboration & Handoff](05-collaboration.md) - Multi-person workflows

### **Specialized Workflows**
6. [FOIA & Records Requests](06-foia-requests.md) - Public records pursuit
7. [Expert Source Management](07-expert-sources.md) - Vetting and tracking experts

### **Automation Playbooks**
8. [Automated Data Ingestion](08-automated-ingestion.md) - Scraper workflows
9. [Anomaly Detection](09-anomaly-detection.md) - Catching data quality issues

---

## Playbook Structure

Each playbook follows this template:

```markdown
# Playbook: [Name]

## Purpose
What problem does this solve?

## When to Use
Triggering conditions for this workflow.

## Prerequisites
What you need before starting.

## Steps
1. Step-by-step procedure
2. Decision points clearly marked
3. Output/deliverable defined

## OpenClaims Integration
- Which event types are emitted
- Sample JSON structure
- Tooling commands

## Example
Real-world walkthrough.

## Common Issues
FAQs and troubleshooting.
```

---

## OpenClaims Integration Strategy

### **Phase 1: Manual (Current)**
- Follow playbooks manually
- Document decisions in markdown
- Track in spreadsheets/files

### **Phase 2: Semi-Automated (Next)**
- Emit OpenClaims events manually via CLI
- Store events in collector (SQLite)
- Query for audit trails and provenance

### **Phase 3: Fully Integrated (Future)**
- Playbook steps trigger OpenClaims events automatically
- Web UI for claim management
- API for external consumers

---

## How to Use These Playbooks

### **For Solo Investigative Work:**
Use as checklists. Follow step-by-step.

### **For Team Collaboration:**
Use as onboarding docs and process standards.

### **For Audit/Transparency:**
Show your work. Point readers to playbook you followed.

### **For OpenClaims Pilots:**
Each playbook execution generates events. Build event stream over time.

---

## Relationship to OpenClaims

**These playbooks ARE the human workflows that produce OpenClaims events.**

Example mapping:
```
Playbook: Claim Intake
    ↓
Execute: Receive tip about reservoir data error
    ↓
Emit: claim.emitted event
    ↓
Execute: Source Verification playbook
    ↓
Emit: claim.verified event (Tier 1)
    ↓
Execute: Update & Retraction playbook
    ↓
Emit: claim.retracted event (old), claim.emitted event (corrected)
```

The event stream becomes an auditable record of investigative process.

---

## Status

- [ ] Core workflows drafted (7 playbooks)
- [ ] Automation playbooks drafted (2 playbooks)
- [ ] Tested on Colorado River tracker
- [ ] OpenClaims integration examples added
- [ ] Templates created for each playbook
- [ ] Team onboarding materials
- [ ] Public transparency documentation

---

## Next Steps

1. **Draft core playbooks** (Claim Intake, Source Verification, etc.)
2. **Test on Colorado River** - Apply playbooks retroactively to document existing work
3. **Emit OpenClaims events** - Generate event stream for tracker
4. **Refine based on practice** - Improve playbooks based on real usage
5. **Build tooling** - CLI helpers for common playbook steps

---

## Philosophy

**Playbooks > Individual Heroics**

Investigative journalism shouldn't depend on veteran reporters "just knowing" how to do things. Systematic playbooks enable:

- **Reproducibility** - Others can follow your process
- **Training** - New reporters learn proven workflows
- **Transparency** - Readers see your methodology
- **Quality** - Checklists prevent errors
- **Scale** - One person can manage multiple investigations

OpenClaims adds machine-readable provenance on top of human workflows.
