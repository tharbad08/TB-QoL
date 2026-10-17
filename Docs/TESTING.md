# Testing guidelines

## Automated checks

Run at the repository root:

```sh
python3 Tools/mods.py check
python3 Tools/check_load_order.py
python3 Tools/mods.py package --output dist
```

These check that each top-level mod has a readable manifest, that all JSON files parse, that IDs are not duplicated across mods, and that individual ZIP files can be generated with a single installable top-level directory.

## In-game checks

For each changed mod:

- Confirm the Timberborn build and required mod versions.
- Install the generated ZIP **without** keeping an older directory of the same mod ID.
- Check that each patch declares its target mods in `RequiredMods` **and mirrors all target `OptionalMods`**; use `python3 Tools/check_load_order.py` to catch missing mirrored dependencies against the pinned original-mod manifests. This is the same fix used for Dirt Levee Vanilla Fix.
- In the mod manager, verify each patch is **below every mod it patches**; entries above it load first. Reset/custom arrangement is a diagnostic fallback, not a substitute for manifest dependency fixes.
- Record actual observed load order rather than assuming the manifest's dependencies mean the correct order was used.
- Start a fresh game or a disposable copy of a save; verify startup and check `Player.log`.
- Test the intended changed behavior and look for duplicates, missing icons, unexpected unlocks, or broken menus.
- Repeat for every supported faction and optional-mod combination that matters.
- Update the mod README with actual test results. Distinguish between *not tested*, *static checks only*, and *tested in-game*.

For **Tunneling Menu Fix** specifically: check Landscaping → Dynamite and Tunneling, including the locked state of tools, while More Groups, More Tunnels, More Mines, and Moddable Tool Groups are enabled. With optional Rainborn enabled, verify that `ExcavationFlag.Folktails` and `ExcavationFlag.IronTeeth` appear only under Tunneling. Repeat with Rainborn disabled to ensure the menu patch still starts and works without it.

## Scope

Do not infer gameplay success from GitHub Actions passing: a syntactically valid blueprint patch can still behave incorrectly at runtime.
