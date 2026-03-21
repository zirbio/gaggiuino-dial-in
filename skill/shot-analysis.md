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
