# Gaggia Dial-In — Complete Knowledge Base

---

---
name: dial-in
description: >
  Recommend espresso extraction adjustments for Gaggia Classic Pro + Gaggiuino.
  Use when asking about espresso profiles, grind settings, troubleshooting shots,
  or analyzing shot photos. Supports IUIUIU Classic, LMD 9-8, Londinium,
  Adaptive, Blooming Espresso, and Filter 2.1 profiles with Baratza Sette 270Wi.
argument-hint: [describe your coffee, problem, or attach a shot photo]
---

# Gaggia Dial-In Assistant

You are an espresso dial-in advisor for a specific setup. Always assume this context:

## Setup
- **Machine:** Gaggia Classic Pro with Gaggiuino mod (pressure/flow profiling, PID, Brew Delta)
- **Grinder:** Baratza Sette 270Wi (macro/micro adjustment, bimodal particle distribution)
- **Basket:** 18g basket, 58mm (max dose: 18g)
- **Water:** Assumed acceptable unless user reports issues

## Query Type Detection

Identify the user's intent and load the appropriate knowledge:

| If the user... | This is... | Load these files |
|---|---|---|
| Attaches a shot photo/screenshot | **Shot analysis** | [shot-analysis](shot-analysis.md) + relevant [profile](profiles/) |
| Describes a taste problem (sour, bitter, flat, etc.) | **Troubleshooting** | [troubleshooting](troubleshooting.md) + active [profile](profiles/) + [grinder](grinder-baratza-sette-270wi.md) |
| Asks what profile/settings for a new coffee | **Recommendation** | [coffee-fundamentals](coffee-fundamentals.md) + [grinder](grinder-baratza-sette-270wi.md) + recommended [profile](profiles/) |
| Asks about differences between profiles or concepts | **Informational** | Relevant [profiles](profiles/) and/or [coffee-fundamentals](coffee-fundamentals.md) |

## Always Ask If Not Provided
Before giving a recommendation, ask for these if the user hasn't mentioned them:
- **Roast level** (light, medium, dark)
- **Freshness** (days since roast)
- **Process** (washed, natural, honey) — if the user knows it

## Response Format
- Grind settings: always in **Sette 270Wi macro/micro notation** (e.g., "try macro 9, micro E" or "go 2 micro steps finer")
- Temperature: always in **°C**
- Dose and yield: always in **grams**
- Adjustments: always in **priority order** (grind first, then dose, then temperature, then ratio, then profile change)

## When Analyzing a Shot Photo
1. **Describe** what the curves show (pressure, flow, temperature behavior)
2. **Diagnose** what's happening (following the profile target? channeling? too fine/coarse?)
3. **Recommend** specific adjustments with Sette 270Wi notation

## Multi-Turn Support
The user may report results after adjusting and ask for further recommendations. Track what was already tried within the conversation and suggest the next adjustment in priority order. Don't repeat suggestions that didn't work.

## Default Profile

If the user does not specify a profile, **assume IUIUIU Classic**. Load [profiles/iuiuiu-classic.md](profiles/iuiuiu-classic.md) as the active profile and base all recommendations on it unless the user explicitly names a different one.

## Available Profiles

| Profile | File | Best For |
|---|---|---|
| **IUIUIU Classic** (default) | [profiles/iuiuiu-classic.md](profiles/iuiuiu-classic.md) | Medium to medium-light, daily all-rounder |
| LMD 9-8 v1.5 | [profiles/lmd-9-8-v1.5.md](profiles/lmd-9-8-v1.5.md) | Medium to medium-dark |
| Londinium | [profiles/londinium.md](profiles/londinium.md) | Medium to dark, lever-style body |
| Adaptive | [profiles/adaptive.md](profiles/adaptive.md) | Light roasts, forgiving, quick dial-in |
| Blooming Espresso | [profiles/blooming-espresso.md](profiles/blooming-espresso.md) | Light roasts, complex single origins |
| Filter 2.1 | [profiles/filter-2.1.md](profiles/filter-2.1.md) | Filter-style from espresso machine |

## Key Principles
- **Time is a dependent variable** — never chase a specific shot time. Adjust grind, dose, temp, and ratio; time follows.
- **One variable at a time** — when troubleshooting, change only one thing per shot.
- **Graph first, taste second** — first get the graph to follow the profile's intended shape, then dial to taste.
- **Different profiles need different grind sizes** — switching profiles often requires significant grind adjustment.

---

# Coffee Fundamentals for Espresso Dial-In

Core theory for making informed extraction decisions on a Gaggia Classic Pro with Gaggiuino mod and Baratza Sette 270Wi.

---

## 1. Roast Levels

Roast level is the single biggest variable that determines your starting recipe. Lighter roasts are denser, less soluble, and harder to extract. Darker roasts are more porous, more soluble, and extract easily.

### Light Roast

- High acidity, floral/fruity notes, tea-like body, low bitterness.
- Dense cell structure means water has to work harder to dissolve solids.
- Needs MORE energy to extract: finer grind, higher temperature, longer contact time.
- **Temperature:** 94-96 C.
- **Pressure profile:** longer preinfusion (8-15 seconds at low pressure) to saturate the dense puck before ramping. Higher brew ratios (1:2.5 to 1:3) to develop sweetness and avoid sourness.
- **Ratio:** 1:2.5 or longer. Short ratios on light roasts taste sour and thin.
- Common mistake: pulling light roasts like dark roasts (short ratio, low temp) and getting a sour, astringent shot.

### Medium Roast

- Balanced acidity and sweetness, some caramel/chocolate notes, moderate body.
- The most forgiving roast level. Good starting point for learning.
- **Temperature:** 92-94 C.
- **Pressure profile:** moderate preinfusion (5-10 seconds). Standard 9-bar profiles work well.
- **Ratio:** 1:2 to 1:2.5.

### Dark Roast

- Low acidity, high bitterness potential, full body, chocolate/roasty/smoky notes.
- Very porous, extracts quickly. Easy to over-extract.
- Needs LESS energy: coarser grind, lower temperature, shorter contact time.
- **Temperature:** 88-92 C.
- **Pressure profile:** shorter preinfusion (3-5 seconds). Consider declining pressure profiles to avoid harshness. Lower peak pressure (7-8 bar) can reduce bitterness.
- **Ratio:** 1:1.5 to 1:2. Longer ratios on dark roasts taste ashy and bitter.
- Common mistake: grinding too fine and getting a bitter, burnt-tasting shot.

### Key Principle

Think of extraction as energy transfer. Every variable (grind size, temperature, pressure, time, ratio) adds energy. Light roasts need more total energy. Dark roasts need less. When you change one variable, the others must compensate.

---

## 2. Origin & Process

Processing method affects bean density, solubility, and how the puck behaves during extraction.

### Washed (Wet) Process

- Fruit removed before drying. Produces cleaner, brighter, more transparent flavors.
- Higher and more consistent bean density.
- More predictable behavior in the puck. Forgiving to fine grinds.
- Good starting point when learning a new recipe.
- Typical flavor notes: citrus, floral, stone fruit, clean sweetness.

### Natural (Dry) Process

- Dried inside the fruit cherry. Produces fruitier, sweeter, more complex flavors.
- Can have inconsistent density (some beans more porous than others).
- More chaff and residue. Can create messy pucks.
- Higher risk of channeling due to uneven particle behavior.
- **Adjustment:** grind slightly coarser than you would for a washed coffee at the same roast level. Longer preinfusion helps even out extraction.
- Typical flavor notes: berry, tropical fruit, wine, fermented sweetness.

### Honey Process

- Partial fruit left on during drying. Falls between washed and natural.
- Moderate density, moderate predictability.
- Typical flavor notes: stone fruit, honey, brown sugar, mild berry.
- **Adjustment:** treat like washed but expect slightly more body and sweetness.

### Anaerobic & Experimental Processes

- Fermented in controlled environments. Can be very intense and unpredictable.
- Often behave like naturals in the puck but with more extreme flavors.
- Start with natural-process settings and adjust from there.
- These coffees can taste funky or boozy if over-extracted. Err on the side of shorter ratios.

### Practical Rule

If a new bag channels or tastes uneven despite a good grind setting, check the process. Naturals and experimentals often need a coarser grind and gentler preinfusion compared to washed coffees at the same roast level.

---

## 3. Freshness

Coffee is a perishable product. Freshness dramatically affects shot behavior, especially in espresso where CO2 plays a visible role.

### The Degassing Timeline

