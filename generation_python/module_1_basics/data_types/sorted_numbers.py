# Сортировка трёх
# На вход программе подаются три целых числа, каждое на отдельной строке.
# Программа должна вывести три числа, каждое на отдельной строке, упорядоченных от большего к меньшему.
# Примечание. Учитывайте, что числа могут быть равны.

x1, x2, x3 = int(input()), int(input()), int(input())

# Находим min и max число, а также среднее число
max_number = max(x1, x2, x3)
min1_number = min(x1, x2, x3) 
middle_number = x1 + x2 + x3 - max_number - min1_number

print(max_number, middle_number, min1_number, sep='\n')

