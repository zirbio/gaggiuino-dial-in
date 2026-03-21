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
