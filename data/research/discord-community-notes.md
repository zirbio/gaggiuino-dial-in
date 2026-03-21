# Discord Community Notes: #dialing-n-profiling

Curated from 4,450 messages in the Gaggiuino Discord #dialing-n-profiling channel (Aug 2025 - Mar 2026).

---

## 1. IUIUIU Classic

### Profile overview
- A versatile, moderate-pressure profile. Pressure is the target curve; flow is the limit.
- Best suited for **medium toward light roasts**. Trends toward citrus/bright flavors due to lower max pressure.
- Not ideal for thick/syrupy espresso or very dark roasts.
- Typical total shot time: **40-50 seconds** as a broad ballpark.

### Key insights

- **Loogle**: "IUIUIU Classic is going to trend more toward citrus flavors due to the lower max pressure. It won't be ideal for all beans, especially not if you're going for thick and syrupy espresso." Recommends Stock 9-bar or LMD 9-8 for thicker body.
- **Talon**: "IUIUIU Classic generally does best with medium toward light roasts. For Dark, try Londinium, or pick up LMD from the Community Profiles." Also: "IUIUIU Classic is a great place to start. That said, it depends on the beans you prefer as well as what basket you're using."
- **zooloo10**: "UIUI classic will move on to the main profile when you fall below 2 bars during the soak phase." -- The soak phase has a stop condition of Pressure Below 2 bar.
- **Maybe Sral**: "I usually go with the question 'which curve is more complicated'. Example is IUIUIU, where the pressure is the target." -- Grind to match the pressure curve; flow is the limit.
- **Community member**: "The soak phase is a max of 30 seconds, however, it has a stop condition of Pressure Below 2 bar, which moves it to the next phase."
- **Talon**: For dark roasts with IUIUIU Classic, "definitely go not coarse and let the shot run faster/finish quicker."
- **lnxslckiscool**: Compiled a roast-to-profile mapping. IUIUIU Classic listed under Medium and Dark Roasts.
- **spikey**: Extended fill phase by 5 seconds in phase 1 and 5 seconds in phase 2, reported improved shots. Another user extended fill phase to 25 seconds total.
- **Loogle**: "iuiuiu classic has pressure and weight stop conditions on the first 2 phases. Hard to say 100% from these pics, but it's most likely that you started the shot without waiting for dropping beats (pressure release)." -- Wait for pressure to release before starting.

### Common pitfalls
- Starting the shot without waiting for the pressure drop ("dropping beats") after warm-up. This can cause the preinfusion to be skipped.
- Using it for very dark roasts -- better to use Londinium, LMD, or Stock 9-bar.
- The [ZA] variant has a globals stop on 60ml pumped which can cause early stops (zooloo10 flagged this as possibly a bug).
- Grind too fine: shot runs too long and pressure pegs at the limit. Grind too coarse: pressure drops off dramatically after the first stop condition.

### Specific dialing examples
- **rocketship8452**: DF64 Gen 2 at grind setting 16, VST 18g basket, 18g in / 34g out in 29s, light roast. Shot tasted sour. Community advised the profile's flow target may be set differently from their expectations.
- **Schwede**: DF54 grinder, grind size 12, 18g in / ~36g out, medium-strength Brazil beans. Shot time very long. Community said grind too fine.
- **SebastianP**: Switching from IUIUIU to Londinium at the same grind size produced a 3-minute extraction. Grind sizes between profiles can be wildly different.

---

## 2. LMD 9-8 (Loogle Med-Dark)

### Profile overview
- Designed by Loogle for **medium through medium-dark** roasts.
- Starts pressure-driven, transitions to flow-driven near the end. The pressure drop-off toward the end is normal and expected as the puck degrades.
- Recommended total shot time per the profile description: **36-46 seconds**.
- Use a **standard basket** (IMS, VST, stock), NOT the HE Unibasket.

### Key insights

