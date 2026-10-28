class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def info(self):
        print(f"Название: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Количество страниц: {self.pages}")
class Book1(Book):
    def info(self):
        super().info()
        print("Дополнительная ингформация о книге 1")
class Book2(Book):
    def info(self):
        super().info()
        print("Дополнительная ингформация о книге 2")
book1 = Book1(title="All tomorows", author="Джевдет Мехмет Кёсемен", pages=118)
book2 = Book2(title="Кровавый меридиан", author="Кормак Маккарти", pages=480)
book1.info()
book2.info()
