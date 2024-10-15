'''
#Zadanie 1 - Jakie uzyskujesz wyniki? Co oznaczają poszczególne operatory?

#int (integer) - Reprezentuje liczby całkowite.
#float (floating-point) - Reprezentuje liczby rzeczywiste.

print ((1 + 2), type (1 + 2),"\n", # wynik: 3 int | dodawaie liczb całkowitych
       (1 + 4.5), type (1 + 4.5),"\n", # wynik: 5.5 float | dodawanie liczby całkowitej i rzeczywistej
       (3 / 2), type (3 / 2),"\n", # wynik: 1.5 float | dzielenie zwykłe
       (4 / 2), type(4 / 2),"\n", # wynik: 2.0 float | dzielenie zwykłe
       (3 // 2), type (3 // 2),"\n", # wynik: 1 int | dzielenie całkowite
       (-3 // 2), type (-3 // 2),"\n", # wynik: -2 int | dzielenie całkowite
       (11 % 2), type (11 % 2),"\n", # wynik: 1 int | reszta z dzielenia dwóch liczb całkowitych - 0 lub 1
       (2 ** 10), type (2 ** 10),"\n", # wynik: 1024 int | potęgowanie
       (8 ** (1/3)), type (8 ** (1/3))) # wynik: 2.0 float | pierwiastkowanie

'''
'''Potęgowanie zwraca int, jeśli wynik jest liczbą całkowitą, np. 2**3 = 8. Pierwiastkowanie zwraca float, bo większość wyników
pierwiastków to liczby ułamkowe, np. 2**0.5 = 1.414. Nawet dokładne pierwiastki, jak 8**(1/3), zwracają float, np. 2.0.'''

#Zadanie 2 - Sprawdź i wyjaśnij działanie następujących instrukcji:
'''
print(int(3.0)
      float(3)
      float("3")
      str(12.4)
      bool(0))'''
