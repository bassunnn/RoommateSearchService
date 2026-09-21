"""Модуль для сохранения и загрузки данных в формате JSON."""

import json
import os
from typing import Any, List


def load_json(filepath: str) -> List[dict[str, Any]]:
    """Загружает список словарей из файла JSON с обработкой ошибок."""
    if not os.path.exists(filepath):
        return []
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_json(filepath: str, data: List[dict[str, Any]]) -> bool:
    """Сохраняет данные в файл JSON."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
        return True
    except OSError:
        return False