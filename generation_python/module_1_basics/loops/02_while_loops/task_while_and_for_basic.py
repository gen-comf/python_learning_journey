# ===== WHILE LOOPS: BASIC =====
# Stepik 7.6: https://stepik.org/lesson/265122/step/1?unit=246071

print("=== Задача 1: Обратный порядок 1")
num = int(input())
while num > 0:
    last_digit = num % 10
    print(last_digit)
    num //= 10


print("=== Задача 2: Обратный порядок 2")
num = int(input())
while num > 0:
    last_digit = num % 10
    print(last_digit, end="")
    num //= 10


print("=== Задача 3: max и min")
num = int(input())
min_num = 9
max_num = 0
while num > 0:
    last_digit = num % 10
    if last_digit > max_num:
        max_num = last_digit
    if last_digit < min_num:
        min_num = last_digit
    num //= 10

print("Максимальная цифра равна", max_num)
print("Минимальная цифра равна", min_num)


print("=== Задача 4: Все вместе")
n = int(input())
total = 0
product = 1
number_of_digit = len(str(n))
first_digit = n // 10 ** (number_of_digit - 1)
last_digit = n % 10
sum1 = first_digit + last_digit

while n != 0:
    x_digit = n % 10
    total += x_digit
    product *= x_digit
    mean = total / number_of_digit
    n = n // 10

print(total, number_of_digit, product, mean, first_digit, sum1, end="\n")


print("=== Задача 5: Вторая цифра")
n = int(input())  # n > 9
number_of_digit = len(str(n))
second_digit = (n // 10 ** (number_of_digit - 2)) % 10
print(second_digit)

print("=== Задача 6: Одинаковые цифры")
num = int(input())  # натуральное число ≥ 1
sample = num % 10  # берём последнюю цифру как образец
all_same = True

temp = num
while temp > 0:
    if temp % 10 != sample:
        all_same = False
        break
    temp //= 10

print("YES" if all_same else "NO")


print("=== Задача 7: Четные цифры")
n = int(input())
count = 0  # счётчик чётных цифр

for i in range(len(str(n)) - 1, -1, -1):  # Проходим по цифрам слева направо
    digit = (n // (10**i)) % 10  # Получаем текущую цифру (слева направо)

    if digit % 2 == 0:
        count += 1
        print(str(count) + "-я четная цифра равна " + str(digit))

if count == 0:
    print("Четных цифр в числе нет")

print("=== Задача 8: Упорядоченные цифры")

n = int(input())
prev_digit = n % 10  # Берём последнюю цифру как предыдущую
temp = n // 10  # убираем уже обработанную цифру
flag = True

while temp > 0:
    current_digit = temp % 10
    if (
        current_digit < prev_digit
    ):  # Сравниваем текущую цифру с предыдущей # текущая д/б >= предыдущей
        flag = False
        break

    prev_digit = current_digit
    temp //= 10

print("YES" if flag else "NO")
