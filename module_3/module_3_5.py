def get_multiplied_digits(number):   #Напишите функцию get_multiplied_digits и параметр number в ней
    str_number = str(number)         #Создайте переменную str_number и запишите строковое представление(str) числа number в неё
    first=int(str_number[0])         #Основной задачей будет отделение первой цифры в числе: создайте переменную first и запишите в неё первый символ из str_number в числовом представлении(int)
    if len(str_number)>1:            #4 пункт можно выполнить только тогда, когда длина str_number больше 1, т.к. в противном случае не получиться взять срез str_number[1:].
        return first * get_multiplied_digits(int(str_number[1:])) #Возвращайте значение first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first                 #Если же длина str_number не больше 1, тогда вернуть оставшуюся цифру first.
print(get_multiplied_digits(548))
print(get_multiplied_digits(293))
print(get_multiplied_digits(6346))
print(get_multiplied_digits(3))



