import random

# Класс Animal
class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    
    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed
    
    def move(self, dx, dy, dz):
        # Изменяем координаты с учетом скорости
        if self._cords[2] + dz * self.speed < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] += dz * self.speed
    
    def get_cords(self):
        print(f"X: {self._cords[0]} Y: {self._cords[1]} Z: {self._cords[2]}")
    
    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")
    
    def speak(self):
        print(self.sound)


# Класс Bird (наследуется от Animal)
class Bird(Animal):
    beak = True
    
    def lay_eggs(self):
        print(f"Here are(is) {random.randint(1, 4)} eggs for you")


# Класс AquaticAnimal (наследуется от Animal)
class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    
    def dive_in(self, dz):
        dz = abs(dz) / 2  # Подводим координаты z
        self._cords[2] -= dz * self.speed


# Класс PoisonousAnimal (наследуется от Animal)
class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


# Класс Duckbill (наследуется от Bird, AquaticAnimal и PoisonousAnimal)
class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"
    
    def __init__(self, speed):
        super().__init__(speed)


# Пример работы программы
db = Duckbill(10)

print(db.live)  # True
print(db.beak)  # True

db.speak()  # Click-click-click
db.attack()  # Be careful, i'm attacking you 0_0

db.move(1, 2, 3)  # Двигаем на 1, 2, 3 с учетом скорости 10
db.get_cords()  # X: 10 Y: 20 Z: 30

db.dive_in(6)  # Погружаемся в воду, уменьшаем Z
db.get_cords()  # X: 10 Y: 20 Z: 0

db.lay_eggs()  # Откладываем яйца