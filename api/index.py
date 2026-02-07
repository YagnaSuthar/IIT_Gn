from __future__ import annotations

import os
import sys

from fastapi import FastAPI
from mangum import Mangum


def _load_backend_app() -> FastAPI:
    """Import the existing FastAPI app from the current backend package.

    This repo already has a backend implementation under ./backend.
    Vercel requires the serverless entrypoint to live under ./api.

    We add ./backend to sys.path so imports like `farmxpert...` resolve.
    """

    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    backend_dir = os.path.join(repo_root, "backend")
    if backend_dir not in sys.path:
        sys.path.insert(0, backend_dir)

    # Prefer the newer/cleaner interfaces API app if present
    try:
        from interfaces.api.main import app as imported_app  # type: ignore
        return imported_app
    except Exception:
        from app.main import app as imported_app  # type: ignore
        return imported_app


app = _load_backend_app()


async def _health() -> dict:
    return {"status": "ok"}


# Ensure a stable health route regardless of whether Vercel forwards the `/api` prefix.
app.add_api_route("/health", _health, methods=["GET"], tags=["health"])
app.add_api_route("/api/health", _health, methods=["GET"], tags=["health"])

handler = Mangum(app)
