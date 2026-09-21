"""Тестирование класса Ad."""

from models import Ad


def test_ad_creation_and_str():
    ad = Ad(1, "центр", 12000.0, "Комната")
    assert ad.price == 12000.0
    assert "центр" in str(ad)


def test_ad_affordability():
    ad = Ad(1, "центр", 15000.0, "Комната")
    assert ad.is_affordable(16000.0) is True
    assert ad.is_affordable(10000.0) is False