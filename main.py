"""Точка входа приложения на базе ООП-модели."""

import os
from datetime import date
from typing import List, Optional
from models import Ad, MatchRequest, User
from storage import (
    find_ad_by_id,
    find_user_by_id,
    load_ads,
    load_matches,
    load_users,
    save_ads,
    save_matches,
)
from utils import input_float, input_int

USERS_FILE = os.path.join("data", "users.json")
ADS_FILE = os.path.join("data", "ads.json")
MATCHES_FILE = os.path.join("data", "matches.json")


def create_new_match(
    matches: List[MatchRequest], users: List[User], ads: List[Ad]
) -> None:
    """Сценарий создания новой заявки на совместный съём."""
    print("\n--- Оформление заявки на жильё ---")
    u_id = input_int("Введите ID пользователя: ")
    user = find_user_by_id(users, u_id)
    if not user:
        print("Ошибка: пользователь с таким ID не найден.")
        return

    ad_id = input_int("Введите ID объявления: ")
    ad = find_ad_by_id(ads, ad_id)
    if not ad:
        print("Ошибка: объявление с таким ID не найдено.")
        return

    # Проверка бизнес-правила: не создавать дубликат активной заявки
    for m in matches:
        if m.user.id == user.id and m.ad.id == ad.id and not m.is_cancelled:
            print("Ошибка: активная заявка на это жилье уже существует!")
            return

    new_id = max([m.id for m in matches], default=0) + 1
    new_match = MatchRequest(
        match_id=new_id,
        user=user,
        ad=ad,
        created_date=str(date.today()),
    )
    matches.append(new_match)
    save_matches(MATCHES_FILE, matches)
    print(f"Заявка #{new_id} успешно создана!")


def cancel_match_scenario(matches: List[MatchRequest]) -> None:
    """Сценарий отмены заявки."""
    m_id = input_int("Введите ID заявки для отмены: ")
    for m in matches:
        if m.id == m_id:
            m.cancel()
            save_matches(MATCHES_FILE, matches)
            print(f"Заявка #{m_id} отменена.")
            return
    print("Заявка с таким ID не найдена.")


def main() -> None:
    """Главная функция приложения."""
    users = load_users(USERS_FILE)
    ads = load_ads(ADS_FILE)
    matches = load_matches(MATCHES_FILE, users, ads)

    while True:
        print("\n" + "=" * 45)
        print("   ROOMMATE SEARCH SERVICE (ПР3 — ООП)")
        print("=" * 45)
        print("1. Показать все объявления")
        print("2. Добавить объявление")
        print("3. Показать пользователей и кандидатов")
        print("4. Рассчитать совместимость кандидатов")
        print("5. Создать заявку на жильё")
        print("6. Показать все заявки")
        print("7. Отменить заявку")
        print("0. Выход")

        choice = input("\nВыберите пункт меню (0-7): ").strip()

        if choice == "1":
            print("\n--- Список объявлений ---")
            for a in ads:
                print(a)
        elif choice == "2":
            dist = input("Район: ").strip()
            price = input_float("Стоимость (руб.): ")
            desc = input("Описание: ").strip()
            new_id = max([a.id for a in ads], default=0) + 1
            new_ad = Ad(new_id, dist, price, desc)
            ads.append(new_ad)
            save_ads(ADS_FILE, ads)
            print("Объявление добавлено!")
        elif choice == "3":
            print("\n--- Список пользователей ---")
            for u in users:
                print(u)
        elif choice == "4":
            print("\n--- Проверка совместимости ---")
            u1_id = input_int("ID первого пользователя: ")
            u2_id = input_int("ID второго пользователя: ")
            u1 = find_user_by_id(users, u1_id)
            u2 = find_user_by_id(users, u2_id)
            if u1 and u2:
                score = u1.calculate_compatibility(u2)
                print(f"Совместимость между {u1.name} и {u2.name}: {score}/4")
            else:
                print("Один из пользователей не найден.")
        elif choice == "5":
            create_new_match(matches, users, ads)
        elif choice == "6":
            print("\n--- Список всех заявок ---")
            if not matches:
                print("Заявок пока нет.")
            for m in matches:
                print(m)
                print("-" * 30)
        elif choice == "7":
            cancel_match_scenario(matches)
        elif choice == "0":
            print("Завершение работы программы.")
            break
        else:
            print("Неверный пункт меню.")


if __name__ == "__main__":
    main()