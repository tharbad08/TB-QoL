# Tunneling Menu Fix (Timberborn 1.1)

Author: **tharbad08**

## What this does

Moves the tunnel / underground-construction icons listed by **More Groups** in
**Landscaping → Dynamite** into the **Tunneling** menu provided by **More Tunnels**
(the group used by More Mines). The fix covers all faction variants of those
tools; only tools available to your active faction appear in game.

* Removes those specific template names from More Groups' `SubGroup_MGDynamite` list.
* Registers them as children of `Tunneling` with their existing explicit ordering
  where supplied by More Groups.
* Prevents a second copy under the default `PlaceableBlockObjectSpec.ToolGroupId`
  for the moved entries. Does not modify dynamite tools, buildings, research,
  recipes, science costs or construction cost.

The changes target **52 template names** across supported factions and other optional
mod variants. They are not 52 visible icons: many names represent alternative
factions or other mods that may not be installed.

## Requirements

- Timberborn 1.1.0.2 or later in the 1.1 series
- Moddable Tool Groups (ID `ModdableToolGroups`, 11.0.0+)
- More Tunnels (ID `MoreTunnels`, 1.5+)
- More Groups (ID `KnatteAnka.MoreGroups`, 1.1.0.2+)
- More Mines (ID `TonWolfe.MoreMines`, 1.1.20+)

**More Organized Tool Groups** (Workshop ID `3612247861`) is not required.

## Install

Extract the `TB_Tunneling_Menu_Fix/` folder into Timberborn's local `Mods`
directory, preserving the folder structure. Do not extract this folder into
any Workshop mod's install folder. Keep existing Workshop mods enabled.

Restart Timberborn, enable `Tunneling Menu Fix` in the game's mod manager,
restart if prompted, and check both menus on a loaded save.

## Expected results

- Landscaping → Dynamite retains explosives and Explosives Factory tools.
- Tunneling contains the pictured tunnel-construction tools alongside other
  More Mines / More Tunnels tools for your faction.
- Only one entry per moved tool is shown; padlocked tools retain the same unlocks.

## Technical files

`ToolGroups/BlockObjectToolGroup.SubGroup_MGDynamite.blueprint.json` uses
`ChildrenToolsTemplateNames#remove`.

`BlockObjectToolGroups/BlockObjectToolGroup.Tunneling.blueprint.json` uses
`ChildrenToolsTemplateNames#append`, `ChildrenExplicitOrderedIds#append`, and
`DoNotIncludePlaceableToolGroup: true` so the group parent is not added twice
for tools whose native ToolGroupId already equals `Tunneling`.

This is a **data-only patch** and contains no DLL.

## Verification

Patch syntax and names were statically checked against the exact Timberborn 1.1
blueprints supplied by the user. **In-game behavior still requires testing.**
