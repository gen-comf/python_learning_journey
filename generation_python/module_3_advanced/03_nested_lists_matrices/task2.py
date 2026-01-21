#!/usr/bin/env python3
"""
МОДУЛЬ 3: Продвинутый Python
РАЗДЕЛ: 03_nested_lists_matrice
УРОК: 4.4 Матрицы часть 1
СТАТУС:  ⏳ 3/7 задач решено (21.01.2026)
СЛОЖНОСТЬ: ⭐☆☆☆☆

Задачи из курса Stepik "Поколение Python: курс для продвинутых"
https://stepik.org/lesson/416754
"""

"""
Паттерн 1: Слова по одному
Ввод: слово1\nслово2\nслово3\n...
matrix = [[input() for j in range(m)] for i in range(n)]

Паттерн 2: Строки целиком
# Ввод: слово1 слово2\nслово3 слово4\n...
matrix = [input().split()[:m] for _ in range(n)]
"""

# функция для вывода квадратной матрицы размерности  n
def print_matrix(matrix, n, width=1):
     
    for r in range(n):
        for c in range(n):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()

# ===== ЗАДАЧА 1 Вывести матрицу 1=====
n = int(input())
m = int(input())

matrix = [[input() for j in range(m)] for i in range(n)]
for row in matrix:
    print(*row)

# ===== ЗАДАЧА 2 Вывести матрицу 2=====
n = int(input())
m = int(input())

matrix = [[input() for j in range(m)] for i in range(n)]
for row in matrix:
    print(*row)
print()
for j in range(m):
    column = [matrix[i][j] for i in range(n)]
    print(*column)

# ===== ЗАДАЧА 3 След матрицы ↘️=====
"""
Следом квадратной матрицы называется сумма элементов главной диагонали. Напишите программу, которая выводит след заданной квадратной матрицы.
На вход программе подается натуральное число n – количество строк и столбцов в матрице, затем элементы матрицы (целые числа) построчно через пробел.
"""
n = int(input())
total = 0
matrix = [list(map(int, input().split())) for _ in range(n)]
total = sum(matrix[i][i] for i in range(len(matrix)))
print(total)   

# решение в одну строку print(sum(list(map(int, input().split()))[i] for i in range(n)))

