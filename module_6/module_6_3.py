import random  # Подключение модуля random

class Animal: #Создаем класс Animal - класс описывающий животных
    live = True  # live = True
    sound = None  # sound = None - звук (изначально отсутствует)
    _DEGREE_OF_DANGER = 0  # _DEGREE_OF_DANGER = 0 - степень опасности  существа

    def __init__(self, speed):
        self._cords = [0, 0, 0]  # _cords = [0, 0, 0] - координаты в пространстве
        self.speed = speed  # speed = ... - скорость передвижения существа (определяется при создании объекта)

    """ И методами:
    1. move(self, dx, dy, dz), который должен менять соответствующие координаты в _cords на dx, dy и dz
    в том же порядке, где множителем будет являться speed. Если при попытке изменения координаты z в _cords значение
    будет меньше 0, то выводить сообщение "It's too deep, i can't dive :(" , при этом изменения не вносятся """

    def move(self, dx, dy, dz):
        self._cords = [int(dx) * int(self.speed), int(dy) * int(self.speed), int(dz) * int(self.speed)]
        if self._cords[2] < 0:
            print(f"It's too deep, i can't dive :(")
            self._cords[2] = 0

    """ 2. get_cords(self), который выводит координаты в формате: "X: <координаты по x>, Y: <координаты по y>,
    Z: <координаты по z>" """

    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    """ 3. attack(self), который выводит "Sorry, i'm peaceful :)", если степень опасности меньше 5 и "Be careful,
    i'm attacking you 0_0" , если равно или больше """

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)

class Bird(Animal): #Создаем класс Bird - класс описывающий птиц. Наследуется от Animal
    beak = True

    """ И методом:
    1. lay_eggs(self), который выводит строку "Here are(is) <случайное число от 1 до 4> eggs for you" """
    def lay_eggs(self):
        egg = random.randint(1, 4)
        print(f"Here is(are) {egg} egg(s) for you")  # Число может быть другим (1-4)

class AquaticAnimal(Animal): #Содаем класс AquaticAnimal - класс описывающий плавающего животного. Наследуется от Animal
    _DEGREE_OF_DANGER = 3

    """ Должен обладать методом:
    1. dive_in(self, dz) - где dz изменение координаты z в _cords. Этот метод должен всегда уменьшать координату z
    в _coords. Чтобы сделать dz положительным, берите его значение по модулю (функция abs). Скорость движения при
    нырянии должна уменьшаться в 2 раза, в отличии от обычного движения. (speed / 2) """

    def dive_in(self, dz):
        self._cords[2] = abs(int(self._cords[2]) // int(self.speed)) - dz // 2

class PoisonousAnimal(Animal): #Содаем класс PoisonousAnimal - класс описывающий ядовитых животных. Наследуется от Animal
    _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal, Bird, AquaticAnimal): #Содаем класс Duckbill - класс описывающий утконоса.
    # Наследуется от классов Bird, AquaticAnimal, PoisonousAnimal
    """ Объект этого класса должен обладать одним дополнительным атрибутом:
    1. sound = "Click-click-click" - звук, который издаёт утконос """
    sound = "Click-click-click"

# Вывод результата:
db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()