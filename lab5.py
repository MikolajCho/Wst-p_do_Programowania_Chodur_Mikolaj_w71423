#Zadanie 1

# import random

# szczesliwy_numerek = random.randint(1, 100)
# print(f"Szczęśliwy numerek: {szczesliwy_numerek}")

# roczniki = [1990, 1991, 1992, 1993, 1994]
# szczesliwy_rocznik = random.choice(roczniki)
# print(f"Szczęśliwy rocznik: {szczesliwy_rocznik}")

# totolotek = random.sample(range(1, 50), 6)
# print(f"Totolotek: {totolotek}")

#Zadanie 2

# import math

# print(math.sqrt(81))

# print(810)

# print(math.sqrt(2) + math.sqrt(3) + math.sqrt(6))

# print(math.sqrt(125))

#Zadanie 3

# import time

# def sekundnik(seconds):
#     while seconds:
#         print(f"Pozostało: {seconds} sekund")
#         time.sleep(1)
#         seconds -= 1
#     print("Czas upłynął!")

# sekundnik(10)

#Zadanie 4

# from datetime import datetime, timedelta

# last_lab_date = datetime(2024, 12, 3)
# kolokwium_date = datetime(2025, 1, 7)

# days_since_last_lab = (datetime.now() - last_lab_date).days
# days_until_kolokwium = (kolokwium_date - datetime.now()).days

# print(f"Dni od ostatnich laboratoriów: {days_since_last_lab}")
# print(f"Dni do kolokwium: {days_until_kolokwium}")

#Zadanie 5

# import keyword

# words = ['for', 'print', 'break', 'done', 'bad']
# for word in words:
#     print(f"{word} is a keyword: {keyword.iskeyword(word)}")

#Zadanie 6

# import math
# import keyword

# print("Math module functions:")
# print(dir(math))

# print("\nKeyword module functions:")
# print(dir(keyword))

#Zadanie 7

# PI = 3.14159

# def obwod_kola(promien):
#     return 2 * PI * promien

# def pole_kola(promien):
#     return PI * promien ** 2

#Zadanie 8

# def c_to_f(celsius):
#     return celsius * 9/5 + 32

# def f_to_c(fahrenheit):
#     return (fahrenheit - 32) * 5/9

# def c_to_k(celsius):
#     return celsius + 273.15

#Zadanie 9

# def kwadrat(x):
#     return x ** 2

# def szescian(x):
#     return x ** 3

# def dodaj(a, b):
#     return a + b

#Zadanie 10

# import random
# import math

# numbers = tuple(random.randint(1, 100) for _ in range(10))
# geometric_mean = math.prod(numbers) ** (1/len(numbers))

# print(f"Numbers: {numbers}")
# print(f"Geometric mean: {geometric_mean}")

#Zadanie 11
# import random

# def zgadywanie_liczby():
#     zakres = int(input("Podaj zakres losowania: "))
#     liczba = random.randint(1, zakres)
#     proby = 3

#     for _ in range(proby):
#         guess = int(input("Zgadnij liczbę: "))
#         if guess < liczba:
#             print("Za mało!")
#         elif guess > liczba:
#             print("Za dużo!")
#         else:
#             print("Brawo! Zgadłeś!")
#             return
#     print(f"Przegrałeś! Liczba to: {liczba}")

# zgadywanie_liczby()

#Zadanie 12

# import math

# def pole_trojkata(a, b, kat):
#     if kat <= 0 or kat >= 180:
#         return "Nieprawidłowy kąt"
#     kat_rad = math.radians(kat)
#     pole = 0.5 * a * b * math.sin(kat_rad)
#     return pole

# print(pole_trojkata(5, 7, 30))

#Zadanie 13

from datetime import datetime, timedelta

def date_info(year, month, day):
    date = datetime(year, month, day)
    day_of_year = date.timetuple().tm_yday
    week_number = date.isocalendar()[1]
    two_weeks_before = date - timedelta(weeks=2)
    next_sunday = date + timedelta(days=(6 - date.weekday()))
    unix_time = int(date.timestamp())

    print(f"Dzień roku: {day_of_year}")
    print(f"Numer tygodnia: {week_number}")
    print(f"Data 2 tygodnie przed: {two_weeks_before}")
    print(f"Data najbliższej niedzieli: {next_sunday}")
    print(f"Czas unixowy: {unix_time}")

date_info(2024, 12, 15)
