'''Zadania z labolatorium 2 - 8, 9, 10, 11'''

#Zadanie 8

# def funkcja(x):
#     return 2*x**2 - 5*x - 8

# x_poczatkowe = -4
# x_koncowe = 4
# krok = 0.5

# x = x_poczatkowe
# while x <= x_koncowe:
#     y = funkcja(x)
#     print(f"x = {x:.1f}, y = {y:.2f}")
#     x += krok

#Zadanie 9

# while True:
#     liczba = int(input("Podaj liczbę całkowitą: "))
#     if liczba < 0:
#         print("Wychodzę z pętli")
#         break

#Zadanie 10

# a = int(input("Podaj pierwszą liczbę: "))
# b = int(input("Podaj drugą liczbę: "))

# while a < b:
#     print(a)
#     a += 1
# while a >= b:
#     print(b)
#     b += 1


#Zadanie 11 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# a = int(input("Podaj pierwszą liczbę: "))
# b = int(input("Podaj drugą liczbę: "))

# while a < b:
#     print(a)
#     a += 1
# while a >= b:
#     print(b)
#     b += 1
    
'''Zadania z labolatorium 3 - 1, 4 '''

#Zadanie 1

# imiona = []
# for i in range(4):
#     imie = input(f"Podaj imię osoby {i + 1}: ")
#     imiona.append(imie)
# imiona.sort()
# print("Lista po sortowaniu: ", imiona)

# imiona.append(input("Podaj imie numer 5: "))
# imiona.append(input("Podaj imie numer 6: "))
# print("Lista po dodaniu dwóch osób: ", imiona)
# imiona.pop()
# print("Lista po usunięciu ostatniego imiona: ",imiona)

# imiona.insert(2, input("Podaj imie osoby do dodania na 3 pozycję: "))
# print("Lista po dodaniu osoby na trzecia pozycje: ", imiona)
# imiona.reverse()
# print("Lista po odwroceniu jkolejnosci: ", imiona)

# imiona *= 2
# print("Lista po zdublowaniu: ", imiona)

# Zadanie 4
# lista=["as", "kft", "ktkkkkkkfs"]
# krotka = tuple(lista)

# print (krotka)
# suma = 0
# sk = 0
# skt = 0
# s = int(input("podaj minimalny rozmiar słowa"))
# slowa = []

# for el in krotka:
#     suma += len(el)
#     print(suma)
# print(f"Liczba znakow w krotce to: {suma}")
# for el in krotka:
#     for z in el:
#         if z == "k":
#             sk += 1
# print(f"w krotce znaleziono {sk} wystąpienia litery 'k'.")

# if el.find("kt") < 0:
#     skt += 1
# print(f"w krotce znalezionao {skt} wystapienia litery 'kt'. ")

# if len(el) >= s:
#     slowa.append(el)
# print(slowa)
# print(f"Słowa o długośi większej  niż {s}, to: ", end=" ")
# print(s, end=" ")

#Zadanie 5

zakupy={"chleb":5.0, "maslo":7.0, "czekolada":12.0, "czipsy":12.0, "woda":3.0}
print(zakupy)
suma_zakupy = 0

for el in zakupy:
    suma_zakupy += zakupy[el]
    print(f"{el} za {zakupy[el] zł"})
print(f"Za akupy zapłacimy: {suma_zakupy}zł.")
