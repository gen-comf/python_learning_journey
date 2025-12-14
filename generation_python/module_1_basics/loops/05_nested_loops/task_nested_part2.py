# ===== WHILE LOOPS: BASIC =====
# Stepik 7.10: https://stepik.org/lesson/298796

print("=== Задача 1: Численный треугольник 2")

n = int(input())
counter = 1

for i in range(1, n + 1):
    for j in range(i):
        print(counter, end=' ')
        counter += 1
    print()


print("=== Задача 2: Численный треугольник 3")
n = int(input())

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end='')
    for j in range(i - 1, 0, -1):
        print(j, end='')
    print()


print("=== Задача 3: Делители-1")
n = int(input())


for i in range(1, n + 1):
    count = 0                   # счетчик делителей числа
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1                           
    print(i, '+' * count, sep='')


print("=== Задача 4: Делители-2")
a, b = int(input()), int(input())
max_sum = 0  # максимальная сумма делителей
best_number = a  # число с максимальной суммой (начальное значение)

for i in range(a, b + 1):
    current_sum = 0                          # сумма делителей ТЕКУЩЕГО числа i

    for j in range(1, i + 1):                # Проверяем все возможные делители от 1 до i
        if i % j == 0:
            current_sum += j                 # суммируем делитель

    if current_sum > max_sum:                    # Сравниваем с максимальной суммой
        max_sum = current_sum
        best_number = i
    elif current_sum == max_sum and i > best_number:       # Если суммы равны, выбираем большее число
        best_number = i

print(best_number, max_sum)


print("=== Задача 5: Цифровой корень")
n = int(input())

while n > 9:                         # пока число больше 9 (больше одной цифры)
    digit_sum =0
    
    while n > 0:                     # Считаем сумму цифр текущего числа
        digit_sum += n % 10
        n = n // 10 
    
    n = digit_sum
   
print(n)    


print("=== Задача 6: Сумма факториалов")
n = int(input())
sum_factor = 0
factorial = 1
for i in range(1, n + 1):
    factorial *= i
    sum_factor += factorial 
    
print(sum_factor)


print("=== Задача 7: Простые числа")