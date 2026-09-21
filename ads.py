"""Модуль обработки и фильтрации объявлений о жилье."""

from typing import Any, Dict, List, Optional


def filter_ads(
    ads: List[Dict[str, Any]],
    max_price: float,
    district: Optional[str] = None
) -> List[Dict[str, Any]]:
    """Фильтрует объявления по бюджету и опционально по району."""
    res = [ad for ad in ads if float(ad.get("price", 0)) <= max_price]
    if district:
        res = [
            ad for ad in res
            if ad.get("district", "").lower() == district.lower()
        ]
    return res


def sort_ads_by_price(
    ads: List[Dict[str, Any]], reverse: bool = False
) -> List[Dict[str, Any]]:
    """Сортирует объявления по цене с использованием lambda-функции."""
    return sorted(
        ads, key=lambda item: float(item.get("price", 0)), reverse=reverse
    )


def add_ad(
    ads: List[Dict[str, Any]], district: str, price: float, description: str
) -> Dict[str, Any]:
    """Добавляет новое объявление в коллекцию."""
    new_id = max([item.get("id", 0) for item in ads], default=0) + 1
    new_ad = {
        "id": new_id,
        "district": district.strip(),
        "price": float(price),
        "description": description.strip(),
    }
    ads.append(new_ad)
    return new_ad