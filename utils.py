"""Модуль безопасного ввода данных от пользователя."""

from typing import Optional


def input_float(prompt: str, default: Optional[float] = None) -> float:
    """Запрашивает число с плавающей точкой, обрабатывая ошибки ввода."""
    while True:
        val = input(prompt).strip()
        if not val and default is not None:
            return default
        try:
            return float(val)
        except ValueError:
            print("Ошибка: введите корректное число.")


def input_int(prompt: str, default: Optional[int] = None) -> int:
    """Запрашивает целое число, обрабатывая ошибки ввода."""
    while True:
        val = input(prompt).strip()
        if not val and default is not None:
            return default
        try:
            return int(val)
        except ValueError:
            print("Ошибка: введите целое число.")


def input_bool(prompt: str, default: bool = False) -> bool:
    """Запрашивает логическое значение (да/нет)."""
    val = input(prompt).strip().lower()
    if not val:
        return default
    return val in ["да", "yes", "y", "true", "1"]