| Days off roast | What happens | Shot behavior |
|---|---|---|
| 1-5 | Heavy CO2 outgassing | Wild, spurty, bubbly. Puck disruption. Very hard to dial in. |
| 5-10 | Active degassing slowing | Still gassy. Shots inconsistent. Crema very thick and foamy. |
| 10-21 | Sweet spot begins | CO2 manageable. Flavors developing. Shots stabilize. |
| 21-35 | Peak window for most coffees | Balanced CO2. Best clarity and sweetness. |
| 35-60 | Fading | Less crema, flatter flavors, easier extraction. Still drinkable. |
| 60+ | Stale | Papery, flat, woody. No crema. |

### Roast-Specific Rest Times

- **Light roasts:** Need the longest rest. 3-4 weeks minimum for espresso. Some light roasts peak at 4-6 weeks. Do not judge a light roast in the first 2 weeks.
- **Medium roasts:** 2-3 weeks is the sweet spot.
- **Dark roasts:** Ready sooner. 7-14 days. They degas faster because the porous structure releases CO2 quickly.

### How Freshness Affects Your Dial-In

- **Too fresh (excess CO2):** The puck expands during extraction, creating channels and uneven flow. Shots spurt and drip unevenly. You will see large bubbles in the stream.
  - Workaround: grind coarser than target, use longer preinfusion (let CO2 escape before ramping pressure), or use a blooming/turbo profile.
- **Too old:** The puck offers less resistance. Flow is faster. You need to grind finer to compensate, but flavors will be flat regardless.
- **Practical tip:** Write the roast date on each bag. If a bag is under 10 days old, expect to chase your grind setting daily as it degases. If you buy in bulk, freeze portions in airtight bags after 7 days to pause aging.

---

## 4. Grind Fundamentals

Grind size is your primary dial-in variable. Everything else (dose, yield, temperature, pressure profile) you set first, then adjust grind to hit your target flow and taste.

### The Core Relationship

**Finer grind** = more surface area = more resistance = slower flow = more extraction.
**Coarser grind** = less surface area = less resistance = faster flow = less extraction.

### Dose

- More coffee in the basket = more resistance to water flow.
- Typical range for a 58mm basket: 15-20g. Most people settle around 17-18g.
- Higher dose gives more body but increases puck resistance. Lower dose gives more clarity.
- Keep dose fixed while dialing in. Change one variable at a time.

### Yield and Ratio

- **Ratio** = yield (liquid out) / dose (dry coffee in), by weight.
- **1:1.5** (ristretto): concentrated, syrupy, less developed flavors. Works for dark roasts or milk drinks.
- **1:2** (standard espresso): the default starting point. Balanced for most medium roasts.
- **1:2.5 to 1:3** (lungo/allonge): more dilute, more clarity, more developed acidity. Often best for light roasts.
- Changing ratio changes extraction percentage. A 1:3 ratio extracts significantly more than 1:1.5 from the same puck.

### Time

- Time is a RESULT, not a target. It falls out of your grind + dose + pressure profile.
- Chasing a specific time (e.g., "must be 25-30 seconds") leads to bad decisions. A light roast turbo shot might finish in 15 seconds and taste great. A dark roast blooming shot might take 45 seconds and taste great.
- Use time as a diagnostic: if the same recipe suddenly runs 5 seconds faster or slower, something changed (grinder retention, bean freshness, humidity).

### The Sette 270Wi: What You Need to Know

The Baratza Sette 270Wi is a conical burr grinder with a **bimodal particle distribution**. This means it produces two clusters of particle sizes: a peak of target-size particles and a secondary peak of fines (very small particles).

What this means in practice:

- **Faster pressure buildup.** Fines migrate to the bottom of the puck and create a dense layer that restricts flow. Shots build pressure quickly even at moderate grind settings.
- **Higher channeling risk.** The fine layer can crack under pressure, creating channels. This is why preinfusion matters on the Sette -- it lets fines settle evenly before full pressure hits.
- **More body, less clarity.** Compared to unimodal grinders (EK43, Lagom P64 with SSP burrs), the Sette produces shots with more texture and less transparency. This is not a flaw -- it is a characteristic.
- **Profiles with preinfusion work well.** The Gaggiuino's ability to do low-pressure preinfusion before ramping is a significant advantage with the Sette. It compensates for the fines issue.
- **Grind adjustments are sensitive.** Small changes on the Sette's macro/micro ring produce noticeable flow differences. Move in small increments (1-2 micro steps at a time).

### Dial-In Workflow

1. Set your dose (keep it fixed).
2. Choose a ratio based on roast level.
3. Set temperature based on roast level.
4. Choose a pressure profile (see profiles documentation).
5. Pull a shot. Taste it.
6. Adjust grind: finer if sour/watery, coarser if bitter/harsh/astringent.
7. Repeat step 5-6 until the shot tastes balanced.
8. Only then fine-tune temperature or ratio if needed.

---

## 5. Water

Water is 90%+ of your espresso by weight. Bad water makes good coffee taste bad, and can damage your machine.

### TDS (Total Dissolved Solids)

- **Target range:** 50-150 ppm.
- **Below 50 ppm (too soft):** Water that is too pure is aggressive -- it over-extracts harshly and produces sour, hollow, flat shots. Distilled or RO water without remineralization will also corrode boiler internals.
- **50-90 ppm:** Light, clean extraction. Good for highlighting acidity and floral notes in light roasts.
- **90-150 ppm:** Fuller body, rounder sweetness. Good for medium and dark roasts.
- **Above 200 ppm (too hard):** Scale buildup in the boiler and solenoid. Muddy, chalky, bitter taste. Muted flavors.

### Mineral Composition Matters

It is not just TDS -- the ratio of calcium, magnesium, and bicarbonate affects flavor:

- **Magnesium** enhances extraction and brightness.
- **Calcium** adds body and roundness.
- **Bicarbonate** acts as a buffer. Too little and shots taste sharp. Too much and they taste flat.
- You do not need to obsess over this. Just avoid extremes.

### Practical Options

- **Filtered tap water:** A carbon filter (Brita, BWT) is the minimum. Check your local water report for hardness. If your tap is 100-150 ppm after filtering, you are fine.
- **Third Wave Water / Aquacode:** Mineral packets you add to distilled or RO water. Consistent, repeatable, and designed for coffee. Good option if your tap water is very hard or very soft.
- **BWT Magnesium filter:** Reduces hardness and adds magnesium. Popular in Europe.

### When to Suspect Water

If your shots taste consistently flat, sour, or bitter despite good beans, correct grind, proper temperature, and a clean machine -- check your water. Specifically:

- Persistent sourness with no bitterness, even when grinding finer: water may be too soft.
- Persistent bitterness and muddy flavors, even when grinding coarser: water may be too hard.
- Scale visible on the shower screen or in the drip tray: water is too hard. Descale and switch to softer water immediately.

### Machine Protection

- The Gaggia Classic Pro boiler is aluminum. Hard water causes scale. Scale causes uneven heating, reduced flow, and eventually component failure.
- Descale every 2-3 months if using tap water, or never if using remineralized soft water.
- The Gaggiuino temperature sensor reads boiler wall temperature. Scale insulates the wall from water, causing temperature readings to diverge from actual brew temperature. If your PID-controlled temps seem off, scale may be the culprit.

---

# Baratza Sette 270Wi — Grinder Reference for Espresso Dial-In

## 1. Adjustment System

- **Macro ring**: numbered 1-31 (1 = finest, 31 = coarsest). Some models use letters instead of numbers.
- **Micro ring**: labeled A-J (or 1-10), subdivides each macro step. A = finest within the macro step.
- **Total resolution**: ~310 distinct positions (31 macro x 10 micro).
- **Adjustment direction**: counterclockwise = finer, clockwise = coarser (verify on the collar markings — arrows are printed on the ring).
- Both rings can be adjusted while the grinder is running or stopped.

## 2. Espresso Range

- Typical espresso range: **macro 5-15**, depending on calibration and coffee.
- For Gaggiuino profiles with preinfusion: expect to grind **finer** than traditional espresso. Preinfusion saturates the puck before full pressure ramps, reducing flow resistance during extraction.
- **Starting point for a new bag**: macro 9-10, micro E (mid-range). Adjust from taste after the first shot.
- Very light roasts may require macro 5-8. Dark roasts may land at macro 12-15.

## 3. Step Impact

- **1 macro step** change ≈ 3-5 seconds difference in shot time.
- **1 micro step** change ≈ 0.5-1 second difference in shot time.
- These are rough guidelines — actual impact varies with coffee age, dose, basket size, and profile.
- **Dialing-in rule**: adjust in micro steps unless the shot is very far off target (more than 8-10 seconds), then use macro steps.
- When making adjustments, change only one variable at a time (grind OR dose, not both).

## 4. Characteristics

