class House:
    def __init__(self, name, number_of_floors):
        # Инициализация атрибутов
        self.name = name
        self.number_of_floors = number_of_floors
    
    def go_to(self, new_floor):
        # Проверка существования этажа
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            # Вывод этажей от 1 до new_floor включительно
            for floor in range(1, new_floor + 1):
                print(floor)
    
    def __len__(self):
        # Возвращаем количество этажей
        return self.number_of_floors
    
    def __str__(self):
        # Строковое представление объекта
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

# Пример выполнения
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))