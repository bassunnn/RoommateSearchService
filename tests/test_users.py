"""Тестирование класса User."""

from models import User


def test_user_creation():
    user = User(1, "Иван", 20, 15000.0, "центр", False)
    assert user.id == 1
    assert user.name == "Иван"
    assert user.budget == 15000.0


def test_user_compatibility():
    u1 = User(1, "Алексей", 22, 16000.0, "центр", False)
    u2 = User(2, "Дмитрий", 24, 15000.0, "центр", False)
    assert u1.calculate_compatibility(u2) == 4