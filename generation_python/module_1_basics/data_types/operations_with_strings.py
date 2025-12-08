# 1) "Python is a great language!", said Fred. "I don't ever remember having this much fun before."
#str1 = str('"Python is a great language!", said Fred. ')
#str2 = str('"I don' + "'" + 't ever remember having this much fun before."')

#print(str1 + str2)

# 2) Напишите программу, которая считывает с клавиатуры две строки – имя и фамилию пользователя –
# и выводит фразу: Hello <введённое имя> <введённая фамилия>! You have just delved into Python.
#  На вход программе подаются две строки (имя и фамилия), каждая на отдельной строке.

#first_name = str(input())
#second_name = str(input())

#print('Hello ' + first_name + ' ' + second_name + '!' + ' ' + 'You have just delved into Python')

# Футбольная команда
# Напишите программу, которая считывает с клавиатуры название футбольной команды и выводит информацию о ней 
# в следующем формате: Футбольная команда <название футбольной команды> имеет длину 
# <длина названия футбольной команды> символов

#football_team = str(input())

#len_team = str(len(football_team))

#print('Футбольная команда' + ' ' + football_team + ' ', 'имеет длину' + ' ' + len_team + ' ' + 'символов')


# Три города
# Даны названия трёх городов. Напишите программу, которая определяет самое короткое и самое длинное 
# название города. На вход программе подаются названия трёх городов, каждое на отдельной строке.
# Программа должна вывести самое короткое и длинное название города, каждое на отдельной строке.

city1 = str(input())
city2 = str(input())
city3 = str(input())

x = min(len(city1), len(city2), len(city3))
y = max(len(city1), len(city2), len(city3))

if x == len(city1):
    print(city1)
elif x == len(city2):
    print(city2)
else:
    print(city3)

if y == len(city1):
    print(city1)
elif y == len(city2):
    print(city2)
else:
    print(city3)
