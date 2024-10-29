def print_params(a = 1, b = "Строка", c = True ):
    print (f"a = {a}, b = {b}, c = {c}")

print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(a=10, c=False)
# Вторая часть задания

values_list = [42, "hello", False]
values_dict = {'a': 3.14, 'b': "world", 'c': [4, 5, 6]}
print("Вызов с распаковкой списка:")
print_params(*values_list)
print("Вызов с распаковкой словаря:")
print_params(**values_dict)
# Третья часть задания

#values_list_2 = ["привет", False]
values_list_2 = [54.32, 'Строка' ]
print("Вызов с распаковкой списка values_list_2 и добавлением значения 42:")
print_params(*values_list_2, 42)