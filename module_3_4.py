def single_root_words(root_word, *other_words):
    same_words = []

    for word in other_words:
        # Дано: если root_word содержится в word, добавляем его в список same_words
        if root_word.lower() in word.lower() or word.lower() in root_word.lower():
            same_words.append(word)
    
    return same_words

# Вызов функции со словами
result = single_root_words("auto", "automobile", "autonomy", "automation", "automatic", "author", "autumn")
# Дополнение
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print("Подходящие слова:", result)
print(result1)
print(result2)