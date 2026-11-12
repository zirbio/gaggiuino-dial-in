# Gaggiuino Website Research — Profile Documentation

## Source: GitHub community branch (Zer0-bit/gaggiuino/profiles)

### Profile System (from User Manual Gen 3)

Gaggiuino profiles consist of **phases**, each with:
- **Type:** PRESSURE or FLOW (which variable is the target)
- **Target:** start value, end value, transition curve (LINEAR, EASE_IN, EASE_OUT, EASE_IN_OUT, INSTANT), time
- **Restriction/Limit:** the other variable's max (e.g., if targeting flow, pressure won't exceed the limit)
- **Stop conditions:** time, pressure above/below, flow above/below, weight change, water pumped
- **Adaptive mode:** adapts start of next phase to match actual end value of previous phase

Global settings per profile: water temperature, stop-on-weight, recipe (coffee in/out, ratio).

### Key Tips from Manual
- Don't expect settings to behave like stock machine
- Dial in based on profile targets, not traditional 25-30s
- Pre-infusion and soak increase flow in extraction phase → grind finer than stock
- Brew Delta makes temp more stable → higher average in-shot temp
- PZ (Pump Zero) calibration affects flow accuracy

---

## IUIUIU Classic

**Description:** Mixed style profile. Flow-driven preinfusion for even puck, free-falling pressure-driven soak for balanced extraction, pressure-driven but flow-limited profiling phase. Good all-rounder.

**Phases (from JSON):**
1. **Preinfusion (FLOW):** Target 3 ml/s (instant), pressure limit 4 bar. Stops at: pressure > 4 bar OR weight > 4g OR 20s OR 60ml pumped
2. **Soak (FLOW):** Target 0 ml/s (pump off, free fall). Stops at: pressure < 2 bar OR 30s
3. **Ramp (PRESSURE):** 0→7.5 bar over 5s (EASE_OUT curve). 5s duration
4. **Extraction (PRESSURE):** 7.5→6 bar (EASE_IN_OUT), flow limit 3 ml/s. Runs until global stop (weight)

**Default recipe:** 18g in, 36g out (1:2 ratio), 93°C

---

## LMD 9-8 v1.5

**Description:** Designed for medium to medium-dark beans. Optimizes even extraction while minimizing overextraction common with darker beans. Transitions from pressure to flow target during extraction.

**Phases (from .md):**
1. **PI (FLOW):** Flow-driven until 2 bar
2. **Soak:** Short soak, transitions after 6s or less (weight/pressure triggers)
3. **Extraction:** Climb to 9 bar over 5s, decrease 1 bar over 4s, then flow-defined. After 10s or pressure drops 3 bar, flow increases to finish

**Default recipe:** 19g in (18-20g range), 38g out (1:2 ratio), standard 20g basket (not HE)

**Notes:**
- "Save the shot" transitions if phases skipped
- 9-8 bar can produce excess crema → lower extraction pressure limits by 1 bar
- v1.5 adds initial phase for missed pressure release

---

## Londinium

**Description:** Simulates Londinium R lever machine extraction. Smooth shots with great body and syrupiness. Similar to previous default profile. Flexible for all bean/roast types.

**Phases (from JSON, verified against `profiles/Londinium.json` and the machine's stored profile, Nov 2026):**
1. **Preinfusion (FLOW):** Target 9 ml/s (instant), pressure limit 4 bar. Stops at: pressure > 4 bar OR 10s OR 65ml pumped
2. **Soak (FLOW):** Target 0 (pump off). Stops at: pressure < 0.7 bar OR 10s
3. **Ramp (PRESSURE):** →9 bar over 1s (EASE_OUT)
4. **Peak (PRESSURE):** 9 bar for 4s, flow limit 3 ml/s
5. **Decline (PRESSURE):** 9→3 bar (EASE_IN_OUT over 20s), flow limit 3 ml/s. Runs until global stop

**Default recipe:** 20g in, 1:2 ratio, stop on 40g, 92°C

---

## Adaptive

**Description:** Adapts to given grind size. Extraction phase decides steady-state flow relative to flow at peak pressure. Pressurized bloom stage maintains puck integrity for consistent resistance. Forgiving to range of grind settings.

**Best for:** Light roasts. For darker: reduce temps and shorter bloom.
**Ratio:** 1:2 to 1:2.5, shot times 25-45s

**Phases (from JSON):**
1. **Preinfusion (FLOW):** Target 7 ml/s (instant), pressure limit 3 bar. Stops at: pressure > 3 bar OR 20s OR 60ml
2. **Bloom (PRESSURE):** Target 3 bar. 6s duration
3. **Ramp (PRESSURE):** 0→9 bar over 5s (LINEAR). 5s duration
4. **Extraction (FLOW):** 0→2.5 ml/s over 25s (LINEAR, adaptive), pressure limit 9 bar. Runs until global stop

**Default recipe:** 15g in, 33g out (1:2.2), 93°C

---

## Blooming Espresso

**Description:** Maximizes extraction quality and quantity. Flow-controlled pre-infusion with long "blooming" phase for full puck saturation before extraction. Best for light roasts, complex beans. Draws out flavors like pour-over while preventing sourness/sharpness.

**Phases (from JSON):**
1. **Preinfusion (FLOW):** Target 4 ml/s, pressure limit 3 bar. Stops at: pressure > 3 bar OR 20s OR 60ml
2. **Bloom (PRESSURE):** Target 2 bar. 20s duration (long bloom!)
3. **Ramp (PRESSURE):** 0→7.5 bar over 5s (EASE_OUT). 5s duration
4. **Extraction (PRESSURE):** 7.5→6 bar (EASE_IN_OUT), flow limit 3 ml/s. Runs until global stop

**Default recipe:** 18g in, 50g out (1:2.8 ratio), 93°C — higher ratio than traditional espresso

---

## Filter 2.1

**Description:** Filter-style coffee from espresso machine. Uses paper filter in basket bottom, puck screen on top. Coarser than espresso but finer than filter. 5:1 ratio. Dilute with 225-250g water.

**Phases (from JSON):**
1. **Preinfusion (FLOW):** Target 4 ml/s, pressure limit 3 bar. Stops at: pressure > 3 bar OR 20s OR 60ml
2. **Soak (FLOW):** Target 0 (pump off). 20s
3. **Extraction (PRESSURE):** Target 3 bar, flow limit 4 ml/s. Runs until global stop

**Default recipe:** 18g in, 90g out (1:5 ratio), 93°C

**Special prep:** Paper filter + puck screen, coarser grind, optional tamp
