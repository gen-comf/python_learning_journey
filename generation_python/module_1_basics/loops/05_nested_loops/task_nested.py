# ===== WHILE LOOPS: BASIC =====
# Stepik 7.9: https://stepik.org/lesson/298795

print("=== Задача 1: Таблица - 1")
n = int(input())
for i in range(n):
    print(str(n), end=' ')
    for j in range(2):
        print(str(n), end=' ')
    print()


print("=== Задача 2: Таблица - 2")
n = int(input())
for i in range(1, n + 1):
    for j in range(1, 5):
        print(i, end=' ')
    print()


print("=== Задача 3: Таблица - 3 (сложение)")
n = int(input())
for i in range(1, n + 1):
    for j in range(1, 10):
        print(i, '+', j, '=', i + j, end='\n')
    print()


print("=== Задача 4: Звездный треугольник")
n = int(input())

middle = (n + 1) // 2               # длина самой длинной строки

for i in range(1, middle + 1):
    print("*" * i)
for i in range(middle - 1, 0, - 1):
    print("*" * i)


print("=== Задача 5: Численный треугольник 1")
n = int(input())

for i in range(1, n + 1):
    for j in range(i):
        print(i, end='')
    print()


print("=== Задача 6: 12 месяцев")
for n in range(1, 14):
    for k in range(1, 13):
        for m in range(1, 12):
            if 28 * n + 30 * k + 31 * m == 365:
                total += 1
                print('n =', n, 'k =', k, 'm =', m)
print('Общее количество натуральных решений =', total)


print("=== Задача 7: Старинная задача")
sum = 100
head = 100

for bull in range(1, 101):              
    for cow in range(1, 101):          
        for calf in range(1, 101):     
            if 10 * bull + 5 * cow + 0.5 * calf == sum:
                if bull + cow + calf == head:
                    print('bull =', bull, 'cow =', cow, 'calf =', calf)


print("=== Задача 8:Гипотеза Эйлера о сумме степеней")
for a in range(1, 151):      
    a5 = a ** 5        
    for b in range(a, 151):          
        b5 = b ** 5
        for c in range(b, 151):
            c5 = c ** 5
            for d in range(c, 151):
                d5 = d ** 5
                
                total = a5 + b5 +c5 +d5
                e = int(total ** 0.2)
                if e <= 150 and e ** 5 == total:
                        print(a+ b + c + d + e)