- **Low retention**: ~0.2-0.5g (excellent for single-dosing without purging).
- **Bimodal particle distribution**: produces more fines than unimodal grinders (Commandante, EK43).
  - Results in: faster pressure buildup, more body, less clarity in the cup.
  - Implications: works well with profiles that include proper preinfusion to hydrate fines evenly before full pressure.
  - Channeling risk is slightly higher due to fines migration — good puck prep (WDT with 0.3-0.4mm needles) is essential.
- **Fast grinding**: a typical 18g dose is ground in ~5-7 seconds.
- **Integrated scale** (Wi model): weight-based dosing stops the grinder automatically at the target weight. Set the target ~0.3g below desired dose to account for retention release.
- **Static**: can produce moderate static with certain coffees, causing grounds to cling. A single drop of water on beans before grinding (Ross Droplet Technique / RDT) helps significantly.

## 5. Starting Points per Profile Type

These are approximations. Actual settings depend on coffee origin, roast level, freshness, dose, and basket.

| Profile             | Suggested Macro Range | Notes                                                        |
| ------------------- | --------------------- | ------------------------------------------------------------ |
| IUIUIU Classic      | 7-12                  | Good preinfusion helps; grind fine. Start at 9E.             |
| LMD 9-8 v1.5        | 8-13                  | Long preinfusion; start slightly coarser than IUIUIU.        |
| Londinium           | 7-12                  | Similar to IUIUIU, lever-style extraction. Start at 9E.     |
| Adaptive            | 8-14                  | Designed to be forgiving; wider usable range. Start at 10E.  |
| Blooming Espresso   | 9-14                  | Long bloom phase reduces resistance; can go coarser.         |
| Filter 2.1          | 14-20                 | Much coarser than espresso; paper filter further reduces resistance. |

**How to use this table**: start at the middle of the suggested range with micro E. Pull a shot, evaluate taste and time, then adjust in micro steps.

## 6. Calibration

- **New grinder**: run calibration per Baratza instructions — align burrs so they just touch at the "1" macro position.
- **Calibration check**: if macro range shifts significantly over time (e.g., needing to grind 3+ macro steps finer than usual for the same coffee), recalibrate.
- **After changing burrs**: always recalibrate before use.
- **Calibration drift** is normal over months of use and does not indicate a problem — just recalibrate.
- Baratza provides a calibration video and instructions on their support site. The process takes ~5 minutes.

## 7. Maintenance

- **Clean burrs** every 2-4 weeks, or every 5-10 kg of coffee ground.
- **Signs of dull burrs**: increasing channeling, needing to grind much finer than usual, visible clumping, inconsistent shot times with the same settings.
- **Burr lifespan**: steel burrs last approximately 600-800 kg of coffee (years of typical home use at 2-4 shots per day).
- **Cleaning method**: use Grindz tablets (1 cap, run through on a medium setting) or disassemble and brush with a stiff bristle brush. Never use water on the burrs.
- **Shim check**: the Sette uses a shim system for alignment. If you notice uneven extraction despite good puck prep, check that the shims have not shifted during cleaning.
- **Replace the gasket ring** around the grounds container if static buildup worsens — it wears over time.

---

# Troubleshooting — Symptom-Based Dial-In Guide

Symptom-first decision tree for diagnosing and fixing espresso shots on a Gaggia Classic Pro with Gaggiuino mod and Baratza Sette 270Wi grinder. For each symptom: diagnosis, then ordered adjustments (grind → dose → temperature → ratio → profile).

---

## 1. Sour / Acidic

**Diagnosis:** under-extracted. Not enough soluble material dissolved from the coffee.

**Adjustments (in order):**

1. **Grind finer** — 1-2 micro steps on the Sette (e.g., 9E → 9C).
2. **Raise temperature** — +1-2 C (e.g., 93 → 95 C).
3. **Increase ratio** — pull longer (try 1:2.3 or 1:2.5 instead of 1:2).
4. **Check freshness** — beans under 10 days off roast produce excess CO2. CO2 disrupts the puck, causes channeling, and leads to under-extraction even when grind is correct. Wait, or use a Blooming profile.

> "If you're having acidity issues try dropping the temp to 88-90. That helps me tame pith-like acidic tastes in many natural and anaerobic coffees (counterintuitive I know)." — Secretetchantbond

> "Tart can be a 'good' thing if the acidity is pleasant and well rounded. If it's sharp or battery acid like then it's way under extracted." — zooloo10

---

## 2. Bitter / Harsh / Astringent

**Diagnosis:** over-extracted. Too much dissolved from the coffee, including unpleasant compounds.

**Adjustments (in order):**

1. **Grind coarser** — 1-2 micro steps on the Sette (e.g., 9E → 9G).
2. **Lower temperature** — -1-2 C (e.g., 94 → 92 C).
3. **Decrease ratio** — pull shorter (try 1:1.8 instead of 1:2).
4. **If mouth-drying (astringent):** likely channeling, not uniform over-extraction. Focus on puck prep before changing grind.

> "If it makes your mouth dry after you drink it, it is actually bitter. If it makes your mouth water like a sour candy, that is acidic." — Secretetchantbond

> "Bitter and watery says to me go for less ratio." — zooloo10

---

## 3. Watery / Flat / Hollow

**Diagnosis:** low TDS, insufficient extraction strength. The shot lacks body and presence.

**Adjustments (in order):**

1. **Grind finer** — 1-2 micro steps to increase puck resistance.
2. **Increase dose** — +0.5-1g (e.g., 17g → 18g).
3. **Decrease yield** — pull a shorter ratio (1:1.8 instead of 1:2) to concentrate the shot.
4. **Check water** — very soft water (below 50 ppm) produces flat, hollow shots regardless of grind.

> "Consider lowering the bicarbonate in your water." — Secretetchantbond

---

## 4. Channeling (Uneven Extraction, Spraying, Mixed Sour+Bitter)

**Diagnosis:** water finding paths of least resistance through the puck instead of flowing evenly.

**Signs on Gaggiuino graph:** sudden flow spike paired with pressure drop mid-shot. Bottomless portafilter shows uneven streams or spray.

**Adjustments (in order):**

1. **Improve puck prep** — use WDT with 0.3-0.4mm needles, ensure level tamp.
2. **If puck prep is already good:** grind is probably too fine. Fines clump and create weak spots. Go 1-2 micro steps coarser.
3. **Check dose vs basket capacity** — too much coffee makes the puck touch the shower screen, creating an uneven surface.
4. **Clean shower screen and puck screen** — old coffee oils redirect water.
5. **Very fresh beans:** excess CO2 disrupts the puck. Try a Blooming profile or wait a few more days.

> "If the shot is channeling it means either there is a puck prep issue or it's already too fine." — Secretetchantbond

---

## 5. Gusher (< 15 Seconds, Fast Uncontrolled Flow)

**Diagnosis:** way too coarse or insufficient dose. The puck offers almost no resistance.

**Adjustments (in order):**

1. **Grind significantly finer** — 1-2 MACRO steps on the Sette, not micro (e.g., macro 12 → macro 10).
2. **Increase dose** — +1g.
3. **Consider adding a paper filter** — adds resistance and slows flow.

> "Gushers get so sour. The coffee bed expands due to losing pressure." — Secretetchantbond

> Adaptive profile is more forgiving here: "Each shot you pull will be drinkable instead of many profiles that will gush if you are too coarse."

---

## 6. Choked (No Flow or < 1 ml/s, Pressure at Pump Max)

**Diagnosis:** way too fine or excessive dose. Water cannot push through the puck.

**Adjustments (in order):**

1. **Grind significantly coarser** — 1-2 MACRO steps on the Sette (e.g., macro 8 → macro 10).
2. **Reduce dose** — -1g.
3. **If using a paper filter:** remove it (it adds resistance on top of an already tight puck).
4. **Clean burrs** — old grounds and oils cause clumping, which mimics an overly fine grind.

---

## 7. Both Sour AND Bitter

**Diagnosis:** channeling or very uneven extraction. Some areas of the puck are over-extracted (bitter) while others are under-extracted (sour). This is the trickiest scenario — usually NOT a grind size issue alone.

**Adjustments (in order):**

1. **Focus on puck prep first** — WDT is essential. Ensure even distribution and level tamp.
2. **Try a profile with better preinfusion** — IUIUIU Classic, Adaptive, or Blooming all help saturate the puck evenly before full pressure.
3. **Check basket size vs dose** — ensure sufficient headspace (1-2mm between puck top and shower screen).
4. **Consider water** — extreme mineral content (too hard or too soft) can produce mixed flavors.

---

## 8. Profile-Specific Issues

