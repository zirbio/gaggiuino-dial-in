# Gaggia Dial-In Skill — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a Claude Code skill (`/dial-in`) that recommends espresso extraction adjustments for a Gaggia Classic Pro + Gaggiuino + Baratza Sette 270Wi setup, including visual shot analysis.

**Architecture:** A single Claude Code skill (`SKILL.md`) backed by modular knowledge files. Knowledge is authored in a development repo (`/Users/silvio_requena/Code/gaggia dial in/`) and installed to `~/.claude/skills/dial-in/`. The skill references knowledge files via markdown links; Claude loads them on-demand.

**Tech Stack:** Markdown knowledge files, Claude Code skill format (YAML frontmatter), Discord scraped data (JSON) as authoring source.

**Spec:** `docs/superpowers/specs/2026-03-21-gaggia-dial-in-skill-design.md`

---

## File Map

All files are authored in the development repo and then symlinked to `~/.claude/skills/dial-in/` for installation.

**Development repo** (`/Users/silvio_requena/Code/gaggia dial in/skill/`):

| File | Responsibility | Action |
|------|---------------|--------|
| `skill/SKILL.md` | Skill entry point — frontmatter, behavior rules, knowledge links | Create |
| `skill/coffee-fundamentals.md` | Roast, grind, extraction, water theory | Create |
| `skill/grinder-baratza-sette-270wi.md` | Grinder-specific settings and characteristics | Create |
| `skill/troubleshooting.md` | Symptom → diagnosis → adjustment decision tree | Create |
| `skill/shot-analysis.md` | How to interpret Gaggiuino pressure/flow/temp curves | Create |
| `skill/profiles/iuiuiu-classic.md` | IUIUIU Classic profile knowledge | Create |
| `skill/profiles/lmd-9-8-v1.5.md` | LMD 9-8 v1.5 profile knowledge | Create |
| `skill/profiles/londinium.md` | Londinium profile knowledge | Create |
| `skill/profiles/adaptive.md` | Adaptive profile knowledge | Create |
| `skill/profiles/blooming-espresso.md` | Blooming Espresso profile knowledge | Create |
| `skill/profiles/filter-2.1.md` | Filter 2.1 profile knowledge | Create |

**Installation:** `~/.claude/skills/dial-in/` → symlink to `skill/` directory in this repo.

**Basket assumption:** Stock double basket (58mm, ~14-18g capacity). Dose ranges in profiles reflect this. If user upgrades to precision basket (IMS/VST), dose range may extend to 20g.

**Source data:**
- `data/raw/discord-dialing-n-profiling-raw.json` — 4,450 Discord messages for community notes curation
- Gaggiuino website (gaggiuino.github.io) — official profile docs
- General espresso extraction knowledge

---

## Task 1: Research Gaggiuino profiles from official website

Before writing any knowledge files, gather official documentation on each profile from the Gaggiuino website.

**Files:** None created yet — this is a research task.

- [ ] **Step 1: Scrape Gaggiuino website profile documentation**

Navigate to `https://gaggiuino.github.io` and find documentation for each profile: IUIUIU Classic, LMD 9-8, Londinium, Adaptive, Blooming Espresso, Filter 2.1. Look for:
- Profile curve descriptions (preinfusion, ramp, hold, decline)
- Recommended starting parameters (dose, yield, time, temperature)
- What each profile is designed for

Use browser automation tools (mcp__claude-in-chrome__*) to navigate and read the website. Fallback: use WebFetch if browser tools are unavailable or the site uses heavy JavaScript rendering.

- [ ] **Step 2: Save research notes**

Save the gathered information to a temporary research file:

```
/Users/silvio_requena/Code/gaggia dial in/data/research/gaggiuino-website-profiles.md
```

Structure: one section per profile with the raw information gathered.

- [ ] **Step 3: Extract community notes from Discord data**

Read `data/raw/discord-dialing-n-profiling-raw.json` and filter for messages mentioning each profile.

**Curation criteria — prioritize messages that contain:**
- Specific grind settings, dose, yield, or temperature numbers
- Before/after comparisons ("I changed X and it improved Y")
- Advice from top contributors (zooloo10, Loogle, Zer0-bit, spikey, Talon — frequent, knowledgeable posters)
- Common pitfalls or warnings
- Profile-specific recommendations tied to coffee type

