"""Тестирование функций подбора кандидатов."""

from matching import calculate_match_score, get_top_candidates


def test_calculate_match_score_full():
    user = {"district": "центр", "smoking": False, "age": 22, "budget": 15000}
    cand = {"district": "центр", "smoking": False, "age": 23, "budget": 15000}
    score = calculate_match_score(user, cand)
    assert score == 4


def test_get_top_candidates():
    user = {"district": "центр", "smoking": False, "age": 22, "budget": 15000}
    candidates = [
        {"name": "A", "district": "север", "smoking": True, "age": 40, "budget": 50000},
        {"name": "B", "district": "центр", "smoking": False, "age": 23, "budget": 15000},
    ]
    top = get_top_candidates(user, candidates, top_n=1)
    assert len(top) == 1
    assert top[0]["name"] == "B"