# Git Repository Setup

Git is now initialized and your first commit is complete!

## What's Been Done

✅ Git repository initialized
✅ .gitignore configured (macOS, Python, IDEs)
✅ All files staged and committed
✅ Initial commit with comprehensive message
✅ Main branch set

---

## Next Steps: Push to GitHub

### Option 1: Create New GitHub Repository (Recommended)

**1. Create repository on GitHub:**
- Go to https://github.com/new
- Repository name: `colorado-river-tracker` (or your choice)
- Description: "Investigative journalism accountability tracker for Colorado River negotiations"
- **Keep it PRIVATE initially** (until outreach is complete and you're ready to publish)
- DO NOT initialize with README (you already have one)

**2. Add remote and push:**

```bash
# Add GitHub as remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/colorado-river-tracker.git

# Push to GitHub
git push -u origin main
```

**3. After outreach completes, make it public:**
- GitHub repo → Settings → "Change visibility" → Make public
- Enable GitHub Pages (Settings → Pages → Source: main branch)

---

### Option 2: Push to Existing Repository

If you already have a repository:

```bash
git remote add origin YOUR_REPO_URL
git push -u origin main
```

---

## Git Workflow Going Forward

### Making Changes

```bash
# Check what's changed
git status

# Stage specific files
git add colorado-river-tracker.html
git add scraper/fetch_reservoirs.py

# Or stage all changes
git add -A

# Commit with message
git commit -m "Update: Arizona increased cut pledge to 800K ac-ft"

# Push to GitHub
git push
```

### Best Practices for Commit Messages

**Format:**
```
<type>: <short description>

<optional longer description>
<optional context/reasoning>

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
```

**Types:**
- `feat:` New feature (e.g., "feat: Add snowpack data scraper")
- `fix:` Bug fix (e.g., "fix: Correct Nevada allocation percentage")
- `docs:` Documentation (e.g., "docs: Update outreach log with AZ response")
- `data:` Data update (e.g., "data: Update reservoir levels May 18")
- `verify:` Verification work (e.g., "verify: Upgrade Lake Mead claim to Tier 1")
- `refactor:` Code cleanup (e.g., "refactor: Simplify state card rendering")

**Examples:**
```bash
git commit -m "data: Update reservoir levels from latest scraper run"

git commit -m "verify: Upgrade California cut figure to Tier 1

Confirmed with CA River Board directly via email.
Added primary source documentation.
"

git commit -m "feat: Add delivered cuts tracking column

Implements Priority 1 from NEXT_STEPS.md.
Distinguishes pledges from actual measured reductions.
"
```

---

## Branching Strategy (Optional)

For collaborative work or experimental features:

```bash
# Create feature branch
git checkout -b feature/snowpack-data

# Make changes, commit
git add snowpack_scraper.py
git commit -m "feat: Add SNOTEL snowpack scraper"

# Push branch
git push -u origin feature/snowpack-data

# Merge when ready (on GitHub via PR, or locally)
git checkout main
git merge feature/snowpack-data
git push
```

---

## When to Commit

**Commit frequently:**
- After completing a logical unit of work
- Before switching tasks
- After fixing a bug
- When verification status changes
- After outreach responses arrive

**Example timeline:**
```
Day 1: Initial commit (done!)
Day 2: Commit outreach emails sent
Day 5: Commit Arizona response
Day 7: Commit updated HTML with AZ feedback
Day 10: Commit all outreach complete
Day 15: Commit final pre-publication version
Day 16: Commit publication announcement
```

---

## GitHub Pages Deployment

Once ready to publish:

**1. Make repository public:**
- Settings → "Change visibility" → Public

**2. Enable GitHub Pages:**
- Settings → Pages
- Source: "Deploy from a branch"
- Branch: `main` / root
- Save

**3. Your site will be at:**
```
https://YOUR_USERNAME.github.io/colorado-river-tracker/colorado-river-tracker.html
```

**4. Optional: Custom domain:**
- Settings → Pages → Custom domain
- Add CNAME record in your DNS
- Example: tracker.yourdomain.com

---

## .gitignore Configured

The following are ignored:
- macOS system files (.DS_Store)
- Python cache (__pycache__)
- Virtual environments (venv/)
- IDE files (.vscode/, .cursor/)
- Old log files (*.log.old)

The following ARE tracked:
- ✅ data.json (live reservoir data)
- ✅ scraper/fetch.log (audit trail)
- ✅ All documentation
- ✅ All source code

---

## Useful Git Commands

```bash
# See what changed
git diff

# See commit history
git log --oneline

# See specific file history
git log --oneline -- colorado-river-tracker.html

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Discard uncommitted changes (CAREFUL!)
git checkout -- filename.html

# See who changed what
git blame colorado-river-tracker.html

# Search commit messages
git log --grep="outreach"

# Show changes in specific commit
git show a066c71
```

---

## Protecting Sensitive Data

**What to NEVER commit:**
- API keys or passwords
- Email addresses of sources (unless public)
- Unpublished investigation notes
- Personal contact info

**If you accidentally commit sensitive data:**
```bash
# Remove from history (BEFORE pushing to GitHub)
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch path/to/sensitive/file" \
  --prune-empty --tag-name-filter cat -- --all

# If already pushed, contact GitHub support
# Or use BFG Repo-Cleaner tool
```

---

## Collaboration Workflow

If working with co-reporters:

**1. Add collaborators:**
- GitHub repo → Settings → Collaborators → Add people

**2. They clone:**
```bash
git clone https://github.com/YOUR_USERNAME/colorado-river-tracker.git
cd colorado-river-tracker
```

**3. Fetch updates:**
```bash
git pull origin main
```

**4. Avoid conflicts:**
- Pull before starting work
- Communicate who's editing what
- Use branches for major changes

---

## Current Status

```
Repository: colorado-river-tracker (local)
Branch: main
Commits: 1
Files tracked: 27
Latest commit: Initial commit: Colorado River Accountability Tracker
```

**Next action:** Create GitHub repository and push

```bash
# After creating GitHub repo:
git remote add origin https://github.com/YOUR_USERNAME/colorado-river-tracker.git
git push -u origin main
```

---

## Quick Reference

| Command | What it does |
|---------|-------------|
| `git status` | See what's changed |
| `git add -A` | Stage all changes |
| `git commit -m "..."` | Commit with message |
| `git push` | Push to GitHub |
| `git pull` | Get latest from GitHub |
| `git log --oneline` | See commit history |
| `git diff` | See uncommitted changes |

You're ready to push to GitHub when you're ready! 🚀
