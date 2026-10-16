# Tunneling Menu Fix

**Timberborn 1.1 · v1.1.0 · data-only compatibility mod**

Moves tunnel and underground-construction tools from **Landscaping → Dynamite** (More Groups) to the **Tunneling** group provided by More Tunnels and used by More Mines.

The mod contains only blueprint JSON. It does not modify construction costs, unlocks, recipes, science requirements, or building behavior.

## Dependencies

- Timberborn 1.1.0.2 or later in the 1.1 series
- Moddable Tool Groups (`ModdableToolGroups`, 11.0.0+)
- More Tunnels (`MoreTunnels`, 1.5+)
- More Groups (`KnatteAnka.MoreGroups`, 1.1.0.2+)
- More Mines (`TonWolfe.MoreMines`, 1.1.20+)

More Organized Tool Groups (Workshop ID `3612247861`) is **not** required.

## Install

Install the required Workshop mods first and enable them. Copy the entire `TunnelingMenuFix` directory into your local Timberborn `Mods` folder (or extract its individually packaged ZIP there), keeping the `manifest.json` directly inside `TunnelingMenuFix`.

**Upgrading from v1.1.0's original ZIP:** Remove the old local `TB_Tunneling_Menu_Fix` folder before installing the renamed `TunnelingMenuFix` folder, so that the same mod is not installed twice.

Restart the game and enable **Tunneling Menu Fix** in the mod manager. Select **Reset load order**, then check the visible order (higher entries load first): **Moddable Tool Groups**, **More Tunnels**, **More Groups**, and **More Mines** must each appear *above* **Tunneling Menu Fix**. Their ordering relative to one another is determined by their own dependency graph. If you keep a custom mod order, move this patch below all four of those mods manually.

The `RequiredMods` manifest fields tell Timberborn which mods are prerequisites; they do not automatically overwrite an already saved custom mod order. Verify the order in-game before judging the menu patch.

## Expected result

- Landscaping → Dynamite retains its explosive-related tools.
- Tunneling contains the six types of tunnel-related tools shown in the original report, including available faction and mod variants.
- Locked tools keep their existing research requirements; no duplicate icons should remain.

## How the patch works

- `ToolGroups/BlockObjectToolGroup.SubGroup_MGDynamite.blueprint.json` removes the named templates from the Dynamite group.
- `BlockObjectToolGroups/BlockObjectToolGroup.Tunneling.blueprint.json` adds those names to the Tunneling group and preserves specified orders.
- [TARGETED_TEMPLATES.md](./TARGETED_TEMPLATES.md) lists all **52 targeted template IDs**. Those represent multiple faction/mod variants, not 52 simultaneously visible buttons.

## Testing status

The JSON and target IDs were statically checked against the supplied Timberborn 1.1 assets. **In-game placement, load order, and duplicate-icon behavior have not yet been verified.**

Maintainer: **tharbad08**.
