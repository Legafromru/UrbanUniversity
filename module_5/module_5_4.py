
class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):  # ,*args, **kwargs
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors <= other

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors > other

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors >= other

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        elif isinstance(other, int):
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

    def __del__(self):
        print(f'"{self.name} снесён, но он останется в истории"')


h1 = House('Красная жара', 10)
print(House.houses_history)
h2 = House ('Солнечный', 20)
print(House.houses_history)
h3 = House ('Стахановский', 5)
print(House.houses_history)
del h2
del h3
print(House.houses_history)