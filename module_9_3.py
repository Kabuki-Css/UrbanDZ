first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Генераторная сборка для разницы длин строк, если они не равны
first_result = (len(a) - len(b) for a, b in zip(first, second) if len(a) != len(b))

# Генераторная сборка для сравнения длин строк без использования zip
second_result = (len(first[i]) == len(second[i]) for i in range(min(len(first), len(second))))

# Вывод результатов
print(list(first_result))  # Output: [3, 4]
print(list(second_result)) # Output: [False, False, True]