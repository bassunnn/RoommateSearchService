"""Модуль расчета совместимости сожителей."""

from typing import Any, Dict, List


def calculate_match_score(user: Dict[str, Any], cand: Dict[str, Any]) -> int:
    """Вычисляет балл совместимости между двумя анкетами (от 0 до 4)."""
    score = 0
    # Проверка района
    if user.get("district", "").lower() == cand.get("district", "").lower():
        score += 1
    # Проверка привычки курения
    if user.get("smoking") == cand.get("smoking"):
        score += 1
    # Проверка возраста (разница не более 5 лет)
    if abs(int(user.get("age", 0)) - int(cand.get("age", 0))) <= 5:
        score += 1
    # Проверка совместимости бюджета
    user_b = float(user.get("budget", 0))
    cand_b = float(cand.get("budget", 0))
    if user_b >= cand_b * 0.8:
        score += 1

    return score


def get_top_candidates(
    user: Dict[str, Any], candidates: List[Dict[str, Any]], top_n: int = 3
) -> List[Dict[str, Any]]:
    """Возвращает топ-N наиболее подходящих кандидатов (lambda-сортировка)."""
    scored = [
        (cand, calculate_match_score(user, cand)) for cand in candidates
    ]
    # Сортировка по убыванию баллов
    scored.sort(key=lambda pair: pair[1], reverse=True)
    return [cand for cand, sc in scored[:top_n] if sc > 0]