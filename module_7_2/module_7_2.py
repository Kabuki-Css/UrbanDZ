def custom_write(file_name, strings):
    strings_positions = {}
    
    with open(file_name, 'w', encoding='utf-8') as file:
        for line_number, string in enumerate(strings, start=1):
            position = file.tell()  # Запоминаем текущую позицию перед записью строки
            file.write(string + '\n')  # Записываем строку в файл с переносом строки
            strings_positions[(line_number, position)] = string  # Сохраняем информацию в словарь
    
    return strings_positions

# Пример использования
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)