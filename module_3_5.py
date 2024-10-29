def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    
    # Если длина строки больше 1, вызываем функцию рекурсивно 
    if len(str_number) > 1:
        # Возвращаем произведение первой цифры 
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        # Если длина строки равна 1, возвращаем первую цифру
        return first
result = get_multiplied_digits(40203)
print("Произведение цифр числа:", result)