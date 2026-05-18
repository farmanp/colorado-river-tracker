# Playbook: Contradiction Protocol

Based on ICIJ (International Consortium of Investigative Journalists) and AP Stylebook standards for handling conflicting sources.

## Purpose

Systematically handle situations where sources contradict each other or where new evidence conflicts with published claims. Maintains integrity while acknowledging uncertainty.

---

## When to Use

- Two sources provide different numbers for the same fact
- Expert opinions conflict
- Official statement contradicts documentary evidence
- Automated scraper produces different result than manual check
- New evidence emerges after publication
- Source disputes your reporting

---

## Principles (AP Stylebook + ICIJ)

### **1. Contradictions Are Not Failures**
Conflicting evidence is normal in investigative work. Your job is to document contradictions transparently, not hide them.

### **2. Hierarchy of Evidence**
Not all sources are equal. Use this hierarchy:

**Highest reliability:**
1. Primary documents (government filings, official data, scientific studies)
2. Multiple independent reputable sources agreeing
3. Expert consensus
4. Direct observation

**Lower reliability:**
1. Single secondary source
2. Anonymous tips
3. Interested party statements
4. Social media

### **3. Present Uncertainty Honestly**
Better to say "sources conflict" than to pick one arbitrarily.

### **4. Never Suppress Contradictory Evidence**
Even if it weakens your story, include contradictions. Readers trust honesty.

---

## Types of Contradictions

### **Type A: Numerical Conflicts**

**Example:** Source 1 says "Arizona pledged 760K ac-ft" but Source 2 says "Arizona pledged 750K ac-ft"

**Resolution steps:**
1. Check if both sources are current (one may be outdated)
2. Verify primary source (which is closer to original document?)
3. Contact both sources for clarification
4. If unresolvable: Report range or note discrepancy

**OpenClaims:**
```json
{
  "event_type": "claim.disputed",
  "claim_ref": "clm_az-cut-amount",
  "dispute": {
    "contradicting_evidence": [{
      "source_id": "src_source2",
      "contradicting_value": "750000",
      "rationale": "Different sources report conflicting figures"
    }],
    "resolution_status": "investigating"
  }
}
```

---

### **Type B: Temporal Conflicts**

**Example:** Document from April says X, document from May says Y

**Resolution:**
- NOT a contradiction - situation changed
- Both are true at different times
- Report both with timestamps

**Presentation:**
> "As of April, Arizona had pledged 750K ac-ft. The state increased its commitment to 760K ac-ft in May."

---

### **Type C: Interpretation Conflicts**

**Example:** Expert A says "this is a crisis", Expert B says "this is manageable"

**Resolution:**
- NOT a factual contradiction - difference of opinion
- Present both views
- Note credentials and potential biases

**Presentation:**
> Experts disagree on severity. Dr. Smith (USGS, 30 years hydrology) calls it "an unprecedented crisis." Dr. Jones (consultant to agriculture industry) argues the situation is "challenging but manageable with existing infrastructure."

---

### **Type D: Methodology Conflicts**

**Example:** Your scraper shows 1,056 ft, USBR dashboard shows 1,062 ft

**Resolution steps:**
1. Verify your methodology (parsing error? wrong selector?)
2. Check timestamp (different measurement times?)
3. Contact authoritative source for clarification
4. Default to primary source if methodology is unclear

**In Colorado River case:**
- USBR is primary/authoritative
- Your scraper is secondary verification
- If conflict, trust USBR unless you have evidence of their error

---

## Step-by-Step Workflow

### **Step 1: Document the Contradiction**

**Create contradiction log entry:**
```markdown
# Contradiction: [Short Title]

**Date identified:** 2026-05-17
**Claim in question:** [Original claim]

**Source A:**
- Statement: [What A says]
- Source type: [Primary/secondary/expert]
- Date: [When stated]
- Tier: [1/2/3]

**Source B:**
- Statement: [What B says]
- Source type: [Primary/secondary/expert]
- Date: [When stated]
- Tier: [1/2/3]

**Type of contradiction:** [Numerical / Temporal / Interpretation / Methodology]

**Status:** Under investigation
```

---

### **Step 2: Investigate Root Cause**

