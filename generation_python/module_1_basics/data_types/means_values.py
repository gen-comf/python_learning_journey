from math import sqrt
a, b = float(input()), float(input())

arithmetic_mean = (a + b) / 2                   # Среднее арифметическое
geometric_mean = sqrt(a * b)                    # Среднее геометрическое  
harmonic_mean = (2 * a * b) / (a + b)           # Среднее гармоническое
quadratic_mean = sqrt((a ** 2 + b ** 2) / 2)    # Среднее квадратичное

print(arithmetic_mean)
print(geometric_mean)
print(harmonic_mean)
print(quadratic_mean)