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

# Создание объекта дома
house = House('ЖК Эльбрус', 30)

# Вызов метода go_to с произвольным числом
house.go_to(5)