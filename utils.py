"""Модуль безопасного ввода данных."""

from typing import Optional


def input_int(prompt: str, default: Optional[int] = None) -> int:
    """Запрашивает целое число с обработкой ошибок."""
    while True:
        raw = input(prompt).strip()
        if not raw and default is not None:
            return default
        try:
            return int(raw)
        except ValueError:
            print("Ошибка: введите целое число.")


def input_float(prompt: str, default: Optional[float] = None) -> float:
    """Запрашивает вещественное число с обработкой ошибок."""
    while True:
        raw = input(prompt).strip()
        if not raw and default is not None:
            return default
        try:
            return float(raw)
        except ValueError:
            print("Ошибка: введите корректное число.")