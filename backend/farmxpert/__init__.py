from __future__ import annotations

import sys
import types
from pathlib import Path


def _ensure_pkg(name: str, path: Path) -> None:
    mod = sys.modules.get(name)
    if mod is None:
        mod = types.ModuleType(name)
        sys.modules[name] = mod
    mod.__path__ = [str(path)]


_base = Path(__file__).resolve().parent.parent

_ensure_pkg(__name__, Path(__file__).resolve().parent)

for _pkg in [
    "app",
    "interfaces",
    "config",
    "models",
    "core",
    "services",
    "agents",
    "repositories",
    "tools",
    "memory_system",
    "scripts",
]:
    _path = _base / _pkg
    if _path.exists() and _path.is_dir():
        _ensure_pkg(f"{__name__}.{_pkg}", _path)
