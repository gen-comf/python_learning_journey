# ===== STRINGS: BASIC =====
# Stepik 13.2: https://stepik.org/lesson/333525

"=== Задача 1: ФИО"
# объявление функции
def print_fio(name, surname, patronymic):
    
    print((surname[0] + name[0] + patronymic[0]).upper())

# считываем данные
name, surname, patronymic = input(), input(), input()

# вызываем функцию
# print_fio(name, surname, patronymic)


"=== Задача 2: Посчитай регистры 🔤"
# объявление функции
def print_case_counts(s):
    
    count_lower = 0
    count_upper = 0
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].islower():
                count_lower += 1
            if s[i].isupper():
                count_upper += 1


    print(f'Букв в верхнем регистре: {count_upper}')
    print(f'Букв в нижнем регистре: {count_lower}')

# считываем данные
s = input()

# вызываем функцию
# print_case_counts(s)


"=== Задача 3: Сумма цифр"
# объявление функции
def print_digit_sum(num):
    res = [int(i) for i in str(n)]
    print(sum(res))   

# считываем данные
n = int(input())

# вызываем функцию
# print_digit_sum(n)


"=== Задача 4: Отсортируй и выведи 📶"
# объявление функции
def print_sorted_hyphen(s):
    res = s.split('-')
    res.sort()
    print('-'.join(res))

# считываем данные
s = input()

# вызываем функцию
#print_sorted_hyphen(s)


"=== Задача 5: Звёздный треугольник ⭐"
# объявление функции
def draw_triangle(fill, base):
    for i in range(1, base//2 + 2):                       
        print(fill * i)

    for i in range(base//2, 0, -1):                       
        print(fill * i)

# считываем данные
fill = input()
base = int(input())

# вызываем функцию
# draw_triangle(fill, base)


"=== Задача 6: В какое время созвон? 🕓🌶️"
# объявление функции
def print_perm_time_call(msc_time):
    res = msc_time.split(':')
    hours = int(res[0])  # Просто преобразуем всё число
    minutes = res[1]

    perm_hours = hours + 2 # Добавляем 2 часа

    # Форматируем вывод
    if perm_hours < 10:
        print(f"Созвон будет в 0{perm_hours}:{minutes}.")
    else:
        print(f"Созвон будет в {perm_hours}:{minutes}.")

# считываем данные
msc_time = input()

# вызываем функцию
# print_perm_time_call(msc_time)

"=== Задача 6: В какое время созвон? 🕓🌶️ Идеальный вариант"
def print_perm_time_call(msc_time):
    hh, mm = msc_time.split(':')   # Разделение
    perm_hh = int(hh) + 2           # Преобразование и вычисление
    #print(f"Созвон будет в {perm_hh:02}:{mm}.")  # Форматированный вывод {perm_hh:02} — добавляет 0 если нужно



"=== Задача 7: Посчитай количества 🔢🌶️"
# объявление функции
def print_symbol_counts(s):
    s = s.lower()
    printed = []  # список для отслеживания уже выведенных букв
    
    for char in sorted(s):  # сортируем исходную строку
        if char not in printed:
            count = s.count(char)
            print(f"{char}: {count}")
            printed.append(char)

# считываем данные
s = input()

# вызываем функцию
# print_symbol_counts(s)