# generation_python/module_1_basics/loops/01_basic_for/task_for_range.py
"""
Подраздел 1: Базовый цикл for
Stepik: https://stepik.org/lesson/265120/step/1?unit=246069

Задачи на цикл for с функцией range()
"""

print("=== Задача 1: Последовательность чисел 1")
m, n = int(input()), int(input())  # m <= n
for i in range(m, n + 1):
    print(i)

print("=== Задача 2: Последовательность чисел 2")
m, n = int(input()), int(input())
if m < n:
    for i in range(m, n + 1):
        print(i)
else:
    for i in range(m, n - 1, -1):
        print(i)

print("=== Задача 3: Последовательность чисел 3. Вариант 1 if")
m, n = int(input()), int(input())  # m > n
for i in range(m, n - 1, -1):
    if i % 2 != 0:
        print(i)

print("=== Задача 3: Последовательность чисел 3. Вариант 2 без if")
m, n = int(input()), int(input())  # m > n
start = m - ((m + 1) % 2)  # (m + 1) % 2 дает 0 если m нечетное, 1 если m четное
for i in range(start, n - 1, -2):
    print(i)

print("=== Задача 4: Последовательность чисел 4.")
m, n = int(input()), int(input())  # m <= n
for i in range(m, n + 1):
    if i % 17 == 0:
        print(i)
    elif i % 3 == 0 and i % 5 == 0:
        print(i)
    elif i % 10 == 9:
        print(i)

print("=== Задача 5: Таблица умножения.")
n = int(input())
for i in range(1, 11):
    print(n, "x", i, "=", i * n)
