"""Точка входа и интерактивный интерфейс приложения."""

import os
from typing import Any, Dict
from ads import add_ad, filter_ads, sort_ads_by_price
from matching import calculate_match_score, get_top_candidates
from storage import load_json, save_json
from utils import input_bool, input_float, input_int

ADS_FILE = os.path.join("data", "ads.json")
CANDIDATES_FILE = os.path.join("data", "candidates.json")


def show_ads_table(ads: list[Dict[str, Any]]) -> None:
    """Выводит список объявлений в читаемом формате."""
    if not ads:
        print("  Объявления не найдены.")
        return
    for item in ads:
        print(
            f"  [{item.get('id')}] Район: {item.get('district')} | "
            f"Цена: {item.get('price')} руб. | {item.get('description')}"
        )


def main() -> None:
    """Главный цикл приложения."""
    ads = load_json(ADS_FILE)
    candidates = load_json(CANDIDATES_FILE)

    current_user = {
        "name": "Алексей",
        "budget": 16000.0,
        "district": "центр",
        "smoking": False,
        "age": 22,
    }

    while True:
        print("\n" + "=" * 45)
        print("      ROOMMATE SEARCH SERVICE (ПР2)")
        print("=" * 45)
        print(f"Ваш профиль: {current_user['name']}, {current_user['age']} лет")
        print(f"Бюджет: {current_user['budget']} руб. | Район: {current_user['district']}")
        print(f"Курение: {'Да' if current_user['smoking'] else 'Нет'}")
        print("-" * 45)
        print("1. Показать все объявления")
        print("2. Фильтровать объявления (бюджет и район)")
        print("3. Добавить объявление")
        print("4. Подобрать соседей (Топ-3)")
        print("5. Изменить свой профиль")
        print("0. Выход")

        choice = input("\nВыберите пункт меню (0-5): ").strip()

        if choice == "1":
            sorted_ads = sort_ads_by_price(ads)
            print("\n--- Список объявлений (по возрастанию цены) ---")
            show_ads_table(sorted_ads)

        elif choice == "2":
            max_p = input_float(
                f"Введите макс. цену (по умолчанию {current_user['budget']}): ",
                default=current_user["budget"],
            )
            dist = input("Введите район (Enter - любой): ").strip() or None
            filtered = filter_ads(ads, max_p, dist)
            print(f"\n--- Найдено: {len(filtered)} ---")
            show_ads_table(filtered)

        elif choice == "3":
            print("\n--- Добавление нового объявления ---")
            dist = input("Район: ").strip()
            price = input_float("Стоимость (руб.): ")
            desc = input("Описание: ").strip()
            new_item = add_ad(ads, dist, price, desc)
            save_json(ADS_FILE, ads)
            print(f"Объявление успешно добавлено с ID #{new_item['id']}!")

        elif choice == "4":
            print("\n--- Рекомендованные кандидаты в соседи ---")
            top = get_top_candidates(current_user, candidates, top_n=3)
            if not top:
                print("Подходящих кандидатов не найдено.")
            for c in top:
                score = calculate_match_score(current_user, c)
                print(
                    f"• {c['name']} (Возраст: {c['age']}, Район: {c['district']}, "
                    f"Бюджет: {c['budget']} руб.) -> Совместимость: {score}/4"
                )

        elif choice == "5":
            print("\n--- Редактирование профиля ---")
            current_user["budget"] = input_float(
                f"Новый бюджет ({current_user['budget']}): ",
                default=current_user["budget"],
            )
            d_input = input(f"Новый район ({current_user['district']}): ").strip()
            if d_input:
                current_user["district"] = d_input
            current_user["age"] = input_int(
                f"Новый возраст ({current_user['age']}): ",
                default=current_user["age"],
            )
            current_user["smoking"] = input_bool(
                "Курите? (да/нет): ", default=current_user["smoking"]
            )
            print("Профиль успешно обновлен!")

        elif choice == "0":
            print("Завершение работы программы.")
            break
        else:
            print("Неверный пункт меню, попробуйте снова.")


if __name__ == "__main__":
    main()