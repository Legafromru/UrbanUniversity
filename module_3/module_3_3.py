def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params() #Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
print_params(1, 2)
print_params(1, 2, 7)
print_params(b = 25) #Проверьте, работают ли вызовы => работают
print_params(c = [1,2,3])

values_list = (1, 'fr', False) #Создайте список values_list с тремя элементами разных типов.
values_dict = {'a':True, 'b':'abcd', 'c':777 } #Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params, и значениями разных типов.
print_params(*values_list) #Передайте values_list и values_dict в функцию print_params, используя распаковку параметров (* для списка и ** для словаря).
print_params(**values_dict)

values_list_2 = (1, 'gt') #Создайте список values_list_2 с двумя элементами разных типов
print_params(*values_list_2, 42) #Проверьте, работает ли print_params(*values_list_2, 42) => работает