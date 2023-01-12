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
    def __init__(self, id_: int, name: str, pages: int):
        """
        Создание и подготовка к работе объекта "Book"

        :param id_: Идентификатор книги
        :param name: Название книги
        :param pages: Количество страниц в книге
        """
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        """
        Метод __str__ должен возвращать строку формата, где "название_книги" берется с помощью атрибута name

        :return: Книга "название_книги"
        """
        return f'Книга "{self.name}"'

    def __repr__(self):
        """
        Метод __repr__ должен возвращать валидную python строку,
        по которой можно инициализировать точно такой же экземпляр

        :return: Book(id_=_, name='_', pages=_)
        """
        return f'Book(id_={self.id_}, name={self.name!r}, pages={self.pages})'


class Library:
    def __init__(self, books: list[Book] = None):
        """
        Создание и подготовка к работе объекта "Library"

        :param books: Список книг
        """
        if books is None:  # Если книги не заданы, создаем пустой список
            books = []
        self.books = books

    def get_next_book_id(self):
        """
        Метод, возвращающий идентификатор для добавления новой книги в библиотеку

        :return: Если книг в библиотеке нет, то возвращает 1.
                 Если книги есть, то возвращает идентификатор последней книги увеличенный на 1
        """
        if len(self.books) == 0:
            return 1
        return self.books[-1].id_ + 1

    def get_index_by_book_id(self, id_: int):
        """
        Метод, возвращающий индекс книги в списке, который хранится в атрибуте экземпляра класса

        :param id_: Идентификатор запрашиваемой книги
        :return: Если книга существует, то возвращает индекс из списка.
                 Если книги нет, то вызывает ошибку ValueError с сообщением: "Книги с запрашиваемым id не существует"
        """
        for book in self.books:
            if id_ == book.id_:
                return self.books.index(book)
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