**Checklist:**
- [ ] Verify both sources are current (not outdated)
- [ ] Check if temporal (situation changed over time)
- [ ] Examine methodology (how did each source derive their claim?)
- [ ] Look for unit confusion (ac-ft vs. af-yr, gallons vs. liters)
- [ ] Check for rounding differences (760,000 vs. 760,423 rounded)
- [ ] Consider potential biases (who benefits from which version?)

---

### **Step 3: Attempt Resolution**

**Contact sources directly:**

Email template:
> Hi [Name],
>
> I'm working on a story about Colorado River negotiations and found conflicting information. Can you help clarify?
>
> **Source 1** ([URL/document]) states: "[Exact quote/figure]"
> **Source 2** ([URL/document]) states: "[Exact quote/figure]"
>
> Questions:
> 1. Are both figures accurate at different times?
> 2. Is there a methodological difference?
> 3. Is one figure outdated or incorrect?
>
> I want to ensure accuracy. Can you point me to the definitive source?
>
> Thank you,
> [Your name]

**If resolution achieved:**
- Update claim with correct information
- Note the discrepancy in methodology section
- Thank sources for clarification

**If resolution not achieved:**
- Present both versions
- Note that sources conflict
- Indicate which source you consider more reliable and why

---

### **Step 4: Assess Hierarchy of Evidence**

**Decision tree:**

```
Is one source PRIMARY and the other SECONDARY?
  YES → Default to primary (but note discrepancy)
  NO ↓

Are both PRIMARY but from different entities?
  YES → Report both, note conflict
  NO ↓

Is one source MORE RECENT?
  YES → Use recent (situation may have changed)
  NO ↓

Is one source MORE CREDIBLE?
  YES → Use credible (explain why)
  NO → Report range or uncertainty
```

---

### **Step 5: Choose Presentation Strategy**

**Strategy A: Report Most Reliable Source + Note Discrepancy**

Use when: One source clearly more authoritative

```html
<!-- Arizona cut: 760,000 ac-ft (KJZZ May 11, 2026 citing state officials) -->
<div>760,000 ac-ft</div>
<!-- NOTE: Some earlier reports cited 750K; state revised upward in May -->
```

**Strategy B: Report Range**

Use when: Both sources roughly equal credibility

```html
<div>Approximately 750,000-760,000 ac-ft</div>
<!-- SOURCES: Estimates range from 750K (Reuters May 1) to 760K (KJZZ May 11) -->
```

**Strategy C: Report Both Explicitly**

Use when: Contradiction is itself newsworthy

```html
<div class="note">
  State officials announced 760K ac-ft in cuts (KJZZ May 11),
  but federal documents show 750K ac-ft (BOR filing May 1).
  Discrepancy under investigation.
</div>
```

**Strategy D: Present Uncertainty**

Use when: Cannot resolve and neither source is clearly better

```html
<div>
  Pledge amount uncertain:
  estimates range from 750K-760K ac-ft pending official clarification.
</div>
```

---

### **Step 6: Update Verification Status**

**In code:**
```javascript
{
  pledged: 760000, // Using most recent official statement
  pledgedTier: 1, // Still Tier 1 (primary source KJZZ/officials)
  pledgedNote: "Earlier estimates cited 750K; revised to 760K May 2026",
  conflictResolved: true,
  conflictResolution: "Temporal - situation changed between April and May"
}
```

**OpenClaims event:**
```json
{
  "event_type": "claim.disputed",
  "claim_ref": "clm_az-cut",
  "dispute": {
    "contradicting_evidence": [...],
    "resolution_status": "resolved",
    "resolution": {
      "method": "source_clarification",
      "outcome": "temporal_change",
      "resolved_at": "2026-05-17T...",
      "resolved_by": { "agent_type": "human", "name": "..." }
    }
  }
}
```

---

## Special Case: Post-Publication Contradictions

### **Scenario: Source Disputes Your Published Work**

**Immediate actions:**
1. **DO NOT take article down** (unless legal threat with merit)
2. **DO NOT dismiss** - take seriously
3. **INVESTIGATE immediately**

