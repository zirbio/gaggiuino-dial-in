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
| Dose | 18 g | 16--20 g |
| Yield | 50 g | 45--55 g |
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
