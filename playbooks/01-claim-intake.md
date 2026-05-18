# Playbook: Claim Intake & Triage

Based on IRE (Investigative Reporters and Editors) and ProPublica methodologies.

## Purpose

Systematically evaluate incoming claims for investigation worthiness. Not every tip, press release, or data point warrants full investigation. This playbook helps you decide what to pursue.

---

## When to Use

- Receiving tips from sources
- Press releases from agencies
- FOIA responses arrive
- Automated scrapers flag anomalies
- Public documents released
- Story idea brainstorming

---

## The Three Questions (ProPublica Method)

Every claim must pass **all three** before investigation:

### **1. Is it TRUE?**
Can this be verified with available evidence?

**Red flags:**
- Anonymous tip with no documentation
- Claim requires insider access you don't have
- "Everyone knows" but no documents exist
- Timeframe for verification exceeds publication needs

**Green lights:**
- Public records exist (FOIA-able)
- Multiple people can confirm
- Data is released regularly (government, academic)
- Physical evidence exists

---

### **2. Is it NEW?**
Has this already been reported thoroughly?

**Red flags:**
- Well-covered by major outlets
- Common knowledge in the field
- Just restating press releases

**Green lights:**
- New angle on known issue
- First to obtain/analyze primary documents
- Connects dots others haven't
- Local impact of national story

**Note:** "Not new but needs accountability tracking" can still pass (like Colorado River cuts).

---

### **3. Does it MATTER?**
Will this change behavior, policy, or public understanding?

**Red flags:**
- Affects very few people
- No policy implications
- Interesting but inconsequential
- "So what?" test fails

**Green lights:**
- Affects large population (40M Colorado River users)
- Public money/resources at stake
- Safety/environmental impact
- Reveals systemic issues
- Holds power accountable

---

## Claim Intake Form

Use this template for every incoming claim:

```markdown
# Claim Intake: [Short Title]

**Date received:** YYYY-MM-DD
**Source:** [How did this come to you?]
**Reporter:** [Your name]

## Claim Statement

[Write claim as precisely as possible, one sentence]

## Initial Assessment

**Is it TRUE (verifiable)?**
- [ ] Yes - sources identified
- [ ] Probably - need to investigate
- [ ] No - cannot verify
- [ ] Unknown - more research needed

**Evidence path:**
[What sources would verify this? FOIA, interviews, data analysis?]

**Is it NEW?**
- [ ] Yes - not previously reported
- [ ] Angle is new
- [ ] No - well-covered
- [ ] Unknown - need clips search

**Previous coverage:**
[Links to existing reporting, if any]

**Does it MATTER?**
- [ ] Yes - significant impact
- [ ] Moderate - worth pursuing if true
- [ ] No - low impact
- [ ] Unknown - depends on findings

**Who's affected:**
[Population size, stakeholders, public interest]

**Policy/behavior change potential:**
[What could change if this is published?]

## Triage Decision

- [ ] **HIGH PRIORITY** - Investigate immediately
- [ ] **MEDIUM PRIORITY** - Investigate when capacity allows
- [ ] **LOW PRIORITY** - Monitor, revisit if new evidence emerges
- [ ] **REJECT** - Does not meet standards, archive

**Reasoning:**
[Why this priority level?]

## Investigation Plan (if pursuing)

**Estimated effort:** [Hours/days/weeks]

**Key sources to pursue:**
1. [Primary source 1]
2. [Primary source 2]
3. [Backup sources]

**Skills/resources needed:**
- [ ] Data analysis
- [ ] FOIA requests
- [ ] Expert interviews
- [ ] Legal review
- [ ] Other: _______

**Dependencies:**
[What needs to happen before you can verify?]

**Deadline:** [If time-sensitive]

## OpenClaims Event

```json
{
  "event_type": "claim.emitted",
  "claim": {
    "claim_id": "clm_[generate]",
    "text": "[exact claim statement]",
    "claim_type": "factual",
    "status": "under_investigation",
    "priority": "high|medium|low",
    "investigation_opened_at": "2026-05-17T..."
  },
  "producer": {
    "agent_type": "human",
    "name": "[reporter name]"
  },
  "context": {
    "source_of_tip": "[where this came from]",
    "public_interest": "[why it matters]"
  }
}
```
```

