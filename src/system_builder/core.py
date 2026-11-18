"""Safe deterministic JSON-intent to file-plan builder."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path, PurePosixPath
from typing import Any


def _safe_relative_path(value: str) -> PurePosixPath:
    if not isinstance(value, str) or not value.strip():
        raise ValueError("file path must be a non-empty string")
    path = PurePosixPath(value)
    if path.is_absolute() or any(part in ("", ".", "..") for part in path.parts):
        raise ValueError(f"unsafe relative path: {value!r}")
    if "\\" in value or ":" in path.parts[0]:
        raise ValueError(f"unsafe relative path: {value!r}")
    return path


def load_intent(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("intent root must be a JSON object")
    if data.get("version") != 1:
        raise ValueError("intent version must be 1")
    files = data.get("files")
    if not isinstance(files, list) or not files:
        raise ValueError("intent must contain a non-empty files list")
    seen: set[str] = set()
    for item in files:
        if not isinstance(item, dict) or not isinstance(item.get("path"), str) or not isinstance(item.get("content"), str):
            raise ValueError("each file requires string path and content")
        safe = _safe_relative_path(item["path"]).as_posix()
        if safe in seen or safe == "manifest.json":
            raise ValueError(f"duplicate or reserved output path: {safe}")
        seen.add(safe)
    return data


def build_plan(intent: dict[str, Any]) -> list[dict[str, str]]:
    if not isinstance(intent, dict) or intent.get("version") != 1:
        raise ValueError("intent version must be 1")
    if not isinstance(intent.get("files"), list) or not intent["files"]:
        raise ValueError("intent must contain a non-empty files list")
    plan = [{"path": _safe_relative_path(item["path"]).as_posix(), "content": item["content"]}
            for item in intent["files"]]
    return sorted(plan, key=lambda item: item["path"])


def generate(intent: dict[str, Any], output_dir: Path) -> dict[str, Any]:
    root = output_dir.resolve()
    plan = build_plan(intent)
    manifest_files = []
    for item in plan:
        target = (root / item["path"]).resolve()
        if not target.is_relative_to(root):
            raise ValueError(f"output escapes destination: {item['path']}")
        if target.exists():
            raise FileExistsError(f"refusing to overwrite: {item['path']}")
        manifest_files.append({"path": item["path"], "sha256": hashlib.sha256(item["content"].encode("utf-8")).hexdigest()})
    manifest_path = root / "manifest.json"
    if manifest_path.exists():
        raise FileExistsError("refusing to overwrite manifest.json")
    # Validate every target before writing any output.
    for item in plan:
        target = root / item["path"]
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(item["content"], encoding="utf-8")
    manifest = {"version": 1, "files": manifest_files}
    root.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\\n", encoding="utf-8")
    return manifest
