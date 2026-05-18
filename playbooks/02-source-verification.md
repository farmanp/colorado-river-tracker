# Playbook: Source Verification

## Purpose

Systematically verify claims against sources using a three-tier system. Ensures every published claim is traceable to defensible evidence.

---

## When to Use

- Before publishing any factual claim
- When receiving a tip or lead
- When source documents are released (FOIA, press releases)
- When contradictory information emerges

---

## Prerequisites

- Claim statement clearly defined
- At least one potential source identified
- Access to source material (or ability to obtain it)

---

## The Three-Tier System

### **Tier 1: Defensible (Safe to Publish)**

**Criteria (ONE of the following):**
- ✅ Multiply confirmed by 2+ reputable independent sources
- ✅ Primary source document (government filing, official press release, USBR data)
- ✅ Peer-reviewed academic publication
- ✅ Direct observation / first-hand reporting

**Verification steps:**
1. Obtain source document/URL
2. Extract exact text/data supporting claim
3. Verify document authenticity (author, date, domain)
4. Document selector (page number, paragraph, timestamp)
5. Compute content digest (SHA-256 if possible)

**Example:**
> Claim: "Lake Mead is at 1,056 ft elevation"
> Source: USBR hourly data page (primary, authoritative)
> Selector: May 17, 2026 reading, table row 2026
> Tier: 1 (primary government data)

---

### **Tier 2: Needs Cross-Check (Attribute Clearly)**

**Criteria:**
- ⚠️ Single reputable source (NYT, AP, Reuters, NPR, local investigative outlets)
- ⚠️ Expert opinion (credentialed, on-record, but uncorroborated)
- ⚠️ Official statement from biased party (state agency promoting their position)

**Verification steps:**
1. Same as Tier 1 (obtain, extract, verify, document)
2. **Additional:** Identify corroborating sources to pursue
3. **Additional:** Mark for priority upgrade to Tier 1

**Publishing rules:**
- ✅ Must attribute explicitly: "According to KJZZ..."
- ✅ Flag in code comments: `<!-- TIER 2: Single source KJZZ -->`
- ⚠️ Upgrade to Tier 1 before final publication if possible

**Example:**
> Claim: "Las Vegas metro population is 2.3M"
> Source: Nevada Independent (reputable outlet, citing Census)
> Tier: 2 (single source, should verify with actual Census data)
> Action: Escalate to primary Census source for Tier 1

---

### **Tier 3: Unverified (DO NOT PUBLISH)**

**Red flags:**
- ❌ Anonymous tip without corroboration
- ❌ Social media post (even from official account) without verification
- ❌ Paraphrased statement ("officials said" without direct quote)
- ❌ Claim you cannot trace to a source
- ❌ Fabricated or inferred content

**Verification steps:**
1. Mark as Tier 3 immediately
2. Pursue primary sources aggressively
3. If unable to verify within reasonable timeframe: REMOVE CLAIM

**Publishing rules:**
- ❌ NEVER publish Tier 3 claims
- ✅ OK to publish "we could not verify X"
- ✅ OK to publish "State declined to provide data on X"

**Example:**
> Claim: "California's cuts will mostly hit agricultural users"
> Source: Inference from general knowledge
> Tier: 3 (not sourced)
> Action: Remove or find primary source (CA River Board documents)

---

## Step-by-Step Workflow

### **Step 1: Receive Claim**

Claim enters via:
- Reporter research
- Public document (press release, FOIA response)
- Tip from source
- Automated scraper output

**Action:** Document claim text exactly.

**OpenClaims event:**
```json
{
  "event_type": "claim.emitted",
  "claim": {
    "claim_id": "clm_[generate_id]",
    "text": "[exact claim statement]",
    "claim_type": "factual",
    "status": "under_investigation"
  },
  "producer": {
    "agent_type": "human",
    "name": "[your name / intake source]"
  }
}
```

---

### **Step 2: Identify Sources**

**Question:** What sources could verify this claim?

**Priority order:**
1. **Primary sources** (government data, official filings, FOIA docs)
2. **Multiple secondary** (2+ reputable outlets reporting same thing)
3. **Expert interviews** (credentialed, on-record)
4. **Single secondary** (last resort)

