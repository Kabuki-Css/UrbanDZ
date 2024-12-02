def apply_all_func(int_list, *functions):
    results = {}  # создаем пустой словарь для результатов
    for func in functions:
        results[func.__name__] = func(int_list)  # вызываем каждую функцию и сохраняем результат по имени функции
    return results

# Пример использования
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))