- **Loogle**: "LMD was intended for the range of Medium through Medium-Dark. Definitely recommend a standard basket, not the HE Unibasket for this profile and bean roast."
- **Loogle**: "the stock profiles aren't going to give you syrupy espresso. For that you'd typically need higher pressure. You could start with a 9-bar Nancy profile and then branch out to LMD 9-8, LPD, and Leva 9."
- **Loogle**: On inconsistency -- "You're getting channeling, which will lead to inconsistencies. Also, if you're using a bean blend you'll run into different bean ratios as you go through." Recommends checking the profile description for grind size references.
- **krby**: "IMO, LMD is pretty easy to dial in." Also: "The puck degrades as time goes on, reducing pressure. To counter this, the LMD profile raises the flow target near the end." And: "It becomes a flow driven profile at the end, so not expected to follow the pressure limit exactly. That drop off at the end is normal."
- **Secretetchantbond**: "No worries, from what I can find it's Chocolate and Nuts flavor profile meaning its likely on the dark side of medium. My preferred profile for those are Cremiuiuino, Londinium, LMD (in that order). Those profiles are Coarse -> fine grind."
- **Zer0-bit**: "Imo depends what you're chasing, if clarity then something that targets that, if balanced then LMD probs spot on."
- **zooloo10**: "As you familiarize yourself with the machine you can try new profiles. Particularly LMD and Leva9 or Londinium are good starting places for dark roast profiles."

### Common pitfalls
- Grinding too fine: pressure stays pegged at 8 bar the entire shot, flow rate becomes extremely low. Solution: grind coarser.
- Grinding too coarse: pressure never reaches the target. Solution: grind finer.
- Using HE baskets with this profile -- Loogle explicitly recommends standard baskets.
- Weight jump in phase 1: LMD has a weight limit of 1g in the first phase. Jumpy scales can trigger this too early, skipping phases (Maybe Sral).
- Dripping during soak with too-fine grind: "Using LMD, it's pressure limited the whole way so I'm guessing I'm too fine."

### Specific dialing examples
- **ClicksMcGee**: LMD 9-8 v1.5, medium/dark roast at 93C, Niche Zero. Two shots 2 ticks apart. krby advised: "you want something right in between these two. The right one is too fine. LMD shouldn't be pegged at the pressure limit all the way to the end."
- **tochoromero**: LMD 8-9 at 90C for Perc Papua New Guinea, "pretty happy with it."
- **Barty McBartface**: DF64 grind size 10 on LMD. Flow never hits target. If ground too coarse, pressure drops; if too fine, flow never reaches target. Classic "sweet spot" search problem.
- **tochoromero**: For Perk Darrrk (dark roast), LMD 9-8 at 85C, 18g in 36g out, Bookoo Cylin basket. Needed to grind much finer than expected. Still a bit bitter.
- **u7karsh**: LMD 9-8, 1.5 clicks on stock calibrated 078s. Shot sour but not harsh, chocolate notes hidden. Community advised to grind finer or try adjusting temp.

---

## 3. Londinium

### Profile overview
- Emulates a Londinium lever machine. Pressure is the target curve.
- Good for **medium to dark roasts**. Often recommended alongside LMD for darker beans.
- Requires a noticeably different grind size than IUIUIU Classic or flow-based profiles.
- Sensitive to small grind adjustments -- can be difficult to dial in on grinders with coarse steps.

### Key insights

- **Maybe Sral**: "For Londinium, the pressure is the more complicated curve. You want to hit that. The flow is just a limit to not go overboard."
- **krby**: "With Londinium, the end of the profile is (I think?) a pressure target and flow limit. You should not be hitting both."
- **Talon**: "Gross generalization, but I feel like coffee profiling culture has moved toward 'as much flow while still following the pressure curve' for shots like Londinium."
- **spikey**: "I found Londinium's really sensitive to tiny changes on my grinder, try one of the Leva profiles." Also: "I was using Londinium; I feel it can be counterproductive, it's sensitive to small adjustments in grind on my low end grinder and I couldn't get reliable performance even between shots."
- **Community tip**: "Leva is like Londinium but doesn't have issues if your grind is way off." -- Leva profiles are more forgiving.
- **Loogle**: "Londinium isn't a great profile for visual PZ calibration -- it doesn't often result in a region with steady pressure, weight flow, and pump flow."
- **Talon**: "Looks in the ball park for Londinium -- followed pressure curve while maintaining most of the flow target. At this point you are in dial-to-taste range."

