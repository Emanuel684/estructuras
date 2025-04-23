class Libro:
    def __init__(
        self,
        bookID,
        title,
        authors,
        average_rating,
        isbn,
        isbn13,
        language_code,
        num_pages,
        ratings_count,
        text_reviews_count,
        publication_date,
        publisher,
    ):
        self.bookID = bookID
        self.title = title
        self.authors = authors
        self.average_rating = float(average_rating) if average_rating else 0.0
        self.isbn = isbn
        self.isbn13 = isbn13
        self.language_code = language_code
        self.num_pages = int(num_pages) if num_pages else 0
        self.ratings_count = int(ratings_count) if ratings_count else 0
        self.text_reviews_count = int(text_reviews_count) if text_reviews_count else 0
        self.publication_date = publication_date
        self.publisher = publisher

    def __str__(self):
        title = self.title[:30] + "..." if len(self.title) > 30 else self.title
        authors = self.authors[:30] + "..." if len(self.authors) > 30 else self.authors
        publisher = (
            self.publisher[:30] + "..." if len(self.publisher) > 30 else self.publisher
        )
        return f"Título: {title.ljust(33)} Autores: {authors.ljust(33)} Editorial: {publisher.ljust(33)} Rating: {self.average_rating:.2f}"


class Valoracion:
    def __init__(self):
        self.cantidad_libros = 0
        self.suma_ratings = 0.0

    @property
    def promedio(self):
        return (
            self.suma_ratings / self.cantidad_libros
            if self.cantidad_libros > 0
            else 0.0
        )

    def agregar_libro(self, rating):
        self.cantidad_libros += 1
        self.suma_ratings += rating

    def __str__(self):
        return f"Libros: {self.cantidad_libros}, Rating promedio: {self.promedio:.2f}"
