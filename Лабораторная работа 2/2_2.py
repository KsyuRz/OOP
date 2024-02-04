import typing

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


class Book:
    def __init__(self, id: int, name: str, pages: int):
        if not isinstance(id, int):
            raise TypeError('id_ должно быть типа int')
        if id < 0:
            raise ValueError('id_ должно быть больше 0')
        self.id = id
        if not isinstance(name, str):
            raise TypeError('Название книги должно быть типа str')
        self.name = name
        if not isinstance(pages, int):
            raise TypeError('Количество страниц должно быть типа int')
        if pages < 0:
            raise ValueError('Количество страниц не должно быть отрицательным')
        self.pages = pages

    def __str__(self):
        return f"Книга \"{self.name}\""

    def __repr__(self):
        return f"Book(id_={self.id}, name=\'{self.name}\', pages={self.pages})"


class Library:
    def __init__(self, books: list[Book] = None):
        self.books: list[Book] = books if books else []

    def get_next_book_id(self):
        if len(self.books) == 0:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int):
        for i, book in enumerate(self.books):
            if book.id == book_id:
                return i
        else:
            raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # Инициализация пустой библиотеки
    print(empty_library.get_next_book_id())  # Проверка следующего id для пустой библиотеки

    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # Инициализация библиотеки с книгами
    print(library_with_books.get_next_book_id())  # Проверка следующего id для библиотеки с книгами

    print(library_with_books.get_index_by_book_id(1))  # Проверка индекса книги с id = 1
