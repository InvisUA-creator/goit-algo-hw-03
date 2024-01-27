import random


def get_number_ticket(min, max, quantity): # створення функції з трьома параметрами
    if (              
        min < 1                            # робимо вибірку по діапазонах
        or max > 1000
        or max < min
        or min > quantity
        or quantity not in range(min, max)
        or quantity > (max - min)
    ):
        return "Error"
    gnlist = []                            # пустий список
    while len(gnlist) < quantity:          # умова
        a = random.randint(min, max)       # генерація від мін до макс
        if a not in gnlist:                # перевірка чи є
            gnlist.append(a)               # якщо ні то + а
    gnlist.sort()                          # сортування списку
    return gnlist


print(get_number_ticket(1, 49, 6))