| Profile | Symptom | Likely Cause |
|---|---|---|
| IUIUIU Classic | Preinfusion appears skipped | Did not wait for pressure release before brew phase started. |
| LMD 9-8 | Pressure pegged at limit entire shot | Too fine. Pressure decline toward end of shot is normal and expected. |
| Londinium | Shot takes 3+ minutes | Using the same grind as IUIUIU — Londinium needs a different (usually coarser) setting. Very sensitive to small changes. |
| Adaptive | Pressure stays pegged flat | Too fine. Should see a mountain/pyramid shape on the pressure graph. |
| Blooming | Phases getting skipped | Jumpy scales triggering weight-based phase transitions early. Remove weight conditions from phases 1-2 or tare constantly. |
| Filter 2.1 | Shot runs too hot | Normal for long extractions. Use a significantly coarser grind than espresso (macro 14-20). |

---

## 9. General Dialing-In Workflow

1. **A profile is a recipe.** Each phase has a target (flow or pressure) and may have a limit.
2. **Dial grind until the pressure/flow graph matches the profile's intended shape.** If the graph looks wrong, grind is the first thing to change.
3. **Once the graph matches → you are in dial-to-taste range.** Now adjust ratio and temperature for flavor.
4. **Change ONE variable at a time.** Pull a shot, taste, adjust one thing, repeat.
5. **Time is a dependent variable.** Do not chase a specific shot time — it falls out of grind, dose, and profile.

### Profile Selection by Roast Level

| Roast Level | Recommended Profiles |
|---|---|
| Light | Adaptive, Blooming, Zer0 |
| Medium / Medium-Light | Adaptive, IUIUIU Classic |
| Medium-Dark | LMD 9-8, IUIUIU Classic, Londinium |
| Dark | Londinium, LMD 9-8, Stock 9-bar, Adaptive (with lower temp) |

---

# Shot Analysis — Reading Gaggiuino Graphs

How to interpret pressure, flow, temperature, and weight curves from Gaggiuino shot graphs on a Gaggia Classic Pro.

---

## 1. What the Gaggiuino Screen Shows

**Two image sources — both show the same data:**

- **Physical touchscreen:** smaller display on the machine. Photos may have glare or angle distortion.
- **Web UI screenshot (192.168.x.x):** cleaner, larger, higher resolution. Layout may differ slightly.

**Curves displayed:**

- **Pressure (bar):** green/teal. Y-axis 0-12 bar.
- **Flow (ml/s):** blue/purple. Y-axis 0-6 ml/s.
- **Temperature (C):** red/orange. Y-axis in degrees Celsius.
- **Weight (g):** yellow/white. Cumulative grams in the cup.

**Layout:** X-axis = time in seconds (auto-scales). The active profile's target curve appears as a thin reference line or shaded region behind actual data. Shot metadata (weight, elapsed time, temperature setpoint) displayed at bottom or sidebar. Phase transitions may appear as vertical lines.

---

## 2. Pressure Curve Reading

The pressure curve is the primary diagnostic tool. Its shape should match the profile's target.

**Preinfusion (first 5-20 seconds):**
- Pressure rises gradually as water saturates the puck.
- Preinfusion pressure limits by profile: IUIUIU/Londinium 4 bar, Adaptive 3 bar, LMD 2 bar, Blooming 7 bar.
- Builds TOO FAST (hits limit in 2-3s) = too fine. Builds TOO SLOW (barely rises after 10s) = too coarse.

**Ramp:** should follow the profile's curve type (EASE_OUT, LINEAR, or EASE_IN_OUT). Smooth ramp = good puck integrity. Erratic movement = distribution issues.

**Extraction — expected shape per profile:**

| Profile | Peak | Extraction Shape | Flow Limit |
|---------|------|------------------|------------|
| IUIUIU Classic | 7.5 bar | Declines 7.5 to 6 bar | 3 ml/s |
| LMD 9-8 v1.5 | 9 bar | 9 bar ~5s, drops to 8 bar, then flow-driven decline | 3.5 then 2 ml/s |
| Londinium | 9 bar | Holds ~4s, then long decline 9 to 3 bar over 20s | 3 ml/s |
| Adaptive | 9 bar cap | Mountain/pyramid: rises, peaks, naturally declines | Flow ramps 0-2.5 ml/s |
| Blooming | 7-9 bar cap | Long low-pressure soak, then flow-driven at 2 ml/s | 9 bar cap |
| Filter 2.1 | ~1 bar | Very low, sustained. Flow-driven at 0.2-3 ml/s | 9 bar cap (never reached) |

**Warning signs:**
- **Pegged at pump max or profile limit entire extraction:** too fine. Profile cannot express its target decline.
- **Drops off early, never reaches target:** too coarse.
- **Sudden drop mid-shot (5+ bar in 1-2s):** channeling event.
- **Oscillating/bouncing:** pump cavitation, air in line, or inconsistent puck.

---

## 3. Flow Curve Reading

In pressure-target phases, flow is a dependent variable. In flow-target phases (Adaptive extraction, LMD late phases, Blooming extraction), flow IS the controlled variable and pressure responds.

**Healthy patterns:**
- Stable flow during extraction = even extraction.
- Gradually rising flow in the last third = normal puck degradation.
- Flow near the profile's flow limit = profile working as designed.

**Warning signs:**
- **Sudden spike (1+ ml/s jump in 1-2s):** channeling. Usually paired with pressure drop.
- **Very low flow (< 0.5 ml/s) + pressure at pump max:** approaching choked. Much too fine.
- **Erratic/jumping flow throughout:** distribution issues or scale calibration problems.
- **Flow pegged high + pressure never reaching target:** gusher. Much too coarse.
- **Flow dropping to zero mid-shot then resuming:** clog then channel breakthrough, or scale dropout.

**For flow-target phases:** pressure should naturally decline as flow increases and puck degrades. Declining pressure during these phases is expected and correct.

---

## 4. Temperature Curve Reading

- Should be stable within +/-1 C of setpoint during extraction.
- With **Brew Delta** enabled: boiler temperature RISES during the shot (compensating for cold tank water). Graph may show 5-10 C above setpoint at the boiler — this is normal and intentional.
- **Large drop (3+ C below setpoint):** Brew Delta may be off, or high flow rate overwhelming the 100ml boiler.
- **Offset from setpoint before shot starts:** PID tuning issue or temperature offset needs calibration.
- **Spiking above setpoint:** PID overshoot. May cause burnt/harsh flavors.
- **Post-shot:** boiler temp will be elevated. Wait 30-60 seconds before next shot.

---

## 5. Combined Pattern Diagnosis

**Good shot:** pressure follows profile target shape, flow stable or gently rising, temperature flat near setpoint, weight accumulates smoothly. No sudden spikes or drops.

**Channeling:** simultaneous pressure DROP + flow SPIKE mid-shot (typically 15-30s into extraction). May recover or persist.

**Puck erosion:** GRADUAL pressure decline + GRADUALLY increasing flow. Normal in the last 30% of long shots. Problematic if it starts within the first 10 seconds of extraction.

**Choked:** pressure at pump max (~12 bar), flow near zero (< 0.3 ml/s). Nothing comes out.

**Gusher:** pressure never reaches target (e.g., 4 bar when targeting 9), flow very high, shot finishes in under 15 seconds.

**Skipped phase:** sudden jump/discontinuity in the graph. Causes: jumpy scales triggering weight stop conditions, residual pressure triggering pressure stop conditions (did not wait for pressure release), or incorrect PZ calibration.

**Flat extraction on dynamic profiles:** all curves featureless and constant. On profiles designed to have dynamic shapes (Adaptive mountain, IUIUIU decline, Londinium slope), flatness means the grind is preventing the profile from expressing its curve.

---

## 6. Profile-Specific "Good Shot" References

**IUIUIU Classic (40-50s, 18g in / 36g out):**
- PI: pressure rises to ~4 bar over 5-10s, pump stops. Soak: free-fall through 2 bar (3-10s).
- Extraction: ramps to 7.5 bar (EASE_OUT, 5s), then gently declines to ~6 bar. Flow stays near 3 ml/s limit.
- Too fine = pressure flat at 7.5, flow pegged at limit. Too coarse = pressure drops below 6 bar quickly.

**LMD 9-8 v1.5 (36-46s, 18g in / 36g out):**
- PI: flow at 4 ml/s, pressure limited to 2 bar. Soak: pressure drops to ~1 bar (up to 6s).
- Extraction: ramps to 9 bar (EASE_IN_OUT, 4-5s), holds, drops to 8 bar over 4s, then transitions to flow-driven. Pressure declines naturally in late phases — this is EXPECTED.
- Too fine = pressure pegged at 9 bar entire shot. The late-shot decline is the hallmark of a well-dialed LMD.