### Common pitfalls
- Using the same grind size as IUIUIU Classic: one user got a 3-minute extraction. Profiles require different grind sizes.
- Grind too coarse: pressure never hits target, flow pegs at the limit. "Grind finer." (zooloo10)
- Expecting pressure to drop fully as depicted: "The pressure drops gradually but not fully." -- This can be normal depending on grind.
- Sensitive to grinder step size: users with coarser-stepping grinders report inconsistency between shots.

### Specific dialing examples
- **trinitrion**: 18g in, target 38g out, 91C. Satisfied with taste. Good starting point reference.
- **Community member**: "Tried coarser and shorter. Got sour and salty. Changed to Londinium to increase preinfusion and soak. Got the sweet chocolate notes I was looking for. Had a slight bitter acid flavor on the finish so reduced temp to 88. It was lovely."
- **pierre_d0119**: Londinium at 90C for medium-dark ratnagiri estate coffee, 1:2 ratio. Fairly bitter, barely hit pressure. Community said grind finer and consider lower temp.
- **KaliATL**: 17g dose, 34g out, Londinium. Sour and harsh. Talon: "Looks in the ballpark. You are in dial-to-taste range."
- **SebastianP**: Same grind as IUIUIU gave a 3-minute Londinium extraction. krby: "Grind sizes can be wildly different between profiles."

---

## 4. Adaptive

### Profile overview
- Adapts to the bean during extraction. Ramps up to a peak pressure, then transitions to a declining flow.
- Designed to work across a range of roasts with appropriate temperature/grind adjustments.
- Should make a **mountain/pyramid shape** in pressure -- should NOT stay pegged at the pressure limit.
- Very forgiving: "relatively bulletproof -- you really have to be out of range to screw it up" (Secretetchantbond).

### Key insights

- **Maybe Sral**: "The magic is in the adaptive start. That just uses what the Ramp up ended in / the Extraction started with and reaches a flow target of around 2.5 g/s after 30s."
- **Secretetchantbond**: "I have had the best success with those Adaptive profiles for making espresso that my wife actually likes (and more than just super dark beans). It's a really great morning profile where you don't have to think too much." Also: "As long as you have decent puck prep and enough grouphead space and you're within 5 clicks of dialed in you can get a pretty nice adaptive shot."
- **Secretetchantbond**: For dark roasts: "Start coarse and grind finer to your preferred pressure. Makes it quick and easy to dial in (less than 3 shots on average) and each shot you pull will be drinkable instead of many profiles that will gush if you are too coarse."
- **sqrt(2)**: For dark roasts on Adaptive: "Lower temperature to 90C or even 85C, depending on darkness. Ratio should be on the shorter side, probably not longer than 1:2."
- **Secretetchantbond**: "Slow feeding reduces fines and the regrinding phenomenon. Lever shots and 9 bar doesn't really go well with ultralights. I would use Adaptive for Light Roasts or Zer0 profiles and shoot for anywhere from 3-8 bar pressures."
- **krby**: "Yup, Adaptive or Zer0 would be my choices. I find the Zer0 profile to be really tolerant of whatever including my own puck prep mistakes."
- **Community tip**: "Adaptive usually has a ramp into the profile phase, then a decline, makes a mountain/pyramid shape; it shouldn't stay pegged at the pressure limit."
- **sqrt(2)**: "That looks weird for Adaptive. Looks like it skipped the soak phase, maybe because of the big headspace of the step down basket."

### Common pitfalls
- Staying pegged at pressure limit = grind too fine. Should see a mountain shape.
- Step-down baskets with large headspace can cause the soak phase to be skipped.
- If using predictive scales (not Bluetooth), weight can jump early and skip phases.

