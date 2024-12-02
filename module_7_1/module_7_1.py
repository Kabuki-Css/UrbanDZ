class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        """Считывает всю информацию из файла __file_name и возвращает в виде строки."""
        try:
            with open(self.__file_name, 'r', encoding='utf-8') as file:
                return file.read().strip()
        except FileNotFoundError:
            return "Файл с продуктами ещё не создан."

    def add(self, *products):
        """Добавляет продукты в файл, если их ещё нет."""
        existing_products = set()
        try:
            with open(self.__file_name, 'r', encoding='utf-8') as file:
                for line in file:
                    product_name = line.strip().split(', ')[0]
                    existing_products.add(product_name)
        except FileNotFoundError:
            pass  # Если файл отсутствует, просто создадим его позже

        with open(self.__file_name, 'a', encoding='utf-8') as file:
            for product in products:
                if product.name in existing_products:
                    print(f"Продукт {product.name} уже есть в магазине")
                else:
                    file.write(f"{product}\n")
                    existing_products.add(product.name)


# Пример использования
if __name__ == "__main__":
    s1 = Shop()

    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # Проверка работы метода __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())  # Проверка содержимого файла
