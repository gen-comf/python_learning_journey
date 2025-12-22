# ===== STRINGS: BASIC =====
# Stepik 11.5: https://stepik.org/lesson/324755

print("=== Задача 1: Инициалы")
fio = input().split()
res = []

for i in range(len(fio)):
    res.append(fio[i][0])

print('.'.join(res), end='.')


print("=== Задача 2: Windows OS")
file_path = input().split('\\')
print(*file_path, sep='\n')          


print("=== Задача 3: Диаграмма")
num = input().split()          # 1 2 3 4 5 строка      
numbers = []
for i in range(len(num)):       # преобразуем в список с целыми числами [1, 2, 3, 4, 5]
    numbers.append(int(num[i]))

plus = []    
for el in numbers:
    plus.append('+' * el)

print(*plus, sep=('\n'))


print("=== Задача 4: Корректный ip-адрес")
ip_adres = input().split('.')

if len(ip_adres) != 4:
    print("НЕТ")
else:
    is_valid = True


    for s in ip_adres:
        if 255 < int(s)  or int(s) < 0:
            is_valid = False
            break

if is_valid:
    print("ДА")
else:
    print("НЕТ")


print("=== Задача 5: Добавь разделитель")
s = input()
separator = input()
res = separator.join(s)

print(res)


print("=== Задача 6: Количество совпадающих пар")
# Ввод и преобразование
str_input = input().split()
numbers = []
for s in str_input:
    numbers.append(int(s))

# Подсчет пар
pair_count = 0
n = len(numbers)

# i идет от 0 до предпоследнего элемента
for i in range(n - 1):
    # j идет от следующего после i до последнего
    for j in range(i + 1, n):
        if numbers[i] == numbers[j]:
            pair_count += 1

print(pair_count)
