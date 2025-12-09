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

print("=== Задача 6: Количество чисел.")
a, b = int(input()), int(input())  # a <= b
counter = 0
for i in range(a, b + 1):
    if (i**3) % 10 == 4 or (i**3) % 10 == 9:
        counter += 1
print(counter)

print("=== Задача 7: Сумма чисел.")
n = int(input())
total = 0
for i in range(n):
    total += int(input())
print(total)

print("=== Задача 8: Асимптотическое приближение.")
from math import log

n = int(input())
total = 1
for i in range(2, n + 1):
    total += 1 / i
print(total - log(n))

print("=== Задача 9: Сумма чисел 2.")
n = int(input())
total = 0
for i in range(1, n + 1):
    if (i**2) % 10 == 2 or (i**2) % 10 == 5 or (i**2) % 10 == 8:
        total += i
print(total)

print("=== Задача 10: Факториал.")
n = int(input())
total = 1
for i in range(2, n + 1):
    total *= i
print(total)

print("=== Задача 11: Без нулей.")
total = 1
for _ in range(10):
    num = int(input())
    if num != 0:
        total *= num
print(total)

print("=== Задача 12: Сумма делителей.")
n = int(input())
total = 0
for i in range(1, n + 1):
    if n % i == 0:
        total += i
print(total)

print("=== Задача 13: Only even numbers.")
flag = True
for _ in range(10):
    if int(input()) % 2 != 0:
        flag = False
if flag == True:
    print("YES")
else:
    print("NO")

print("=== Задача 14: Знакочередующаяся сумма.")
total = 0
n = int(input())
for i in range(1, n + 1):
    if i % 2 == 0:
        total -= i
    else:
        total += i
print(total)

print("=== Задача 15: Наибольшие числа.")
n = int(input())  # n >= 2
largest1 = 0
largest2 = 0

for _ in range(n):
    num = int(input())
    if num > largest1:
        largest2 = largest1
        largest1 = num
    elif num > largest2 or largest2 == largest1:
        largest2 = num
print(largest1)
print(largest2)

print("=== Задача 16: Последовательность Фибоначчи.")
n = int(input())  # n <= 100
a, b = 1, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
