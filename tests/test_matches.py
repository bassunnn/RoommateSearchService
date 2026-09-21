"""Тестирование связывания объектов в MatchRequest."""

from models import Ad, MatchRequest, User


def test_match_request_linking_and_cancel():
    user = User(1, "Алексей", 22, 16000.0, "центр", False)
    ad = Ad(1, "центр", 15000.0, "Комната")
    match = MatchRequest(1, user, ad, "2026-10-01")

    assert match.user.name == "Алексей"
    assert match.ad.price == 15000.0
    assert match.is_cancelled is False

    match.cancel()
    assert match.is_cancelled is True