# Задача "Нули ничто, отрицание недопустимо!":
# Дан список чисел [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# Нужно выписывать из этого списка только положительные числа до тех пор, пока не встретите отрицательное или
# не закончится список (выход за границу).
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
_index = 0
while _index <= len(my_list) and my_list[_index] >= 0: #или вместо второго условия использовать 11, 12 строки (но так короче)
    if my_list[_index] == 0:
        _index = _index + 1
        continue
    #elif my_list[_index] < 0:
    #    break
    print(my_list[_index])
    _index = _index + 1