### Specific dialing examples
- **Secretetchantbond**: Blackstrap from Irving Farms (medium light). Recommended 1:2.2 at 93C. Best flavor separation was at 85C with Adaptive for Light Roasts. "Shot was exceptional compared to the more flat profiles at higher temps."
- **JG13**: Friendo Blendo (Four Barrel), Adaptive V2. Started at grind size 6 (over 1 min), moved coarser. Shots increasingly sour when coarsening. Community said: "sour and slow often means puck prep issue, not grind."
- **NLS44**: Typically uses medium-light with Adaptive. For dark roast transition, sqrt(2) recommended: "Lower temperature to 90C or even 85C."

---

## 5. Blooming Espresso

### Profile overview
- Long preinfusion with a bloom (pump off) phase, then extraction at pressure.
- Intended for **light roasts**. The bloom allows puck saturation and CO2 release.
- Can be challenging to dial in -- not recommended unless you have beans to burn through.
- Paper filter is "kind of a must" (pierre_d0119, referencing Scott Rao).

### Key insights

- **pierre_d0119**: "John Buckman of Decent Espresso and Scott Rao both note that dialing in blooming shots is challenging, and not recommended unless you have a lot of coffee to burn through." Also: "Paper filter is kind of a must for blooming shots. Originally he would sandwich with paper filters on top and bottom."
- **Maybe Sral**: Known Blooming glitch: "if the weight rises too early, Phases 1 and 2 will be skipped and Phase 3 has no pressure limit, but an adaptive flow target." Solution: "remove the weight conditions from phases 1 and 2, or fix your jumpy scales."
- **zooloo10**: "If the predictive scale thinks coffee is in the cup and starts counting weight early it's possible to skip phases prematurely. Hence the suggestion of taring like mad -- continuously hitting the tare button until espresso begins flowing."
- **Maybe Sral**: "The sweetest shot I ever had was a choked Blooming that ran well over 1 min. Sweet and fruit AF though. Might be hard to reproduce."
- **Zer0-bit**: "If you own a HE basket you should be able to use Zer0 or Blooming with great success."
- **Secretetchantbond**: "Bloom also allows for what some theorize to be a re-settling phase where the grounds are slightly free to move and can theoretically lead to less channeling when re-pressurizing."
- **NothingIsReal404**: "If it's still too fresh, blooming would be best." -- Bloom helps release CO2 from very fresh beans.
- **Community tip**: "Forget shot times -- blooming is supposed to have a super long preinfusion. How does it taste?"

### Common pitfalls
- Scales triggering phase skip: the #1 reported issue. Weight conditions on phases 1 and 2 cause premature advancement if scales are jumpy or not tared properly.
- Expecting short shot times: blooming shots are inherently long. Do not judge by time alone.
- Not using paper filters: reduces extraction evenness on blooming shots.
- Pressure never reaching target in phase 4: likely too coarse, or puck already degraded from the bloom.

### Specific dialing examples
- **lewismcgillion**: 20g in, 40g out, light roast. Tastes okay but a bit bitter. Already not hitting 9 bar. Community suggested: "if not hitting 9 bar and bitter, check puck prep or try lower temp."
- **green**: Compared blooming espresso and adaptive v2 with light roasts. "Managed to get some pretty balanced shots in terms of mouthfeel and sweetness with low bitterness/acidity. But I can't say that clarity was impressive."

---

## 6. Filter 2.1

### Profile overview
- A long, high-ratio "filter-style" espresso profile.
- Intended for very long shots (1:5 ratio range).
- Very few community discussions about dialing specifics.

### Key insights

