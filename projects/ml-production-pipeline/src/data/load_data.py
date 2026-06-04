"""Basic data loading utilities for Week 1 scaffolding.

The first version intentionally supports only simple local files. Later weeks can
extend this module with database ingestion, validation, and pipeline orchestration.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

from src.utils.logger import get_logger


logger = get_logger(__name__)


def load_csv(path: str | Path) -> list[dict[str, str]]:
    """Load a CSV file into a list of row dictionaries."""
    file_path = Path(path)
    _ensure_file_exists(file_path)

    logger.info("Loading CSV data from %s", file_path)
    with file_path.open("r", encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def load_json(path: str | Path) -> Any:
    """Load a JSON file and return the decoded object."""
    file_path = Path(path)
    _ensure_file_exists(file_path)

    logger.info("Loading JSON data from %s", file_path)
    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def _ensure_file_exists(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError(f"Data file not found: {path}")

    if not path.is_file():
        raise ValueError(f"Expected a file path, got: {path}")
