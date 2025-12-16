# ===== STRINGS: BASIC =====
# Stepik 9.3: https://stepik.org/lesson/296416



print("=== Задача 1: Заглавные буквы")
s = input()
if s != s.title():
    print("NO")
else:
    print("YES") 


print("=== Задача 2: sWAP cASE")
s = input()
s = s.swapcase()
print(s)


print("=== Задача 3: Хороший оттенок")
s = input().lower()
if 'хорош' in s:
    print("YES")
else:
    print("NO") 


print("=== Задача 4: Нижний регистр")
s = input()
total = 0
for i in s:
    if i != i.upper():
        total += 1
print(total) 

print("=== Задача 4.1: Нижний регистр")
s = input()
s_alfa = 'abcdefghijklmnopqrstuvwxyz'
total = 0
for i in range(len(s)):
    if s[i] in s_alfa:
        total += 1
print(total)
