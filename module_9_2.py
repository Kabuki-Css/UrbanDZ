first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# Первая задача: список длин строк из first_strings, длина которых не менее 5 символов
first_result = [len(word) for word in first_strings if len(word) >= 5]

# Вторая задача: список кортежей, где сравниваются каждое слово из first_strings с каждым из second_strings
second_result = [(word1, word2) for word1 in first_strings for word2 in second_strings if len(word1) == len(word2)]

# Третья задача: словарь, где ключ - строка, а значение - длина этой строки, и только те строки, у которых чётная длина
third_result = {word: len(word) for word in first_strings + second_strings if len(word) % 2 == 0}

# Вывод результатов
print(first_result)
print(second_result)
print(third_result)