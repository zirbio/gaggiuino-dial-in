# Adaptive Dark Roast v2 (community)

Listed in the community catalogue as "Adaptive for Dark Roast v2"; the profile is named "Adaptive Dark Roast v2" once installed.

## Description

A community variant of [Adaptive](adaptive.md) for darker roasts. It keeps the Adaptive idea -- a pressurized bloom followed by a flow-driven extraction capped at 9 bar -- but fills to a higher pressure, runs cooler, and controls the extraction by flow so the pressure curve descends. The author's description: "Extraction phase is flow limited to allow for a descending pressure curve which makes for a gentler and sweeter shot. v1 is body focused whereas v2 will get you more flavor separation."

**Phases** (from `Adaptive for Dark Roast v2.json` in the community repository):

1. **Fill (PRESSURE 6 bar)** -- Pump fills at full flow until pressure exceeds 6 bar, or 10 s pass.
2. **Bloom (PRESSURE 2 bar)** -- Holds 2 bar for 6 s.
3. **Ramp (PRESSURE 0 → 9 bar, LINEAR 5 s)** -- Flow limited to 2 ml/s. Ends after 7 s, or as soon as flow exceeds 3 ml/s.
4. **Extraction (FLOW 0 → 4 ml/s, EASE_IN over 60 s)** -- Pressure limited to 9 bar. Flow rises slowly at first and faster later; the puck's resistance sets the pressure, which should peak and then fall. Runs until stop-on-weight.

**Defaults in the JSON:** 90 °C, stop-on-weight 32 g (1:1.8 with 18 g in).

**v1 vs v2:** v1 (88 °C, 34 g) ends with a slow pressure ramp from 0 to 5 bar over 120 s and is the body-focused version. v2 is the flavor-separation version described here.

## Best Suited For

- **Roast level:** Medium-dark to dark.
- **Decaf (untested hypothesis):** Decafs tend to extract easily and channel more, so a cooler, flow-controlled profile with a descending pressure curve is a reasonable candidate when regular Adaptive pegs at 9 bar. This is reasoning, not community-validated; confirm by taste.
- **Flavor goals:** Sweet, gentle, low bitterness. Short ratio, so it works well in milk.

## Starting Parameters

| Parameter | Value | Range |
|-----------|-------|-------|
| Dose | 18 g | 17--18 g |
| Yield | 32 g | 32--38 g |
| Ratio | 1:1.8 | 1:1.8--1:2.1 |
| Temperature | 90 °C | 86--92 °C |
| Shot time | ~35 s | 30--45 s (estimate; time is a dependent variable) |
| Basket | Standard | -- |

**Sette 270Wi grind setting:**

- Macro range: **8--14** (as Adaptive)
- Starting point: **10E**, then grind finer. As with Adaptive, approach the sweet spot from the coarse side.

## How to Adjust

1. **Grind size** -- Read the pressure during the extraction phase.
   - Pressure peaks and then declines while flow rises: in range, dial to taste.
   - Pressure stays pinned at 9 bar while flow lags behind its target: too fine, go 2--4 micro steps coarser.
   - Pressure barely reaches 3--4 bar and the shot runs fast: too coarse, go finer.
2. **Ratio** -- Lengthen toward 1:2 if it tastes sour or thin; keep 1:1.8 for body in milk.
3. **Temperature** -- Lower to 86--88 °C if bitter or ashy; raise to 91--92 °C if flat or sour on a medium-dark coffee.
4. **Profile change** -- Want more body: v1. Lighter coffee: regular [Adaptive](adaptive.md) or IUIUIU Classic.

## Community Notes

- Shared in the Gaggiuino Discord thread for the Adaptive dark-roast variants (thread linked from the profile's description in the catalogue).
- The general Adaptive rule still applies: "it shouldn't stay pegged at the pressure limit"; a mountain shape means the grind is right.
- For dark roasts on Adaptive, the community recommends lower temperatures (85--90 °C) and ratios no longer than about 1:2.

## Common Mistakes

1. **Using the regular Adaptive grind.** The higher fill pressure and flow-limited ramp change the puck resistance; re-dial.
2. **Judging by the 9 bar cap.** 9 bar is a limit, not a target. Staying there means too fine.
3. **Jumpy scales.** Stop-on-weight at 32 g is short; a predictive scale that overshoots changes the ratio noticeably.
