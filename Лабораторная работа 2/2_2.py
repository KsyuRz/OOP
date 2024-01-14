BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]
# Создаем класс Книга
class Book:
    # ССоздаем конструктор для класса Книга
    def __init__(self, id_: int, name: str, pages: int):
        self.id_ = id_
        self.name = name
        self.pages = pages

    # Методы
    def __str__(self):
        return f"Книга \"{self.name}\""

    def __repr__(self):
        return f"Book(id_={self.id_}, name=\'{self.name}\', pages={self.pages})"

# Создаем класс Библиотека
class Library:
    # Создаем конструктор для класса Библиотека
    def __init__(self, books: list[Book] = None):
        self.books: list[Book] = books if books else []

    # Метод для создания id для добавления новой книги в список
    def get_next_book_id(self):
        if len(self.books) == 0:
            return 1
        return self.books[-1].id_ + 1

    # Метод для поиска книги
    def get_index_by_book_id(self, book_id: int):
        for i, book in enumerate(self.books):
            if book.id_ == book_id:
                return i
        else:
            raise ValueError("Книги с запрашиваемым id не существует")
            # Выводим сообщение об ошибке, если книга с заданным id не существует в списке


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1