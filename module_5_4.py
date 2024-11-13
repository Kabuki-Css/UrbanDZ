class House:
    # Атрибут класса для хранения истории
    houses_history = []

    def __new__(cls, *args, **kwargs):
        # Добавляем название здания в историю
        cls.houses_history.append(args[0])
        # Возвращаем новый объект
        return super().__new__(cls)
    
    def __init__(self, name, number_of_floors):
        # Инициализация атрибутов
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        # При удалении объекта выводим сообщение
        print(f"{self.name} снесён, но он останется в истории")
        
# Пример выполнения программы
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)  # Вывод истории

h2 = House('ЖК Акация', 20)
print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

# Выводим финальную историю
print(House.houses_history)