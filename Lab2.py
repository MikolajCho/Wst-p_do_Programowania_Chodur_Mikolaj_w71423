#Zadanie 8 - Napisz program weryfikujący czy użytkownik jest pełnoletni.
'''
wiek = int(input("Podaj swój wiek"))
if wiek >= 18:
    print("Użytkownik jest pełnoletni")
else:
    print("Użytkownik nie jest pełnoletni")
'''
#Zadanie 9 - Stwórz automatyczny cennik biletowy według warunków:

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
