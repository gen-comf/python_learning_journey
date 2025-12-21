# ===== STRINGS: BASIC =====
# Stepik 11.3: https://stepik.org/lesson/327207

print("=== Задача 1: Все сразу 1 🌶️")

"""Дополните приведённый ниже код, чтобы он:
Вывел длину списка;
Вывел последний элемент списка;
Вывел список в обратном порядке (вспоминаем срезы);
Вывел «YES» (без кавычек), если список содержит числа 5 и 17, или «NO» (без кавычек) в противном случае;
Вывел список с удалёнными первым и последним элементами.
Примечание. Каждый вывод необходимо осуществлять на новой строке."""


numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 
           10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 
           1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]

print(len(numbers))
print(numbers[-1])
print(numbers[::-1])
if 5 in numbers and 17 in numbers:
    print("YES")
else:
    print("NO")

del numbers[0]
del numbers[-1]
print(numbers)


print("=== Задача 2: Список строк")
n = int(input())
list_text = []

for i in range(n):
    text = input()
    list_text.append(text)

print(list_text)


print("=== Задача 3: Алфавит")
alfabet = []
multiplier = 1
for code in range(97, 123):
    alfabet.append(chr(code) * multiplier)
    multiplier += 1
print(alfabet)


print("=== Задача 4: Список кубов")
n = int(input())
list_cubes = []

for i in range(n):
    digit = int(input())**3
    list_cubes.append(digit)

print(list_cubes)


print("=== Задача 5: Список делителей")
n = int(input())
list_divisors = []

for divisor in range(1, n + 1):
    if n % divisor == 0:
        list_divisors.append(divisor)

print(list_divisors)


print("=== Задача 6: Суммы двух")
n = int(input())
temp_list = []
cur_list = []

for i in range(n):
    digit = int(input())
    temp_list.append(digit)

for j in range(len(temp_list) - 1 ):
    cur_list.append(temp_list[j] + temp_list[j + 1])

print(cur_list)


print("=== Задача 7: Удалите нечётные индексы")
temp = []
for _ in range(int(input())):
    digit = int(input())
    temp.append(digit)

cur_list = []
for i in range(0, len(temp), 2):
    cur_list.append(temp[i])

print(cur_list)


print("=== Задача 8: k-ая буква слова")
temp = []
for _ in range(int(input())):
    text = input()
    temp.append(text)

print(f"Введенные строки: {temp}")  # Для наглядности

k = int(input())
cur_list = []

for i in range(len(temp)):
    if k <= len(temp[i]):  # Правильная проверка для каждой строки
        # k-я буква имеет индекс k-1
        cur_list.append(temp[i][k-1])  # Правильный индекс
    else:
        continue  # Пропускаем короткие строки

print(f"Собранные буквы: {cur_list}")
print("".join(cur_list))  # Выводим как строку без пробелов


print("=== Задача 9: Символы всех строк")
resuslt = []
for i in range(int(input())):
    text = input()
    resuslt.extend(text)

print(resuslt)