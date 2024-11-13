class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    
    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        return self.number_of_floors == (other.number_of_floors if isinstance(other, House) else other)

    def __lt__(self, other):
        return self.number_of_floors < (other.number_of_floors if isinstance(other, House) else other)

    def __le__(self, other):
        return self.number_of_floors <= (other.number_of_floors if isinstance(other, House) else other)

    def __gt__(self, other):
        return self.number_of_floors > (other.number_of_floors if isinstance(other, House) else other)

    def __ge__(self, other):
        return self.number_of_floors >= (other.number_of_floors if isinstance(other, House) else other)

    def __ne__(self, other):
        return self.number_of_floors != (other.number_of_floors if isinstance(other, House) else other)

    def __add__(self, value):
        self.number_of_floors += value
        return self

    __radd__ = __add__

    def __iadd__(self, value):
        self.number_of_floors += value
        return self

# Пример выполнения
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)

print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__