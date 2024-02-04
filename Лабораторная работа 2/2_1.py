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


if __name__ == '__main__':
    # Инициализация списка книг
    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # Проверка метода __str__

    print(list_books)  # Проверка метода __repr__
