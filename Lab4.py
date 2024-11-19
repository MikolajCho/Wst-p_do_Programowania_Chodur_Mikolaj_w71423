'''Zadania z lab4'''

#Zadanie 1

# import math

# def pole_kola(r):
#     if r < 0:  
#         print("Promień nie może być liczbą ujemną.")
#     elif r == 0:
#         print("Pole wynosi 0")
#     else:
#         pole = math.pi * r**2 
#         print(f"Pole koła o promieniu {r} wynosi {pole:.1f}")


# pole_kola(5)   
# pole_kola(-3)
# pole_kola(0)

#Zadaine 2

# def pole_trapezu(a, b, h):

#     if a <= 0 or b <= 0 or h <= 0:
#         print("Wszystkie wymiary (a, b, h) muszą być liczbami dodatnimi.")
#     else:
#         pole = 0.5 * (a + b) * h
#         print(f"Pole trapezu o podstawach {a} i {b} oraz wysokości {h} wynosi {pole:.1f}")


# pole_trapezu(4, 6, 5)
# pole_trapezu(-3, 6, 5)

#Zadanie 3

# def sprawdz_dodatnia(x):
#     if x > 0:
#         print(f"Liczba {x} jest dodatnia.")
#     elif x==0:
#         print("0")
#     else:
#         print(f"Liczba {x} nie jest dodatnia.")


# sprawdz_dodatnia(5)
# sprawdz_dodatnia(-3)
# sprawdz_dodatnia(0)

#Zadanie 4

# def oblicz_bmi(waga, wzrost):
#     bmi = waga / wzrost**2
#     if bmi < 18.5:
#         kategoria = "Niedowaga"
#     elif 18.5 <= bmi < 24.9:
#         kategoria = "Prawidłowa masa ciała"
#     elif 25 <= bmi < 29.9:
#         kategoria = "Nadwaga"
#     else:
#         kategoria = "Otyłość"
#     print(f"Twoje BMI wynosi {bmi:.2f}.")
#     print(f"Kategoria: {kategoria}")

# oblicz_bmi(70, 1.75)
# oblicz_bmi(50, 1.60)
# oblicz_bmi(90, 1.80)

#Zadanie 5

# def srednia(lista):
#     if len(lista) == 0:
#         return 0
#     return sum(lista) / len(lista)

# liczby = [5, 10, 15, 20, 25]

# wynik = srednia(liczby)

# print(f"Średnia z listy wynosi: {wynik}")

#Zadanie 6

# def funkcja(imie, wiek=20):
#     """
#     Funkcja wypisuje imię i wiek osoby.

#     Parametry:
#     imie (str): Imię osoby.
#     wiek (int, optional): Wiek osoby. Domyślnie 20.
#     """
#     print(f"Imię: {imie}")
#     print(f"Wiek: {wiek}")

# # Wyświetlanie dokumentacji funkcji
# print(funkcja.__doc__)


#Zadanie 7

# import math

# def pole_trojkata(a, b, c):
#     if a <= 0 or b <= 0 or c <= 0:
#         return "Boki muszą być dodatnie."
#     if a + b <= c or a + c <= b or b + c <= a:
#         return "Boki nie tworzą trójkąta."
#     p = (a + b + c) / 2
#     pole = math.sqrt(p * (p - a) * (p - b) * (p - c))
#     return pole

# print(f"Pole trójkąta: {pole_trojkata(3, 4, 5)}")
# print(f"Pole trójkąta: {pole_trojkata(1, 1, 3)}")
# print(f"Pole trójkąta: {pole_trojkata(-3, 4, 5)}")

#Zadanie 8

# a=float(input("Podaj liczbę a: "))
# n=float(input("Podaj stopień potęgi: "))

# def Potega(a, n):
#     if n == 1:
#         #print("Potega pierwszego stopnia wynosi 1")
#         return a
#     else:
#         #print(f"Potega wynpsi: {a} * Potega(a, n-1)")
#         return a * Potega(a, n-1)
# Potega(a, n)

#Zadanie 9

# n=float(input("Podaj liczbę miesięcy: "))

# def Fib(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return Fib(n-1) + Fib(n-2)

# print(Fib(n))

#Zadanie 10