**Exclude:** general chatter, memes, off-topic, short reactions ("nice shot!"), questions without answers.

Save to:

```
/Users/silvio_requena/Code/gaggia dial in/data/research/discord-community-notes.md
```

Structure: one section per profile with curated insights from the Discord data.

---

## Task 2: Write `coffee-fundamentals.md`

The theoretical foundation referenced by all other files.

**Files:**
- Create: `skill/coffee-fundamentals.md`

**Sources:** General espresso extraction knowledge, Sette 270Wi characteristics.

- [ ] **Step 1: Write coffee-fundamentals.md**

Write the file covering:
1. **Roast levels** — light/medium/dark: solubility, acidity, bitterness, recommended temperature ranges, pressure profiles
2. **Origin & process** — washed/natural/honey: bean density, solubility, extraction behavior, grind/temp implications
3. **Freshness** — degassing timeline (7-30 days), optimal window for espresso, effect on preinfusion and channeling
4. **Grind fundamentals** — grind-dose-yield-time relationship, particle size distribution basics, the Sette 270Wi's bimodal distribution and its implications
5. **Water** — basic TDS range (50-150 ppm), why it matters, avoid distilled/very hard

Keep it concise and actionable — this is a reference for decision-making, not a textbook. Target: 150-250 lines.

- [ ] **Step 2: Review for accuracy and completeness**

Read the file back. Check that:
- Each section gives actionable guidance (not just theory)
- Sette 270Wi is mentioned where grind distribution matters
- No contradictions between sections
- Language is clear for someone new to specialty coffee

---

## Task 3: Write `grinder-baratza-sette-270wi.md`

**Files:**
- Create: `skill/grinder-baratza-sette-270wi.md`

**Sources:** Baratza Sette 270Wi specs, general grinder knowledge, Discord mentions of grind settings.

- [ ] **Step 1: Research Sette 270Wi specifics**

If needed, look up current Baratza Sette 270Wi documentation for:
- Macro/micro adjustment range and step size
- Grind size range for espresso
- Retention characteristics
- Particle distribution profile (bimodal)

- [ ] **Step 2: Extract grind-related insights from Discord data**

Filter Discord messages for mentions of grind settings, Sette, macro, micro, grind size. Extract useful data points (what settings people use for which profiles).

```bash
cat "data/raw/discord-dialing-n-profiling-raw.json" | python3 -c "
import json, sys
data = json.load(sys.stdin)
for m in data:
    c = m.get('content','').lower()
    if any(kw in c for kw in ['sette', 'macro', 'micro', 'grind size', 'grind setting', 'grind finer', 'grind coarser']):
        print(f\"{m.get('username','?')} ({m.get('timestamp','')[:10]}): {m.get('content','')[:200]}\")
" | head -50
```

- [ ] **Step 3: Write grinder-baratza-sette-270wi.md**

Write the file covering:
1. **Adjustment system** — 30 macro steps (lettered A-Z + numbers), 10 micro steps per macro, total resolution
2. **Espresso range** — typical macro range for espresso (around 5-15 depending on calibration)
3. **Step impact** — approximate effect: 1 macro step ≈ 3-5 seconds shot time change, 1 micro step ≈ 0.5-1 second
4. **Characteristics** — low retention (~0.5g), bimodal particle distribution (more fines than unimodal grinders), fast grinding
5. **Starting points per profile type** — table with approximate grind ranges
6. **Calibration** — how to recalibrate, when to recalibrate
7. **Maintenance** — burr cleaning frequency, signs of dull burrs

Target: 80-120 lines.

---

## Task 4: Write `profiles/iuiuiu-classic.md`

The primary profile — most used, most Discord data available (71 mentions + "classic" mentions).

**Files:**
- Create: `skill/profiles/iuiuiu-classic.md`

**Sources:** Gaggiuino website research (Task 1), Discord community notes (Task 1), general knowledge.

- [ ] **Step 1: Write iuiuiu-classic.md**

Follow the profile template:
1. **Description** — what the IUIUIU Classic curve does: preinfusion, pressure ramp, hold at 9 bar, natural decline. Explain the philosophy behind it.
2. **Best suited for** — which roast levels, origins, processes work best
3. **Starting parameters** — dose (18g), yield (36g), time (~30s), temperature (93°C for medium, adjust for roast), Sette 270Wi grind range
4. **How to adjust** — priority-ordered: grind → dose → temperature → yield ratio. Specific guidance for sour vs bitter vs flat results.
5. **Community notes** — curated from Discord data (Task 1, Step 3)
6. **Common mistakes** — what users typically get wrong

