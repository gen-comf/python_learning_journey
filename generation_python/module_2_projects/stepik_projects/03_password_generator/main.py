#!/usr/bin/env python3
"""
Проект 3: Генератор безопасных паролей

Программа генерирует заданное количество паролей и включает в себя умную настройку 
на длину пароля, а также на то, какие символы требуется в него включить, а какие исключить.
"""
#функция проверка на дурака TODO

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
similar_symbol = 'il1Lo0O'

#1. 
import random
def generate_password(length, chars):
    
    """Генерирует пароль из выбранных символов и заданной длиной."""
    chars = random.sample(chars, length)
    return ''.join(chars)

#2. 
def get_password_settings():
    """Получает настройки и ВОЗВРАЩАЕТ набор символов."""
    print("=== НАСТРОЙКИ ПАРОЛЯ ===")
    
    # Запрашиваем параметры
    pwd_quantity = int(input('Сколько паролей вам нужно сгенерировать? '))
    pwd_len = int(input('Какой длины должен быть пароль(рекомендуемая длина не менее 8)?  '))
    while pwd_len < 8:
        pwd_len = int(input('Введите длину не менее 8)?  '))
    
    # Собираем символы
    chars = ''
    if input('Включать ли в пароль цифры от 0 до 9? (y/n): ').lower() == 'y':
        chars += digits
    if input('Включать ли в пароль прописные буквы? (y/n): ').lower() == 'y':
        chars += uppercase_letters
    if input('Включать ли в пароль строчные буквы? (y/n): ').lower() == 'y':
        chars += lowercase_letters
    if input('Включать ли в пароль символы "!#$%&*+-=?@^_"? (y/n): ').lower() == 'y':
        chars += punctuation
    if input('Исключать ли неоднозначные символы "il1Lo0O"? (y/n): ').lower() == 'y':
        for i in similar_symbol:
            chars = chars.replace(i, '')

    
    if not chars:
        print("\n⚠ Вы не выбрали ни одного типа символов!")
        print("Добавляю цифры по умолчанию.")
        chars = digits

    # Возвращаем параметры для генерации
    return {
        'quantity': pwd_quantity,
        'length': pwd_len,
        'chars': chars
    }


#3. Основная программа
settings = get_password_settings()

# Проверяем, что символы есть
if not settings['chars']:
    print("Ошибка: не выбрано ни одного типа символов!")
else:
    print("\n=== ВАШИ ПАРОЛИ ===")
    for i in range(settings['quantity']):
        password = generate_password(settings['length'], settings['chars'])
        print(f"{i+1}. {password}")
