#Zadanie 8 - Napisz program weryfikujący czy użytkownik jest pełnoletni.
'''
wiek = int(input("Podaj swój wiek"))
if wiek >= 18:
    print("Użytkownik jest pełnoletni")
else:
    print("Użytkownik nie jest pełnoletni")
'''
#Zadanie 9 - Stwórz automatyczny cennik biletowy według warunków:
'''
wiek = int(input("Podaj swój wiek: "))

if wiek <= 4:
    print("Wstęp jest bezpłatny.")
elif wiek <= 18:
    print("Bilet kosztuje 10 zł.")
else:
    czy_student = input("Czy jesteś studentem? (tak/nie): ").strip().lower()
    if czy_student == "tak":
        print("Bilet kosztuje 15 zł.")
    else:
        print("Bilet kosztuje 20 zł.")
'''

'''Zadanie 10 - Napisz program porządkowania trzech liczb x, y, z podawanych przez użytkownika. Posortuj
je od najmniejszej do największej, bez użycia wbudowanych funkcji.'''
'''
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x > y:
    x, y = y, x
if x > z:
    x, z = z, x
if y > z:
    y, z = z, y
print(x, y, z)
'''

'''Zadanie 11 - Napisz program rozwiązywania równania kwadratowego 𝑎𝑎𝑥𝑥2 + 𝑏𝑏𝑏𝑏 + 𝑐𝑐 = 0, gdzie a, b i c
są współczynnikami podawanymi przez użytkownika.'''
'''
import math

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

delta = b**2 + 4*a*c
if delta > 0:
x1 = (b)
x2 = 
if delta > 0:
    elif delta == 0
else:

print(a)
'''

#PĘTLE Zadanie 1
'''
for i in range(1, 101):
    print(i)'''
'''
for i in range (100, -1, -1):
    print(i)
    '''
'''
for i in range (7, 78, 7):
    print(i)
'''
'''
    for i in range (20, -1, -2):
    print(i)
    '''
#Zadanie 2 
'''
ile = int(input("ile lini gwiazdek wyświetlić?: "))
for i in range(ile):
    for j in range (ile - i):
        print("*", end=" ")
    print(" ")
'''
#Zadanie 5
tekst = "Rzeszów jest piękny"
print(tekst[0])
print(tekst[6])
print(tekst[9])
print(tekst[12])
print(tekst[1])
