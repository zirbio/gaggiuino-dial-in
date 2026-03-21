# LMD 9-8 v1.5 (Loogle Med-Dark)

## Description

A profile designed by Loogle for medium to medium-dark roasts. It optimizes even extraction while minimizing the bitterness and harshness that come from overextracting darker coffees. The pressure curve climbs to 9 bar, then deliberately drops to 8 bar, tapering further as the puck erodes. This declining pressure mirrors what happens naturally in a lever machine and keeps the tail end of the shot clean.

**Phases:**

1. **Pre-infusion** -- Flow-driven until pressure reaches 2 bar. Gently saturates the puck.
2. **Soak** -- Short hold (~6 s). Can also transition on weight or pressure triggers. Lets water penetrate the full puck before extraction pressure begins.
3. **Ramp** -- Pressure climbs from current level to 9 bar over 5 s. This is where extraction begins in earnest.
4. **Decline** -- Pressure drops from 9 bar to 8 bar over 4 s, reducing channeling risk as the puck weakens.
5. **Flow transition** -- The profile transitions to flow-defined control as the puck allows. Flow increases gently toward the end to finish the shot without excessive contact time.

The v1.5 revision added an initial phase to handle missed pressure release (e.g., if the group head still holds pressure from a previous shot).

## Best Suited For

- **Roast level:** Medium to medium-dark (City+ through Full City+).
- **Origin:** Versatile -- works well with Brazil, Colombia, Guatemala, and blends.
- **Process:** Washed and natural. Performs well on chocolatey, nutty, caramel-forward coffees.

## Starting Parameters

| Parameter | Value | Range |
|-----------|-------|-------|
| Dose | 19 g | 18--20 g |
| Yield | 38 g | 36--40 g |
| Ratio | 1:2 | 1:1.8--1:2.2 |
| Temperature | 93 °C | 91--95 °C |
| Shot time | ~30 s | 25--35 s (total, incl. PI) |
| Basket | Standard (NOT HE) | -- |

**Sette 270Wi grind setting:**

- Macro range: **8--13**
- Starting point: **10E** (macro 10, micro E)
- Adjust in 2-micro-step increments until the pressure curve matches the profile shape.

## How to Adjust

Follow this priority order -- exhaust each before moving to the next:

1. **Grind size** -- If pressure is pegged at the limit for the entire shot, grind coarser (2 micro steps). If pressure never reaches 8 bar during extraction, grind finer.
2. **Ratio** -- If the shot tastes sour or thin, pull longer (1:2.2). If bitter or ashy, pull shorter (1:1.8).
3. **Temperature** -- For darker roasts, drop to 91--92 °C. For medium roasts leaning lighter, try 94--95 °C.
4. **Profile change** -- If you cannot get a balanced cup after adjusting the above, the coffee may be too light for this profile. Switch to Adaptive or Blooming Espresso.

## Community Notes

- "Easy to dial in" (krby). Most users get a good shot within 2--3 attempts.
- The pressure drop-off toward the end of the shot is intentional and normal -- do not fight it.
- The 9-8 bar range can produce excessive crema on some coffees. If the shot is foamy and lacks clarity, lower the extraction pressure limits by 1 bar (8-7 bar).
- **Use a standard basket, not an HE (high-extraction) basket** (confirmed by Loogle). HE baskets change flow resistance and the profile was not designed for them.
- If pressure stays pegged at the limit for the entire shot, the grind is too fine. Back off 2--4 micro steps on the Sette.
- Weight jumps in phase 1 caused by jumpy/predictive scales can cause the profile to skip phases prematurely. If this happens, verify scale behavior or remove weight-based triggers from early phases.

## Common Mistakes

1. **Grinding too fine.** The most common issue. If pressure is pegged at the 9-bar limit for the entire extraction with no drop-off, the grind is too fine. The profile needs room for the pressure to decline naturally.
2. **Using HE baskets.** The profile was designed and tested with standard Gaggia baskets. HE baskets have different flow characteristics that break the intended pressure curve.
3. **Ignoring the pressure shape.** A healthy shot should show a clear ramp to 9 bar, a decline to 8 bar, and then further drop-off. If the curve is flat at 9 bar, adjust grind.
4. **Weight-triggered phase skips.** Scales that send erratic weight data (especially predictive/fast-response scales) can trigger phase transitions too early. Watch for sudden jumps from phase 1 to phase 3.
5. **Using too light a roast.** This profile is optimized for medium-dark. Light roasts will tend to underextract and taste sour regardless of adjustments.
