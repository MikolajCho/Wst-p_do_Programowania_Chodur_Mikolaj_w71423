'''Zadania od 8 do 14 z Lab 2'''

#Zadanie 8
# def funkcja(x):
#     return 2 * x**2 - 5 * x - 8

# x_poczatkowe = -4
# x_koncowe = 4
# krok = 0.5

# x = x_poczatkowe
# while x <= x_koncowe:
#     y = funkcja(x)
#     print(f"x = {x:.1f}, y = {y:.2f}")
#     x += krok

# #Zadanie 9
# while True:
#     liczba = int(input("Podaj liczbę całkowitą: "))
#     if liczba < 0:
#         print("Wychodzę z pętli")
#         break

# #Zadanie 10
# a = int(input("Podaj pierwszą liczbę: "))
# b = int(input("Podaj drugą liczbę: "))

# if a < b:
#     while a <= b:
#         print(a)
#         a += 1
# else:
#     while b <= a:
#         print(b)
#         b += 1

# #Zadanie 11

# a = int(input("Podaj pierwszą liczbę: "))
# b = int(input("Podaj drugą liczbę: "))

# if a < b:
#     while a <= b:
#         if a % 2 != 0:
#             a += 1
#             continue
#         print(a)
#         a += 1
# else:
#     while b <= a:
#         if b % 2 != 0:
#             b += 1
#             continue
#         print(b)
#         b += 1

# #Zadanie 12

# n = int(input("Podaj liczbę studentów: "))
# suma = 0
# i = 0

# while i < n:
#     punkty = float(input(f"Podaj liczbę punktów dla studenta {i + 1}: "))
#     suma += punkty
#     i += 1

# srednia = suma / n
# print(f"Średnia punktów w grupie: {srednia:.2f}")

# #Zadanie 13

# n = int(input("Podaj liczbę studentów: "))
# suma = 0
# i = 0

# while True:
#     punkty = float(input(f"Podaj liczbę punktów dla studenta {i + 1}: "))
#     if punkty < 0 or punkty > 100:
#         print("Punkty poza zakresem 0-100, pomijam.")
#         continue
#     suma += punkty
#     i += 1
#     if i >= n:
#         break

# srednia = suma / n
# print(f"Średnia punktów w grupie: {srednia:.2f}")

# # Zadanie 14 - z continue
# while True:
#     dana = int(input("Podaj liczbę: "))
#     if dana < 0:
#         print("To nie jest liczba nieujemna")
#         continue
#     print(f"Pierwiastek kwadratowy: {dana ** 0.5}")
#     print("Dziękujemy za skorzystanie z naszej aplikacji")
#     break

#Zadanie 14 - bez continue

# while True:
#     dana = int(input("Podaj liczbę: "))
#     if dana < 0:
#         print("To nie jest liczba nieujemna")
#     else:
#         print(f"Pierwiastek kwadratowy: {dana ** 0.5}")
#         print("Dziękujemy za skorzystanie z naszej aplikacji")
#         break

'''Zadania z lab 3'''

# # Zadanie 1
# names = ["Anna", "Ewa", "Jan", "Piotr"]
# names.sort()
# print("Posortowana lista:", names)

# names.extend(["Kasia", "Tomek"])
# last_person = names.pop()
# print("Ostatnia osoba:", last_person)

# names.insert(2, "Marek")
# print("Lista po dodaniu na 3 pozycji:", names)

# names.reverse()
# names *= 2
# print("Odwrócona i zdublowana lista:", names)

# # Zadanie 2
# sentence = input("Podaj zdanie: ")

# # a)
# letters = sorted(set(filter(str.isalpha, sentence.lower())))
# alphabet = set('abcdefghijklmnopqrstuvwxyz')
# missing_letters = alphabet - set(letters)
# print("Występujące litery:", letters)
# print("Brakujące litery:", missing_letters)

# # b)
# filtered_sentence = ''.join([char for i, char in enumerate(sentence) if i % 2 == 0])
# print("Zdanie po usunięciu znaków na nieparzystych indeksach:", filtered_sentence)

# # c)
# title_case_sentence = ' '.join(word.capitalize() for word in sentence.split())
# print("Zdanie z wielkimi literami na początku:", title_case_sentence)

# # d)
# words = sentence.split()
# longest_word = max(words, key=len)
# print("Najdłuższe słowo:", longest_word, "o długości:", len(longest_word))

