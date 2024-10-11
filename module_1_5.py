#Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
immutable_var=(1, 'str', True)
#Выполните операции вывода кортежа immutable_var на экран.
print(immutable_var)
#Попытайтесь изменить элементы кортежа immutable_var. Объясните, почему нельзя изменить значения элементов кортежа.

#immutable_var[0]=2 =>TypeError: 'tuple' object does not support item assignment (кортежи не поддерживают изменения)

#Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
mutable_list=[1,125,'a','57sdf']
print(mutable_list)
#Измените элементы списка mutable_list.
mutable_list[1]=258
mutable_list[1]=mutable_list[1]-58
mutable_list[2]='abcd', 33 #вставим кортеж
#Выведите на экран измененный список mutable_list.
print(mutable_list)

