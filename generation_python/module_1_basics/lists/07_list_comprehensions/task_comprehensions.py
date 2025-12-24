# ===== STRINGS: BASIC =====
# Stepik 11.7: https://stepik.org/lesson/326725

print("=== Задача 1: Палиндром")
palindromes = [number for number in range(100,1000) if str(number) == str(number)[::-1]]

print(palindromes)


print("=== Задача 2: Списочное выражение 1")
res = [i**2 for i in range(1, int(input()) + 1)]

for el in res:
    print(el)


print("=== Задача 3: Списочное выражение 2")
res = [int(el) ** 3 for el in input().split()]

for kub in res:
    print(kub, end=' ')
    # или print(*kub)


print("=== Задача 4: В одну строку 1")
res = [word for word in input().split()]
print(*res, sep='\n')


print("=== Задача 5 В одну строку 2")
res = [el for el in input() if el in '1234567890']
print(*res, sep='')


print("=== Задача 6 В одну строку 3")
kvad = [int(el)**2 for el in input().split() 
        if int(el) % 2 == 0 and (int(el)**2) % 10 != 4]

print(*kvad)