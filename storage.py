"""Модуль преобразования данных JSON в объекты и обратно."""

import json
import os
from typing import List, Optional
from models import Ad, MatchRequest, User


def load_users(filepath: str) -> List[User]:
    """Загружает список пользователей в виде объектов User."""
    if not os.path.exists(filepath):
        return []
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)
            return [User.from_data(item) for item in data]
    except (json.JSONDecodeError, OSError, KeyError):
        return []


def save_users(filepath: str, users: List[User]) -> None:
    """Сохраняет список объектов User в JSON."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(
            [u.to_dict() for u in users], file, ensure_ascii=False, indent=2
        )


def load_ads(filepath: str) -> List[Ad]:
    """Загружает список объявлений в виде объектов Ad."""
    if not os.path.exists(filepath):
        return []
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)
            return [Ad.from_data(item) for item in data]
    except (json.JSONDecodeError, OSError, KeyError):
        return []


def save_ads(filepath: str, ads: List[Ad]) -> None:
    """Сохраняет список объектов Ad в JSON."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(
            [a.to_dict() for a in ads], file, ensure_ascii=False, indent=2
        )


def find_user_by_id(users: List[User], user_id: int) -> Optional[User]:
    """Вспомогательный поиск пользователя по ID."""
    for u in users:
        if u.id == user_id:
            return u
    return None


def find_ad_by_id(ads: List[Ad], ad_id: int) -> Optional[Ad]:
    """Вспомогательный поиск объявления по ID."""
    for a in ads:
        if a.id == ad_id:
            return a
    return None


def load_matches(
    filepath: str, users: List[User], ads: List[Ad]
) -> List[MatchRequest]:
    """Загружает заявки, связывая их с реальными объектами User и Ad."""
    if not os.path.exists(filepath):
        return []
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            raw_data = json.load(file)
            matches = []
            for item in raw_data:
                user = find_user_by_id(users, item.get("user_id", 0))
                ad = find_ad_by_id(ads, item.get("ad_id", 0))
                if user and ad:
                    match_obj = MatchRequest(
                        match_id=item["id"],
                        user=user,
                        ad=ad,
                        created_date=item["created_date"],
                        is_cancelled=item.get("is_cancelled", False),
                    )
                    matches.append(match_obj)
            return matches
    except (json.JSONDecodeError, OSError, KeyError):
        return []


def save_matches(filepath: str, matches: List[MatchRequest]) -> None:
    """Сохраняет заявки в JSON."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(
            [m.to_dict() for m in matches], file, ensure_ascii=False, indent=2
        )