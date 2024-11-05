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
    
'''Zadania z labolatorium 3 - '''

#Zadanie 1

imiona = []
for i in range(4):
    imie = input(f"Podaj imię osoby {i + 1}: ")
    imiona.append(imie)
imiona.sort()
print("Lista po sortowaniu: ", imiona)

imiona.append(input("Podaj imie numer 5: "))
imiona.append(input("Podaj imie numer 6: "))
print("Lista po dodaniu dwóch osób: ", imiona)
imiona.pop()
print("Lista po usunięciu ostatniego imiona: ",imiona)

imiona.insert(2, input("Podaj imie osoby do dodania na 3 pozycję: "))
print("Lista po dodaniu osoby na trzecia pozycje: ", imiona)
imiona.reverse()
print("Lista po odwroceniu jkolejnosci: ", imiona)

imiona *= 2
print("Lista po zdublowaniu: ", imiona)
