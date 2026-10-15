# TB-QoL

A collection of **independent, JSON-only quality-of-life and compatibility mods** for [Timberborn](https://store.steampowered.com/app/1062090/Timberborn/).

Each mod has its own top-level folder, manifest, assets, dependencies, documentation, and downloadable ZIP. **This repository is not a single combined mod**: install only the mods you want.

## Mods

| Mod | Version | Game | Purpose | Testing |
| --- | --- | --- | --- | --- |
| [Tunneling Menu Fix](./TunnelingMenuFix/) | 1.1.0 | Timberborn 1.1 | Moves tunnel tools from the Dynamite submenu into Tunneling | Static checks passed; in-game testing pending |

See each mod's README for its requirements and installation instructions.

## Install

1. Download the ZIP for an individual mod from a successful [GitHub Actions run](./actions/workflows/validate-mods.yml) (under **Artifacts**), or use the mod's source folder.
2. Extract **only that mod's folder** into Timberborn's local `Mods` directory. The folder must contain its own `manifest.json`.
3. Enable the mod and its dependencies in the game's mod manager and restart if prompted.

**Important:** If you already installed the earlier `TB_Tunneling_Menu_Fix` folder, remove it before installing the new `TunnelingMenuFix` folder; both contain the same mod ID.

## Repository layout

```text
TB-QoL/
├── TunnelingMenuFix/      # One complete, independently installable mod
│   ├── manifest.json
│   ├── README.md
│   └── ...                # Blueprint JSON and other mod files
├── Docs/                 # Adding and testing mods
├── Tools/                # Shared validation + ZIP packaging
├── .github/workflows/    # Per-mod CI validation and downloads
└── README.md             # Catalog of all mods
```

For new mods, add another **top-level PascalCase directory** beside `TunnelingMenuFix/`. Do not put unrelated mod files in another mod's directory.

## Validate and package locally

Requires only Python 3 (standard library):

```sh
python3 Tools/mods.py check
python3 Tools/mods.py package --output dist
```

`dist/` will contain one ZIP per mod, each with the correct top-level install folder. The same commands run in GitHub Actions. The checks validate manifests and JSON syntax; they **do not** replace in-game testing.

See [Adding a mod](./Docs/ADDING_MODS.md), [Testing](./Docs/TESTING.md), and [AI/contributor guidance](./AGENTS.md).

**Maintained by [tharbad08](https://github.com/tharbad08).**
