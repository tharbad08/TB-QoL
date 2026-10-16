#!/usr/bin/env python3
"""Check that compatibility patches mirror upstream OptionalMods.

This verifies the pinned manifests in Docs/load-order-baseline.json. It cannot
guarantee the ordering of a user's manually reordered Timberborn mod list.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    baseline = json.loads((ROOT / "Docs/load-order-baseline.json").read_text(encoding="utf-8"))
    errors = []
    for folder, spec in baseline["Patches"].items():
        manifest = json.loads((ROOT / folder / "manifest.json").read_text(encoding="utf-8"))
        required = [v["Id"] for v in manifest.get("RequiredMods", [])]
        optional = [v["Id"] for v in manifest.get("OptionalMods", [])]
        declared = set(required)
        expected_required = set(spec["RequiredMods"])
        if not expected_required.issubset(declared):
            errors.append(f"{folder}: missing RequiredMods: {sorted(expected_required - declared)}")
        all_optional = set()
        for upstream in spec["MirrorOptionalModsOf"]:
            if upstream not in declared:
                errors.append(f"{folder}: upstream mod not required: {upstream}")
            all_optional.update(baseline["UpstreamMods"][upstream]["OptionalMods"])
        expected_optional = all_optional - declared - {manifest["Id"]}
        actual_optional = set(optional)
        if len(optional) != len(actual_optional):
            errors.append(f"{folder}: duplicate OptionalMods IDs")
        if declared & actual_optional:
            errors.append(f"{folder}: optional mods also required: {sorted(declared & actual_optional)}")
        if manifest["Id"] in actual_optional:
            errors.append(f"{folder}: self-dependency")
        if missing := expected_optional - actual_optional:
            errors.append(f"{folder}: missing mirrored OptionalMods: {sorted(missing)}")
        print(f"{folder}: {len(required)} required, {len(optional)} optional, "
              f"{len(expected_optional)} expected mirrored optional")
    for error in errors:
        print(f"ERROR {error}", file=sys.stderr)
    if errors:
        return 1
    print("Load-order manifest mirrors match upstream snapshots.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
