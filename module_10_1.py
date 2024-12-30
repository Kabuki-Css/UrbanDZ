import time
from threading import Thread
from datetime import datetime

def write_words(word_count, file_name):
    with open(file_name, 'w') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            time.sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

# Вызов функции без использования потоков
start_time = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time = datetime.now()
print(f"Время выполнения функций без потоков: {end_time - start_time}")

# Создание и запуск потоков
threads = []

start_time_threads = datetime.now()

for args in [(10, 'example5.txt'), (30, 'example6.txt'), (200, 'example7.txt'), (100, 'example8.txt')]:
    thread = Thread(target=write_words, args=args)
    threads.append(thread)
    thread.start()

# Ожидание завершения всех потоков
for thread in threads:
    thread.join()

end_time_threads = datetime.now()
print(f"Время выполнения функций с использованием потоков: {end_time_threads - start_time_threads}")