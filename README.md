# Gaggiuino Dial-In

Espresso dial-in assistant for Claude Code — built for Gaggia Classic Pro + Gaggiuino + Baratza Sette 270Wi.

## What is this?

A [Claude Code skill](https://docs.anthropic.com/en/docs/claude-code) that helps you dial in espresso shots. Describe your coffee, a problem you're having, or attach a shot photo, and the skill recommends grind adjustments, profile changes, temperature tweaks, and more — all specific to this setup.

## Supported Setup

| Component | Model |
|-----------|-------|
| **Machine** | Gaggia Classic Pro |
| **Mod** | [Gaggiuino](https://gaggiuino.github.io/) (pressure/flow profiling, PID, Brew Delta) |
| **Grinder** | Baratza Sette 270Wi (macro/micro adjustment) |
| **Basket** | Stock double basket, 58mm (~14–18g) |

## Supported Profiles

| Profile | Style | Best for |
|---------|-------|----------|
| **IUIUIU Classic** | Flow → soak → pressure | All-rounder, great starting point |
| **LMD 9-8 v1.5** | Lever-inspired | Medium-dark roasts, body-forward |
| **Londinium** | Long preinfusion, lever decline | Traditional espresso, chocolate/nut notes |
| **Adaptive** | Auto-adjusting | Varying coffees without manual tuning |
| **Blooming Espresso** | Long bloom/soak | Light roasts, fruit-forward |
| **Filter 2.1** | Low pressure, long extraction | Filter-style clarity in espresso form |
| **Leva 9 v0.9** (community) | Spring-lever emulation, decline by water pumped | Medium to medium-dark, body, milk drinks |
| **Adaptive Dark Roast v2** (community) | Flow-driven, descending pressure, 90 °C | Medium-dark to dark, sweet and gentle |

## Installation

### Claude Code (CLI)

Copy the `skill/` directory into your Claude Code skills location:

```bash
# Clone the repo
git clone https://github.com/zirbio/gaggiuino-dial-in.git

# Copy the skill to your project or global skills
cp -r gaggiuino-dial-in/skill/ ~/.claude/skills/dial-in/
```

Then use it with:

```
/dial-in my coffee is a light roast Ethiopian natural, what profile and settings should I use?
```

### Optional: read shots from GLP

[GLP (Gaggiuino Local Profiler)](https://github.com/mxkissnr/gaggiuino-local-profiler) syncs every shot from the machine and stores your beans and tasting notes locally. Its built-in MCP server lets the skill read your shots directly, so you can just ask it to analyze your last shot.

1. Run GLP (Home Assistant app or standalone Docker) and add your machine under **Settings → Machines**.
2. Turn on **Settings → AI assistants (MCP)**. Leave the write tools off; the skill only reads.
3. Register the server in Claude Code under the name `glp`, keeping the token out of the config file with a headers helper that prints `{"X-GLP-Token":"<token>"}`:

   ```bash
   claude mcp add-json --scope user glp '{"type":"http","url":"http://127.0.0.1:8099/api/mcp","headersHelper":"/path/to/glp-mcp-headers"}'
   ```

The skill uses GLP when its tools are available and falls back to descriptions and photos otherwise. See `skill/glp-shot-data.md`.

### Grok (grok.com)

The `grok/` directory sets Grok up with the same rules as the skill, connected to GLP and to the Gaggiuino (read-only) through the bridge in `tools/glp-grok-bridge/`. See `grok/README.md`.

### Claude iOS App (via Projects)

The `ios/` directory contains a consolidated knowledge base file ready to paste into a Claude Project as context. See `ios/dial-in-project-context.md`.

## Usage Examples

**Get a recommendation for a new coffee:**
```
/dial-in I have a medium-light washed Colombian. What profile and grind should I start with?
```

**Troubleshoot a bad shot:**
```
/dial-in Using IUIUIU Classic, 18g in, 36g out in 28s but it tastes sour and thin. Grind at 9D.
```

**Analyze a shot photo:**
```
/dial-in [attach photo] What do you see in this shot? Using Londinium profile.
```

**Analyze your latest shot from GLP:**
```
/dial-in Analyze my last shot
```

**Learn about profiles:**
```
/dial-in What's the difference between IUIUIU Classic and Blooming Espresso?
```

## Repository Structure

```
.
├── skill/                  # Claude Code skill files
│   ├── SKILL.md            # Skill entry point
│   ├── coffee-fundamentals.md
│   ├── grinder-baratza-sette-270wi.md
│   ├── troubleshooting.md
│   ├── shot-analysis.md
│   ├── glp-shot-data.md    # Reading shots from GLP via MCP
│   └── profiles/           # Per-profile knowledge
│       ├── iuiuiu-classic.md
│       ├── lmd-9-8-v1.5.md
│       ├── londinium.md
│       ├── adaptive.md
│       ├── blooming-espresso.md
│       ├── filter-2.1.md
│       ├── leva-9.md
│       └── adaptive-dark-roast-v2.md
├── ios/                    # Claude iOS app context
│   └── dial-in-project-context.md
├── grok/                   # Grok instructions and setup
├── tools/glp-grok-bridge/  # MCP bridge for Grok (assign coffee, read machine profiles)
├── data/
│   ├── raw/                # Anonymized Discord community data
│   └── research/           # Processed research notes
│       ├── discord-community-notes.md
│       ├── gaggiuino-website-profiles.md
│       └── profiles/       # Per-profile research (md + json)
└── docs/                   # Design specs and plans
```

## Contributing

This is a personal project, but contributions are welcome:

- **Found an error?** Open an issue describing what's wrong
- **Have a profile to add?** Open an issue or PR with the profile details
- **Grinder-specific tips?** If you use a different grinder with Gaggiuino, PRs welcome for additional grinder knowledge files

## Data Sources

The knowledge base was built from:
- [Gaggiuino documentation](https://gaggiuino.github.io/)
- Community discussions (anonymized)
- Personal testing and experimentation