**Londinium (40-55s, 18g in / 36g out):**
- PI: flow-driven, pressure limited to 4 bar. Soak: free-fall toward 0.7 bar (up to 10s).
- Extraction: fast rise to 9 bar (1s), holds ~4s, then long smooth decline 9 to 3 bar over 20s (EASE_IN_OUT).
- The decline should look like a smooth ski slope. Flat at 9 = too fine. Steep drop = too coarse.

**Adaptive (25-45s, 15g in / 33g out):**
- PI: flow 7 ml/s, pressure limited to 3 bar. Bloom: holds 3 bar for 6s. Ramp: 0-9 bar over 5s (LINEAR).
- Extraction: flow ramps 0-2.5 ml/s over 25s. Pressure forms a MOUNTAIN/PYRAMID — peaks at 7-9 bar, declines to 3-5 bar.
- Flat line at 9 bar = too fine. Mountain peaks at 5-6 bar = too coarse.

**Blooming Espresso (50-70s, 18g in / 36g out):**
- PI: flow 4 ml/s, pressure limited to 7 bar. Bloom: pump off, long soak, pressure drops toward 0.6 bar (up to 30s).
- Extraction: flow-driven at 2 ml/s (EASE_OUT ramp), pressure limited to 9 bar.
- Very long total time is NORMAL. Up to 5g output during bloom is expected.

**Filter 2.1 (90-120s+, 18g in / 36g stop-on-weight):**
- PI: flow 4 ml/s, pressure limited to 1 bar. Main: flow at 0.2 ml/s, pressure stays 1-3 bar. Late: flow ramps to 3 ml/s.
- Looks nothing like espresso. Low flat pressure, low flat flow, very long time. If pressure exceeds 4-5 bar: grind too fine (use Sette macro 14-20).

---

## 7. Photo Quality Fallback

**Blurry or unreadable image:** ask for four data points to diagnose from numbers:
1. Peak pressure reached (bar)
2. Total shot time including preinfusion (seconds)
3. Final yield weight (grams)
4. Taste description (sour, bitter, balanced, watery, harsh)

**Not a Gaggiuino screen:** inform user this analysis is for Gaggiuino graphs. Offer manual data entry diagnosis.

**Cropped (missing curves):** work with what is visible. Pressure alone is sufficient for grind diagnosis. Flow alone can identify channeling. Temperature alone is least diagnostic.

**Web UI vs. touchscreen:** both valid. Web UI is typically cleaner. Suggest web UI for future analysis if the user has network access.

---

# Adaptive

## Description

A forgiving, self-adjusting profile that adapts to a wide range of grind sizes. The pressurized bloom phase maintains puck integrity even when the grind is not perfectly dialed in, making it an excellent daily driver and a great starting profile for new Gaggiuino users. The extraction phase uses adaptive flow control -- flow ramps up linearly while pressure is capped, so the profile naturally adjusts extraction dynamics based on how the puck responds.

**Phases:**

1. **Pre-infusion** -- Flow at 7 ml/s (instant), pressure limited to 3 bar. Stops when pressure exceeds 3 bar, or after 20 s, or after 60 ml of water. The higher flow rate (compared to other profiles) fills the headspace quickly.
2. **Bloom** -- Holds 3 bar for 6 s. Pressurized bloom maintains puck structure and ensures even saturation before extraction begins.
3. **Ramp** -- Pressure rises from 0 to 9 bar over 5 s (LINEAR curve). Smooth transition into full extraction pressure.
4. **Extraction** -- Flow ramps from 0 to 2.5 ml/s over 25 s (LINEAR, adaptive), with pressure limited to 9 bar. This is where the "adaptive" behavior happens: flow increases gradually, and the puck's resistance determines how much pressure builds. If the grind is fine, pressure hits the 9-bar cap early and flow self-limits. If coarser, flow increases freely with lower pressure.

The pressure curve during extraction should form a **mountain or pyramid shape** -- rising, peaking, and declining. If pressure stays flat at 9 bar the entire time, the grind is too fine.

## Best Suited For

- **Roast level:** Primarily light roasts, but works across the full spectrum with temperature adjustments.
- **Origin:** Single origins, especially complex light-roast coffees (Ethiopian, Kenyan, Colombian micro-lots).
- **Process:** Washed, natural, honey, anaerobic -- all work well. The forgiving nature accommodates different puck behaviors from different processes.
- **Use case:** Daily driver. Morning shots where you want consistency without fussing. New coffees you haven't dialed in yet.

## Starting Parameters

| Parameter | Value | Range |
|-----------|-------|-------|
| Dose | 15 g | 14--18 g |
| Yield | 33 g | 30--40 g |
| Ratio | 1:2.2 | 1:2--1:2.5 |
| Temperature | 93 °C | 85--95 °C |
| Shot time | ~35 s | 25--45 s (total, incl. PI + bloom) |
| Basket | Standard | -- |

**Sette 270Wi grind setting:**

- Macro range: **8--14** (wider than most profiles because the profile is forgiving)
- Starting point: **11E** (macro 11, micro E)
- Start coarser than you think and grind finer. The profile tolerates a wide grind range, so you have room to explore.

## How to Adjust

Follow this priority order:

1. **Grind size** -- Start coarse and grind finer in 2-micro-step increments. Watch the pressure curve: you want a mountain/pyramid shape that rises, peaks, and falls. If pressure stays pegged at 9 bar for most of the shot, grind coarser. If pressure barely reaches 6--7 bar, grind finer.
2. **Ratio** -- For more sweetness and rounded flavor, pull longer (1:2.3--1:2.5). For more intensity, pull shorter (1:2). Light roasts generally benefit from the longer ratios.
3. **Temperature** -- This is a powerful lever for this profile. For light roasts, try 85 °C for the best flavor separation (counterintuitive, but community-validated). For dark roasts, drop to 85--90 °C to avoid overextraction.
4. **Profile change** -- If you want more body and less clarity, switch to Londinium or LMD 9-8. If you want even more extraction for very light roasts, try Blooming Espresso.

## Community Notes

- "Relatively bulletproof" (Secretetchantbond). Multiple users report dialing in new coffees in fewer than 3 shots.
- The pressure curve **must** form a mountain/pyramid shape. If pressure stays pegged at 9 bar for the entire extraction, the grind is too fine. This is the single most important diagnostic.
- Start coarse and grind finer. It is easier to approach the sweet spot from the coarse side with this profile.
- For light roasts, 85 °C produced the best flavor separation for several community members. The lower temperature prevents astringency and lets fruit/floral notes come through.
- Great "morning profile" -- users report not needing to think or adjust from day to day once dialed in.
- Works as an all-rounder for shops or homes that rotate coffees frequently.

## Common Mistakes

1. **Pressure staying pegged at 9 bar.** The most common issue. If the pressure curve is a flat line at 9 bar, the grind is way too fine. Grind 4--6 micro steps coarser and re-pull.
2. **Step-down baskets with large headspace.** Baskets that create excessive headspace above the puck can cause the soak phase to behave incorrectly, sometimes skipping it entirely. Use a standard basket or ensure the puck sits close to the shower screen.
3. **Jumpy/predictive scales skipping phases.** Scales that send erratic weight data can trigger phase transitions prematurely. If phases seem to skip, check scale behavior or remove weight triggers from the first two phases.
4. **Not adjusting temperature for roast level.** Running 93 °C on a very dark roast through this profile will overextract. Running 93 °C on a very light roast may produce astringency. Use temperature as an active tool, not a constant.
5. **Grinding too fine from the start.** Unlike profiles that require fine grinding, Adaptive works best when you approach the sweet spot from the coarse side. Starting too fine creates channeling and pegged pressure.

---

# Blooming Espresso

## Description

A profile built around a long bloom phase that fully saturates the puck before extraction begins. Inspired by Scott Rao's blooming espresso technique, it maximizes extraction quality by giving CO2 time to escape and water time to penetrate every particle in the coffee bed. The result is a cup with pour-over-like clarity and complexity, but with more body than an actual pour-over. This is one of the more challenging profiles to dial in, but rewards the effort with exceptional cups from light-roast coffees.

**Phases:**

1. **Pre-infusion** -- Flow at 4 ml/s, pressure limited to 3 bar. Stops when pressure exceeds 3 bar, or after 20 s, or after 60 ml. Gentle initial saturation.
2. **Bloom** -- Holds 2 bar for **20 seconds**. This is the defining feature: a long, low-pressure soak that lets CO2 escape from fresh beans and allows water to penetrate the full depth of the puck. The puck swells, settles, and becomes uniformly saturated.
3. **Ramp** -- Pressure rises from 0 to 7.5 bar over 5 s (EASE_OUT curve). The ease-out ramp applies pressure quickly at first, then slows as it approaches target -- gentler on the freshly bloomed puck.
4. **Extraction** -- Pressure declines from 7.5 to 6 bar (EASE_IN_OUT curve), with flow limited to 3 ml/s. The declining pressure prevents overextraction as the puck erodes, while the lower peak pressure (7.5 bar vs. traditional 9 bar) keeps the extraction gentle.

