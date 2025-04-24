import csv
from datetime import datetime
from functools import total_ordering
from typing import List, Optional


@total_ordering
class Libro:
    """
    La clase `Libro` representa un libro con sus atributos principales y proporciona métodos
    para comparar libros y leer datos desde un archivo CSV.

    Atributos:
        - bookID (str): Identificador único del libro.
        - title (str): Título del libro.
        - authors (str): Autores del libro.
        - average_rating (float): Calificación promedio del libro.
        - isbn (str): Código ISBN del libro.
        - isbn13 (str): Código ISBN-13 del libro.
        - language_code (str): Código del idioma del libro.
        - num_pages (Optional[int]): Número de páginas del libro (puede ser None).
        - ratings_count (int): Cantidad de calificaciones del libro.
        - text_reviews_count (int): Cantidad de reseñas textuales del libro.
        - publication_date (str): Fecha de publicación del libro en formato "MM/DD/YYYY".
        - publisher (str): Editorial del libro.

    Métodos:
        - __init__: Constructor que inicializa los atributos del libro.
        - __str__: Devuelve una representación en cadena del libro.
        - __repr__: Alias de `__str__`.
        - __lt__: Compara dos libros por su calificación promedio (menor que).
        - __eq__: Compara dos libros por su calificación promedio (igualdad).
        - leerCSV: Método estático que lee un archivo CSV y devuelve una lista de objetos `Libro`.
    """

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
        """
        Constructor que inicializa los atributos del libro.

        Args:
            book_id (str): Identificador único del libro.
            title (str): Título del libro.
            authors (str): Autores del libro.
            average_rating (float): Calificación promedio del libro.
            isbn (str): Código ISBN del libro.
            isbn13 (str): Código ISBN-13 del libro.
            language_code (str): Código del idioma del libro.
            num_pages (Optional[int]): Número de páginas del libro (puede ser None).
            ratings_count (int): Cantidad de calificaciones del libro.
            text_reviews_count (int): Cantidad de reseñas textuales del libro.
            publication_date (str): Fecha de publicación del libro en formato "MM/DD/YYYY".
            publisher (str): Editorial del libro.
        """
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
        """
        Devuelve una representación en cadena del libro.

        Returns:
            str: Representación en cadena del libro.
        """
        return (
            f"Libro(title='{self.title}', authors='{self.authors}', "
            f"average_rating={self.average_rating}, num_pages={self.num_pages}, "
            f"publication_date='{self.publication_date}')"
        )

    __repr__ = __str__

    def __lt__(self, other):
        """
        Compara dos libros por su calificación promedio (menor que).

        Args:
            other (Libro): Otro objeto `Libro` para comparar.

        Returns:
            bool: True si este libro tiene una calificación promedio menor que el otro.
        """
        return self.average_rating < other.average_rating

    def __eq__(self, other):
        """
        Compara dos libros por su calificación promedio (igualdad).

        Args:
            other (Libro): Otro objeto `Libro` para comparar.

        Returns:
            bool: True si ambos libros tienen la misma calificación promedio.
        """
        return self.average_rating == other.average_rating

    @staticmethod
    def leerCSV(archivo: str) -> List["Libro"]:
        """
        Lee un archivo CSV y devuelve una lista de objetos `Libro`.

        Args:
            archivo (str): Ruta al archivo CSV.

        Returns:
            List[Libro]: Lista de objetos `Libro` creados a partir del archivo CSV.
        """
        libros = []
        with open(archivo, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for i, row in enumerate(reader):
                try:
                    # Validar campos numéricos
                    if not row["  num_pages"].isdigit():
                        row["  num_pages"] = None

                    libro = Libro(
                        book_id=row["bookID"],
                        title=row["title"],
                        authors=row["authors"],
                        average_rating=row["average_rating"],
                        isbn=row["isbn"],
                        isbn13=row["isbn13"],
                        language_code=row["language_code"],
                        num_pages=row["  num_pages"],
                        ratings_count=row["ratings_count"],
                        text_reviews_count=row["text_reviews_count"],
                        publication_date=row["publication_date"],
                        publisher=row["publisher"],
                    )
                    datetime.strptime(libro.publication_date, "%m/%d/%Y")

                    libros.append(libro)
                except (ValueError, KeyError) as e:
                    print(f"Error en línea {i + 1}: {e}. Registro omitido.")
        return libros
