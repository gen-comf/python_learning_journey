# generation_python/module_1_basics/loops/01_basic_for/task_for_range.py
"""
Подраздел 1: Базовый цикл for
Stepik: https://stepik.org/lesson/265120/step/1?unit=246069

Задачи на цикл for с функцией range()
"""

print("=== Задача 1: Последовательность чисел 1")
m, n = int(input()), int(input())   # m <= n
for i in range(m, n + 1):
    print(i)

print("=== Задача 2: Последовательность чисел 2")
m, n = int(input()), int(input())
if m < n:   
    for i in range(m, n + 1):
        print(i)
else:
    for i in range(m, n + 1, - 1):
        print(i)