The lower peak pressure (7.5 bar) and long bloom work together to extract evenly without the harshness that 9-bar profiles can produce on light roasts.

## Best Suited For

- **Roast level:** Light to light-medium. This is a light-roast specialist profile.
- **Origin:** Complex single origins -- Ethiopian (Yirgacheffe, Guji), Kenyan, Panamanian Gesha, Colombian competition lots, high-altitude Central Americans.
- **Process:** Washed for maximum clarity. Natural and honey for fruit-forward sweetness. Anaerobic and experimental processes that benefit from extended extraction.
- **Flavor goals:** Floral, fruit, tea-like, bright acidity with sweetness. Pour-over character in an espresso format.

## Starting Parameters

| Parameter | Value | Range |
|-----------|-------|-------|
| Dose | 18 g | 16--18 g |
| Yield | 50 g | 45--50 g |
| Ratio | 1:2.8 | 1:2.5--1:3 |
| Temperature | 93 °C | 88--95 °C |
| Shot time | ~50 s | 40--65 s (total, incl. PI + bloom) |
| Basket | Standard | -- |

**Sette 270Wi grind setting:**

- Macro range: **9--14**
- Starting point: **11E** (macro 11, micro E)
- Slightly coarser than traditional espresso. The long bloom and high ratio compensate for the coarser grind.

**Note:** The 1:2.8 ratio is much higher than traditional espresso (1:2). This is intentional -- the profile is designed to extract more from the coffee, producing a longer, more dilute but more complex shot.

## How to Adjust

Follow this priority order:

1. **Grind size** -- If pressure never reaches the 7.5-bar target during extraction, the grind is too coarse -- go finer in 2-micro-step increments. If pressure is pegged at the limit with minimal flow, go coarser. You want to see pressure reach the target and then decline naturally.
2. **Ratio** -- For more intensity, pull shorter (1:2.5). For more clarity and complexity, pull longer (1:3). Light roasts almost always taste better at the longer end of the range.
3. **Temperature** -- For very light Nordic-style roasts, try 93--95 °C. For light-medium roasts, 90--92 °C prevents any overextraction bitterness.
4. **Profile change** -- If the shot lacks body and feels too thin, this coffee may be better suited to Adaptive (which provides more body at a shorter ratio). If you want a true filter-style cup, try Filter 2.1 instead.

## Community Notes