---

## Triage Workflow

### **Step 1: Rapid Assessment (5 minutes)**

**Answer YES/NO:**
1. Can I verify this with public records or on-record sources?
2. Is the timeframe realistic for my capacity?
3. Does this pass the "so what?" test?

**If 3 YES → Continue to Step 2**
**If any NO → Document reason, archive**

---

### **Step 2: Clips Check (15 minutes)**

**Search existing coverage:**
- Google News: "[key terms] site:propublica.org OR site:nytimes.com OR site:revealnews.org"
- LexisNexis (if available)
- Outlet-specific archives

**Question:** Has this specific angle been covered?

**If novel OR adds accountability → Continue to Step 3**
**If thoroughly covered → Reject OR reframe angle**

---

### **Step 3: Source Mapping (30 minutes)**

**List all potential sources:**

**Primary (government, academic):**
- FOIA-able documents: ___________
- Public data: ___________
- Official reports: ___________

**Secondary (experts, stakeholders):**
- Who would know?: ___________
- Who's affected?: ___________
- Who's responsible?: ___________

**Question:** Can I reach Tier 1 verification with these sources?

**If YES → Continue to Step 4**
**If NO but close → MEDIUM PRIORITY (pursue if capacity)**
**If NO and far → Reject**

---

### **Step 4: Impact Assessment (15 minutes)**

**IRE Impact Framework:**

**Scope:** How many people affected?
- 1K-10K: Local
- 10K-100K: Regional
- 100K-1M: State
- 1M+: National

**Severity:** What's at stake?
- Money: $_______ public funds
- Safety: Health/environmental risk level
- Rights: Discrimination, access, due process
- Democracy: Transparency, accountability

**Changeability:** Can reporting create change?
- Policy reform potential: High / Medium / Low
- Behavior change potential: High / Medium / Low
- Accountability potential: High / Medium / Low

**If 2+ HIGH ratings → HIGH PRIORITY**
**If 1 HIGH or 2+ MEDIUM → MEDIUM PRIORITY**
**Otherwise → LOW PRIORITY**

---

### **Step 5: Assign Priority**

**HIGH PRIORITY (start immediately):**
- All three questions are strong YES
- Significant public impact (1M+ affected OR major policy implications)
- Time-sensitive (legislative session, deadline, event)
- Exclusive or first-to-report opportunity

**MEDIUM PRIORITY (pursue when capacity allows):**
- Verifiable but requires more effort
- Moderate impact
- New angle on known issue
- Builds on previous reporting

**LOW PRIORITY (monitor, revisit):**
- Verifiable but unclear impact
- Interesting but not urgent
- May become HIGH if new evidence emerges

**REJECT:**
- Cannot verify with available sources
- Already thoroughly reported with no new angle
- Fails "so what?" test
- Outside scope/mission

---

## SPJ Code of Ethics Integration

Every intake decision must respect:

**Seek Truth and Report It:**
- Verify before investigating (don't pursue unverifiable claims)
- Consider all sides (who benefits from this being/not being true?)

**Minimize Harm:**
- Does investigation risk outing confidential sources?
- Could publicity harm vulnerable people?
- Is the public interest strong enough to justify potential harm?

**Act Independently:**
- Does this claim come from a biased source?
- Are you being manipulated into a particular narrative?
- Can you verify independently of the source pushing this?

**Be Accountable:**
- Document why you pursued or rejected this claim
- Be transparent about limitations of available evidence

---

## Common Intake Sources

### **1. Press Releases**

**Triage approach:**
- Default to MEDIUM (verify claims, don't just repackage)
- Look for what's NOT said (gaps are often the story)
- Cross-reference with previous releases (changed position?)

**Red flag:** PR designed to preempt negative story
**Green light:** Official data release that enables new analysis

---

### **2. Tips from Sources**

**Triage approach:**
- Evaluate source motivation (whistleblower? grudge? competitor?)
- Require documentation or path to documentation
- Protect confidentiality during evaluation

**Red flag:** Anonymous tip with no verification path
**Green light:** Document provided + corroboration path clear

---

### **3. Automated Scrapers**

**Triage approach:**
- Validate data quality first (parse errors? anomalies?)
- Compare to baseline/historical (is change significant?)
- Determine if change is newsworthy or just noise

**Red flag:** Scraper error mistaken for real change
**Green light:** Statistically significant change + context matters

---

### **4. FOIA Responses**

**Triage approach:**
- Assess completeness (heavy redactions? missing pages?)
- Look for unexpected revelations
- Compare to what agency said publicly

**Red flag:** Heavily redacted with no newsworthy unredacted content
**Green light:** Contradicts official narrative OR reveals new data

---

## Examples from Colorado River Tracker

### **Example 1: Reservoir Elevation Data**

**Claim:** "USBR publishes hourly reservoir elevations"

**Triage:**
- TRUE: Verified USBR endpoints exist, data is public
- NEW: Not the data itself, but automated accountability tracking is new angle
- MATTERS: 40M people depend on these reservoirs, negotiations ongoing

**Decision:** HIGH PRIORITY (became core feature of tracker)

**Impact:** Automated monitoring enables real-time accountability

---

### **Example 2: State Cut Commitments**

**Claim:** "Arizona pledged 760K ac-ft cuts, California 440K, Nevada 50K"

**Triage:**
- TRUE: Press releases + news coverage confirm
- NEW: No public tracker showing pledged vs delivered distinction
- MATTERS: $1.4T economy at stake, Dec 2026 deadline

**Decision:** HIGH PRIORITY (became Priority 1 feature: Pledged vs Delivered)

**Impact:** Distinguishes commitments from actions, prevents greenwashing

---

### **Example 3: Individual Farmer Water Use (REJECTED)**

**Claim:** "Farmer John Smith uses X acre-feet per year"

**Triage:**
- TRUE: Potentially verifiable through water district records
- NEW: Individual-level data not typically reported
- MATTERS: Fails "so what?" test - individual usage not policy-relevant

**Decision:** REJECT (privacy concerns, no public interest in single farmer)

**Lesson:** Focus on systemic issues, not individual blame

---

## Decision Matrix

| TRUE? | NEW? | MATTERS? | Priority | Action |
|-------|------|----------|----------|---------|
| ✅ | ✅ | ✅ | HIGH | Investigate now |
| ✅ | ✅ | ⚠️ | MEDIUM | Investigate if capacity |
| ✅ | ⚠️ | ✅ | MEDIUM | Find new angle or reject |
| ✅ | ❌ | ✅ | LOW | Monitor for new developments |
| ❌ | Any | Any | REJECT | Cannot verify |
| Any | ❌ | ❌ | REJECT | Fails newsworthiness + impact |

---

## Output

**For HIGH PRIORITY claims:**
1. Create investigation ticket/folder
2. Emit OpenClaims claim.emitted event
3. Assign to reporter (yourself or team member)
4. Set target completion date
5. Begin [Source Verification](02-source-verification.md) playbook

**For MEDIUM PRIORITY:**
1. Add to backlog with priority score
2. Revisit monthly or when capacity allows

**For LOW PRIORITY:**
1. Archive with brief notes
2. Set reminder to revisit in 3-6 months

**For REJECT:**
1. Document rejection reason
2. Archive (may be useful context later)
3. If from source, explain why (builds trust for future tips)

---

## Checklist

Before deciding on any claim:

- [ ] Claim stated clearly and precisely
- [ ] All three questions answered (TRUE, NEW, MATTERS)
- [ ] Clips search completed
- [ ] Source mapping done (can I verify this?)
- [ ] Impact assessment complete
- [ ] Priority assigned with justification
- [ ] SPJ ethics considerations addressed
- [ ] Documentation created (intake form completed)
- [ ] Next steps clear (which playbook to execute next)

---

## Next Playbook

After intake triage:
- If HIGH PRIORITY → [Source Verification](02-source-verification.md)
- If MEDIUM → Add to backlog, monitor capacity
- If collaboration needed → [Collaboration & Handoff](05-collaboration.md)