**Email response template:**
> Thank you for reaching out. I take accuracy seriously and want to investigate your concern.
>
> Can you provide:
> 1. Specific claim(s) you believe are incorrect
> 2. Correct information with source documentation
> 3. Best contact method for follow-up questions
>
> I will review and respond within [48 hours / 1 week].

**Investigation:**
- Pull original sources
- Review notes/recordings
- Check if situation has changed since publication
- Consult with editor if major error

**Outcomes:**

**A. Source is correct - you made an error:**
- Issue correction prominently
- Update article with correction notice
- Apologize to source
- Emit claim.retracted + new claim.emitted events

**B. Source is incorrect - your reporting stands:**
- Respond politely with your evidence
- Offer to include their perspective if substantial
- No correction needed

**C. Both partially correct - nuance needed:**
- Update article with added context
- Note: "Updated to include additional information"
- Emit claim.verified event with updated evidence

---

## Examples from Colorado River Tracker

### **Example 1: Lake Mead Elevation (Methodology Conflict)**

**Contradiction:**
- **Scraper:** 1,015.5 ft (May 17, 6pm)
- **USBR official:** 1,062 ft (Dec 2025 reading)

**Investigation:**
- Scraper captured 1936 historical data (parsing bug!)
- Not a real contradiction - scraper error

**Resolution:**
- Fixed scraper regex
- Re-scraped: Now shows 1,056 ft (May 17, current)
- Still doesn't match USBR's 1,062 ft (Dec 2025)

**Final analysis:**
- Temporal difference (Dec → May = 6 ft drop plausible)
- USBR is authoritative source
- Scraper is secondary verification

**Presentation:** Use most recent (1,056 ft), note source + timestamp

**Lesson:** Methodology conflicts often reveal technical errors, not real discrepancies

---

### **Example 2: Nevada Allocation (Unit Confusion)**

**Contradiction:**
- **Source A:** Nevada's allocation is 300,000 ac-ft/yr
- **Source B:** Nevada's allocation is 1.8% of total

**Investigation:**
- Both correct! Different units.
- 300K ac-ft is ~1.8% of 16.5M ac-ft total river flow
- Not a contradiction - same fact, different expression

**Resolution:** Use both for context
- Primary: 300,000 ac-ft/yr (concrete number)
- Context: "approximately 1.8% of total flow"

---

### **Example 3: Upper Basin Position (Interpretation Conflict)**

**Contradiction:**
- **Reporting:** "Upper Basin refuses mandatory cuts"
- **UCRC response:** "We're not refusing - we're already cutting via reduced snowmelt"

**Investigation:**
- Factually: True that Upper Basin hasn't pledged specific ac-ft cuts
- Interpretation: Depends on definition of "cuts"

**Resolution:**
- Update language to be more precise
- Change "refuses" → "has not agreed to mandatory cuts"
- Add Upper Basin rationale explicitly: "argues natural snowmelt reduction = automatic cuts"

**Lesson:** Interpretive language can be inflammatory. Be precise about facts vs. characterization.

---

## Red Flags: When Contradictions Signal Deeper Issues

### **Multiple Independent Sources Contradict Your Key Claim**
→ STOP. Re-verify everything. May need to retract.

### **Primary Source Contradicts Your Secondary Source**
→ Default to primary. Update immediately.

### **Your Source Recants**
→ Major red flag. Investigate why. Possible scenarios:
- Pressured to recant (story stands, note pressure)
- Genuine error (issue correction)
- Fabrication revealed (retract, investigate fraud)

### **Document You Cited Is Altered**
→ Check Internet Archive for original
→ Note alteration in reporting
→ Screenshot/archive everything going forward

---

## Checklist

When contradiction arises:

- [ ] Documented both conflicting versions
- [ ] Investigated root cause (temporal? methodological? interpretive?)
- [ ] Contacted sources for clarification
- [ ] Assessed hierarchy of evidence
- [ ] Chose appropriate presentation strategy
- [ ] Updated code/article with resolution
- [ ] Emitted OpenClaims dispute event (if applicable)
- [ ] Learned lesson for future verification

---

## Next Playbook

After resolving contradiction:
- If correction needed: [Update & Retraction](04-update-retraction.md)
- If verification enhanced: [Source Verification](02-source-verification.md)
- If methodology improved: [Automated Data Ingestion](08-automated-ingestion.md)
