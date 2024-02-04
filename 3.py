class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError
        self._name = name

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, author: str) -> None:
        if not isinstance(author, str):
            raise TypeError
        self._author = author

    def __str__(self):
        return f"Книга: {self.name}. Автор: {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name=name, author=author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, pages: int) -> None:
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int!")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным!")
        self._pages = pages

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}, Страниц {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name=name, author=author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, duration: float) -> None:
        if not isinstance(duration, float):
            raise TypeError("Длительность должна быть типа float!")
        if duration <= 0:
            raise ValueError("Длительность должна быть положительной!")
        self._duration = duration

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}, Продолжительность {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"


if __name__ == "__main__":
    paper_book = PaperBook("Первая книга", "Первый автор", 322)
    print(str(paper_book))
    print(repr(paper_book))
    audio_book = AudioBook("Вторая книга", "Второй автор", 14.88)
    print(str(audio_book))
    print(repr(audio_book))