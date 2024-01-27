import re

raw_numbers = [                     # список тел.які треба опрацювати
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]


def normalize_phone(phone_number):   # функція
    p1 = r"[\d\+]+"                  # Вибираємо всі цифри та +
    phone_number = "".join(re.findall(p1, phone_number)) # обєднує всі цифри та символ + без пробілів
    if len(phone_number) == 10:                          # умова
        phone_number = "+38" + phone_number                
    elif len(phone_number) == 12:
        phone_number = "+" + phone_number
    return phone_number                                  # повернення


for phone in raw_numbers:                                # перебір кожного номера 
    print(normalize_phone(phone))                        # вивід зміненого номера
