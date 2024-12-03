'''Zadania z lab 5'''

#Zadanie 1
#a)

# import random

# szczesliwy_numerek = random.randint(1, 22)

# print(szczesliwy_numerek)

#b)

# import random

# roczniki = [2000, 2001, 2002, 2003, 2004, 2005, 2006]

# szczesliwy_rocznik = random.choice(roczniki)

# print(szczesliwy_rocznik)

#c)

#w domu

#Zadanie 2

# import math

# w1 = math.sqrt(2) + math.sqrt(3) + math.sqrt(6)
# w1 = math.floor(w1)
# w2 = math.ceil(w1)
# w3 = math.sqrt(-5)
# print(w1, w2)

#Zadanie 3

# import time

# def sekundnik(czas):
#     while czas > 0:
#         print(f'Pozostało {czas} sekund.')
#         time.sleep(1)
#         czas -= 1
#     print("czas minął")
# czas_do_odlicznia = int(input("Podaj czas w sekundach: "))
# sekundnik(czas_do_odlicznia)

#Zadanie 4 w domu

# from datetime import datetime

# dzis = date.today()
# zajecia

#Zadanie 10

import random
import math

# Pobranie przedziału od użytkownika
dolna_granica = int(input("Podaj dolną granicę przedziału: "))
górna_granica = int(input("Podaj górną granicę przedziału: "))

# Losowanie 10 liczb z zadanego przedziału
krotka = tuple(random.randint(dolna_granica, górna_granica) for _ in range(10))

print(f"Twoja krotka: {krotka}")

# Obliczanie średniej geometrycznej
produkty = 1
for liczba in krotka:
    produkty *= liczba

srednia_geometryczna = produkty ** (1/10)

print(f"Średnia geometryczna krotki wynosi: {srednia_geometryczna}")
