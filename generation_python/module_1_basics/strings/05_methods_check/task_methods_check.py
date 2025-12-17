# ===== STRINGS: BASIC =====
# Stepik 9.4: https://stepik.org/lesson/303084

print("=== Задача 1: Плохие комментарии")

n = int(input())

for i in range(1, n + 1):
    comment = input()
    
    if comment == "" or comment.isspace():
        print(str(i) + ':', "COMMENT SHOULD BE DELETED")     
    else:
        print(str(i) + ':', comment)


print("=== Задача 2: Проверь никнейм")
nick_name = input()

if (nick_name[0] == '@' and 
    5 <= len(nick_name) <=15 and 
    nick_name[1:].isalnum() and 
    nick_name[1:] == nick_name[1:].lower()):

    print("Correct")
else:
    print("Incorrect")


print("=== Задача 3: Автомобильный номер ")
auto_number = input()
letters = "АВЕКМНОРСТУХ"

if len(auto_number) not in (9, 10):             # 1. Проверка общей длины
    print("NO")
    exit()

part1 = auto_number[:7]
part2 = auto_number[7:]

if not part2.isdigit() or len(part2) not in (2, 3):         # 2. Проверка part2 (цифровая часть)
    print("NO")
    exit()

if not (part1.endswith('_') and                            # 3. Проверка part1 (буквенно-цифровая часть с _)
    len(part1) == 7 and
    part1[0] in letters and
    part1[1:4].isdigit() and
    part1[4:6].isalpha() and
    all(char in letters for char in part1[4:6])):

    print("NO")
    exit()

print("YES")      




    