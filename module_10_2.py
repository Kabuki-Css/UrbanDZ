import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power, enemies=100):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = enemies
        self.days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        
        while self.enemies > 0:
            self.enemies -= self.power
            self.days += 1
            print(f"{self.name} сражается {self.days} день(дня)..., осталось {max(0, self.enemies)} воинов.")
            time.sleep(1)  # Задержка в 1 секунду
        
        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")

if __name__ == "__main__":
    # Создание объектов класса Knight
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)

    # Запуск потоков
    first_knight.start()
    second_knight.start()

    # Ожидание завершения потоков
    first_knight.join()
    second_knight.join()

    # Вывод сообщения об окончании битв
    print("Битвы завершены!")