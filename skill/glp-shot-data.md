# Reading Shot Data from GLP (Gaggiuino Local Profiler)

[GLP](https://github.com/mxkissnr/gaggiuino-local-profiler) syncs every shot from the Gaggiuino and stores the curves together with the user's notes (bean, dose, grind setting, rating). When its MCP server is connected to Claude Code (server name `glp`), read the data directly instead of asking the user to describe the shot or send a photo.

## When to Use It

Use GLP when the `mcp__glp__*` tools are available and the user:
- asks to analyse "my last shot", "today's shots" or a shot id
- asks how a bean is going, or which grind worked best for it
- asks for a recommendation and you need the recent history of the bean

If the tools are not available, or GLP has no matching shot, fall back to the normal flow (description or photo) and say so in one line.

## Tools (read-only)

| Tool | Use it for |
|---|---|
| `list_shots` | Find shots, newest first. Filter by bean name, minimum rating or date range |
| `get_shot` | One shot's metrics, score and annotation. Ask for the curve when diagnosing |
| `compare_shots` | 2–5 shots side by side with deltas against the first one |
| `list_beans` | The bean library: roaster, origin, process, roast level and date, stock, remembered grind settings |
| `get_library` | Grinders, baskets, puck screens and recipes |
| `get_analytics_summary` | Trends over a time window (default 30 days) |
| `get_machine_status` | Whether GLP can reach the machine and when it last synced |
| `get_maintenance_status` | Descaling, backflush and gasket status |

GLP also offers two ready-made prompts: `analyse_shot` and `dial_in_bean`.

## Workflow: Analyse a Shot

1. `list_shots` with `limit` 1 (or the bean filter) to find the shot id.
2. `get_shot` with `include_curve: true` (the default 100 samples per series is enough).
3. Read `profile_name` and load the matching file in [profiles/](profiles/). If it is not one of the documented profiles, say so and analyse it against general principles. `profile_name` is often empty for shots GLP imported from the machine's history (GLP 3.7.0 does not copy the name over). In that case, infer the profile from the target curves (`target_pressure`, `target_flow`) and the preinfusion length, and state the guess so the user can correct it.
4. Get context for the bean: `list_shots` filtered by the bean, then `compare_shots` against the previous one or two shots of the same bean. The difference between consecutive shots is what the last adjustment changed.
5. Analyse with [shot-analysis](shot-analysis.md): describe the curves, diagnose, recommend.

## Reading the Data Correctly

- **Grind setting** is a free-text field typed by the user. Interpret it in Sette 270Wi notation (e.g., `9E` = macro 9, micro E). If it is empty, ask for it; never guess it from the shot time.
- **Rating and notes** are the user's taste verdict. Taste overrides GLP's score: a high score with "sour" in the notes is a sour shot.
- **GLP score (0–100) and its grind suggestion** target a generic 25–32 s extraction. That does not fit long-preinfusion or blooming profiles (Londinium, Blooming Espresso, Filter 2.1). Use the profile file's targets, not GLP's, and remember that time is a dependent variable.
- **Missing data** (no bean, no dose, no weight because the scale was off) must be stated, not filled in. Ask for it when it changes the recommendation.
- **Timestamps** are UTC. Convert them to Europe/Madrid before talking about "this morning" or "yesterday".
- **GLP's grind suggestion** (`best_grind_setting`) is numeric. It does not map onto Sette macro/micro notation, so ignore it and recommend in Sette notation from the comparison yourself.
- **Roast date** comes from the bean's bag. Compute days since roast from it and use it as the freshness input.

## Limits

- The connection is read-only by design: do not try to annotate shots, change settings or touch the machine through GLP. Tell the user to add notes in the GLP app.
- GLP syncs every few minutes and only while the computer hosting it is on and on the home network. A shot pulled seconds ago may not be there yet; `get_machine_status` shows the last sync.
