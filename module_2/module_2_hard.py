'''Во вторую вставку нужно было написать те пары чисел друг за другом, чтобы число из первой вставки было кратно
(делилось без остатка) сумме их значений.
Пример кратности(деления без остатка):
1 + 2 = 3 (сумма пары)
9 / 3 = 3 (ровно 3 без остатка)
9 кратно 3 (9 делится на 3 без остатка)
Пример 1:
9 - число из первой вставки
1218273645 - нужный пароль (1 и 2, 1 и 8, 2 и 7, 3 и 6, 4 и 5 - пары; число 9 кратно сумме каждой пары)
Составьте алгоритм, используя циклы, чтобы в независимости от введённого числа n (от 3 до 20) программа выдавала нужный
пароль result, для одного введённого числа.
11 - число из первой вставки
11029384756 - нужный пароль (1 и 10, 2 и 9, 3 и 8, 4 и 7, 5 и 6 - пары; число 11 кратно сумме каждой пары)'''
result = ''
namber = int(input('Введите число от 3 до 20 '))
for i in range(1, namber):
    for j in range(i+1, namber):
        if namber % (i + j) == 0:
            result += str(i) + str(j)
print('Нужный Вам пароль -', result)
