'''Создайте класс House.
Вунтри класса House определите метод __init__, в который передадите название и кол-во этажей.
Внутри метода __init__ создайте атрибуты объекта self.name и self.number_of_floors, присвойте им переданные значения.
Создайте метод go_to с параметром new_floor и напишите логику внутри него на основе описания задачи.
Создайте объект класса House с произвольным названием и количеством этажей.
Вызовите метод go_to у этого объекта с произвольным числом.'''

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor): #Метод go_to выводит на экран(в консоль) значения от 1 до new_floor(включительно)
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor + 1):
                print(i)

a = House('Красная жара', 17)
b = House ('Солнечный', 5)
a.go_to(5)
b.go_to(9)