**Action:** List all potential sources, prioritize by tier potential.

---

### **Step 3: Obtain Source Material**

**For documents:**
- Download / archive immediately (URLs change, PDFs disappear)
- Save with timestamp: `source-2026-05-17-kjzz-arizona-cuts.html`
- Compute SHA-256 hash for integrity

**For interviews:**
- Record (with permission)
- Transcribe key sections verbatim
- Get on-record confirmation

**For scraped data:**
- Log full response body
- Document selector/parsing logic
- Validate against secondary source

---

### **Step 4: Extract Evidence**

**Find the exact portion supporting your claim:**

**For text:**
- Paragraph number or text span (char offset)
- Exact quote if quoting

**For data:**
- Table cell, row number, column name
- Screenshot if helpful

**For PDFs:**
- Page number + highlighted text
- Byte range if programmatic

**OpenClaims representation:**
```json
{
  "sources": [{
    "source_id": "src_kjzz-2026-05-11",
    "uri": "https://kjzz.org/content/1890761/...",
    "observed_at": "2026-05-11T14:22:00Z",
    "digest": {
      "algorithm": "sha256",
      "encoding": "base64url",
      "value": "[hash_of_page]"
    }
  }],
  "evidence": [{
    "evidence_id": "ev_kjzz-az-cut",
    "source_ref": "src_kjzz-2026-05-11",
    "claim_ref": "clm_az-760k-cut",
    "selector": {
      "type": "text_span",
      "paragraph": 7,
      "text": "Arizona...760,000 acre-feet..."
    },
    "support_type": "supports_directly"
  }]
}
```

---

### **Step 5: Assess Tier**

**Decision tree:**

```
Is this a primary source (govt, academic, official filing)?
  YES → Tier 1
  NO ↓

Do you have 2+ independent reputable sources?
  YES → Tier 1
  NO ↓

Do you have 1 reputable source?
  YES → Tier 2 (mark for upgrade)
  NO → Tier 3 (DO NOT PUBLISH)
```

**Action:** Assign tier, document reasoning.

---

### **Step 6: Document & Tag**

**In code (HTML/JS):**
```javascript
{
  pledged: 760000,
  pledgedTier: 1, // SOURCE: KJZZ May 11, 2026 — specific figure cited
  pledgedSource: 'KJZZ-2026-05-11'
}
```

**In HTML comments:**
```html
<!-- CLAIM: Arizona pledged 760K ac-ft cuts | TIER: 1 | SOURCE: KJZZ May 11, 2026 -->
```

**In verification log:**
```markdown
## Claim: Arizona cut pledge
- Statement: "Arizona pledged 760,000 ac-ft cuts over 2026-2028"
- Tier: 1
- Source: KJZZ May 11, 2026 (https://kjzz.org/...)
- Evidence: Paragraph 7, direct quote from Buschatzke press call
- Verified by: [Your name]
- Verified date: 2026-05-17
```

---

### **Step 7: Emit Verification Event (OpenClaims)**

**If Tier 1 achieved:**
```json
{
  "event_type": "claim.verified",
  "claim_ref": "clm_az-760k-cut",
  "verification": {
    "result": "supported",
    "confidence": "high",
    "method": "primary_source_verification",
    "lifecycle_status": "verified",
    "validator": {
      "agent_type": "human",
      "name": "[your name]"
    },
    "verified_at": "2026-05-17T19:30:00Z"
  },
  "sources": [...],
  "evidence": [...]
}
```

**If Tier 2 (needs upgrade):**
```json
{
  "event_type": "claim.verified",
  "verification": {
    "result": "supported",
    "confidence": "medium",
    "lifecycle_status": "needs_corroboration",
    "notes": "Single source KJZZ, pursuing primary source for Tier 1"
  }
}
```

**If Tier 3 (unverifiable):**
- Don't emit verified event
- Either remove claim OR emit disputed event with rationale

---

## Decision Points

### **What if sources contradict?**

Execute [Contradiction Protocol](03-contradiction-protocol.md).

### **What if I can only get Tier 2?**

