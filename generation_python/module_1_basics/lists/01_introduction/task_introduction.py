# ===== STRINGS: BASIC =====
# Stepik 11.1: https://stepik.org/lesson/324750

print("=== Задача 1: Список чисел")

n = int(input())
x = list(range(1, n + 1))

print(x)


print("=== Задача 2: Список букв")

n = int(input())  
alphabet = 'abcdefghijklmnopqrstuvwxyz'
result = list(alphabet[:n])  # Берем первые n букв и преобразуем в список
print(result)


print("=== Задача 3: Список нечётных чисел")
n = int(input())
odd_digits = list(range(1, n + 1, 2))
print(odd_digits)


print("=== Задача 4:  Каждый второй предмет")
things = input()
result = []
for i in range(0, len(things), 2):
    result.append(things[i])

print(list(result))