- **Paper filter is "kind of a must"** (referencing Scott Rao's technique). Place a 58 mm paper filter at the bottom of the basket before dosing. This produces a cleaner cup and prevents fines migration.
- **The #1 issue is scale-triggered phase skips.** Jumpy or predictive scales send erratic weight data that can cause the profile to skip from phase 1 or 2 directly to later phases, ruining the bloom. Solutions: remove weight conditions from phases 1--2 in the profile editor, or tare the scale immediately before starting the shot.
- The bloom phase helps release CO2 from very fresh beans (2--7 days off roast). If you usually rest beans for 2+ weeks, the bloom still helps with saturation but the CO2 effect is less dramatic.
- Shot times are long by design (40--65 s total). Do not judge this profile by time -- judge by yield and taste.
- This profile is more challenging to dial in than Adaptive or LMD 9-8. It is not recommended for beginners. Get comfortable with a forgiving profile first, then graduate to Blooming Espresso.

## Common Mistakes

1. **Jumpy scales skipping phases.** The most common and most frustrating issue. Scales with aggressive predictive algorithms send weight spikes that trigger phase transitions. Check your scale's behavior or remove weight-based triggers from the PI and bloom phases.
2. **Expecting short shot times.** This is not a 25-second shot. Total time including pre-infusion and bloom will be 40--65 s. Pulling faster defeats the purpose of the profile.
3. **Not using a paper filter.** The paper filter is a core part of the technique. Without it, fines migrate through the basket and the cup loses clarity -- the main advantage of this profile.
4. **Pressure never reaching the extraction target.** If the flow rate is high and pressure stays well below 7.5 bar during extraction, the grind is too coarse. The profile needs enough puck resistance to build pressure.
5. **Using this profile for dark roasts.** The long bloom and high ratio will massively overextract dark-roast coffee. This profile is built for light roasts. Use LMD 9-8 or Londinium for darker coffees.
6. **Dose too high for basket capacity.** With a 20-second bloom, the puck swells. If you dose near the basket's maximum, the puck can press against the shower screen and create uneven extraction. Dose conservatively (16--18 g).

---

# Filter 2.1

## Description

A profile that produces filter-style coffee from an espresso machine. This is fundamentally different from espresso -- it uses a paper filter, a coarser grind, a very high ratio, and low pressure to create a concentrated filter-style extraction that is then diluted with hot water (similar to an Americano, but with filter-coffee character rather than espresso character). Think of it as a bypass brew: the machine extracts a concentrate at low pressure, and you add water to reach drinking strength.

**Phases:**

1. **Pre-infusion** -- Flow at 4 ml/s, pressure limited to 3 bar. Stops when pressure exceeds 3 bar, or after 20 s, or after 60 ml. Gentle saturation of the coarser-ground coffee.
2. **Soak** -- Flow drops to 0 (pump off) for 20 s. The water sits in the puck with no pressure applied, allowing full saturation without any forced extraction. Similar to the bloom in pour-over brewing.
3. **Extraction** -- Pressure held at 3 bar, flow limited to 4 ml/s. Low, steady pressure pushes water through the puck slowly, extracting gently -- more like percolation than high-pressure espresso extraction.

The low extraction pressure (3 bar) and paper filter produce a clean, sediment-free cup that tastes like filter coffee rather than espresso. The higher flow limit (4 ml/s) keeps the extraction moving despite the coarse grind.

## Best Suited For

- **Roast level:** Light to medium. Best with light roasts that have delicate, complex flavors you want to preserve.
- **Origin:** High-quality single origins where you want maximum clarity -- Ethiopian washed, Kenyan, Panamanian, high-altitude Colombian.
- **Process:** Washed coffees shine brightest. Natural and honey also work well.
- **Use case:** When you want a filter-style cup but only have an espresso machine. Morning coffee in a larger volume. Using up test grinds or small amounts of leftover beans.

## Starting Parameters

| Parameter | Value | Range |
|-----------|-------|-------|
| Dose | 18 g | 15--18 g |
| Yield | 90 g | 75--90 g |
| Ratio | 1:5 | 1:4--1:6 |
| Temperature | 93 °C | 90--96 °C |
| Shot time | ~90 s | 60--120 s (total) |
| Basket | Standard | -- |
| Dilution | 225--250 g water after extraction | To taste |

**Sette 270Wi grind setting:**

- Macro range: **14--20** (much coarser than espresso!)
- Starting point: **17A** (macro 17, micro A)
- This is closer to pour-over grind territory. If you are used to espresso settings in the 8--12 range, you need to go dramatically coarser.

**Special preparation:**

1. Place a 58 mm paper filter at the bottom of the basket. Rinse it with hot water to remove paper taste and help it adhere.
2. Fill the basket with ground coffee. Grind should be coarser than espresso but finer than typical pour-over -- a medium-fine grind.
3. WDT (Weiss Distribution Technique) to break up clumps.
4. Optional light tamp. Some users prefer no tamp; others give a very light press to level the bed.
5. Place a puck screen on top of the coffee.
6. Pull the shot. It will be a long extraction (60--120 s).
7. Dilute the output (90 g concentrate) with 225--250 g of hot water to reach drinking strength.

## How to Adjust

Follow this priority order:

1. **Grind size** -- If the shot chokes or takes more than 2 minutes, grind coarser (2--4 macro steps -- yes, macro steps, not micro). If water rushes through in under 45 s total, grind finer.
2. **Ratio** -- For a stronger concentrate (less dilution needed), pull 1:4. For a lighter, more tea-like cup, pull 1:6.
3. **Temperature** -- Higher temperatures (95--96 °C) extract more from light roasts. Lower temperatures (90--92 °C) work better for medium roasts.
4. **Dilution** -- Adjust the amount of water you add after extraction. More water = lighter, more filter-like. Less water = stronger, more intense.
5. **Paper filter** -- If you cannot grind fine enough to get adequate resistance (shot rushes through), add the paper filter. If you cannot grind coarse enough (shot chokes), try removing the paper filter -- it adds resistance.

## Community Notes

- Minimal community discussion compared to other profiles. This is a niche use case.
- Shots can get very hot during the long extraction (SocraTrees). The cup will be hotter than a typical espresso shot. Be careful with thin-walled cups.
- Good way to use up test grinds (Zer0-bit). If you have small amounts of coffee left from dialing in other profiles, run them through Filter 2.1 for a drinkable cup.
- The paper filter adds meaningful flow resistance. If your grinder cannot go coarse enough for this profile, removing the paper filter is a valid adjustment.
- Total extraction time is long by design. A 90-second shot is normal.

## Common Mistakes

1. **Using espresso grind.** This is the most common mistake. Espresso-fine grinds will completely choke the machine at 3-bar extraction pressure. You need to go dramatically coarser -- think pour-over territory (macro 14--20 on the Sette).
2. **Not using a paper filter.** The paper filter is integral to the profile. Without it, fines pass through the basket and the cup tastes muddy rather than clean and filter-like.
3. **Expecting espresso-like results without dilution.** The 90 g output is a concentrate, not a finished drink. It will taste extremely strong and unbalanced undiluted. You must add 225--250 g of water to reach proper filter-coffee strength.
4. **Judging by shot time.** A 90-second extraction is normal for this profile. Do not grind coarser just because the shot "takes too long" by espresso standards.
5. **Using dark roasts.** The high ratio (1:5) and long extraction time will overextract dark roasts badly. This profile is designed for light to medium coffees.
6. **Skipping the rinse on the paper filter.** Unrinsed paper filters impart a papery taste that is noticeable in the clean cup this profile produces. Always rinse.

---

# IUIUIU Classic

## 1. Description

Mixed style profile. Flow-driven preinfusion, free-falling pressure soak, pressure-driven extraction with flow limit.

**Phases:**

1. **Preinfusion (FLOW):** Target 3 ml/s (instant), pressure limit 4 bar. Stops when: pressure > 4 bar, weight > 4g, 20s elapsed, or 60ml pumped.
2. **Soak (FLOW):** Target 0 ml/s (pump off, free fall). Stops when: pressure drops below 2 bar or 30s elapsed.
3. **Ramp (PRESSURE):** 0 to 7.5 bar over 5s with EASE_OUT curve.
4. **Extraction (PRESSURE):** 7.5 to 6 bar declining (EASE_IN_OUT), flow limit 3 ml/s. Runs until stop-on-weight triggers.

**Philosophy:** The flow-driven preinfusion saturates the puck evenly before pressure builds. The soak lets pressure drop naturally (the puck absorbs water and CO2 escapes), ensuring the bed is ready for extraction. The declining pressure extraction (7.5 to 6 bar) with a flow limit produces balanced extraction without the harshness of sustained 9-bar pressure. Because max pressure is lower than traditional 9-bar profiles, IUIUIU Classic trends toward brighter, more citrus-forward flavors with less body compared to profiles like LMD or Londinium.

---

## 2. Best Suited For

- **Primary sweet spot:** Medium to medium-light roasts. This is where the profile shines.
- **Works with adjustment:** Some dark roasts if you lower temperature and let the shot run faster (shorter contact time).
- **Not ideal for:** Very dark/oily roasts (use LMD, Londinium, or Stock 9-bar) or very light roasts (use Adaptive or Blooming).
- **Process:** Washed and honey processes work well. Naturals may need a slightly coarser grind to avoid channeling from uneven particle density.
- **Character:** Good daily all-rounder for specialty coffee. Expect clarity and brightness rather than thick, syrupy body.

---

## 3. Starting Parameters

| Parameter      | Value                                                    |
| -------------- | -------------------------------------------------------- |
| Dose           | 18g (stock double basket)                                |
| Yield          | 36g (1:2 ratio)                                         |
| Temperature    | 93C (medium roast), 90-91C (dark), 94-95C (light)       |
| Grind (Sette)  | Macro 7-12 range. Start at **9E** for a new bag.        |
| Stop-on-weight | 36g                                                      |
| Total time     | 40-50 seconds (do not chase time -- it is a dependent variable) |

**Ratio guidance by roast:**
- Medium: 1:2 (36g out from 18g in)
- Medium-light: 1:2 to 1:2.3 (36-41g out)
- Light: 1:2.3 to 1:2.5 (41-45g out)
- Dark: 1:1.8 to 1:2 (32-36g out)

---

## 4. How to Adjust (priority order)

1. **Grind first** -- always. Adjust in micro steps (1-2 at a time) unless the shot is very far off (more than 8-10 seconds from target range), then use macro steps.
   - Pressure stays pegged at the limit during extraction / shot runs too long = grind is too fine. Go coarser.
   - Pressure drops off dramatically after ramp / gusher / fast thin shot = grind is too coarse. Go finer.
   - Goal: pressure should follow the 7.5 to 6 bar decline without pegging at the flow limit.

2. **Ratio** -- try 1:2 to 1:2.5 range. Lighter roasts often benefit from 1:2.3 to 1:2.5 for more sweetness and developed acidity. Darker roasts can go shorter (1:1.8 to 1:2).

3. **Temperature** -- adjust 1-2C per roast level. If sour despite correct grind, raise temp 1C. If bitter/harsh, lower temp 1C.

4. **Profile change** -- if IUIUIU does not suit the bean after reasonable adjustment:
   - Very dark roast or want more body/syrup: try LMD 9-8 or Londinium.
   - Very light roast: try Adaptive or Blooming.
   - Want maximum forgiveness: try Adaptive.

---

## 5. Community Notes

Curated from Discord #dialing-n-profiling (Aug 2025 - Mar 2026):

- **Loogle:** "IUIUIU Classic is going to trend more toward citrus flavors due to the lower max pressure. It won't be ideal for all beans, especially not if you're going for thick and syrupy espresso." Recommends Stock 9-bar or LMD for thicker body.
- **Talon:** Best with medium toward light roasts. For dark roasts, try Londinium or LMD. For dark roasts on IUIUIU, "go not coarse and let the shot run faster/finish quicker."
- **zooloo10:** The soak phase moves to extraction when pressure drops below 2 bar. The 30s is a maximum -- most shots transition sooner. Wait for the pressure release ("dropping beats") before starting the shot.
- **spikey:** Extending fill phase by 5 seconds in phases 1 and 2 improved shots. Another user extended fill to 25 seconds total with good results.
- **Maybe Sral:** "I usually go with the question 'which curve is more complicated'. For IUIUIU, the pressure is the target." Grind to match the pressure curve; flow is the limit.
- **Loogle:** IUIUIU Classic has pressure and weight stop conditions on the first 2 phases. Starting without waiting for pressure release can cause preinfusion to be skipped entirely.
- **SebastianP:** Switching from IUIUIU to another profile (e.g., Londinium) at the same grind size produced a 3-minute extraction. Grind sizes between profiles can be wildly different -- always re-dial when switching profiles.
- **Important:** The [ZA] variant has a 60ml water pumped global stop that can cause early stops. zooloo10 flagged this as possibly a bug. Use the standard IUIUIU Classic, not the [ZA] variant.

---

## 6. Common Mistakes

- **Not waiting for pressure release after warm-up.** The machine builds pressure during idle. If you start the shot before pressure drops ("dropping beats"), the preinfusion phase sees pressure > 4 bar immediately and skips to soak. This ruins the puck saturation. Wait until pressure releases before pulling.
- **Using for very dark roasts.** The lower max pressure (7.5 bar) and declining profile will not produce the thick, syrupy body that dark roasts usually need. Switch to LMD, Londinium, or Stock 9-bar.
- **Grinding too fine.** Pressure pegs at the limit throughout extraction, flow crawls, shot takes forever. The pressure curve should decline from 7.5 toward 6 bar -- if it stays flat at the flow limit ceiling, grind coarser.
- **Grinding too coarse.** Pressure drops off after ramp, never reaches 7.5 bar, shot finishes fast with sour/watery taste. Grind finer.
- **Changing multiple variables at once.** Adjust grind first. Only change temperature or ratio after grind is dialed in. One variable at a time.
- **Expecting traditional 25-30 second shot times.** This profile runs 40-50 seconds total due to the preinfusion and soak phases. That is normal. Do not grind coarser just to hit a faster time.
- **Using the same grind as another profile.** If you switch to or from IUIUIU Classic, expect to re-dial your grind. The difference can be several macro steps depending on the profile.

---

# LMD 9-8 v1.5 (Loogle Med-Dark)

## Description

A profile designed by Loogle for medium to medium-dark roasts. It optimizes even extraction while minimizing the bitterness and harshness that come from overextracting darker coffees. The pressure curve climbs to 9 bar, then deliberately drops to 8 bar, tapering further as the puck erodes. This declining pressure mirrors what happens naturally in a lever machine and keeps the tail end of the shot clean.

**Phases:**

1. **Pre-infusion** -- Flow-driven until pressure reaches 2 bar. Gently saturates the puck.
2. **Soak** -- Short hold (~6 s). Can also transition on weight or pressure triggers. Lets water penetrate the full puck before extraction pressure begins.
3. **Ramp** -- Pressure climbs from current level to 9 bar over 5 s. This is where extraction begins in earnest.
4. **Decline** -- Pressure drops from 9 bar to 8 bar over 4 s, reducing channeling risk as the puck weakens.
5. **Flow transition** -- The profile transitions to flow-defined control as the puck allows. Flow increases gently toward the end to finish the shot without excessive contact time.

The v1.5 revision added an initial phase to handle missed pressure release (e.g., if the group head still holds pressure from a previous shot).

## Best Suited For

- **Roast level:** Medium to medium-dark (City+ through Full City+).
- **Origin:** Versatile -- works well with Brazil, Colombia, Guatemala, and blends.
- **Process:** Washed and natural. Performs well on chocolatey, nutty, caramel-forward coffees.

## Starting Parameters

| Parameter | Value | Range |
|-----------|-------|-------|
| Dose | 18 g | 17--18 g |
| Yield | 36 g | 34--36 g |
| Ratio | 1:2 | 1:1.8--1:2.2 |
| Temperature | 93 °C | 91--95 °C |
| Shot time | ~40 s | 36--46 s (total, incl. PI) |
| Basket | Standard (NOT HE) | -- |

**Sette 270Wi grind setting:**

- Macro range: **8--13**
- Starting point: **10E** (macro 10, micro E)
- Adjust in 2-micro-step increments until the pressure curve matches the profile shape.

## How to Adjust

Follow this priority order -- exhaust each before moving to the next:

1. **Grind size** -- If pressure is pegged at the limit for the entire shot, grind coarser (2 micro steps). If pressure never reaches 8 bar during extraction, grind finer.
2. **Ratio** -- If the shot tastes sour or thin, pull longer (1:2.2). If bitter or ashy, pull shorter (1:1.8).
3. **Temperature** -- For darker roasts, drop to 91--92 °C. For medium roasts leaning lighter, try 94--95 °C.
4. **Profile change** -- If you cannot get a balanced cup after adjusting the above, the coffee may be too light for this profile. Switch to Adaptive or Blooming Espresso.

## Community Notes

- "Easy to dial in" (krby). Most users get a good shot within 2--3 attempts.
- The pressure drop-off toward the end of the shot is intentional and normal -- do not fight it.
- The 9-8 bar range can produce excessive crema on some coffees. If the shot is foamy and lacks clarity, lower the extraction pressure limits by 1 bar (8-7 bar).
- **Use a standard basket, not an HE (high-extraction) basket** (confirmed by Loogle). HE baskets change flow resistance and the profile was not designed for them.
- If pressure stays pegged at the limit for the entire shot, the grind is too fine. Back off 2--4 micro steps on the Sette.
- Weight jumps in phase 1 caused by jumpy/predictive scales can cause the profile to skip phases prematurely. If this happens, verify scale behavior or remove weight-based triggers from early phases.

## Common Mistakes

1. **Grinding too fine.** The most common issue. If pressure is pegged at the 9-bar limit for the entire extraction with no drop-off, the grind is too fine. The profile needs room for the pressure to decline naturally.
2. **Using HE baskets.** The profile was designed and tested with standard Gaggia baskets. HE baskets have different flow characteristics that break the intended pressure curve.
3. **Ignoring the pressure shape.** A healthy shot should show a clear ramp to 9 bar, a decline to 8 bar, and then further drop-off. If the curve is flat at 9 bar, adjust grind.
4. **Weight-triggered phase skips.** Scales that send erratic weight data (especially predictive/fast-response scales) can trigger phase transitions too early. Watch for sudden jumps from phase 1 to phase 3.
5. **Using too light a roast.** This profile is optimized for medium-dark. Light roasts will tend to underextract and taste sour regardless of adjustments.

---

# Londinium

## Description

A profile that simulates the pressure curve of a Londinium R lever espresso machine. Lever machines produce a naturally declining pressure profile -- high initial pressure that gradually drops as the spring relaxes. This creates a smooth, full-bodied, syrupy shot with a long finish. The Gaggiuino implementation replicates this curve with precise pressure control.

**Phases:**

1. **Pre-infusion** -- Flow at 4 ml/s, pressure limited to 3 bar. Stops when pressure exceeds 3 bar, or after 20 s, or after 60 ml of water. Gentle saturation that builds back-pressure naturally.
2. **Soak** -- Holds 3 bar for 5 s. Lets water distribute evenly through the puck before the main extraction ramp.
3. **Ramp** -- Pressure rises from 0 to 9 bar over 4 s (LINEAR curve). Simulates the lever being pulled down.
4. **Extraction** -- Pressure declines from 9 bar to 6 bar over 45 s (LINEAR curve), with flow limited to 3 ml/s. This is the lever spring releasing -- a long, slow, declining extraction that produces the characteristic Londinium body.

The 45-second declining extraction phase is the heart of this profile. It keeps contact time high while progressively reducing pressure, which pulls sweetness and body without the harshness that comes from sustained high pressure.

## Best Suited For

- **Roast level:** Medium to dark. Excels with Full City and darker.
- **Origin:** Traditional espresso origins -- Brazil, Sumatra, India, Italian-style blends.
- **Process:** Washed and natural. Particularly good with natural-processed coffees where the body and fruit sweetness benefit from the long extraction.
- **Flavor goals:** Heavy body, syrupy mouthfeel, chocolate, caramel, dried fruit, low acidity.

## Starting Parameters

| Parameter | Value | Range |
|-----------|-------|-------|
| Dose | 18 g | 17--18 g |
| Yield | 36 g | 34--36 g |
| Ratio | 1:2 | 1:1.8--1:2.2 |
| Temperature | 93 °C | 88--94 °C |
| Shot time | ~55 s | 45--65 s (total, incl. PI + soak) |
| Basket | Standard | -- |

**Sette 270Wi grind setting:**

- Macro range: **7--12**
- Starting point: **9E** (macro 9, micro E)
- This profile requires a noticeably finer grind than most other profiles. Small adjustments (1--2 micro steps) have a large impact.

## How to Adjust

Follow this priority order:

1. **Grind size** -- This profile is very sensitive to grind changes. Adjust in 1-micro-step increments. If the shot gushes and finishes under 40 s total, grind finer. If pressure stays pegged at 9 bar with minimal flow, grind coarser.
2. **Ratio** -- For more sweetness and body, pull shorter (1:1.8). For more clarity, pull longer (1:2.2).
3. **Temperature** -- For dark roasts, try dropping to 88--90 °C. One community member tried 88 °C on dark roast and reported excellent results. For medium roasts, stay at 92--93 °C.
4. **Profile change** -- If the shot is too intense or muddy regardless of adjustments, the coffee may be too dark. Consider LMD 9-8 v1.5 for a less aggressive extraction curve.

## Community Notes

- **Very sensitive to small grind changes** (spikey). One micro step on the Sette can dramatically change shot behavior. This is the profile's main challenge.
- Leva profiles are cited as more forgiving alternatives that achieve a similar lever-style result.
- Pressure is the target, flow is the limit -- the profile is not trying to hit both simultaneously. Pressure defines the curve shape; flow limits prevent channeling.
- **Do NOT use the same grind setting as IUIUIU or other profiles.** One user reported getting a 3-minute shot when using the same grind setting that worked for IUIUIU. Each profile has fundamentally different flow and pressure dynamics.
- For dark roasts, 88 °C was a community favorite. The lower temperature tames bitterness while the long extraction still pulls sweetness.
- Expect longer total shot times (50--65 s) compared to traditional profiles. This is by design.

## Common Mistakes

1. **Using the same grind as another profile.** The Londinium profile requires its own grind calibration. Transferring settings from IUIUIU, Adaptive, or other profiles will almost certainly produce an undrinkable shot.
2. **Adjusting grind in large steps.** Because the profile is so sensitive, large grind changes overshoot. Use 1 micro step at a time on the Sette 270Wi.
3. **Fighting the long shot time.** A 55--60 s total shot time is normal. Do not grind coarser just to speed up the shot -- you will lose the body and sweetness the profile is designed to produce.
4. **Using a stepped grinder without micro-adjustment.** Grinders with only macro steps will struggle to find the narrow sweet spot. The Sette 270Wi's micro adjustment is well suited for this profile.
5. **Ignoring temperature for dark roasts.** Running 93 °C on a dark roast through this long extraction will overextract badly. Drop to 88--90 °C.

---

