# РИМСКИЕ ЦИФРЫ
# На вход программе подаётся целое число. Необходимо преобразовать в римскую цифру 

num = int(input())

a = 'I'
b = 'V'
c = "X"

if 1 <= num <= 10:
    if 1 <= num <= 3:
        print(a * num)
    elif num == 4:
        print(a + b)
    elif 5 <= num <= 8:
        print(b + a * (num - 5))
    elif num == 9:
        print(a + c)
    else:
        print(c)
else:
    print("ошибка")