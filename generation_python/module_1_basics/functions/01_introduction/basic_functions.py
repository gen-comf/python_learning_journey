# 1. Самая простая функция
def say_hello():
    """Функция без параметров"""
    print("Привет! Это мой первый опыт с функциями в Python.")

# Вызов функции
say_hello()

# 2. Функция с параметром
def greet(name):
    """Функция с одним параметром"""
    print(f"Добро пожаловать, {name}!")

# Вызов с аргументом
greet("gen-comf")

# 3. Функция с возвратом значения
def add(a, b):
    """Функция с двумя параметрами и возвратом значения"""
    result = a + b
    return result

# Использование возвращаемого значения
sum_result = add(5, 3)
print(f"5 + 3 = {sum_result}")

# 4. Встроенные функции, которые вы уже знаете
numbers = [1, 2, 3, 4, 5]
print(f"Длина списка: {len(numbers)}")
print(f"Сумма элементов: {sum(numbers)}")
print(f"Максимальное значение: {max(numbers)}")


print("=== Задача 1: Звёздный прямоугольник 1")
def draw_box():
    rows = 14
    cols = 10

    for i in range(rows):
        if i == 0 or i == rows - 1:
            # Верхняя и нижняя границы
            print('*' * cols)
    
        else:
            # Боковые границы с пробелами внутри
            print('*' + ' ' * (cols-2) + '*')




print("=== Задача 2: Звёздный триугольник 1")
def draw_triangle():
    katet = 10

    for i in range(1, katet + 1):
        print('*' * i)
    print()