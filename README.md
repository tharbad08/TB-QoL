# TB-QoL

A collection of **independent, JSON-only quality-of-life and compatibility mods** for [Timberborn](https://store.steampowered.com/app/1062090/Timberborn/).

Each mod has its own top-level folder, manifest, assets, dependencies, documentation, and downloadable ZIP. **This repository is not a single combined mod**: install only the mods you want.

## Mods

| Mod | Version | Game | Purpose | Testing |
| --- | --- | --- | --- | --- |
| [Tunneling Menu Fix](./TunnelingMenuFix/) | 1.1.2 | Timberborn 1.1 | Moves tunnel tools and optional Rainborn excavation flags into Tunneling | Static checks passed; in-game testing pending |
| [Monument Cost Rebalance](./MonumentCostRebalance/) | 1.0.1 | Timberborn 1.1 | Removes precious-metal costs from the two final wonders while keeping More Mines Metal Parts and restoring vanilla Metal Blocks | Static checks passed; in-game testing pending |

See each mod's README for its requirements and installation instructions.

## Install

1. Download the ZIP for an individual mod from a successful [GitHub Actions run](./actions/workflows/validate-mods.yml) (under **Artifacts**), or use the mod's source folder.
2. Extract **only that mod's folder** into Timberborn's local `Mods` directory. The folder must contain its own `manifest.json`.
3. Enable the mod and its prerequisites. The patch manifests declare their target mods in `RequiredMods` **and mirror the target mods' optional dependencies**, following the fix previously needed by Dirt Levee Vanilla Fix. The latter avoids a known dependency-ordering failure in Timberborn 1.1.
4. Restart the game and verify the patch applies. If a custom mod-manager order was already saved, verify the targets are above each patch; do not rely on a manual sort as the only fix.

**Important:** If you already installed the earlier `TB_Tunneling_Menu_Fix` folder, remove it before installing the new `TunnelingMenuFix` folder; both contain the same mod ID.

## Repository layout

```text
TB-QoL/
├── TunnelingMenuFix/      # Mod 1: tunnel tools menu patch
│   ├── manifest.json
│   ├── README.md
│   └── ...                # Blueprint JSON and other mod files
├── MonumentCostRebalance/ # Mod 2: endgame monument costs
│   ├── manifest.json
│   ├── README.md
│   └── ...                # Two monument blueprint overrides
├── Docs/                 # Adding and testing mods
├── Tools/                # Shared validation + ZIP packaging
├── .github/workflows/    # Per-mod CI validation and downloads
└── README.md             # Catalog of all mods
```

For new mods, add another **top-level PascalCase directory** beside `TunnelingMenuFix/` and `MonumentCostRebalance/`. Do not put unrelated mod files in another mod's directory.

## Validate and package locally

Requires only Python 3 (standard library):

```sh
python3 Tools/mods.py check
python3 Tools/check_load_order.py
python3 Tools/mods.py package --output dist
```

`dist/` will contain one ZIP per mod, each with the correct top-level install folder. The same commands run in GitHub Actions. The checks validate manifests and JSON syntax **and enforce upstream optional-dependency mirroring** against the [pinned 1.1 manifest baseline](./Docs/load-order-baseline.json). They **do not** replace in-game testing.

See [Adding a mod](./Docs/ADDING_MODS.md), [Testing](./Docs/TESTING.md), and [AI/contributor guidance](./AGENTS.md).

**Maintained by [tharbad08](https://github.com/tharbad08).**
