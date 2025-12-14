# ===== ЭКЗАМЕН 1: ЦИКЛЫ (РАЗДЕЛ 8 STEPIK) =====
# Промежуточный экзамен после разделов 7.1-7.10

# Задача 1: Ревью кода-7
def task_1():
    """Решение задачи 1. """
n = int(input())
s = 0
while n > 0:
    if (n % 10) % 2 == 0:
        s += n % 10
    n = n // 10
print(s)


# Задача 2: Ревью кода-8
def task_2():
    """Решение задачи 2."""
n = 8
count = 0
maximum = -10**12
for i in range(1, n + 1):
    x = int(input())
    if x % 4 == 0:
        count += 1
        if x > maximum:
             maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')


# Задача 3: Ревью кода-9
def task_3():
    """Решение задачи 3."""
n = 4
count = 0
maximum = -10**8
for i in range(1, n + 1):
    x = int(input())
    if x % 2 != 0:
        count += 1
        if x > maximum:
            maximum = x
            
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')

# Задача 4: Звездная рамка
def task_4():
    """Решение задачи 4."""
n = int(input())

print('*' * 19)
for i in range(n - 2):
    print('*' + ' '*17 + '*')
if n > 1:
    print('*' * 19)



# Задача 5: Третья цифра
def task_5():
    """Решение задачи 5."""
n = int(input())

while n > 999:
    n = n // 10
else:
    print(n % 10)


# Задача 6: Все вместе 2
def task_6():
    """Решение задачи 6."""
number = int(input())

count_3 = 0
last_digit = number % 10
count_last_digit = 0
count_even_digits = 0
sum_greater_than_5 = 0
product_greater_than_7 = 1
count_0_5 = 0


while number > 0:
    cur_digit = number % 10

    if cur_digit == 3:
        count_3 += 1
    if cur_digit == last_digit:
        count_last_digit += 1
    if cur_digit % 2 == 0:
        count_even_digits += 1
    if cur_digit > 5:
        sum_greater_than_5 += cur_digit
    if cur_digit > 7:
        product_greater_than_7 *= cur_digit
    if cur_digit == 0 or cur_digit == 5:
        count_0_5 += 1

    number //= 10


print(count_3)
print(count_last_digit)
print(count_even_digits)
print(sum_greater_than_5)
print(product_greater_than_7)
print(count_0_5)

# Задача 7 Числа Рамануджана
def task_7():
    """Решение задачи 7."""
for a in range(1, 33):      
     
    for c in range(1, a):          
        
        for d in range(1, c):
            
            for b in range(1, d):
                             
                          
                if a != b and a != c and a != d and a**3 + b**3  == c**3 + d**3:
                    print(a**3 + b**3)

