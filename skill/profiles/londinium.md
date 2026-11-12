# Londinium

## Description

A profile that simulates the pressure curve of a Londinium R lever espresso machine. Lever machines produce a naturally declining pressure profile -- high initial pressure that gradually drops as the spring relaxes. This creates a smooth, full-bodied, syrupy shot with a long finish. The Gaggiuino implementation replicates this curve with precise pressure control.

**Phases** (from the community JSON; the same definition the machine stores with each shot):

1. **Pre-infusion (FLOW)** -- Flow at 9 ml/s (instant), pressure limited to 4 bar. Stops when pressure exceeds 4 bar, after 10 s, or after 65 ml of water. A fast fill that saturates the headspace and puck quickly.
2. **Soak (FLOW 0, pump off)** -- Pressure falls freely. Stops when pressure drops below 0.7 bar, or after 10 s. The puck absorbs water and settles before the lever "pull".
3. **Ramp (PRESSURE)** -- Pressure rises to 9 bar in 1 s (EASE_OUT). Simulates the lever being released onto the puck.
4. **Peak (PRESSURE)** -- Holds 9 bar for 4 s, flow limited to 3 ml/s.
5. **Decline (PRESSURE)** -- Pressure falls from 9 to 3 bar over 20 s (EASE_IN_OUT), flow limited to 3 ml/s. It then stays at 3 bar until stop-on-weight. This is the spring relaxing -- the declining pressure pulls sweetness and body without the harshness of sustained high pressure.

**Defaults in the JSON:** 92 °C, stop-on-weight 40 g, recipe 20 g in at 1:2. With the 18 g basket, set stop-on-weight to 36--40 g.

## Best Suited For

- **Roast level:** Medium to dark. Excels with Full City and darker.
- **Origin:** Traditional espresso origins -- Brazil, Sumatra, India, Italian-style blends.
- **Process:** Washed and natural. Particularly good with natural-processed coffees where the body and fruit sweetness benefit from the long extraction.
- **Flavor goals:** Heavy body, syrupy mouthfeel, chocolate, caramel, dried fruit, low acidity.

## Starting Parameters

| Parameter | Value | Range |
|-----------|-------|-------|
| Dose | 18 g | 17--18 g |
| Yield | 36 g | 34--40 g |
| Ratio | 1:2 | 1:1.8--1:2.2 |
| Temperature | 92 °C | 88--94 °C |
| Shot time | ~45 s | 40--55 s (total, incl. PI + soak) |
| Basket | Standard | -- |

**Sette 270Wi grind setting:**

- Macro range: **7--12**
- Starting point: **9E** (macro 9, micro E)
- Needs its own grind setting; do not reuse the IUIUIU one. On this setup, one washed Peruvian coffee followed the Londinium curve at 8B and the IUIUIU curve at 5E, so expect to go coarser than IUIUIU, not finer.
- Small adjustments (1--2 micro steps) have a large impact.

## How to Adjust

Follow this priority order:

1. **Grind size** -- Pressure is the target and flow is the limit, so read the flow line. Adjust in 1-micro-step increments.
   - Pressure follows the 9 → 3 bar decline and flow sits around 1--2.5 ml/s: in range, dial to taste.
   - Pressure falls below the target before or during the decline, with flow pinned at the 3 ml/s limit: too coarse, go finer.
   - Pressure follows the target but flow stays under ~1 ml/s and the shot drags well past 55 s: too fine, go coarser.
2. **Ratio** -- For more sweetness and body, pull shorter (1:1.8). For more clarity, pull longer (1:2.2).
3. **Temperature** -- For dark roasts, try dropping to 88--90 °C. One community member tried 88 °C on dark roast and reported excellent results. For medium roasts, stay at 92--93 °C.
4. **Profile change** -- If the shot is too intense or muddy regardless of adjustments, the coffee may be too dark. Consider LMD 9-8 v1.5 for a less aggressive extraction curve. If the grind sensitivity is the problem, try [Leva 9](leva-9.md), a more forgiving lever emulation.

## Community Notes

- **Very sensitive to small grind changes** (spikey). One micro step on the Sette can dramatically change shot behavior. This is the profile's main challenge.
- Leva profiles are cited as more forgiving alternatives that achieve a similar lever-style result ("Leva is like Londinium but doesn't have issues if your grind is way off"). See [leva-9](leva-9.md).
- Pressure is the target, flow is the limit -- the profile is not trying to hit both simultaneously. Pressure defines the curve shape; flow limits prevent channeling.
- **Do NOT use the same grind setting as IUIUIU or other profiles.** One user reported getting a 3-minute shot when using the same grind setting that worked for IUIUIU. Each profile has fundamentally different flow and pressure dynamics.
- For dark roasts, 88 °C was a community favorite. The lower temperature tames bitterness while the long extraction still pulls sweetness.
- "The pressure drops gradually but not fully" can be normal depending on grind.

## Common Mistakes

1. **Using the same grind as another profile.** The Londinium profile requires its own grind calibration. Transferring settings from IUIUIU, Adaptive, or other profiles will almost certainly produce an undrinkable shot.
2. **Adjusting grind in large steps.** Because the profile is so sensitive, large grind changes overshoot. Use 1 micro step at a time on the Sette 270Wi.
3. **Judging by shot time alone.** 40--55 s total is normal because of the fill and soak. Do not grind coarser just to speed up the shot -- you will lose the body and sweetness the profile is designed to produce.
4. **Leaving the default 40 g stop-on-weight with an 18 g dose.** The JSON is set up for 20 g in. With 18 g, 40 g out is 1:2.2; set 36 g for a classic 1:2.
5. **Ignoring temperature for dark roasts.** Running 93 °C on a dark roast through this long extraction will overextract badly. Drop to 88--90 °C.