- **kamado-spro**: Looking for ZP6 guidelines. "Is Filter 2.1 the way to go with a 1:5 ratio and what generally are your doses and range of grind settings?" -- No detailed community response recorded.
- **SocraTrees**: "I tried the Filter 2.1 today and the shot was too hot to drink by the end." -- Long extraction time means hot liquid accumulation.
- **The Asian Invasion**: "Making filter 2.1, can I just use steam wand water with a profile to stop on weight?" -- Community didn't flag issues with this approach.
- **Zer0-bit**: For dialing grind without wasting beans: "Grind a few beans and feel the powder with your fingers. If too fine it resembles flour; in the zone it should resemble fine salt. The beans used for dialing you can keep separate and do something like filter 2/3." -- Filter profiles are a useful way to use up test grinds.

### Notes
- This profile has minimal community discussion compared to others. Most users gravitate toward espresso-ratio profiles for daily use.

---

## 7. Grinder Insights

### General principles

- **Zer0-bit**: "There's 10k grinder models in the world, how you think a grind recommendation would be transmitted?" -- Grind settings are not transferable between grinder models.
- **NothingIsReal404**: "Even the same model of grinders can have a different grind size at the same setting."
- **zooloo10**: "Different beans can have big fluctuations in grind. On my Philos most beans I grind at like 28 +/- 2, but occasionally I'll get a bean that's at like 38."
- **NothingIsReal404**: "The coffee itself can need a grind size change every few days from roast as the gas escapes."

### Grinder-specific notes

- **DF64 / DF64 Gen 2**: Zero point is adjustable. Stock zero may actually be quite coarse. Check and reset zero if shots gush. User reports: grind setting 16 for light roast on IUIUIU Classic (rocketship8452). Stock burrs may limit how fine you can go for lighter roasts.
- **DF54**: Grind size 10-12 range for medium roasts on LMD (Glassius). Consider upgrading to Ditting steel burrs -- "probably worth it, but be prepared to chew through a few kilos of seasoning beans" (pierre_d0119). User at grind size 12 for IUIUIU Classic with medium beans reported very long shots (too fine).
- **Eureka (Specialita, Mignon Oro, Manuale)**: Some Eurekas struggle with very light/dense beans. spikey: "I couldn't grind some light roasted or dense beans in my Eureka Manuale." Zer0-bit started using Eureka with standard burrs "straight up" without seasoning issues. The 64mm Mignon Oro handles light roasts fine.
- **Niche Zero**: 2 ticks on the Niche is a meaningful change (ClicksMcGee). FireKingDad uses Niche Zero with IUIUIU [Dark] at 20g in / 30g out.
- **1Zpresso J-Ultra**: Used with LMD for medium-dark. Maybe Sral: "I am always outside the 1zpresso recommended range for espresso by 10-20 clicks."
- **Varia VS3**: Ahole4Sure went from grind setting 2.9 to 3.2 when switching from Londinium to Cremiuiuino.
- **Lagom Casa**: Suggested as a quality upgrade. skaparis was preparing to switch to it from an older grinder.
- **P64**: Secretetchantbond: "My light and medium roasts are usually around 50um on my P64."

### Burrs and paper filters

- **spikey**: "For bottom paper filter in your 58mm Pullman, use a 56/56.5mm. 58s will fold and crease and I get spraying." Also: "Without paper your flowing area at the bottom is the area of the holes, but with filter you're opening up the entire bottom surface of the basket for flow."
- **spikey**: "If you can't grind finer, try without the paper filter." -- Paper adds resistance; removing it effectively makes the grind coarser.
- **Zer0-bit**: "Nope, you can pseudo-HE it by adding a paper filter at the bottom but IMO it's not the same."
- **Secretetchantbond**: "Fines to clog the filter would really only come into play on dark roasts that generate enough to cause a problem."

### Puck screens and shower screens

- **Zer0-bit**: "I think a lot of people don't realize how much the puck screens or shower screen cleanliness plays a role. For the puck screen it matters how dense and how many holes it has; a vast amount of puck screens are super restricting."
- **Loogle**: "You could extend the fill time, increase the fill flow slightly, add a puck screen, or change basket size if headspace is too large."
- **sol**: "With my VST 7g single basket, I usually use a thin Sworks puck screen which keeps the puck from expanding during fill and soak."

### Baskets

