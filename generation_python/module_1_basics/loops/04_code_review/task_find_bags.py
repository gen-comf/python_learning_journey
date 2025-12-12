# ===== WHILE LOOPS: BASIC =====
# Stepik 7.8: https://stepik.org/lesson/311433/step/13?unit=293861

print("=== Задача 1: Ревью кода-1")
n = int(input())
product = 1
while n > 0:
    digit = n % 10
    product = product * digit
    n = n // 10
print(product)


print("=== Задача 1: Ревью кода-2")
n = int(input())
while n >= 10:
    n = n // 10
print(n)


print("=== Задача 1: Ревью кода-3")
s = 0
for i in range(1, 8):
    n = int(input())
    if n % 2 == 0:
        s += n
print(s)


print("=== Задача 1: Ревью кода-4")
count = 0
p = 1
for _ in range(1, 11):
    x = int(input())
    if x >= 0:
        p = p * x
        count += 1
if count != 0:
    print(count)
    print(p)
else:
    print('NO')


print("=== Задача 1: Ревью кода-5")
n = int(input())
max_digit = 0                   
count = - 1                        
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        count += 1                 
        if digit > max_digit:        
            max_digit = digit                         
    n = n // 10                      
if count < 0 :                         
    print('NO')
else:
    print(max_digit)


print("=== Задача 1: Ревью кода-6")
max_digit = - 1000000                    
total = 0 
for _ in range(1, 11):
    x = int(input())
    if x < 0:
        total += x                
        if x > max_digit:
            max_digit = x
if max_digit == - 1000000:
    print("NO")
else:
    print(total)
    print(max_digit)
