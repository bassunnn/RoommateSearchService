"""Модуль описания класса объявления о жилье."""

from typing import Any, Dict


class Ad:
    """Класс, представляющий объявление о совместной аренде."""

    def __init__(
        self,
        ad_id: int,
        district: str,
        price: float,
        description: str,
    ) -> None:
        self.id = ad_id
        self.district = district
        self.price = float(price)
        self.description = description

    def is_affordable(self, budget: float) -> bool:
        """Проверяет, доступна ли цена для указанного бюджета."""
        return budget >= self.price

    def to_dict(self) -> Dict[str, Any]:
        """Преобразует объект в словарь для сохранения в JSON."""
        return {
            "id": self.id,
            "district": self.district,
            "price": self.price,
            "description": self.description,
        }

    @classmethod
    def from_data(cls, data: Dict[str, Any]) -> "Ad":
        """Создает объект Ad из словаря данных."""
        return cls(
            ad_id=data["id"],
            district=data["district"],
            price=data["price"],
            description=data["description"],
        )

    def __str__(self) -> str:
        return (
            f"[{self.id}] Район: {self.district} | "
            f"Цена: {self.price} руб. | {self.description}"
        )