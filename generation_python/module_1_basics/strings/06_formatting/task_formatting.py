# ===== STRINGS: BASIC =====
# Stepik 9.6: https://stepik.org/lesson/1209103

print("=== Задача 1: Курсы валют")
# На <дата>: 1€ = <курс евро>₽, 1¥ = <курс юаня>₽

data = input()
rate_e = input()
rate_y = input()

print(f'На {data}: 1€ = {rate_e}₽, 1¥ = {rate_y}₽')


print("=== Задача 2: Сумма кубов 🆚 Куб суммы")
a, b = int(input()), int(input())

total_3 = a**3 + b**3
sum_3 = (a + b)**3

print(f'Для чисел {a} и {b}:')
print(f'  Сумма кубов: {a}**3 + {b}**3 = {total_3}')
print(f'  Куб суммы: ({a} + {b})**3 = {sum_3}')


print("=== Задача 3: (Не) Активное похудение")
day_number = int(input())
current_weight = float(input())

norm_weight_loss = float(100 - day_number*0.2)


if norm_weight_loss >= current_weight:
    print("Все идет по плану")
    print(f'# {day_number}: ТЕКУЩИЙ ВЕС = {current_weight}, ЦЕЛЬ по ВЕСУ = {norm_weight_loss}')
else:
    print("Что-то пошло не так")
    print(f'# {day_number}: ТЕКУЩИЙ ВЕС = {current_weight}, ЦЕЛЬ по ВЕСУ = {norm_weight_loss}')