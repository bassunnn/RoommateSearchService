"""Модуль описания класса пользователя."""

from typing import Any, Dict


class User:
    """Класс, представляющий пользователя сервиса."""

    def __init__(
        self,
        user_id: int,
        name: str,
        age: int,
        budget: float,
        district: str,
        smoking: bool,
    ) -> None:
        self.id = user_id
        self.name = name
        self.age = age
        self.budget = float(budget)
        self.district = district
        self.smoking = smoking

    def calculate_compatibility(self, other: "User") -> int:
        """Вычисляет балл совместимости с другим пользователем (от 0 до 4)."""
        score = 0
        if self.district.lower() == other.district.lower():
            score += 1
        if self.smoking == other.smoking:
            score += 1
        if abs(self.age - other.age) <= 5:
            score += 1
        if self.budget >= other.budget * 0.8:
            score += 1
        return score

    def to_dict(self) -> Dict[str, Any]:
        """Преобразует объект в словарь для сохранения в JSON."""
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "budget": self.budget,
            "district": self.district,
            "smoking": self.smoking,
        }

    @classmethod
    def from_data(cls, data: Dict[str, Any]) -> "User":
        """Создает объект User из словаря данных."""
        return cls(
            user_id=data["id"],
            name=data["name"],
            age=data["age"],
            budget=data["budget"],
            district=data["district"],
            smoking=data["smoking"],
        )

    def __str__(self) -> str:
        smoke = "Курит" if self.smoking else "Не курит"
        return (
            f"[{self.id}] {self.name}, {self.age} лет | "
            f"Бюджет: {self.budget} руб. | Район: {self.district} | {smoke}"
        )