- **Secretetchantbond**: "A/B experiment with IMS convex competitizione and Pullman 876 (PERC Papua New Guinea). IMS basket was comforting but a little bland. Pullman basket had much greater separation of juicy flavors but had less body."
- **Loogle**: Use standard basket (IMS, VST, Pullman) for LMD. Not HE baskets.
- **NothingIsReal404**: "I recently had a lighter roast and had to switch to an IMS basket to grind coarser and reach 7 bar."
- **Secretetchantbond**: "I find that I am rarely filling baskets to their designated weight. Use a nickel test to check your grouphead space."
- **NothingIsReal404**: "If the dose is too high for a certain basket it can contact the shower screen/dispersion plate and also mess with the puck."

---

## 8. Troubleshooting Insights

### Sour shots

- **NothingIsReal404**: "Usually you would grind coarser to reduce bitterness which would be the opposite direction of a choked shot. Past following the profile, you can reduce temperature or decrease the ratio."
- **Secretetchantbond**: "If you're having acidity issues try dropping the temp to 88-90. That helps me tame pith-like acidic tastes in many natural and anaerobic coffees (counterintuitive I know). Flow could be a little slower. Grind a touch finer. If still acidic after that, lengthen your ratio."
- **NothingIsReal404**: "Some can even taste more acidic and sour from a finer grind." -- Finer grind increases fines, which can over-extract certain acids.
- **zooloo10**: "Tart can be a 'good' thing if the acidity is pleasant and well rounded. If it's sharp or battery acid like then it's way under extracted."
- **Secretetchantbond**: "The trick is maintaining pressure for an even extraction, that's why gushers get so sour. The coffee bed expands due to losing pressure and then all of a sudden there is a lot more space between the coffee particles."
- **Loogle**: "Are you sure your tastes can differentiate sour, bitter, and astringent? Sometimes people conflate them, which makes dialing much more difficult."

### Bitter shots

- **Secretetchantbond**: "Temp will slow the flow and the coarser grind should remove the bitterness."
- **Secretetchantbond**: Differentiating bitter vs. acidic: "If it makes your mouth dry after you drink it, it is actually bitter you are tasting. If it makes your mouth water like a sour candy, that is acidic."
- **zooloo10**: "Bitter and watery says to me go for less ratio. It should make it more intense and bring it more towards balance."
- **zooloo10**: Salami shot exercise: "Split a shot into 3-4 sequential parts, tasting each." Trains bitter/acid recognition.
- **Secretetchantbond**: "Want more from the bean (darker/bitter flavor and thicker body) - higher pressure, finer, shorter shot. Want less (more acid/fruit/thinner) - lower pressure, coarser, longer."
- **zooloo10**: "Early in the shot is all the easy to extract stuff, salts and acids. As the shot goes on it gets thinner and more of the hard to extract things come through, some of those are the tannins and bitter tasting compounds, as well as more and more fines."

### Channeling

- **Secretetchantbond**: "If the shot is channeling it means either there is a puck prep issue or it's already too fine." Also: flow going to zero after rampup during extraction is a sign of channeling.
- **Loogle**: "You're getting channeling, which will lead to inconsistencies. Also, if you're using a bean blend you'll run into different bean ratios as you go through."
- **Loogle**: "The concern I'd have is that there could be forced channels created if the fill outpaces the natural diffusion via capillary action."
- **spikey**: "Pre-infusion: line pressure (2-3 bar) is used to gently soak the puck to allow for more even extraction and less channeling before full 9 bar pressure."
- **Secretetchantbond**: "Bloom also allows for a re-settling phase where the grounds are slightly free to move and can theoretically lead to less channeling when re-pressurizing."

### Flat / hollow shots

- **Secretetchantbond**: "If your shot was flat then you may want to consider lowering the bicarbonate in your water. I think mine is about 30ppm."
- **Secretetchantbond**: On a hollow-tasting espresso blend at 1:2: "one click coarser grind with 14g out was very salty/sour. Same grind on 18g out was very bitter and watery and hollow." -- Single-dose pulls (8g in 16g out) may have limited flavor complexity.