- [ ] **Step 2: Cross-reference with coffee-fundamentals.md**

Read both files. Ensure recommendations are consistent (e.g., if coffee-fundamentals says "light roast → higher temp", the profile's adjustment guidance should align).

---

## Task 5: Write remaining 5 profile files

Each follows the same template as IUIUIU Classic.

**Files:**
- Create: `skill/profiles/lmd-9-8-v1.5.md`
- Create: `skill/profiles/londinium.md`
- Create: `skill/profiles/adaptive.md`
- Create: `skill/profiles/blooming-espresso.md`
- Create: `skill/profiles/filter-2.1.md`

**Sources:** Gaggiuino website research (Task 1), Discord community notes (Task 1).

- [ ] **Step 1: Write lmd-9-8-v1.5.md**

LMD 9-8 is the second most used profile. Follow the 6-section template. This is a Lever Machine Digital emulation — long preinfusion, pressure ramp mimicking lever, natural decline. 93 Discord mentions for "lmd".

- [ ] **Step 2: Write londinium.md**

Londinium lever profile. Long preinfusion at low pressure, then ramp, hold, gradual decline. 71 Discord mentions. Follow the 6-section template.

- [ ] **Step 3: Write adaptive.md**

Adaptive profile — adjusts based on flow feedback. 65 Discord mentions. Follow the 6-section template.

- [ ] **Step 4: Write blooming-espresso.md**

Blooming espresso — extended low-pressure preinfusion (bloom phase), then extraction. 71 Discord mentions. Follow the 6-section template.

- [ ] **Step 5: Write filter-2.1.md**

Filter 2.1 — longer, lower-pressure extraction mimicking filter coffee. Different from traditional espresso. 9 Discord mentions (less community data available). Follow the 6-section template.

- [ ] **Step 6: Cross-reference all profiles**

Read all 6 profile files sequentially. Check:
- Template consistency (all 6 sections present in each)
- No contradictory advice between profiles
- Starting parameters are realistic and distinct per profile
- Grind ranges don't overlap incorrectly

---

## Task 6: Write `troubleshooting.md`

**Files:**
- Create: `skill/troubleshooting.md`

**Sources:** coffee-fundamentals.md (theory), profile files (profile-specific quirks), Discord data (common problems).

- [ ] **Step 1: Extract troubleshooting insights from Discord**

Filter Discord messages for symptom keywords: sour, bitter, flat, channeling, gusher, choked, astringent, watery, fast, slow.

```bash
cat "data/raw/discord-dialing-n-profiling-raw.json" | python3 -c "
import json, sys
data = json.load(sys.stdin)
for m in data:
    c = m.get('content','').lower()
    if any(kw in c for kw in ['sour', 'bitter', 'channel', 'gusher', 'choke', 'astringent', 'watery', 'flat', 'too fast', 'too slow']):
        print(f\"{m.get('username','?')}: {m.get('content','')[:250]}\")
        print('---')
" | head -100
```

- [ ] **Step 2: Write troubleshooting.md**

Structure as a symptom-based decision tree:

1. **Sour/acidic** → under-extracted → ordered adjustments with Sette 270Wi specifics
2. **Bitter/harsh/astringent** → over-extracted → ordered adjustments
3. **Watery/flat** → low TDS → adjustments
4. **Channeling** → uneven distribution → puck prep + grind adjustments
5. **Gusher** (< 15s shot) → way too coarse/low dose → emergency adjustments
6. **Choked** (no flow) → way too fine/high dose → emergency adjustments
7. **Both sour AND bitter** → channeling or uneven extraction → specific guidance
8. **Profile-specific notes** — common issues per profile (e.g., "Blooming shots tend to X")

Each entry: symptom → diagnosis → adjustment order (grind first, then dose, then temp, then ratio, then profile change) → Sette 270Wi specifics.

Target: 100-150 lines.

---

## Task 7: Write `shot-analysis.md`

**Files:**
- Create: `skill/shot-analysis.md`

**Depends on:** Tasks 4-5 (profile files must exist for "profile-specific good references" section).

**Sources:** Gaggiuino UI knowledge, espresso extraction science, Discord shot discussions.

- [ ] **Step 1: Write shot-analysis.md**

Guide for interpreting Gaggiuino shot photos/screenshots:

1. **What the Gaggiuino screen shows** — identify the curves: pressure (bar), flow (ml/s), temperature (°C), weight (g). Color coding. X-axis = time. **Two image sources:** (a) photo of the physical Gaggiuino touchscreen on the machine, (b) screenshot from the Gaggiuino web UI at 192.168.x.x — describe differences in layout/rendering between both so the skill can interpret either.
2. **Pressure curve reading**
   - Preinfusion phase: what good preinfusion looks like per profile type
   - Ramp: gradual vs sudden, what each means
   - Peak/plateau: stability, target pressure per profile
   - Decline: natural decline rate, forced decline, what steep vs gentle means
3. **Flow curve reading**
   - Stable flow = even extraction
   - Rising flow = puck degradation (normal late in shot)
   - Sudden spike = channeling
   - Very low flow = too fine or high dose
   - Erratic flow = distribution issues
4. **Temperature curve reading**
   - Should be stable (± 1°C)
   - Large drops = machine can't keep up (not typical with Gaggiuino PID)
   - Offset from set point = PID tuning issue
5. **Combined pattern diagnosis** — what combinations of curves indicate:
   - Good shot: stable pressure at target, smooth flow, stable temp
   - Channeling: pressure drop + flow spike simultaneously
   - Puck erosion: gradual pressure drop + increasing flow
   - Choked: pressure at pump max + minimal flow
6. **Profile-specific "good" references** — brief description of what a good shot looks like for each of the 6 profiles
7. **Photo quality fallback** — if image is blurry/cropped, ask for: peak pressure, total time, yield weight, and taste description

Target: 120-180 lines.

---

## Task 8: Write `SKILL.md`

The skill entry point that ties everything together.

**Files:**
- Create: `skill/SKILL.md`

- [ ] **Step 1: Write SKILL.md**

```yaml
---
name: dial-in
description: >
  Recommend espresso extraction adjustments for Gaggia Classic Pro + Gaggiuino.
  Use when asking about espresso profiles, grind settings, troubleshooting shots,
  or analyzing shot photos. Supports IUIUIU Classic, LMD 9-8, Londinium,
  Adaptive, Blooming Espresso, and Filter 2.1 profiles with Baratza Sette 270Wi.
argument-hint: [describe your coffee, problem, or attach a shot photo]
---
```

Body content:

1. **Setup context** — machine, grinder, basket (hardcoded assumptions)
2. **Query type detection** — how to identify which use case applies:
   - Photo attached → Use Case 4 (shot analysis)
   - Mentions a problem/symptom → Use Case 2 (troubleshooting)
   - Asks "what profile/settings" for a coffee → Use Case 1 (recommendation)
   - Asks about differences/concepts → Use Case 3 (informational)
3. **Knowledge loading matrix** — encode the spec's loading matrix as explicit instructions in the skill body:

   | Query type | Load these files |
   |---|---|
   | Recommendation (new coffee) | [coffee-fundamentals](coffee-fundamentals.md) + [grinder](grinder-baratza-sette-270wi.md) + recommended [profile](profiles/) |
   | Troubleshooting (shot problem) | [troubleshooting](troubleshooting.md) + active [profile](profiles/) + [grinder](grinder-baratza-sette-270wi.md) |
   | Informational (compare/explain) | relevant [profiles](profiles/) and/or [coffee-fundamentals](coffee-fundamentals.md) |
   | Visual analysis (shot photo) | [shot-analysis](shot-analysis.md) + active [profile](profiles/) |
4. **Response format rules** — grind in macro/micro, temp in °C, dose/yield in grams
5. **Always ask if missing** — roast level, freshness, process
6. **Multi-turn support** — handle iterative dial-in within conversation

Target: 60-100 lines. Keep it concise — the knowledge lives in the referenced files.

- [ ] **Step 2: Verify all files exist**

```bash
ls -la "/Users/silvio_requena/Code/gaggia dial in/skill/"
ls -la "/Users/silvio_requena/Code/gaggia dial in/skill/profiles/"
head -10 "/Users/silvio_requena/Code/gaggia dial in/skill/SKILL.md"
```

Verify all 11 files exist (SKILL.md + 4 knowledge files + 6 profiles) and SKILL.md frontmatter is valid YAML.

---

## Task 9: Install skill

**Files:** None modified — this is an installation/symlink task.

- [ ] **Step 1: Create symlink from dev repo to Claude Code skills directory**

```bash
ln -s "/Users/silvio_requena/Code/gaggia dial in/skill" ~/.claude/skills/dial-in
```

- [ ] **Step 2: Verify installation**

```bash
ls -la ~/.claude/skills/dial-in/
ls -la ~/.claude/skills/dial-in/profiles/
head -10 ~/.claude/skills/dial-in/SKILL.md
```

Verify: symlink exists, all files are accessible, SKILL.md frontmatter is valid.

---

## Task 10: Smoke test the skill

**Files:** None modified — this is a verification task.

- [ ] **Step 1: Test Use Case 1 — Recommendation (light roast)**

In a new Claude Code session, run:
```
/dial-in I have a light roast Ethiopian natural, 10 days off roast. What should I use?
```

Verify: asks relevant follow-ups if needed, recommends a profile with specific parameters, references Sette 270Wi settings.

- [ ] **Step 2: Test Use Case 1b — Recommendation (dark roast)**

```
/dial-in I have a dark roast Brazilian blend for espresso, 3 weeks off roast. What profile?
```

Verify: recommends a DIFFERENT profile/settings than Step 1 (dark roast should get different temp, possibly different profile).

- [ ] **Step 3: Test Use Case 2 — Troubleshooting**

```
/dial-in My IUIUIU Classic shots are coming out sour. 18g in, 36g out, 22 seconds.
```

Verify: diagnoses under-extraction, suggests grinding finer with specific Sette steps, ordered adjustments.

- [ ] **Step 4: Test Use Case 3 — Informational**

```
/dial-in What's the difference between Londinium and Blooming Espresso?
```

Verify: compares the two profiles clearly, explains when to use each.

- [ ] **Step 5: Test Use Case 4 — Visual analysis**

Attach a photo of a Gaggiuino shot screen and run:
```
/dial-in What do you think of this shot?
```

Verify: identifies curves, diagnoses issues, suggests adjustments.

- [ ] **Step 6: Test multi-turn dial-in session**

After Step 3, continue the conversation:
```
I ground 2 micro steps finer and now it's 28 seconds but tastes bitter and astringent.
```

Verify: recognizes this is a follow-up, adjusts advice (went too fine → back off slightly or lower temp).

- [ ] **Step 7: Test photo fallback**

Send a non-coffee image or describe "I can't take a photo right now":
```
/dial-in [attach a random non-coffee image] What do you think of this shot?
```

Verify: the skill recognizes it's not a Gaggiuino screen and asks for manual data (pressure, time, yield, taste).

- [ ] **Step 8: Fix any issues found**

If any test reveals problems (wrong advice, missing context, broken file references), fix the relevant knowledge or skill file.

---

## Task 11: Create iOS deployment (optional)

**Files:**
- Create: `/Users/silvio_requena/Code/gaggia dial in/ios/dial-in-project-context.md`

- [ ] **Step 1: Concatenate knowledge files for iOS**

```bash
cd "/Users/silvio_requena/Code/gaggia dial in/skill"
echo "# Gaggia Dial-In — Complete Knowledge Base" > /tmp/dial-in-ios.md
echo "" >> /tmp/dial-in-ios.md
for f in coffee-fundamentals.md grinder-baratza-sette-270wi.md troubleshooting.md shot-analysis.md; do
  cat "$f" >> /tmp/dial-in-ios.md
  echo -e "\n---\n" >> /tmp/dial-in-ios.md
done
for f in profiles/*.md; do
  cat "$f" >> /tmp/dial-in-ios.md
  echo -e "\n---\n" >> /tmp/dial-in-ios.md
done
cp /tmp/dial-in-ios.md "/Users/silvio_requena/Code/gaggia dial in/ios/dial-in-project-context.md"
```

- [ ] **Step 2: Create a Claude Project on iOS**

Instructions for the user:
1. Open Claude app on iOS
2. Create a new Project called "Gaggia Dial-In"
3. Add `dial-in-project-context.md` as project context
4. Add the SKILL.md behavior instructions as project instructions
5. Test with the same use cases as Task 9
