# ===== STRINGS: BASIC =====
# Stepik 9.7: https://stepik.org/lesson/313439


print("=== Задача 1: Какая следующая буква?")

letter_rus = input()

if ord(letter_rus) == 1071:
    print('Дальше букв нет')
    exit()
else:
    print(chr(ord(letter_rus) + 1))


print("=== Задача 2: Символы в диапазоне")
a, b = int(input()), int(input())

for i in range(a, b + 1):
    print(chr(i), end=' ')


print("=== Задача 3: Простой шифр")
text = input()

for i in text:
    print(ord(i), end=' ')


print("=== Задача 4: Самое тяжёлое слово")
max_sum = 0
max_word = ""

for _ in range(4):  # 4 слова
    word = input()
    current_sum = 0
    
    # Считаем сумму кодов для текущего слова
    for char in word:
        current_sum += ord(char)
    
    # Сравниваем с максимальной
    if current_sum > max_sum:
        max_sum = current_sum
        max_word = word

print(f"Слово с наибольшей суммой кодов: '{max_word}'")
print(f"Сумма его кодов: {max_sum}")


print("=== Задача 5: Стоимость ответа")
message = input()
coins = 0
for i in message:
    coins += (ord(i))

print(f"Текст сообщения: '{message}'", f'Стоимость сообщения: {coins * 3}'+chr(128029), sep = '\n')


print("=== Задача 6: Накручиваем стоимость ответа")
message = input()
cost_old = 0
cost_new = 0
eng_ch = 'eyopaxcETOPAHXCBM'
rus_ch = 'еуорахсЕТОРАНХСВМ'

# 1. Считаем старую стоимость
for i in message:
    cost_old += ord(i) * 3

# 2. Создаём новое сообщение с заменой
new_message = ''
for char in message:
    if char in eng_ch:
        # Находим индекс английской буквы в eng_ch
        index = eng_ch.find(char)  
        # Берём соответствующую русскую букву
        new_message += rus_ch[index]
    else:
        # Если буква не в списке для замены, оставляем как есть
        new_message += char
# 3. Считаем новую стоимость
for char in new_message:
    cost_new += ord(char) * 3

# 4. Вывод
print(f"Старая стоимость: {cost_old}" + chr(128029), f'Новая стоимость: {cost_new}'+chr(128029), sep = '\n')


print("=== Задача 7: Шифр Цезаря")
n = int(input())
code = input()

# 1. Создаём сдвинутый алфавит для ДЕКОДИРОВАНИЯ
alfa = 'abcdefghijklmnopqrstuvwxyz'
shifted_alfa = ''

for char in alfa:
    # Для декодирования сдвигаем ВПРАВО (индекс + n)
    # % 26 обеспечивает цикличность (z → a)
    new_index = (alfa.index(char) + n) % 26
    shifted_alfa += alfa[new_index]

# 2. Декодируем сообщение
decoded_message = ''
for char in code:
    # Находим позицию зашифрованной буквы в сдвинутом алфавите
    index_in_shifted = shifted_alfa.index(char)
    # Берём соответствующую букву из оригинального алфавита
    decoded_message += alfa[index_in_shifted]

print(decoded_message)


print("=== Задача 8: Сбой в системе 1 вариант")
message = input()

#1. Список всех русских кодов
russian_codes = []

#2. Перебираем все коды русских букв
for code in range(1040, 1104):  # от А до я без Ё ё
    # Преобразуем число в строку и добавляем в список
    russian_codes.append(str(code))

for code_str in russian_codes:
    old = f'[u-{code_str}]'
    new = chr(int(code_str))
    message = message.replace(old, new)

print(message)

print("=== Задача 8: Сбой в системе 2 вариант")
message = input()

for i in range(ord('А'), ord('я') + 1):
    message = message.replace(f'[u-{str(i)}]', chr(i))

print(message)