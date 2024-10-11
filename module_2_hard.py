def generate_password(n):
    # Проверка, что n в диапазоне от 3 до 20
    if n < 3 or n > 20:
        raise ValueError("n должно быть от 3 до 20")

    # Инициализация пароля и множества для уникальных пар
    password = ''
    unique_pairs = set()

    # Генерация уникальных пар
    for i in range(1, n // 2 + 1):  # Первая половина
        for j in range(n, n // 2, -1):  # Вторая половина
            if i < j:  # Уникальность пар
                pair_sum = i + j
                if n % pair_sum == 0:  # Проверка кратности
                    unique_pairs.add(f"{i}{j}")

    # Сортируем пары и формируем пароль
    for pair in sorted(unique_pairs):
        password += pair

    return password

# Основная часть программы
try:
    n = int(input("Введите число от 3 до 20: "))
    result = generate_password(n)
    print(f"Сгенерированный пароль: {result}")
except ValueError as e:
    print(e)