# ===== STRINGS: BASIC =====
# Stepik 13.4: https://stepik.org/lesson/331754

"=== Задача 1: Конвертер километров ==="
# объявление функции
def convert_to_miles(km):
    miles = km * 0.6214
    return miles

# считываем данные
# num = int(input())

# вызываем функцию
# print(convert_to_miles(num))

"=== Задача 2: </code> ==="
# объявление функции
def code_format(text):
    return f'<code>{text}</code>'

# считываем данные
#text = input()

# вызываем функцию
#print(code_format(text))


"=== Задача 3: Количество дней 🗓️ ==="
# объявление функции
def get_days(month):
    if month in [4, 6, 9, 11]:
        return 30
    elif month in [2]:
        return 28
    else:
        return 31

# считываем данные
# num = int(input())

# вызываем функцию
# print(get_days(num))


"=== Задача 4: Математика округлит 🧠 ==="
# объявление функции
def math_round_to_int(num):
    res = str(num).split('.')
    if int(res[1][0]) >= 5:
        return int(res[0]) + 1
    else:
        return int(res[0])

# считываем данные
#num = float(input())

# вызываем функцию
# print(math_round_to_int(num))


"=== Задача 5: Делители 1 ==="
# объявление функции
def get_factors(num):
    result = []
    for i in range(1, num // 2 + 1):        # в целях экономии памяти, можно сделать цикл до середины вместо range(1, n + 1)
        if num % i == 0:
            result.append(i)

    result.append(num)                      # а затем добавить само число как последний делитель
    return result

# считываем данные
# n = int(input())

# вызываем функцию
# print(get_factors(n))


"=== Задача 6: Делители 2 ==="
def get_factors(num):
    divisors = []
    for i in range(1, num // 2 + 1):        # в целях экономии памяти, можно сделать цикл до середины вместо range(1, n + 1)
        if num % i == 0:
            divisors.append(i)

    divisors.append(num)                      # а затем добавить само число как последний делитель
    return len(divisors)

# считываем данные
#n = int(input())

# вызываем функцию
#print(get_factors(n))


"=== Задача 7: С каждого по одному 1️⃣ ==="
# объявление функции
def get_unique(numbers):
    result =[]
    for i in numbers:
        if not i in result:
            result.append(i)

    return result

# считываем данные
#numbers = eval(input())

# вызываем функцию
#print(get_unique(numbers))


"=== Задача 7: Последнее вхождение 🔚 ==="
# объявление функции
def get_last_index(data, value):
    for i in range(len(data) - 1, -1, -1):
        if data[i] == value:
            return i
        
    return "ERROR!"
           

# считываем данные
#data = eval(input())
#value = eval(input())

# вызываем функцию
#print(get_last_index(data, value))

"=== Задача 8: Найти всех 👀 ==="
# объявление функции
def find_all(target, symbol):
    result = []
    for i in range(len(target)):
        if target[i] == symbol:         # Сравниваем символ на позиции i
            result.append(i)            # Добавляем индекс i
    return result
        

# считываем данные
###print(find_all(s, char))

"=== Задача 9: Merge lists 1 ==="
# объявление функции
def merge(list1, list2):
    list3 = list1 + list2
    list3.sort()
    return list3

# считываем данные
#numbers1 = [int(c) for c in input().split()]
#numbers2 = [int(c) for c in input().split()]

# вызываем функцию
#print(merge(numbers1, numbers2))

"=== Задача 10: Merge lists 2 ==="
# Функция слияния двух отсортированных списков
def quick_merge(list1, list2):
    result = []
    p1 = 0  # указатель на первый элемент списка list1
    p2 = 0  # указатель на первый элемент списка list2

    while p1 < len(list1) and p2 < len(list2):  # пока не закончился какой-нибудь из списков
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):   # прицепление остатка
        result += list1[p1:]
    else:                 # иначе прицепляем остаток другого списка
        result += list2[p2:]
    
    return result


"""# Основная программа
n = int(input())  # количество списков

# Считываем первый список
result_list = list(map(int, input().split()))

# Последовательно сливаем остальные списки
for _ in range(n - 1):
    current_list = list(map(int, input().split()))
    result_list = quick_merge(result_list, current_list)

# Выводим результат
print(*result_list)"""
