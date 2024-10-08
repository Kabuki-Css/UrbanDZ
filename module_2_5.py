def get_matrix(n, m, value):
    matrix = [] 

    # Создания строк матрицы
    for i in range(n):
        # Пустая строка
        row = []
        for j in range(m):
            row.append(value)  # Добавляем значение
        matrix.append(row)
    return matrix

# Выводим данные согласно заданию
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print("Результат работы функции get_matrix:")
print(result1)
print(result2)
print(result3)