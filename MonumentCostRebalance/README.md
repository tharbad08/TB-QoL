# Monument Cost Rebalance

A small, **JSON-only** Timberborn 1.1 compatibility mod (v1.0.1) by **tharbad08**.

Changes only More Mines' construction costs for the **Folktails Earth Recultivator** and **Iron Teeth Earth Repopulator**. The original vanilla monument definitions are not edited.

## New construction costs

| Resource | Folktails Earth Recultivator | Iron Teeth Earth Repopulator |
|---|---:|---:|
| Gears | 2,000 | 1,500 |
| Treated Planks | 2,000 | 2,000 |
| Metal Blocks | **1,500** (was 800) | **2,000** (was 1,300) |
| Metal Parts | 400 | 400 |
| Gold Nuggets | **0** (was 400) | **0** (was 400) |
| Silver Bars | **0** (was 400) | **0** (was 400) |
| **Total construction resources** | **5,900** | **5,900** |

All other requirements remain unchanged, including the 20,000 Science unlock costs, construction times, wonder activation materials, and the costs of other More Mines buildings and monuments.

## Requirements

- Timberborn 1.1.0.2 or later in the 1.1 series
- [More Mines](https://steamcommunity.com/sharedfiles/filedetails/?id=3723216060), mod ID `TonWolfe.MoreMines`, version 1.1.20 or later

The other required mods of More Mines are managed by More Mines itself.

## Installation

1. Ensure **More Mines** and its dependencies are installed and enabled.
2. Copy the **entire `MonumentCostRebalance` folder** into your local Timberborn `Mods` folder, or extract the released ZIP there. The folder must directly contain `manifest.json`.
3. Enable **Monument Cost Rebalance** in the game's mod manager, restart the game, and check both monuments' construction-cost tooltips.

Do not edit the More Mines Workshop directory. **Version 1.0.1 fixes dependency sorting** by retaining More Mines in `RequiredMods` and mirroring its optional dependencies (`TonWolfe.Market`, `KnatteAnka.MoreGroups` and `Redic.NewStyles`) in this mod's `OptionalMods`. These remain **optional**, not new installation requirements. Mirroring the parent dependencies avoids the same manifest-ordering issue previously fixed in Dirt Levee Vanilla Fix. Verify that **More Mines** appears above **Monument Cost Rebalance**. Manually rearranging a custom order should be a fallback, not the fix itself.

## Implementation

Patches the existing `TWBuildingCostModifierListSpec.CostModifiers` list supplied by More Mines on two blueprints:

- `Buildings/Monuments/EarthRecultivator/EarthRecultivator.Folktails.blueprint.json`
- `Buildings/Monuments/EarthRepopulator/EarthRepopulator.IronTeeth.blueprint.json`

The original `ModIds: ["TonWolfe.MoreMines"]` condition is preserved. Only the two cost lists change: `TWGoldNugget` and `TWSilverBar` are removed, and `MetalBlock` is increased by 700. The 400 `MetalPart` requirement is retained. `BuildingSpec` and all other components stay untouched.

## Validation

The patch JSON and exact changes were compared with the user's original-game and More Mines Timberborn 1.1 blueprints. **Not yet tested in game**; please check both faction monuments with More Mines enabled.
