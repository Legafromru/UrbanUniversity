'''Необходимо дополнить класс House следующими специальными методами:
    __eq__(self, other) - должен возвращать True, если количество этажей одинаковое у self и у other.
    Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=) должны присутствовать в классе и возвращать результаты
    сравнения по соответствующим операторам. Как и в методе __eq__ в сравнении участвует кол-во этажей.
    __add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
    __radd__(self, value), __iadd__(self, value) - работают так же как и __add__ (возвращают результат его вызова).

Остальные методы арифметических операторов, где self - x, other - y:'''

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

    def __eq__(self, other):
        return self.number_of_floors == other

    def __lt__(self, other):
        return self.number_of_floors < other

    def __le__(self, other):
        return self.number_of_floors <= other

    def __gt__(self, other):
        return self.number_of_floors > other

    def __ge__(self, other):
        return self.number_of_floors >= other

    def __ne__(self, other):
        return self.number_of_floors != other

    def __add__(self, value):# __add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)

    def __radd__(self, value): #__radd__(self, value), __iadd__(self, value) - работают так же как и __add__ (возвращают результат его вызова).
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __str__(self):
        return f'Название: ЖК "{self.name}", Колличество этажей: {self.number_of_floors}'


h1 = House('Красная жара', 10)
h2 = House ('Солнечный', 20)
print(h1)
print(h2)
print(h1 == h2) # __eq__
h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)
h1 += 10 # __iadd__
print(h1)
h2 = 10 + h2 # __radd__
print(h2)
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__