### Gushers

- **Secretetchantbond**: "Gushers get so sour. The coffee bed expands due to losing pressure and then all of a sudden there is a lot more space between the coffee particles allowing more water to run through even when the grinds are fine. By maintaining pressure wherever the coffee allows it, it maintains a stable filter (the coffee bed)."
- **Secretetchantbond**: For Adaptive, gushers are less likely: "Each shot you pull will be drinkable instead of many profiles that will gush if you are too coarse."

### Temperature guidance

- **Secretetchantbond**: "Temperature is far less dogmatic than what people are claiming. I have had great coferments at 80 degrees and wonderful Ethiopians at 85 and Colombian Italian roasts at 92. Each bean is different and I found a relatively harsh and easily extracted bean does well with colder temps."
- **Secretetchantbond**: "You want an inverse of water temp to flow rate. High flow -> lower temp, Low flow -> higher temp. It helps from overextracting/getting harsh flavors."
- **sqrt(2)**: For dark roasts: "Lower temperature to 90C or even 85C, depending on darkness."
- **NothingIsReal404**: "As for a specific temp you could try, 88 to even 76 if it's extremely bitter and old."

### Dose and ratio guidance

- **Talon**: "I think of grind size as getting the shot to run the profile as intended, and yield as a function of roast level to mitigate for astringency."
- **Talon**: "I tend to live in 18 in, 42 out land (1:2.3) with medium to medium-light."
- **Talon**: "Don't stay married to the 1:2 ratio. Try something wider, like 1:2.3 or 1:2.5."
- **zooloo10**: "Ratio for profiles a lot of times is a suggestion. To me ratio is a combo of the profile and the bean."
- **zooloo10**: "It's pretty rare for me to actually run a 1:3 on most light roasts. I tend to taste bitter/astringent flavors."
- **Secretetchantbond**: "You have to updose your lights and downdose your darks. Light roasts cannot maintain pressure as well as the darks because you will have fewer fines in the light grind."
- **zooloo10**: "Extraction is controlled by lots of things: Grind, Ratio, Temp. Time is a dependent variable."

### Profile selection quick reference (from community consensus)

| Roast Level | Recommended Profiles |
|---|---|
| Light | Adaptive, Blooming, Zer0, Allonge, Extractamundo Dos |
| Medium / Medium-Light | Adaptive, IUIUIU Classic, Zer0 |
| Medium-Dark | LMD 9-8, IUIUIU Classic, Londinium, Leva 9 |
| Dark | Londinium, LMD 9-8, LPD, Leva 9, Stock 9-bar, Adaptive for Dark |

### General dialing-in workflow (Loogle's summary)

1. A profile is a recipe for extracting coffee, designed for a specific dose.
2. Each phase has a **target** (flow or pressure) and may have a **limit** (the other). Never two targets.
3. When the grind is "dialed in" the graphed pressure and flow follow the general target shape.
4. Once the graph matches the profile intent, you are in the **dial-to-taste range**. Further adjustments are slight grind and ratio changes based on sour/bitter/dry/sweet/thin/thick preferences.
5. Phase stop conditions (time, weight, volume, pressure) can move the shot to the next phase.

### Common beginner mistakes

- **Changing multiple variables at once**: Pick one variable (grind, temp, ratio) and adjust incrementally.
- **Ignoring targets vs. limits**: If pressure is pegged at the limit, you are too fine. If flow is pegged at the limit, you may be too coarse.
- **Not waiting for machine warmup/pressure drop**: Start shot only after pressure has released and temp is stable.
- **Not taring scales properly**: Especially critical for Blooming and profiles with weight-based stop conditions.
- **PZ calibration**: If predictive weight is way off from actual, calibrate PZ. zooloo10: "You shouldn't have a 15g error when calibrated properly."
- **Using wrong basket for the profile**: HE baskets for flow profiles (Zer0, Blooming), standard baskets for pressure profiles (LMD, Londinium).
