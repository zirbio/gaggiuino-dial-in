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
| Dose | 18 g | 17--19 g |
| Yield | 36 g | 34--38 g |
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
