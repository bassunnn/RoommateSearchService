from datetime import date

# -------------------------------------------------------------------
# Начальные данные (моделирование сущностей через базовые типы данных)
# -------------------------------------------------------------------
current_date = date(2026, 9, 20)

user_name = "Алексей"
user_budget = 16000.0
user_district = "центр"
user_age = 22
user_smoking = False

candidate_name = "Дмитрий"
candidate_budget = 15000.0
candidate_district = "центр"
candidate_age = 24
candidate_smoking = False

ad_price = 15000.0
ad_district = "центр"


# -------------------------------------------------------------------
# 1. Функция проверки соответствия цены бюджету
# -------------------------------------------------------------------
def check_budget_match(budget: float, price: float) -> bool:
    """Проверяет, укладывается ли стоимость жилья в бюджет пользователя."""
    if budget >= price:
        return True
    return False


# -------------------------------------------------------------------
# 2. Функция расчета совместимости двух пользователей
# -------------------------------------------------------------------
def calculate_compatibility(
    user_age: int,
    cand_age: int,
    user_smk: bool,
    cand_smk: bool,
    user_dist: str,
    cand_dist: str,
) -> int:
    """Вычисляет балл совместимости (от 0 до 3) без использования циклов."""
    score = 0

    # Проверка совпадения района
    if user_dist.lower() == cand_dist.lower():
        score += 1

    # Проверка отношения к курению
    if user_smk == cand_smk:
        score += 1

    # Проверка разницы в возрасте (не более 5 лет)
    age_difference = abs(user_age - cand_age)
    if age_difference <= 5:
        score += 1

    return score


# -------------------------------------------------------------------
# 3. Функция формирования вердикта по подбору
# -------------------------------------------------------------------
def get_match_verdict(
    is_budget_ok: bool, score: int, candidate_name: str
) -> str:
    """Формирует итоговый статус рекомендации кандидата."""
    if not is_budget_ok:
        return "Не рекомендуется: стоимость жилья превышает бюджет"

    if score == 3:
        return f"Отличный мэтч! {candidate_name} идеально вам подходит (3/3 совпадений)."
    elif score == 2:
        return f"Хороший мэтч. С кандидатом {candidate_name} есть базовые совпадения (2/3)."
    else:
        return f"Низкая совместимость с кандидатом {candidate_name} ({score}/3 совпадений)."


# -------------------------------------------------------------------
# Основной сценарий выполнения
# -------------------------------------------------------------------
if __name__ == "__main__":
    is_affordable = check_budget_match(user_budget, ad_price)
    compatibility_score = calculate_compatibility(
        user_age,
        candidate_age,
        user_smoking,
        candidate_smoking,
        user_district,
        candidate_district,
    )
    verdict = get_match_verdict(
        is_affordable, compatibility_score, candidate_name
    )

    print("=== ROOMMATE SEARCH SERVICE (ПР1) ===")
    print(f"Дата проверки: {current_date}")
    print(
        f"Пользователь: {user_name}, Бюджет: {user_budget} руб., Район: {user_district}"
    )
    print(
        f"Кандидат: {candidate_name}, Бюджет: {candidate_budget} руб., Район: {candidate_district}"
    )
    print(f"Стоимость жилья: {ad_price} руб.")
    print("-" * 40)
    print(
        f"Жилье по карману: {'Да' if is_affordable else 'Нет'}"
    )
    print(f"Балл совместимости: {compatibility_score} из 3")
    print(f"Итог: {verdict}")