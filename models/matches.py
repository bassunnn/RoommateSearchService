"""Модуль описания класса заявки на совместный съём (связь сущностей)."""

from typing import Any, Dict
from .users import User
from .ads import Ad


class MatchRequest:
    """Заявка, связывающая Пользователя и Объявление (Композиция)."""

    def __init__(
        self,
        match_id: int,
        user: User,
        ad: Ad,
        created_date: str,
        is_cancelled: bool = False,
    ) -> None:
        self.id = match_id
        self.user = user
        self.ad = ad
        self.created_date = created_date
        self.is_cancelled = is_cancelled

    def cancel(self) -> None:
        """Отменяет заявку без её удаления из коллекции."""
        self.is_cancelled = True

    def to_dict(self) -> Dict[str, Any]:
        """Сохраняет в JSON только внешние ключи (ID), а не сами объекты."""
        return {
            "id": self.id,
            "user_id": self.user.id,
            "ad_id": self.ad.id,
            "created_date": self.created_date,
            "is_cancelled": self.is_cancelled,
        }

    def __str__(self) -> str:
        status = "ОТМЕНЕНА" if self.is_cancelled else "АКТИВНА"
        return (
            f"Заявка #{self.id} от {self.created_date} [{status}]\n"
            f"  Кандидат: {self.user.name} (бюджет: {self.user.budget} руб.)\n"
            f"  Жилье: {self.ad.district}, {self.ad.price} руб."
        )