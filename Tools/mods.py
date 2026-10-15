#!/usr/bin/env python3
"""Validate and package independently installable, data-only Timberborn mods."""
from __future__ import annotations

import argparse
import json
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OMIT_NAMES = {".DS_Store", "Thumbs.db"}
OMIT_DIRS = {"__pycache__", ".git", ".github"}
BANNED_SUFFIXES = {".dll", ".pdb", ".sav", ".zip", ".7z"}


def discover_mods() -> list[Path]:
    """A mod is a direct child of the repository root with a manifest.json."""
    return sorted(
        (p for p in ROOT.iterdir()
         if p.is_dir() and not p.name.startswith(".")
         and (p / "manifest.json").is_file()),
        key=lambda p: p.name.casefold(),
    )


def load_json(path: Path) -> object:
    # Catch accidental duplicate JSON keys as well as syntax errors.
    def unique_pairs(items: list[tuple[str, object]]) -> dict[str, object]:
        result: dict[str, object] = {}
        for key, value in items:
            if key in result:
                raise ValueError(f"duplicate JSON key: {key}")
            result[key] = value
        return result

    return json.loads(path.read_text(encoding="utf-8-sig"),
                      object_pairs_hook=unique_pairs)


def included_files(mod: Path) -> list[Path]:
    files: list[Path] = []
    for path in sorted(mod.rglob("*")):
        parts = path.relative_to(mod).parts
        if any(part in OMIT_DIRS or part.startswith(".") for part in parts):
            continue
        if path.is_symlink():
            raise ValueError(f"symlink not allowed: {path.relative_to(ROOT)}")
        if not path.is_file() or path.name in OMIT_NAMES:
            continue
        if path.suffix.lower() in BANNED_SUFFIXES:
            raise ValueError(f"binary/archive or save file in mod: {path.relative_to(ROOT)}")
        files.append(path)
    return files


def validate(mods: list[Path]) -> int:
    if not mods:
        print("ERROR: no top-level mod directories containing manifest.json", file=sys.stderr)
        return 1

    problems: list[str] = []
    seen_ids: dict[str, str] = {}
    for mod in mods:
        try:
            files = included_files(mod)
            for path in files:
                if path.suffix.lower() == ".json":
                    load_json(path)
            manifest = load_json(mod / "manifest.json")
            if not isinstance(manifest, dict):
                raise ValueError("manifest.json must contain a JSON object")
            for key in ("Id", "Name", "Version"):
                if not isinstance(manifest.get(key), str) or not manifest[key].strip():
                    raise ValueError(f"manifest.json missing non-empty {key}")
            identity = manifest["Id"].casefold()
            if identity in seen_ids:
                raise ValueError(f"duplicate mod ID {manifest['Id']} (also in {seen_ids[identity]})")
            seen_ids[identity] = mod.name
            if not (mod / "README.md").is_file():
                raise ValueError("missing per-mod README.md")
            print(f"OK  {mod.name}  {manifest['Version']}  ({len(files)} files)")
        except (ValueError, OSError, UnicodeError, json.JSONDecodeError) as ex:
            problems.append(f"{mod.name}: {ex}")

    for problem in problems:
        print(f"ERROR: {problem}", file=sys.stderr)
    return 1 if problems else 0


def package(mods: list[Path], output: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)
    for mod in mods:
        path = output / f"{mod.name}.zip"
        with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as archive:
            for file in included_files(mod):
                archive.write(file, arcname=f"{mod.name}/{file.relative_to(mod).as_posix()}")
        print(f"ZIP {path.relative_to(ROOT) if path.is_relative_to(ROOT) else path}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("check", "package"))
    parser.add_argument("--output", default="dist",
                        help="Directory for independently installable ZIPs")
    args = parser.parse_args()
    mods = discover_mods()
    if validate(mods):
        return 1
    if args.command == "package":
        package(mods, Path(args.output).resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
