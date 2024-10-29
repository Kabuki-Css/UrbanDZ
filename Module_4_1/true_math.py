# Второй модуль (Возврашает бесконечность Inf при делении на 0)
from math import inf

def divide (first, second):
    if second == 0:
        return inf
    return first / second