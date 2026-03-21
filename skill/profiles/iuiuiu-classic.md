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
