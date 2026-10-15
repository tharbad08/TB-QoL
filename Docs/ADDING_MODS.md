# Adding a mod

Keep the structure similar to a multi-project Timberborn mod repository: **one directory per independent mod at the repository root**.

## Folder structure

```text
NewModName/
├── manifest.json           # Required
├── README.md               # Required
├── SomeBlueprints/         # Any paths expected by Timberborn
│   └── Example.blueprint.json
└── ...                     # Optional localization/other mod assets
```

Use PascalCase for the repository and installation directory (e.g. `NewModName`). Do not add an extra `Mods/` or `src/` wrapper inside it; ZIP packages always include one installable top-level folder.

## Checklist

1. Give the mod a unique and stable `manifest.json` `Id`, along with its `Name` and `Version`.
2. Put its own blueprint JSON and resources under that mod folder. Do not edit another mod to make it work.
3. Document the intended game version, required/optional Workshop mods, changes, installation steps, and testing status in `NewModName/README.md`.
4. Add a row to the root [mod catalog](../README.md).
5. Run `python3 Tools/mods.py check` and `python3 Tools/mods.py package --output dist`. Inspect the ZIP root.
6. Test in game and document the game version, faction, dependencies, and results. Static JSON validation alone does not prove compatibility.

No C# solution or single shared manifest is needed for data-only mods.

## Publishing

The shared [GitHub Actions workflow](../.github/workflows/validate-mods.yml) checks all mod directories and uploads a **separate ZIP for each mod** after successful validation. Find these ZIPs in the run's **Artifacts**. They are build artifacts, not an automatically published GitHub Release.

New folder names become ZIP root paths. If you rename a previously installed mod directory, document removing the old local directory to avoid loading two copies.

Do not put source archives, Steam downloads, user saves, logs, or game DLLs in this repository.
