# Gaggia Dial-In Skill — Design Spec

## Overview

A Claude Code skill (`/dial-in`) that recommends espresso extraction adjustments for a Gaggia Classic Pro with the Gaggiuino mod and a Baratza Sette 270Wi grinder. The skill serves as both a dial-in advisor and coffee education tool.

## User Context

- **Machine:** Gaggia Classic Pro + Gaggiuino mod
- **Grinder:** Baratza Sette 270Wi
- **Coffee:** Specialty, varied origins and roasts
- **Profiles available:** IUIUIU Classic (primary), LMD 9-8 v1.5, Londinium, Adaptive, Blooming Espresso, Filter 2.1
- **Basket:** To be confirmed (stock double or aftermarket precision basket — affects dose range)
- **Water:** Assumed acceptable; only addressed reactively if relevant
- **Deployment:** Claude Code skill (primary) + Claude iOS app (via Claude Projects with knowledge pasted as context)

## Use Cases

### 1. Recommendation from scratch
User describes a coffee and asks what profile/settings to use.

**Flow:**
- Skill asks for roast level, origin, process, freshness (if not provided)
- Recommends profile + dose + grind setting + temperature + target yield/time
- References `coffee-fundamentals.md` + recommended profile's `.md`

### 2. Troubleshooting
User describes a problem with a specific shot/profile.

**Flow:**
- Skill identifies the symptom (sour, bitter, flat, channeling, etc.)
- Consults `troubleshooting.md` + the active profile's `.md`
- Suggests adjustments ordered by impact: grind first, then dose, then temperature, then profile change
- All grind adjustments reference Sette 270Wi macro/micro clicks

### 3. Informational query
User asks about differences between profiles or coffee concepts.

**Flow:**
- Loads relevant profile `.md` files or `coffee-fundamentals.md`
- Compares and explains

### 4. Visual shot analysis
User attaches a photo of executed shot (Gaggiuino screen or web UI screenshot).

**Flow:**
- Interprets pressure, flow, and temperature curves using `shot-analysis.md`
- Identifies: preinfusion behavior, ramp rate, peak pressure, decline pattern, flow stability, temperature stability
- Diagnoses issues and suggests specific adjustments
- Handles both physical screen photos and web UI screenshots (192.168.x.x)
- **Fallback:** If the photo is blurry, cropped, or not from a Gaggiuino screen, the skill states what it cannot interpret and asks for a better image or manual data entry (pressure/flow/time values)

### Multi-turn sessions
The skill supports iterative dial-in within a single conversation. The user can report results after adjusting and get further recommendations. State is not persisted across conversations.

## Discord Data Processing
The raw scraped data (`data/raw/discord-dialing-n-profiling-raw.json`) is processed via **manual curation**: relevant insights are extracted and written into the "Community notes" sections of each profile `.md`. The raw JSON is not loaded at runtime — it serves only as a source during the authoring phase.

## File Structure

### Development (this repo)
```
gaggia-dial-in/                                    # /Users/silvio_requena/Code/gaggia dial in/
├── data/
│   └── raw/
│       └── discord-dialing-n-profiling-raw.json   # scraped backup (4,450 msgs)
└── docs/
    └── superpowers/specs/                         # design specs
```

### Installed skill (Claude Code)
```
~/.claude/skills/dial-in/                          # personal skill directory
├── SKILL.md                                       # skill entry point (frontmatter + instructions)
├── coffee-fundamentals.md                         # roast, grind, extraction, water
├── troubleshooting.md                             # symptom-based decision tree
├── grinder-baratza-sette-270wi.md                 # grinder-specific adjustments
├── shot-analysis.md                               # how to read Gaggiuino curves
└── profiles/
    ├── iuiuiu-classic.md
    ├── lmd-9-8-v1.5.md
    ├── londinium.md
    ├── adaptive.md
    ├── blooming-espresso.md
    └── filter-2.1.md
```

### Skill frontmatter (`SKILL.md`)
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

The knowledge files live alongside `SKILL.md` in the same directory. `SKILL.md` references them via markdown links (e.g., `[coffee-fundamentals](coffee-fundamentals.md)`), and Claude loads them on-demand when invoked.

### Claude iOS app
The skill format does not work on iOS. For iOS usage, the knowledge files will be concatenated into a single document and added as project context in a Claude Project. This is a secondary deployment target.

## Knowledge Files — Content Specification

### `coffee-fundamentals.md`

Covers the theory the user needs to make informed decisions:

- **Roast levels:** Light vs medium vs dark — effect on solubility, acidity, bitterness. What temperature and pressure each favors. How to adjust extraction approach per roast.
- **Origin & process:** Washed, natural, honey — effect on bean density, solubility, and extraction behavior. How process affects grind and temperature choices.
- **Freshness:** Degassing timeline, optimal window for espresso, how fresh beans affect preinfusion and channeling risk.
- **Grind fundamentals:** Grind-dose-yield-time relationship. How particle size distribution (specifically the Sette 270Wi's bimodal distribution) influences extraction.
- **Water:** Basic TDS guidance, why it matters for extraction and flavor.

### `grinder-baratza-sette-270wi.md`

- Useful espresso range (macro/micro settings)
- How much each macro and micro click changes extraction time (approximate seconds)
- Characteristics: low retention, bimodal particle distribution, implications for profiles
- Calibration guidance
- Recommended starting points per profile type
- Maintenance notes affecting grind consistency

### `profiles/*.md` (consistent structure per profile)

Each profile file follows the same template:

1. **Description:** What the profile does — preinfusion, ramp, hold, decline curve explained
2. **Best suited for:** Roast types, origins, processes that work well
3. **Starting parameters:** Dose (g), yield (g), time target (s), temperature (°C), Sette 270Wi grind range (macro/micro)
4. **How to adjust:** Priority-ordered list of what to change when the shot is off
5. **Community notes:** Curated insights from Discord's #dialing-n-profiling channel
6. **Common mistakes:** What users typically get wrong with this profile

### `troubleshooting.md`

Symptom-based decision tree:

- **Sour/acidic** → under-extracted → grind finer / raise temp / raise ratio
- **Bitter/harsh** → over-extracted → grind coarser / lower temp / lower ratio
- **Watery/flat** → low TDS → more dose / less yield / finer grind
- **Channeling** → uneven distribution → WDT technique, grind adjustment, dose check
- **Gusher** → way too coarse or low dose → significant grind/dose change needed
- **Choked** → way too fine or high dose → significant grind/dose change needed

Each adjustment references Sette 270Wi specifics (e.g., "adjust 1 macro step ≈ ~3-5 second change in shot time").

### `shot-analysis.md`

Guide for interpreting Gaggiuino shot graphs:

- **Pressure curve:** Slow vs fast ramp meaning, plateau stability, decline rate and what it indicates
- **Flow curve:** Stability as indicator of even extraction, sudden spikes = channeling, relationship with grind
- **Temperature curve:** PID stability, thermal surfing artifacts, what fluctuations mean
- **Problem patterns:** Visual examples described in text (e.g., "pressure drops suddenly mid-shot while flow spikes = channeling")
- **Profile-specific interpretation:** What "good" looks like for each profile type

## Skill Behavior (`SKILL.md`)

### Always assumes
- Machine: Gaggia Classic Pro + Gaggiuino
- Grinder: Baratza Sette 270Wi
- User drinks specialty coffee

### Always asks if not provided
- Roast level
- Coffee freshness (days since roast)
- Process (washed/natural/honey) if user knows it

### Response style
- Concise, actionable recommendations
- Grind settings always in Sette 270Wi macro/micro notation
- Temperature in °C
- Dose and yield in grams
- When analyzing a photo: describe what the curves show, then diagnose, then recommend

### Knowledge loading matrix

| Use Case | Files loaded |
|---|---|
| 1. Recommendation | `coffee-fundamentals.md` + `grinder-*.md` + recommended `profiles/*.md` |
| 2. Troubleshooting | `troubleshooting.md` + active `profiles/*.md` + `grinder-*.md` |
| 3. Informational | Relevant `profiles/*.md` and/or `coffee-fundamentals.md` |
| 4. Visual analysis | `shot-analysis.md` + active `profiles/*.md` |

The skill's frontmatter references all knowledge files. On invocation, only the relevant subset is loaded based on query type.

## Build Order

All files are authored in the development repo and then installed to `~/.claude/skills/dial-in/`.

1. `coffee-fundamentals.md` — theoretical foundation
2. `grinder-baratza-sette-270wi.md` — grinder reference used by all profiles
3. `profiles/iuiuiu-classic.md` — primary profile, richest with Discord data
4. Remaining profiles (LMD, Londinium, Adaptive, Blooming, Filter 2.1)
5. `troubleshooting.md` — cross-references profiles
6. `shot-analysis.md` — visual interpretation guide
7. `SKILL.md` — the skill entry point, written last
8. Install: symlink or copy `~/.claude/skills/dial-in/` → skill files
9. (Optional) Concatenate knowledge files into a single doc for Claude iOS Project

## Data Sources

- **Gaggiuino website** (gaggiuino.github.io) — official profile documentation
- **Discord #dialing-n-profiling** — 4,450 scraped messages (Aug 2025 - Mar 2026) stored in `data/raw/`
- **General espresso extraction knowledge** — established principles
- **Sette 270Wi documentation** — grinder specifics

## Future Considerations

- Could evolve into a webapp
- Could scrape additional Discord channels (#profiles, #shots-n-bad-latte-art)
- Could add new profiles as Gaggiuino updates
- Could add other grinders if the user changes equipment
- Raw Discord data available for RAG or other analysis if needed later
