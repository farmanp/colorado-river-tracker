# Getting Started with Investigative Journalism Playbooks

Quick start guide for using these playbooks with or without OpenClaims integration.

---

## What You Have

### **Core Playbooks** (Ready to Use)
1. ✅ **[Claim Intake & Triage](01-claim-intake.md)** - Evaluate what's worth investigating
2. ✅ **[Source Verification](02-source-verification.md)** - Three-tier verification system
3. ✅ **[Contradiction Protocol](03-contradiction-protocol.md)** - Handle conflicting sources

### **Coming Soon**
4. ⏳ Update & Retraction - Correcting published work
5. ⏳ Collaboration & Handoff - Team workflows
6. ⏳ FOIA & Records Requests - Public records pursuit
7. ⏳ Expert Source Management - Vetting experts
8. ⏳ Automated Data Ingestion - Scraper workflows
9. ⏳ Anomaly Detection - Catching data issues

---

## How to Use (Two Paths)

### **Path 1: Manual (Start Here)**

Use playbooks as checklists without OpenClaims:

1. **Print or bookmark** playbooks you need
2. **Follow step-by-step** for each investigation
3. **Document in markdown** (like `outreach_log.md`)
4. **Track in spreadsheets** or simple files

**Pros:**
- Start immediately, no setup
- Learn workflows through practice
- No technical barriers

**Cons:**
- Manual tracking = risk of missing steps
- Hard to query/audit past decisions
- Limited collaboration features

---

### **Path 2: OpenClaims-Integrated (After Launch)**

Emit structured events as you follow playbooks:

1. **Follow same playbooks** (workflows don't change)
2. **Emit events** using OpenClaims CLI/SDK
3. **Store in collector** (SQLite database)
4. **Query for insights** (audit trail, patterns)

**Pros:**
- Machine-readable provenance
- Queryable audit trail
- API-ready for external consumers
- Team collaboration easier

**Cons:**
- Requires OpenClaims setup
- Learning curve for tooling
- Overkill for single investigation

---

## Quick Start: Using Playbooks Today

### **Scenario: New Tip Arrives**

**Step 1:** Open [Claim Intake & Triage](01-claim-intake.md)

**Step 2:** Fill out intake form (copy template)

**Step 3:** Answer three questions:
- Is it TRUE (verifiable)?
- Is it NEW?
- Does it MATTER?

**Step 4:** Assign priority (HIGH/MEDIUM/LOW/REJECT)

**Step 5:** If HIGH, proceed to [Source Verification](02-source-verification.md)

**Time:** 30-60 minutes for intake

---

### **Scenario: Verifying a Claim**

**Step 1:** Open [Source Verification](02-source-verification.md)

**Step 2:** Identify sources (primary > secondary)

**Step 3:** Obtain source material

**Step 4:** Extract evidence (specific page/paragraph)

**Step 5:** Assess tier (1/2/3)

**Step 6:** Document in code + verification log

**Time:** 1-4 hours per claim depending on complexity

---

### **Scenario: Sources Conflict**

**Step 1:** Open [Contradiction Protocol](03-contradiction-protocol.md)

**Step 2:** Document contradiction (both versions)

**Step 3:** Investigate root cause

**Step 4:** Attempt resolution (contact sources)

**Step 5:** Choose presentation strategy

**Step 6:** Update verification status

**Time:** 2-8 hours depending on complexity

---

## Integration with Colorado River Tracker

### **What's Already Following Playbooks**

**✅ Claim Intake:**
- Reservoir data claims evaluated via triage
- State commitment claims verified as HIGH PRIORITY

**✅ Source Verification:**
- Three-tier system embedded in HTML comments
- All claims tagged with Tier 1/2/3
- Sources documented in inline comments

**✅ Contradiction Protocol:**
- Lake Mead 1936 data bug caught via contradiction
- Scraper validation prevents future contradictions

**✅ Outreach:**
- Pre-publication review following journalism ethics
- Structured response tracking in `outreach_log.md`

### **What Could Use Playbooks**

**⏳ FOIA Requests:**
- No playbook yet for pursuing USBR internal documents
- Could request irrigation district allocation data

**⏳ Expert Interviews:**
- No playbook yet for vetting hydrologists/policy experts
- Could interview academics for context

**⏳ Collaboration:**
- Solo project currently
- Playbook would help if bringing on co-reporter

---

## Adding OpenClaims Later

### **Phase 1: Retroactive Event Emission**

After Colorado River tracker publishes, generate OpenClaims events for existing claims:

**Script concept:**
```python
# export_claims.py
# Reads colorado-river-tracker.html
# Extracts all Tier 1/2/3 claims
# Emits OpenClaims events
# Stores in collector

for state in states:
    emit_claim_event(
        claim_id=f"clm_{state}_cut",
        text=f"{state} pledged {cut} ac-ft cuts",
        tier=state.pledgedTier,
        sources=[...],
        evidence=[...]
    )
```

**Output:** Event stream documenting full verification history

---

### **Phase 2: Live Event Emission**

For future investigations, emit events as you work:

**During intake:**
```bash
openclaims emit claim \
  --text "Arizona increased cut pledge to 800K ac-ft" \
  --type factual \
  --status under_investigation
```

**During verification:**
```bash
openclaims emit verification \
  --claim-id clm_az-800k \
  --result supported \
  --tier 1 \
  --source "KJZZ June 1 2026" \
  --evidence page:7,paragraph:3
```

**After publication:**
```bash
openclaims emit status \
  --claim-id clm_az-800k \
  --status published \
  --published-at "2026-06-15T..."
```

---

### **Phase 3: API Integration**

Expose claims via API for other journalists:

```bash
# Query all Tier 1 claims about Arizona
curl https://api.coloradorivertracker.org/claims?state=Arizona&tier=1

# Get full provenance for specific claim
curl https://api.coloradorivertracker.org/claims/clm_az-760k-cut/provenance

# Export to JSON-LD for semantic web
openclaims export-jsonld clm_az-760k-cut > claim.jsonld
```

**Use cases:**
- Other reporters cite your verified claims
- Academics analyze negotiation history
- Fact-checkers reference your provenance

---

## Best Practices (IRE + ProPublica + ICIJ)

### **From These Playbooks:**

**IRE (Investigative Reporters and Editors):**
- Impact framework (scope, severity, changeability)
- Three questions (TRUE, NEW, MATTERS)

**ProPublica:**
- Tier system for verification
- Public interest focus
- Document everything

**ICIJ (International Consortium):**
- Contradiction handling
- Hierarchy of evidence
- Collaborative workflows

**AP Stylebook:**
- Present uncertainty honestly
- Verify independently
- Attribute clearly

**SPJ Code of Ethics:**
- Seek truth, minimize harm
- Act independently, be accountable

---

## Workflow Example: Full Investigation Cycle

### **Day 1: Intake**
- Tip arrives: "Upper Basin secretly planning cuts"
- Follow [Claim Intake](01-claim-intake.md)
- Assess: TRUE (maybe), NEW (yes), MATTERS (yes if true)
- **Decision:** HIGH PRIORITY

### **Day 2-5: Verification**
- Follow [Source Verification](02-source-verification.md)
- FOIA Upper Basin state water agencies
- Interview UCRC commissioners (on-record)
- Search for primary documents
- **Result:** Cannot verify "secretly" - no evidence of secret plans
- **Revised claim:** "Upper Basin considering voluntary cuts" (Tier 2, single source)

### **Day 6: Contradiction**
- Official statement contradicts source's characterization
- Follow [Contradiction Protocol](03-contradiction-protocol.md)
- Contact original source for clarification
- **Resolution:** Source meant "not publicly announced" not "secret"
- **Update:** Remove loaded language, stick to facts

### **Day 7-10: Outreach**
- Contact all 4 Upper Basin states
- Offer opportunity to comment
- **Responses:** 2 confirm considering, 2 decline comment

### **Day 11: Publish**
- Story: "Two Upper Basin States Consider Voluntary Cuts"
- Based on Tier 2 sources (attributed)
- Includes official responses
- Notes 2 states declined comment

### **Day 12+: Post-Publication**
- Monitor for responses
- Update if new evidence emerges
- Emit OpenClaims events documenting full workflow

**Total time:** ~2 weeks from tip to publication

---

## Common Questions

### **Do I need OpenClaims to use these playbooks?**
No! Playbooks work standalone. OpenClaims adds machine-readable provenance layer.

### **Can I modify these playbooks?**
Yes! Adapt to your needs. These are templates, not rigid rules.

### **What if I'm not a journalist?**
Playbooks apply to any fact-verification work: research, analysis, due diligence.

### **How do I know when to use which playbook?**
Follow the decision trees at end of each playbook. They link to next steps.

### **What if my team uses different tools?**
Playbooks are tool-agnostic. Adapt to your spreadsheets, databases, CMSs, etc.

---

## Next Steps

### **To Start Using Playbooks Today:**
1. Read [Claim Intake & Triage](01-claim-intake.md)
2. Apply to Colorado River tracker retroactively (practice)
3. Use for next investigation

### **To Integrate OpenClaims Later:**
1. Finish Colorado River launch first
2. Write export script for existing claims
3. Test OpenClaims collector with real data
4. Refine based on practice
5. Document as case study for others

### **To Build More Playbooks:**
1. Draft remaining 6 workflows (Update/Retraction, Collaboration, FOIA, Experts, Automation, Anomaly Detection)
2. Test on Colorado River tracker
3. Refine based on practice
4. Share publicly for other journalists

---

## Resources

**Investigative Journalism Standards:**
- IRE: https://www.ire.org/
- ProPublica: https://www.propublica.org/about/
- ICIJ: https://www.icij.org/about/
- SPJ Code of Ethics: https://www.spj.org/ethicscode.asp

**OpenClaims:**
- Spec: `/Users/farman/Documents/openclaims/spec/`
- CLI: `/Users/farman/Documents/openclaims/packages/validator-cli/`
- Python SDK: `/Users/farman/Documents/openclaims/python/`

**Colorado River Tracker:**
- Outreach materials: `outreach_emails.md`, `outreach_log.md`
- Verification log: `fact-check-checklist.md`
- Scraper: `scraper/fetch_reservoirs.py`

---

## Philosophy

**Good journalism is systematic, not heroic.**

These playbooks codify best practices so you can:
- **Reproduce** quality journalism reliably
- **Train** new reporters faster
- **Collaborate** with shared standards
- **Audit** your own work
- **Defend** your methodology publicly

OpenClaims adds a machine-readable layer so:
- **Others can cite** your verified claims
- **Researchers can analyze** patterns
- **Fact-checkers can reference** your provenance
- **AI systems can learn** from your methodology

**Start simple. Add structure as you grow.**

You're ready! Open [Claim Intake & Triage](01-claim-intake.md) and start using playbooks today.
