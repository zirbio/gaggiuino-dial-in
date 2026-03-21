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
