def add_everything_up(a, b):
    if isinstance(a, (int, float)) and isinstance(b, str) or isinstance(a, str) and isinstance(b, (int, float)):
        return f"{a}{b}"  # возвращаем строковое представление значений в том порядке
    else:
        return a + b  # стандартная операция сложения для чисел и одинаковых типов

# Примеры
print(add_everything_up(123.456, 'строка'))  # выводит '123.456строка'
print(add_everything_up('яблоко', 4215))     # выводит 'яблоко4215'
print(add_everything_up(123.456, 7))         # выводит 130.456