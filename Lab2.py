#LABORATORIUM 1 - ZADANIA 8, 9, 10, 11, 12, 13, 14

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

# Zadanie 12 




'''
'''

# Zadanie 13 - Prosty kalkulator

'''

def kalkulator():
    """
    Python 3.10+ wprowadził konstrukcję match-case jako odpowiednik switch z innych języków.
    Tutaj używamy tradycyjnego if-elif jako przykład rozwiązania działającego na starszych wersjach.
    """
    try:
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))
        operacja = input("Podaj operację (+, -, *, /): ")
        
        if operacja == "+":
            wynik = a + b
        elif operacja == "-":
            wynik = a - b
        elif operacja == "*":
            wynik = a * b
        elif operacja == "/":
            if b == 0:
                print("Nie można dzielić przez zero!")
                return
            wynik = a / b
        else:
            print("Nieznana operacja!")
            return
            
        print(f"Wynik: {wynik}")
    except ValueError:
        print("Podano nieprawidłowe wartości!")

# Zadanie 14 - Sprawdzanie rozszerzenia pliku Excel
def sprawdz_excel():
    """
    Metoda endswith() sprawdza, czy string kończy się podanym ciągiem znaków.
    Można podać krotkę z wieloma możliwymi zakończeniami.
    Zwraca True/False.
    """
    nazwa_pliku = input("Podaj nazwę pliku: ")
    rozszerzenia_excel = ('.xlsx', '.xls', '.xlsm')
    
    if nazwa_pliku.endswith(rozszerzenia_excel):
        print("To jest plik Excela")
    else:
        print("To nie jest plik Excela")

# Wywołanie funkcji
print("\nSortowanie trzech liczb:")
sortuj_liczby()

print("\nRozwiązywanie równania kwadratowego:")
rownanie_kwadratowe()

print("\nKalkulator:")
kalkulator()

print("\nSprawdzanie pliku Excel:")
sprawdz_excel()

#LABORATORIUM 2 - ZADANIA 1, 2, 3, 4, 5, 6, 7

# Zadanie 1 - Ciągi liczb
# a) 1 do 100

for i in range(1, 101):
    print(i, end=", ")
print()

# b) 100 do 0
for i in range(100, -1, -1):
    print(i, end=", ")
print()

# c) 7, 14, ..., 77
for i in range(7, 78, 7):
    print(i, end=", ")
print()

# d) 20, 18, ..., 0
for i in range(20, -1, -2):
    print(i, end=", ")
print()

# Zadanie 2 - Gwiazdki
n = int(input("Podaj liczbę wierszy: "))

# a) Prostokąt
print("\nWzór a:")
for i in range(n):
    print("* " * 3)

# b) Trójkąt rosnący
print("\nWzór b:")
for i in range(1, n + 1):
    print("* " * i)

# c) 



'''
'''

# Zadanie 3 - Ciąg arytmetyczny
n = int(input("\nPodaj liczbę elementów (n): "))
a = float(input("Podaj pierwszy element (a): "))
r = float(input("Podaj różnicę (r): "))

for i in range(n):
    print(a + i * r, end=", ")
print()

# Zadanie 4 - Silnia
n = int(input("\nPodaj liczbę do obliczenia silni: "))
silnia = 1
for i in range(1, n + 1):
    silnia *= i
print(f"{n}! = {silnia}")

# Zadanie 5 - Indeksowanie tekstu
tekst = "Rzeszów jest piękny"
print(f"a) Pierwsza litera: {tekst[0]}")
print(f"b) Wybrane litery: {tekst[6]}, {tekst[9]}, {tekst[12]}, {tekst[1]}")

# Zadanie 6 - Indeksowanie tekstu
tresc = "Python jest super"
print(f"a) Znak zerowy: {tresc[0]}")
print(f"b) Ostatni znak: {tresc[-1]}")
print(f"c) Co drugi: {tresc[::2]}")
print(f"d) Co trzeci od pierwszego: {tresc[1::3]}")
print(f"e) Od 10 do końca: {tresc[10:]}")
print(f"f) Od końca: {tresc[::-1]}")

# Zadanie 7 - Operacje na łańcuchach
# a)
imie = input("\nPodaj imię: ")
print(f"Witaj {imie}")

# b)
wiek = input("Podaj wiek: ")
print(f"Twój wiek to: {wiek}")

# c)
imie = input("Podaj imię: ")
nazwisko = input("Podaj nazwisko: ")
print(f"Inicjały: {imie[0]}{nazwisko[0]}")

# d)
lancuch = input("Podaj łańcuch: ")
print(lancuch * 5)

# e)
lancuch1 = input("Podaj pierwszy łańcuch: ")
lancuch2 = input("Podaj drugi łańcuch: ")
lancuch3 = lancuch1 + lancuch2
print(f"Połączone łańcuchy: {lancuch3}")

# f)
lancuch1 = input("Podaj pierwszy łańcuch: ")
lancuch2 = input("Podaj drugi łańcuch: ")
pol1 = len(lancuch1) // 2
pol2 = len(lancuch2) // 2
lancuch3 = lancuch1[:pol1] + lancuch2[pol2:]
print(f"Nowy łańcuch: {lancuch3}")
'''
