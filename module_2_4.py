numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Создадим пустые списки
primes = []
not_primes = []

# Создаём перебор
for num in numbers:
    if num == 1: # Раз число особенное исключим его из вывода
        continue
    is_prime = True
    if num < 2:
        is_prime = False
    
# Создаём проверку на простое число    
    for divisor in range(2, int(num**0.5) + 1):
        if num % divisor == 0:
            is_prime = False
            break 
    
    # Ракспределяем числа по спискам
    if is_prime:
         primes.append(num)
    else:
        not_primes.append(num)
# Выводим списки
print("Primes:", primes)
print("Not Primes:", not_primes)

