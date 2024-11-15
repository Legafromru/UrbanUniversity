'''В true_math создайте функцию divide, которая принимает два параметра first и second.
Функция должна возвращать результат деления first на second, но когда в second записан 0 - возвращать бесконечность.
Бесконечность можно импортировать из встроенной библиотеки math (from math import inf)'''
from math import inf
def divide (a,b):
    if b != 0:
        c = a / b
        return c
    else:
        return inf
