# ===== ЭКЗАМЕН 1: Списки (РАЗДЕЛ 12 STEPIK) =====
# Промежуточный экзамен после разделов 11.1-11.8 https://stepik.org/lesson

print("=== Задача 1: Список чётных вариант 1")
res = []
n = int(input())
for i in range(1, n+1):
    if i % 2 == 0:
        res.append(i)
print(res)


print("=== Задача 1: Список чётных вариант 2")
print([el for el in range(1, int(input()) + 1) if el % 2 == 0 ])


print("=== Задача 2: Сумма двух списков вариант 1")
L = list(map(int, input().split()))
M = list(map(int, input().split()))

res = []

for i in range(len(L)):
    res.append(L[i] + M[i])

print(*res)

print("=== Задача 2: Сумма двух списков вариант 2")
L = input().split()
M = input().split()

print(*[int(L[i]) + int(M[i]) for i in range(len(L))])


print("=== Задача 3: Сумма чисел")
text = input().split()
res = []

for i in range(len(text)):
    res.append(int(text[i]))
    x = sum(res)
    
print("+".join(text) + '=', x, sep='')


print("=== Задача 4: Валидный номер 📞🌶️🌶️")
s = input()

parts = s.split('-')    

# Вариант 1: abc-def-hijk (3 части)
if len(parts) == 3:
     # Проверяем длины частей (parts[0] = abc ...)
    if len(parts[0]) == 3 and len(parts[1]) == 3 and len(parts[2]) == 4:
        # Проверяем, что все части состоят только из цифр
        if parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit():
            print("YES")
        else:
            print("NO")
    else:
        print("NO")    
    

# Вариант 2: 7-abc-def-hijk (4 части)
elif len(parts) == 4:
    # Проверяем: первая часть должна быть '7'
    if parts[0] == '7':
        # Проверяем длины остальных частей
        if len(parts[1]) == 3 and len(parts[2]) == 3 and len(parts[3]) == 4:
            # Проверяем, что все части состоят только из цифр
            if parts[1].isdigit() and parts[2].isdigit() and parts[3].isdigit():
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    else:
        print("NO")
# Любое другое количество частей - неправильно
else:
    print("NO")

print("=== Задача 4: Валидный номер Вариант 2📞🌶️🌶️")
seq = input().split("-")
lens = [len(el) for el in seq]

if lens == [1, 3, 3, 4] and "".join(seq).isdigit() and seq[0] == "7":
    print("YES")
elif lens == [3, 3, 4] and "".join(seq).isdigit():
    print("YES")
else:
    print("NO")


print("=== Задача 5: Самый длинный ↔️")
res = [len(word) for word in input().split()]
print(max(res))


print("=== Задача 6: Молодёжный жаргон 👦")
print(*[word[1:] + word[0] + 'ки' for word in input().split()])