# Leva 9 v0.9 (community)

## Description

A community profile that emulates a spring lever machine. In a real spring lever, pressure does not fall with elapsed time but with the volume of water that leaves the cylinder. Leva 9 copies that: the decline is a chain of small pressure steps, and each step ends after a fixed amount of water has been pumped. A tighter puck lets less water through, so the decline slows down; a looser puck speeds it up. That makes the curve adapt to the grind instead of following a stopwatch, which is why the community calls it more forgiving than Londinium.

**Phases** (from `Leva 9 v0.9.json` in the community repository):

1. **Fill (PRESSURE 1.5 bar)** -- Pump fills the headspace at full flow until pressure exceeds 1.5 bar, 3 g are in the cup, or 10 s pass.
2. **Rise (PRESSURE 0 → 3 bar, EASE_OUT 2 s)** -- Stops when pressure exceeds 3 bar, 3 g are in the cup, or 10 s pass.
3. **Hold (PRESSURE 3 bar)** -- Pre-infusion hold. Stops after 7 s or 10 g in the cup.
4. **Ramp (PRESSURE 0 → 9 bar, EASE_IN_OUT 4 s)** -- Flow limited to 5 ml/s. Ends after 7 ml pumped.
5. **Spring decline (PRESSURE 9 → 4.5 bar)** -- 12 linear steps of 0.3 bar each. Each step ends after 3 ml pumped. Flow limited to 4 ml/s in the first step and 3 ml/s after that. The last step (4.8 → 4.5 bar) runs until the shot is stopped.

**Defaults in the JSON:** 93 °C. **No stop-on-weight is set** (global stop 0). Set stop-on-weight yourself (36--40 g for 18 g in) or the last phase will keep running at 4.5 bar.

The creator's target: about 40 g in the cup by the time pressure reaches 6 bar.

## Best Suited For

- **Roast level:** Medium to medium-dark. The community lists it with Stock 9 bar, LMD 9-8 and LPD as the profiles to try for medium and darker beans aiming for body.
- **Origin:** Versatile. One user called a medium-roast Colombian (1700 m, Antioquia) on Leva "absolutely incredible".
- **Flavor goals:** Lever-style body and sweetness, thicker than IUIUIU Classic. A good fit for milk drinks.

## Starting Parameters

| Parameter | Value | Range |
|-----------|-------|-------|
| Dose | 18 g | 17--18 g |
| Yield | 36 g | 34--40 g (set stop-on-weight: the profile has none) |
| Ratio | 1:2 | 1:1.9--1:2.2 |
| Temperature | 93 °C | 90--94 °C |
| Shot time | ~45 s | 35--60 s (estimate from the phase structure; time is a dependent variable) |
| Basket | Standard | -- |

**Sette 270Wi grind setting:**

- Macro range: **7--12**
- Starting point: **9E**, or the setting that already follows the Londinium curve for the same coffee (both peak at 9 bar).
- Adjust in 1--2 micro steps.

## How to Adjust

Follow this priority order:

1. **Grind size** -- Pressure is the target; read whether the puck can hold it and how fast the decline runs.
   - Pressure never builds past 2--3 bar in pre-infusion, or falls below the step targets with flow pinned at the 3 ml/s limit: too coarse, go finer. ("Leva is a pressure driven profile and you didn't reach the initial target.")
   - Pressure follows the steps and flow stays around 1--2.5 ml/s: in range, dial to taste.
   - Flow stays very low and pressure lingers near 9 bar for a long time (the steps advance by water pumped, so a choked puck stalls the decline): too fine, go coarser.
2. **Ratio** -- Shorter (1:1.9) for more body in milk, longer (1:2.2) if it tastes under-extracted or lacks sweetness.
3. **Temperature** -- 94 °C for medium roasts leaning light; 90--91 °C for darker roasts.
4. **Profile change** -- If it is still harsh or too heavy, try Leva 6 v0.9 from the community catalogue (same idea, starting at 6 bar) or IUIUIU Classic. For more clarity on lighter coffees, Adaptive.

## Community Notes

- "Leva is like Londinium but doesn't have issues if your grind is way off."
- "Zer0 and Leva are good profiles and also pretty popular. Leva simulates a lever more accurately than Londinium."
- With step-down baskets and a large headspace, Leva 9 can struggle to fill. "You can just extend the fill phase." With the standard 18 g basket this should not apply.
- **The profile depends heavily on the calculated pump flow, so PZ calibration matters.** If the decline runs much faster or slower than the cup weight suggests, check the PZ calibration before blaming the grind.

## Common Mistakes

1. **Not setting stop-on-weight.** The community JSON ships without one. Set it before the first shot.
2. **Using a badly calibrated PZ.** The steps end on pumped water, so a wrong pump-flow estimate distorts the whole curve.
3. **Starting before the pressure release.** The first two phases stop on pressure; residual pressure after warm-up can skip the fill. Wait for the "dropping beats".
4. **Jumpy scales.** Phases 1--3 also stop on cup weight (3 g, 3 g, 10 g). A scale that jumps early skips the pre-infusion.
