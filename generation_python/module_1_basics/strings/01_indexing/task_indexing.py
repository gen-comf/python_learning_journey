# ===== STRINGS: BASIC =====
# Stepik 9.1: https://stepik.org/lesson/284101

print("=== Задача 1: В столбик 1")

s = input()
for i in range(len(s)):
    if i % 2 == 0:
        print(s[i])


print("=== Задача 2: В столбик 2")
s = input()
len_1 = len(s)
for i in range(len(s)-1, -1, -1):
    print(s[i])


print("=== Задача 3: ФИО")
first_name = input()
last_name = input()
middle_name = input()

initials = last_name[0] + first_name[0] + middle_name[0]

print(initials)


print("=== Задача 4: Цифра 1")
s = input()
total = 0
for i in range(len(s)):
    total += int(s[i])

print(total)


print("=== Задача 5: Цифра 2")
s = input()
digits = ('0123456789')
for i in range(len(s)):
    if s[i] in digits:
        print('Цифра')
        break
else:
    print('Цифр нет')


print("=== Задача 6: Сколько раз?")   
s = input()
n = '+'
m = '*'
total_n = 0
total_m = 0

for i in range(len(s)):
    if s[i] in n:
        total_n +=1
    if s[i] in m:
        total_m +=1

print('Символ + встречается', total_n, 'раз')
print('Символ * встречается', total_m, 'раз')


print("=== Задача 7: Одинаковые соседи")   
s = input()
total = 0

for i in range(0, len(s)-1):
    if s[i] == s[i + 1]:
        total += 1
print(total)


print("=== Задача 8: Гласные и согласные")  
s = input().lower()
a = 'ауоыиэяюе'
b = 'бвгджзйклмнпрстфхцчшщ'
total_a= 0
total_b= 0

for i in range(len(s)):
    
    if s[i] in a:
        total_a += 1
    
    if s[i] in b:
        total_b += 1
    

print('Количество гласных букв равно', total_a)
print('Количество согласных букв равно', total_b)


print("=== Задача 9: Decimal to Binary 10")  
n = int(input())
s =""
while n  > 0:           #Преобразование десятичных чисел в двоичные
    s += str(n % 2)
    n = n//2
reversed_s = s[::-1]    #записываем строку наоборот
print(reversed_s)