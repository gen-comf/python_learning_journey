# ===== STRINGS: BASIC =====
# Stepik 11.4: https://stepik.org/lesson/328948

print("=== Задача 1: Значение функции ")
list_x = []

for _ in range(int(input())):
    x = int(input())
    list_x.append(x)
    

print(*list_x, sep='\n')
print()

list_x2 = []
for number in list_x:
    list_x2.append(number**2 + 2*number +1)

print(*list_x2, sep='\n')


print("=== Задача 2: Remove outliers ")
list_x = []
for _ in range(int(input())):
    x = int(input())
    list_x.append(x)

list_x.remove(max(list_x))
list_x.remove(min(list_x))

print(*list_x, sep='\n')


print("=== Задача 3: Без дубликатов")
str_list = []
for _ in range(int(input())):
    str_x = input()
    if str_x not in str_list:
        str_list.append(str_x)

print(*str_list, sep='\n')


print("=== Задача 4: Google search - 1")
temp_list = []
for _ in range(int(input())):
    temp_list.append(input())   # Сохраняем оригинал

search_str = input().lower()    # Поисковый запрос в нижнем регистре

for el in temp_list:
    if search_str in el.lower(): # Сравниваем с версией в нижнем регистре         
        print(el)                   # Выводим оригинал

print("=== Задача 5: Google search - 2")
temp_list = []
for _ in range(int(input())):
    temp_list.append(input())   # Сохраняем оригинал

search_list = []
for _ in range(int(input())):
    search_list.append(input().lower())    # Сохраняем поисковые запросы в нижнем регистре

for el in temp_list:                        # Проверяем, что ВСЕ запросы из search_list есть в el
    all_found = True            
    for query in search_list:
        if query not in el.lower():          # Приводим строку к нижнему регистру
            all_found = False
            break
        
    if all_found:
        print(el)


print("=== Задача 6: Negatives, Zeros and Positives")
digits_list = []

for _ in range(int(input())):
    digits_list.append(int(input()))    # заваодим все вводимые числа в список


digits_negat = []
digits_zero = []
digits_pozit = []

for digit in digits_list:                               # сортируем числа по соответствующим спикам
    if digit < 0:
            digits_negat.append(digit)
    if digit == 0:
            digits_zero.append(digit)
    if digit > 0:
            digits_pozit.append(digit)

digits_list = digits_negat + digits_zero + digits_pozit     # соединяем списки в 1

print(*digits_list, sep='\n')