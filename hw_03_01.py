from datetime import datetime


def get_days_from_today(target_date): # створення функції з одним параметром
    try:
        target_date = datetime.strptime(
            target_date, "%Y-%m-%d"
        )  # переведення до рядку дати яку ввів користувач
        current_datetime = datetime.today()  # сьогоднішня дата
        days_dif = (
            current_datetime - target_date
        ).days  # віднімаємо від сьогодні те що ввів користувач
        return days_dif
    except ValueError as e:
        print(f"Введений некоректний формат дати: {e}")
        return None


target_date = input()
result = get_days_from_today(target_date)
if result is not None:
    print(result)
else:
    print("Введіть дані у форматі - Рік-Місяць-День")