**Options:**
1. Publish with clear attribution
2. Delay publication to pursue Tier 1
3. Remove claim entirely

**Factors:**
- How critical is the claim to the story?
- How likely is Tier 1 upgrade?
- What's the publication deadline?

### **What if the source is paywalled?**

- Pay for legitimate access (journalism expense)
- Request via library / institutional access
- FOIA the underlying document if government
- Contact source directly for verification

### **What if source is offline/dead link?**

- Check Internet Archive Wayback Machine
- Contact publisher for archived version
- If unrecoverable: Tier 3 (cannot verify)

---

## Examples from Colorado River Tracker

### **Example 1: Lake Mead Elevation**

**Claim:** "Lake Mead is at 1,056 ft"

**Step 1:** Claim received from automated scraper
**Step 2:** Primary source: USBR hourly data endpoint
**Step 3:** Obtained HTML response, archived with SHA-256 hash
**Step 4:** Extracted table cell with elevation reading
**Step 5:** Tier 1 (primary government data, authoritative)
**Step 6:** Tagged in data.json with source URL + timestamp
**Step 7:** Emitted claim.verified event

**Result:** ✅ Published (Tier 1)

---

### **Example 2: Nevada Population**

**Claim:** "Las Vegas metro population is 2.3M"

**Step 1:** Claim needed for context
**Step 2:** Found in Nevada Independent article (secondary source)
**Step 3:** Archived article, noted citation to Census estimates
**Step 4:** Extracted paragraph mentioning 2.3M
**Step 5:** Tier 2 (single reputable source, cites Census but we didn't verify primary)
**Step 6:** Tagged as Tier 2, noted "should verify with Census"
**Step 7:** Published with attribution: "approximately 2.3M" + footnote

**Result:** ⚠️ Published with Tier 2 caveat (acceptable for context figure)

**Follow-up:** Priority upgrade - get actual Census data for Tier 1

---

### **Example 3: Fabricated Quote Caught**

**Claim:** "Utah's Shawcroft said the Upper Basin has no water left to give"

**Step 1:** Claim drafted as paraphrase of general position
**Step 2:** Could not locate exact quote in sources
**Step 3:** Searched UCRC press releases, news coverage
**Step 4:** Found **different actual quote** (not our paraphrase)
**Step 5:** Tier 3 (original claim unverifiable - we made it up)
**Step 6:** REMOVED fabricated quote, replaced with verbatim from UCRC
**Step 7:** Emitted claim.retracted event, new claim.emitted with correct quote

**Result:** ✅ Caught before publication, corrected

**Lesson:** Never paraphrase. Always use exact quotes or don't attribute.

---

## Common Issues

### **"The source says it, but I can't find it in the document"**

→ Tier 3. If you can't point to it, you can't verify it.

### **"Everyone knows this is true"**

→ Tier 3. "Common knowledge" isn't verifiable. Find a source.

### **"My source is confidential"**

→ Can publish as "according to a source familiar with negotiations" BUT claim is Tier 2 at best. Need corroborating evidence for Tier 1.

### **"The official website changed and now the data is gone"**

→ Use Internet Archive. If unrecoverable, note in methodology: "Based on archived USBR data from [date]"

### **"This is just a number, do I need a source?"**

→ YES. Every number needs a source. "40 million people depend on Colorado River" needs citation.

---

## Checklist

Before publishing any claim:

- [ ] Claim statement is exact and unambiguous
- [ ] Source(s) identified and obtained
- [ ] Evidence extracted with selector (page/paragraph/span)
- [ ] Tier assigned (1, 2, or 3)
- [ ] If Tier 3: Claim removed or marked "unverified"
- [ ] If Tier 2: Attributed explicitly, upgrade path identified
- [ ] If Tier 1: Documented in code comments + verification log
- [ ] OpenClaims event emitted (optional but recommended)

---

## Next Playbook

After verification:
- If claim is disputed: See [Contradiction Protocol](03-contradiction-protocol.md)
- If claim needs update: See [Update & Retraction](04-update-retraction.md)
- For team work: See [Collaboration & Handoff](05-collaboration.md)
