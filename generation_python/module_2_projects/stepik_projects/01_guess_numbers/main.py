#!/usr/bin/env python3
"""
Угадайка чисел

Игра, где компьютер загадывает число, а пользователь угадывает.
"""
# 1. вспомогательная функция которая находит наименьшее число попыток для угадывания числа от [1, n]
def calculate_min_attempts(n):
    if n <= 1:
        return 1
    
    attempts = 0 

    while n > 0:
        attempts += 1
        n //= 2             # делим диапазон пополам

    return attempts   
# считываем данные
#n = int(input())
# вызываем функцию
#attempts = calculate_min_attempts(n)
#print(attempts)


# 2. Вспомогательная программа проверки корректности введенных данных
def is_valid(s):
    # Убираем пробелы в начале и конце
    s = s.strip()                  
    # Пустая строка или не только цифры
    if not s or not s.isdigit():
        return False

    # Проверяем диапазон
    num = int(s)
    return 1 <= num <= 100
       
# считываем данные
#s = input()
# вызываем функцию
#print(is_valid(s))



# Компьютер загадывает число
import random
secret_number = random.randint(1, 100)
# Инициализируем счётчик попыток
attempts = 0
print("Добро пожаловать в числовую угадайку")
      
while True:
    print("Введите число от 1 до 100")
    s = input()
    # Проверяем корректность
    if is_valid(s):
        # Преобразуем в число
        user_number = int(s)
        # можно добавить счетчик введенных попыток
        attempts += 1

        # Проверяем угадал ли
        if user_number < secret_number:
            print('Ваше число меньше загаданного, попробуйте еще разок')                
            
        elif user_number > secret_number:
            print('Ваше число больше загаданного, попробуйте еще разок')
            
        else:
            print(f'Вы угадали, поздравляем! Число попыток: {attempts}')    
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            # предлагаем сыграть еще раз
            play_again = input("\nХотите сыграть еще? (да/нет): ")
            if play_again.lower() != 'да':
                print("Спасибо за игру!")
                break   # Выход из основного цикла игры
            else:
                # Перезапускаем игру
                print("\n" + "="*50)
                print("Новая игра!")
                print("="*50)
                secret_number = random.randint(1, 100)  # Новое число
                attempts = 0  # Сброс счётчика
                continue                          

    else:
        print('А может быть все-таки введем целое число от 1 до 100?')
        


