def calculate_structure_sum(data_structure):
    total = 0
    for item in data_structure:
        if isinstance(item, (list, tuple, set)):
            # Рекурсивно обрабатываем элементы в списках, кортежах и множествах
            total += calculate_structure_sum(item)
        elif isinstance(item, dict):
            # Рекурсивно обрабатываем ключи и значения словаря, игнорируя некорректные ключи
            total += calculate_structure_sum(item.values())
            for key in item.keys():
                if isinstance(key, (int, float)):
                    total += key
                elif isinstance(key, str):
                    total += len(key)
        elif isinstance(item, str):
            # Добавляем длину строки
            total += len(item)
        elif isinstance(item, (int, float)):
            # Суммируем числовые значения
            total += item

    return total

# Данные программиста
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)