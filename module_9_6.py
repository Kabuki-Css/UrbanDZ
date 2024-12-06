def all_variants(text):
    n = len(text)
    for i in range(1 << n):
        variant = ''.join(text[j] for j in range(n) if (i & (1 << j)))
        yield variant

# Пример работы функции
a = all_variants("abc")

for i in a:
    print(i)