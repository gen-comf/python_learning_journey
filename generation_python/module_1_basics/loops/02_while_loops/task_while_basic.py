# ===== WHILE LOOPS: BASIC =====
# Stepik 7.4: https://stepik.org/lesson/265121/step/1

print("=== Задача 1: До КОНЦА 1")
word = input()

while word != "КОНЕЦ":
    print(word)
    word = input()

print("=== Задача 2: До КОНЦА 2")
word = input()

while word != "КОНЕЦ" and word != "конец":
    print(word)
    word = input()

print("=== Задача 3: Количество членов")
word = input()
total = 0
while word != "стоп" and word != "хватит" and word != "достаточно":
    total += 1
    word = input()
print(total)

print("=== Задача 4: Пока делимся")
num = int(input())

while num % 7 == 0:
    print(num)
    num = int(input())

print("=== Задача 5: Сумма чисел")
num = int(input())
total = 0

while num >= 0:
    total += num
    num = int(input())
print(total)

print("=== Задача 6: Количество пятерок 5")
num = int(input())
score = 0

while 5 >= num > 0:
    if num == 5:
        score += 1
    num = int(input())
print(score)

print("=== Задача 7: Первый никнейм")
nickname = input()
while "_" in nickname:
    nickname = input()
print(nickname)

print("=== Задача 8: Сколько ждать?")
count = 0
start_counting = False

name = input()
while name != "Левон":
    if name == "Александра":
        start_counting = True
    elif start_counting:
        count += 1
    name = input()

print(count)

print("=== Задача 9: Ведьмаку заплатите чеканной монетой")
price = int(input())
total_coins = 0

while price >= 25:
    price -= 25
    total_coins += 1
while price >= 10:
    price -= 10
    total_coins += 1
while price >= 5:
    price -= 5
    total_coins += 1
while price >= 1:
    price -= 1
    total_coins += 1
print(total_coins)
