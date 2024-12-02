class WordsFinder:
    def __init__(self, *file_names):
        """Инициализация класса. Сохраняет переданные имена файлов."""
        self.file_names = list(file_names)

    def get_all_words(self):
        """
        Возвращает словарь, где ключ - название файла, значение - список слов из файла.
        """
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    # Чтение файла, перевод в нижний регистр
                    text = file.read().lower()
                    # Удаление пунктуации (включая специфический случай с тире)
                    for punct in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        text = text.replace(punct, ' ')
                    # Разбиение текста на слова
                    words = text.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                # Если файл не найден, создаём пустую запись
                all_words[file_name] = []
        return all_words

    def find(self, word):
        """
        Находит первое вхождение слова в каждом файле.
        Возвращает словарь: название файла -> позиция (или -1, если слова нет),
        где позиция начинается с 1.
        """
        word = word.lower()
        all_words = self.get_all_words()
        result = {}
        for file_name, words in all_words.items():
            try:
                result[file_name] = words.index(word) + 1
            except ValueError:
                result[file_name] = -1
        return result

    def count(self, word):
        """
        Считает количество вхождений слова в каждом файле.
        Возвращает словарь: название файла -> количество.
        """
        word = word.lower()
        all_words = self.get_all_words()
        result = {file_name: words.count(word) for file_name, words in all_words.items()}
        return result
    
finder2 = WordsFinder(r'C:\Users\BG-NoutMSI\Desktop\UrbanDZ\module_7_3\test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

finder1 = WordsFinder(r'C:\Users\BG-NoutMSI\Desktop\UrbanDZ\module_7_3\Walt Whitman - O Captain! My Captain!.txt',
                      r'C:\Users\BG-NoutMSI\Desktop\UrbanDZ\module_7_3\Rudyard Kipling - If.txt',
                      r'C:\Users\BG-NoutMSI\Desktop\UrbanDZ\module_7_3\Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))