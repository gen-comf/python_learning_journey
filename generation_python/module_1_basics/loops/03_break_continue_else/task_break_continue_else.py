# ===== WHILE LOOPS: BASIC =====
# Stepik 7.7: https://stepik.org/lesson/298794/step/1?unit=280621

print("=== Задача 1: Наименьший делитель")
n = int(input())

for i in range(2, n + 1):
    if n % i == 0:
        print(i)
        break


print("=== Задача 2: Следуй правилам")

n = int(input())

for i in range(1, n + 1):
    if 5 <= i <= 9:
        continue
    if 17 <= i <= 37:
        continue
    if 78 <= i <= 87:
        continue
    print(i)
