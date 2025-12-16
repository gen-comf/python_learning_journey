# ===== STRINGS: BASIC =====
# Stepik 9.4: https://stepik.org/lesson/303083



print("=== Задача 1: Количество слов")
text = input()
print(text.count(" ") + 1)


print("=== Задача 2: Минутка генетики")
text = input().upper()

print('Аденин:', text.count('А'))
print('Гуанин:', text.count('Г'))
print('Цитозин:', text.count('Ц'))
print('Тимин:', text.count('Т'))


print("=== Задача 3: Очень странные дела")
n = int(input())
message_Odi = 0
for _ in range(0, n):
    text = input()
    if text.count('11') == 3:
        message_Odi += 1

print(message_Odi)


print("=== Задача 4: Количество цифр")

text = input()
text_1 = text
for digits in '0123456789':
    text_1 = text_1.replace(digits, '')

print(len(text) - len(text_1))


print("=== Задача 5: .com or .ru")
text = input()
if text.endswith('.com') or text.endswith('.ru'):
    print("YES")
else:
    print("NO")



print("=== Задача 7: Первое и последнее вхождение")
text = input()

if text.count("f") == 0:
    print("NO")
elif text.count("f") == 1:
    print(text.find('f'))
else:
    print(text.find('f'), text.rfind('f'))


print("=== Задача 8: Удаление фрагмента")
text = input()

text_1 = text[0:text.find('h')] + text[text.rfind('h') + 1:]
      
print(text_1)
