def all_variants(text):
    n = len(text)
    for mask in range(1, 1 << n):  # От 1 до 2^n - 1 (включительно)
        subsequence = ''
        for i in range(n):
            if mask & (1 << i):  # Проверяем, установлен ли i-й бит в маске
                subsequence += text[i]
        yield subsequence

# Пример использования
a = all_variants("abc")

for i in a:
    print(i)