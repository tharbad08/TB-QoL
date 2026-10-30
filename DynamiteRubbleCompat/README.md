# Dynamite Rubble Compatibility — 1.1.1

Runtime compatibility add-on for Timberborn 1.1. The original Workshop Dynamite Rubble 1.0.0 patches vanilla `Dynamite.Detonate` and `Timberborn.Explosions.Tunnel.Explode`; More Mines and More Tunnels have distinct explosion implementations that bypass those hooks.

This mod patches `TonWolfe.DeepMines.TWTunnel.Explode` (More Mines) and `Opolame.MoreTunnels.Scripts.ImprovedTunnel.Explode` (More Tunnels). Before and after each completed explosion, it checks the *actual terrain voxel* through `ITerrainService.Underground`. Only a removed voxel triggers the existing `DynamiteRubbleService.SpawnDirt(coordinates, 1)`, preserving **3 Dirt for one destroyed terrain block**. A tunnel that does not destroy terrain produces no Dirt. The original ore and recovered-goods processing is untouched.

## Requirements / versions

- Timberborn 1.1, minimum game version 1.1.0.2.
- Dynamite Rubble 1.0.0 (Workshop 3677595367).
- More Mines 1.1.20 (Workshop 3723216060).
- More Tunnels 1.5 (Workshop 3471578532).
- Harmony and More Mines' own required dependencies.

The manifest lists all three patch targets under `RequiredMods`, and mirrors their optional dependencies to enforce the established load-order rule. This is an **add-on**: keep the original mods installed. Do not replace their DLLs.

## Installation

Use only the **compiled** artifact from the [Build Dynamite Rubble Compatibility](../.github/workflows/build-dynamite-rubble-compat.yml) workflow. Extract its single `DynamiteRubbleCompat/` directory into your local Mods directory; its install layout is `DynamiteRubbleCompat/version-1.1/manifest.json` and `DynamiteRubbleCompat/version-1.1/Scripts/DynamiteRubbleCompat.dll`. Do not copy game, Harmony or upstream mod DLLs into the patch.

## Code and safety

- Minimal Harmony attribute-based patch; no transpilers, no manual `System.Reflection`, no replacements or skips of upstream `Explode` work.
- The only private-member access is the normal Harmony field-parameter injection for the verified private `_terrainService` and `_blockObject` fields. There is no public API exposing these fields directly.
- The patch does **not** globally reward all terrain changes. Other explosion mods need their distinct methods verified before additional hooks.
- Mod author: **tharbad08**.

## Verification (2026-10-30)

Inspected the supplied Dynamite Rubble 1.0.0 DLL and the pinned game / More Mines 1.1.20 / More Tunnels 1.5 DLLs. Verified target methods, public Dirt-spawning method, private fields, and native voxel query. **Compilation and in-game behavior are not yet verified.**

Test in a disposable game/save: ordinary dynamite, vanilla tunnel, More Mines stacked and non-stacked tunnels, More Tunnels tunnel, explosions in empty cells, and ore destruction. Verify exactly 3 Dirt per removed block, no duplicate drops, and no new `Player.log` exceptions on both factions.
