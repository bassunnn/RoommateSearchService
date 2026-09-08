import json
from typing import List, Dict
import os

# 1. Фильтрация объявлений по бюджету и району
def filter_ads(ads: List[Dict], max_price: float, district: str = None) -> List[Dict]:
    result = [a for a in ads if a.get("price", 0) <= max_price]
    if district:
        result = [a for a in result if a.get("district", "").lower() == district.lower()]
    return result

# 2. Ранжирование совместимости пользователей
def match_users(user1: Dict, user2: Dict) -> int:
    score = 0
    if user1.get("budget") >= user2.get("budget", 0) * 0.8:
        score += 1
    if user1.get("district") == user2.get("district"):
        score += 1
    if user1.get("smoking") == user2.get("smoking"):
        score += 1
    if abs(user1.get("age", 0) - user2.get("age", 0)) <= 5:
        score += 1
    return score

# 3. Топ-N лучших соседей
def top_neighbors(user: Dict, candidates: List[Dict], top_n: int = 3) -> List[Dict]:
    scored = [(c, match_users(user, c)) for c in candidates]
    scored.sort(key=lambda x: x[1], reverse=True)
    return [c for c, s in scored[:top_n] if s > 0]

# --- Консольный интерфейс ---
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(text):
    print("\n" + "="*50)
    print(f"  {text}")
    print("="*50)

def show_ads(ads):
    if not ads:
        print("  Объявлений не найдено.")
        return
    for i, ad in enumerate(ads, 1):
        print(f"  {i}. {ad.get('district', 'Не указан')} | {ad.get('price', 0)} руб. | {ad.get('description', 'Без описания')}")

def show_candidates(candidates):
    if not candidates:
        print("  Подходящих соседей не найдено.")
        return
    for i, c in enumerate(candidates, 1):
        print(f"  {i}. Возраст: {c.get('age', '?')} | Бюджет: {c.get('budget', 0)} руб.")
        print(f"     Район: {c.get('district', '?')} | Курит: {'Да' if c.get('smoking') else 'Нет'}")
        print(f"     Совместимость: {match_users(current_user, c)}/4")
        print()

def main_menu():
    global current_user
    # Тестовые данные
    ads = [
        {"price": 15000, "district": "центр", "description": "Комната 15м², рядом метро"},
        {"price": 12000, "district": "спартак", "description": "Уютная комната в спальнике"},
        {"price": 18000, "district": "центр", "description": "Студия, свежий ремонт"},
        {"price": 10000, "district": "спартак", "description": "Эконом вариант"},
    ]
    
    candidates = [
        {"budget": 14000, "district": "центр", "smoking": False, "age": 24},
        {"budget": 10000, "district": "спартак", "smoking": True, "age": 30},
        {"budget": 16000, "district": "центр", "smoking": False, "age": 20},
        {"budget": 13000, "district": "спартак", "smoking": False, "age": 21},
    ]
    
    current_user = {"budget": 15000, "district": "центр", "smoking": False, "age": 22}

    while True:
        clear_screen()
        print_header("ROOMMATE SEARCH SERVICE")
        print("\n  Ваш профиль:")
        print(f"  Бюджет: {current_user['budget']} руб.")
        print(f"  Район: {current_user['district']}")
        print(f"  Возраст: {current_user['age']}")
        print(f"  Курит: {'Да' if current_user['smoking'] else 'Нет'}")
        
        print("\n  Меню:")
        print("  1. Поиск объявлений")
        print("  2. Поиск соседей (топ-3)")
        print("  3. Изменить свой профиль")
        print("  4. Выход")
        
        choice = input("\n  Выберите действие (1-4): ").strip()
        
        if choice == '1':
            clear_screen()
            print_header("ПОИСК ОБЪЯВЛЕНИЙ")
            max_price = float(input("  Введите макс. цену (руб.): ") or current_user['budget'])
            district = input("  Введите район (Enter - любой): ").strip() or None
            filtered = filter_ads(ads, max_price, district)
            show_ads(filtered)
            input("\n  Нажмите Enter для продолжения...")
            
        elif choice == '2':
            clear_screen()
            print_header("ПОИСК СОСЕДЕЙ")
            print("  Топ-3 подходящих соседа:\n")
            top = top_neighbors(current_user, candidates, 3)
            show_candidates(top)
            input("\n  Нажмите Enter для продолжения...")
            
        elif choice == '3':
            clear_screen()
            print_header("РЕДАКТИРОВАНИЕ ПРОФИЛЯ")
            try:
                budget = input(f"  Бюджет ({current_user['budget']}): ").strip()
                if budget:
                    current_user['budget'] = float(budget)
                
                district = input(f"  Район ({current_user['district']}): ").strip()
                if district:
                    current_user['district'] = district
                
                age = input(f"  Возраст ({current_user['age']}): ").strip()
                if age:
                    current_user['age'] = int(age)
                
                smoking = input(f"  Курите? (да/нет) ({'да' if current_user['smoking'] else 'нет'}): ").strip().lower()
                if smoking in ['да', 'yes', 'y']:
                    current_user['smoking'] = True
                elif smoking in ['нет', 'no', 'n']:
                    current_user['smoking'] = False
                
                print("\n  Профиль обновлен!")
            except ValueError:
                print("  Ошибка: введите корректные данные")
            
            input("\n  Нажмите Enter для продолжения...")
            
        elif choice == '4':
            print("\n  До свидания!")
            break
        else:
            print("  Неверный выбор!")
            input("  Нажмите Enter...")

if __name__ == "__main__":
    current_user = {}
    main_menu()