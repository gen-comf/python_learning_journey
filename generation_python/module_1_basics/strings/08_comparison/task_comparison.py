# ===== STRINGS: BASIC =====
# Stepik 9.8: https://stepik.org/lesson/1402735

print("=== Задача 1: Волшебное число")

min_word = max_word = input()

#1. Находим минимальную и максимальную строки
for _ in range(3):
    words = input()
    if words < min_word:
        min_word = words
    if words > max_word:
        max_word = words


2#. находим произведение последних символов строк и возводим произведение в квадрат
magic_number = (ord(min_word[-1]) * ord(max_word[-1]))**2
print(f'{magic_number}')


print("=== Задача 2: Строковые минимум и максимум")
text = maxi_str = mini_string = input()

while text != "КОНЕЦ":
    text = input()
    if text == "КОНЕЦ":
        break  # Выходим из цикла
    if text > maxi_str:
        maxi_str = text
    if text < mini_string:
        mini_string = text

print(f'Минимальная строка ⬇️: {mini_string}')
print(f'Максимальная строка ⬆️: {maxi_str}')


print("=== Задача 3: Необычное сравнение")
str_a, str_b = input(), input()

#1. приводим строки к одному виду
new_a = str_a.lower()
new_b = str_b.lower()

#2. оставляем только буквы
letter1 = ''
for char in str_a.lower():
    if  'a' <= char <= 'z' or 'а' <= char <= 'я':
        letter1 += char


letter2 = ''
for char in str_b.lower():
    if  'a' <= char <= 'z' or 'а' <= char <= 'я':
        letter2 += char

#3. Сравниваем новые строки
if letter2 == letter1:
    print("YES")
else:
    print("NO")


print("=== Задача 4: Сортируем слова")
word1, word2, word3 = input(), input(), input()

first = min(word1, word2, word3)
third = max(word1, word2, word3)

if word1 != first and word1 != third:
    second = word1
elif word2 != first and word2 != third:
    second = word2
else:
    second = word3

print(first, second, third, end=' ')


print("=== Задача 5: Название класса")
n = int(input())
digits = '0123456789'
alfa = 'АБВГДЕЖЗИЙКЛМНОП'
output = ''

for _ in range(n):
    cl = input()
     
    if len(cl) == 2 and cl[0] in digits and cl[1] in alfa:
        print("YES")
    else:
        print("NO")


print("=== Задача 6: Порядок книг")
n = int(input())
book_1 = input()      
flag = True
# 1. Обрабатываем первую книгу                                                   
book_1_temp = book_1[:book_1.find(' ')] + book_1[book_1.find(',') + 2:]     

# 2. Обрабатываем остальные книги
for i in range(n - 1):
    book_next = input()
    book_next_temp = book_next[:book_next.find(' ')] + book_next[book_next.find(',') + 2:]
   
    # Если следующая книга МЕНЬШЕ предыдущей → порядок нарушен
    if book_next_temp < book_1_temp:       
        flag = False                             
        break
    # Иначе обновляем предыдущую книгу для следующего сравнения
    book_1_temp = book_next_temp 

if flag:
    print("YES")
else:
    print("NO")
