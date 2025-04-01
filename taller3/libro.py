import csv
from functools import total_ordering
from typing import List, Optional


@total_ordering
class Libro:
    def __init__(
        self,
        book_id: str,
        title: str,
        authors: str,
        average_rating: float,
        isbn: str,
        isbn13: str,
        language_code: str,
        num_pages: Optional[int],
        ratings_count: int,
        text_reviews_count: int,
        publication_date: str,
        publisher: str,
    ):
        self.bookID = book_id
        self.title = title
        self.authors = authors
        self.average_rating = float(average_rating)
        self.isbn = isbn
        self.isbn13 = isbn13
        self.language_code = language_code
        self.num_pages = int(num_pages) if num_pages else None
        self.ratings_count = int(ratings_count)
        self.text_reviews_count = int(text_reviews_count)
        self.publication_date = publication_date
        self.publisher = publisher

    def __str__(self):
        return (
            f"Libro(title='{self.title}', authors='{self.authors}', "
            f"rating={self.average_rating}, pages={self.num_pages}, "
            f"published='{self.publication_date}')"
        )

    __repr__ = __str__

    def __lt__(self, other):
        return self.average_rating < other.average_rating

    def __eq__(self, other):
        return self.average_rating == other.average_rating

    @staticmethod
    def leerCSV(archivo: str) -> List["Libro"]:
        libros = []
        with open(archivo, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for i, row in enumerate(reader):
                try:
                    # Validar campos numéricos
                    if not row["num_pages"].isdigit():
                        row["num_pages"] = None

                    libro = Libro(
                        book_id=row["bookID"],
                        title=row["title"],
                        authors=row["authors"],
                        average_rating=row["average_rating"],
                        isbn=row["isbn"],
                        isbn13=row["isbn13"],
                        language_code=row["language_code"],
                        num_pages=row["num_pages"],
                        ratings_count=row["ratings_count"],
                        text_reviews_count=row["text_reviews_count"],
                        publication_date=row["publication_date"],
                        publisher=row["publisher"],
                    )
                    libros.append(libro)
                except (ValueError, KeyError) as e:
                    print(f"Error en línea {i + 1}: {e}. Registro omitido.")
        return libros
