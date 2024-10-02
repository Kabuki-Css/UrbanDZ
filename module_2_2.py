first = input ("Введите 3-и целых числа для first: ")
second = input ("Введите 3-и целых числа для second: ")
third = input ("Введите 3-и целых числа для third: ")
if first == second == third:
    print("3")
elif first == second or first == third or second == third:
    print("2")
else:
    print("0")