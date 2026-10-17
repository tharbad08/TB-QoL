# Repository instructions

This is a **multi-mod Timberborn repository**. Follow this file when making changes, including automated or AI-assisted contributions.

- Each mod lives in its own top-level PascalCase directory (for example, `TunnelingMenuFix/`). Never place unrelated mods under a single shared manifest.
- Preserve each mod's `manifest.json` ID, requirements, paths and load behavior unless the task explicitly changes them.
- Keep changes scoped to the requested mod. Do not alter other mods, their manifests, or third-party Workshop source just to make a patch work.
- This collection is intended for **JSON-only mods**. Do not introduce compiled binaries or runtime dependencies without explicit approval.
- Maintain clear requirements, installation, compatibility, and test status in each mod's own README.
- Validate JSON and package every mod with `python3 Tools/mods.py check` and `python3 Tools/mods.py package --output dist` before committing.
- If an external mod or game version is required, use explicit IDs and versions when verified. Never guess game APIs or mark untested gameplay as verified.
- When reorganizing, preserve mod IDs and explain any local folder rename that could cause duplicate installations.
- Only use **tharbad08** as maintainer/author identity in manifests, documentation and commit metadata. Do not include private names or identifying paths.
- For compatibility patches, **`RequiredMods` alone may NOT produce correct default load order**. This occurred for `DirtLeveeVanillaFix` (October 2026) and then both TB-QoL mods. Resolve actual target manifests, keep their IDs in `RequiredMods`, **mirror all their `OptionalMods` on the patch as optional** (excluding IDs already required), and include optional dependencies of every patched upstream mod. Optional targets must stay optional; avoid duplicates and circular self-dependencies. Do not offer manual sorting as the primary fix.
- For a nonmandatory integration (for example, Rainborn’s excavation flag), declare the upstream ID under **`OptionalMods`**, not `RequiredMods`; add it to the baseline’s `OptionalPatchMods` regression checks. Never turn an optional integration into a mandatory mod dependency.
- Update `Docs/load-order-baseline.json` with the verified upstream manifest IDs, versions, and optional dependencies, and maintain `Tools/check_load_order.py` coverage. Run `python3 Tools/check_load_order.py` during validation. This checks the dependency-mirroring pattern, but does not independently simulate Timberborn's runtime sorting.
- A patch is not proven working until tested in game. Be candid about what was checked.
- Upstream PRs must follow that upstream project's own contribution guidelines and coding style; these repository instructions do not override them.
