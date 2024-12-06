from math import sqrt
import datetime
try:
    num = int(input("""Введите число для нахождения квадратного корня
>>> """))
    print(sqrt(num))
except ValueError:
    print("Введеное значение не является числом")
print("Текущее время:", datetime.datetime.now())