# # e)
# replaced_sentence = ''.join(['@' if sentence.count(char) > 1 else char for char in sentence])
# print("Zdanie po zamianie powtarzających się znaków:", replaced_sentence)

# # Zadanie 3
# string = input("Podaj ciąg znaków: ")
# is_palindrome = string == string[::-1]
# print("Czy ciąg jest palindromem?", "Tak" if is_palindrome else "Nie")

# Zadanie 4
# n = int(input("Podaj n: "))
# x = int(input("Podaj x: "))
# strings = [input(f"Podaj ciąg {i+1}: ") for i in range(n)]
# strings_tuple = tuple(strings)

# # a)
# total_chars = sum(len(s) for s in strings_tuple)
# print("Ilość znaków w liście:", total_chars)

# # # b)
# # k_count = sum(s.count('k') for s in strings_tuple)
# # print("Ilość liter 'k':", k_count)

# # # c)
# # kt_count = sum(s.count('kt') for s in strings_tuple)
# # print("Ilość ciągów 'kt':", kt_count)

# # # d)
# # s = int(input("Podaj s: "))
# # longer_than_s = sum(1 for s in strings_tuple if len(s) > s)
# # print("Ilość ciągów dłuższych niż s:", longer_than_s)

# # Zadanie 5
# zakupy = {"chleb": 3.5, "mleko": 2.0, "masło": 5.0}
# print("Lista zakupów:", zakupy)
# print("Suma wydatków:", sum(zakupy.values()))

# Zadanie 6
# rachunki = {"styczeń": 120, "luty": 150, "marzec": 100}
# max_value = max(rachunki.values())
# min_value = min(rachunki.values())
# total = sum(rachunki.values())
# average = total / len(rachunki)
# print("Maksymalna:", max_value, "Minimalna:", min_value, "Suma:", total, "Średnia:", average)

# last_month = list(rachunki.values())[-1]
# if last_month > average:
#     print("Trzeba zacisnąć pasa")
# else:
#     print("Wszystko okay")

# # Zadanie 7
# import random

# a = random.randint(3, 7)
# b = random.randint(3, 7)
# X = {random.randint(0, 10) for _ in range(a)}
# Y = {random.randint(0, 10) for _ in range(b)}

# print("Zbiór X:", X)
# print("Zbiór Y:", Y)

# # a)
# print("Czy X zawiera 5?", 5 in X)

# # b)
# print("Czy X jest podzbiorem Y?", X.issubset(Y))

# # c)
# print("Czy Y jest podzbiorem X?", Y.issubset(X))

# # d)
# print("Suma X i Y:", X.union(Y))

# # e)
# print("Różnica X i Y:", X.difference(Y))

# # f)
# print("Różnica Y i X:", Y.difference(X))

# # g)
# print("Część wspólna X i Y:", X.intersection(Y))

# # h)
# print("Najwyższy element w X i Y:", max(X.union(Y)))

# # i)
# first_element = next(iter(X))
# X.remove(first_element)
# Y.add(first_element)
# print("X po usunięciu pierwszego elementu:", X)
# print("Y po dodaniu elementu:", Y)

# # j)
# X.update(Y)
# print("X po dodaniu elementów Y:", X)

# # k)
# X.clear()
# Y.clear()
# print("X i Y po wyczyszczeniu:", X, Y)

# # Zadanie 8
# numbers = input("Podaj pięć cyfr oddzielonych przecinkiem: ").split(',')
# if len(numbers) != 5:
#     print("Niepoprawna ilość cyfr.")
# else:
#     numbers = list(map(int, numbers))
#     numbers_set = set(numbers)
#     random_element = random.choice(list(numbers_set))
#     print("Wylosowany element:", random_element)
#     if random_element == min(numbers_set) or random_element == max(numbers_set):
#         print("Wylosowany element jest najmniejszy lub największy.")

# # Zadanie 9
# for y in range(6):
#     for x in range(5):
#         if (x, y) in [(0, 1), (2, 3), (2, 4), (3, 4)]:
#             print("X", end=" ")
#         elif (x, y) in [(1, 1), (2, 0), (3, 3), (5, 3)]:
#             print("*", end=" ")
#         elif y == 2:
#             print("-", end=" ")
#         else:
#             print(".", end=" ")
#     print()

# Zadanie 11
alphabet = list('abcdefghijklmnopqrstuvwxyz')
n = int(input("Podaj n: "))
sublists = [alphabet[i:i + n] for i in range(0, len(alphabet), n)]
print("Podzielona lista:", sublists)
