import csv
from collections import defaultdict
from datetime import datetime
from typing import List

from bag import Bag
from bst import BST
from libro import Libro
from max_pq import MaxPQ
from valoracion import Valoracion


class AnalisisDatos:

    @staticmethod
    def leerCSV(archivo: str) -> List["Libro"]:
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

    @staticmethod
    def indexarPorAutor(libros):
        """Crea un BST indexado por autor con sus libros en una Bag.

        Args:
            libros (list): Lista de objetos Libro

        Returns:
            BST: Árbol binario de búsqueda con autores como llaves y Bags de libros como valores
        """

        # Usamos un diccionario temporal para agrupar por autor
        autores_dict = defaultdict(list)
        for libro in libros:
            autores_dict[libro.authors].append(libro)

        # Convertimos el diccionario a un BST
        bst = BST()
        for autor, libros_autor in autores_dict.items():
            bag = Bag()
            for libro in libros_autor:
                bag.add(libro)
            bst.put(autor, bag)

        return bst

    @staticmethod
    def topM(bst_autores, autor, m):
        """Obtiene los top M libros de un autor según su rating.

        Args:
            bst_autores (BST): BST indexado por autores
            autor (str): Nombre del autor a buscar
            m (int): Cantidad de libros a retornar

        Returns:
            MaxPQ: Cola de prioridad con los top M libros del autor
        """
        # Buscamos los libros del autor en el BST
        libros_autor = bst_autores.get(autor)
        if libros_autor is None:
            return MaxPQ()

        # Creamos una MaxPQ basada en el rating
        pq = MaxPQ()
        for libro in libros_autor:
            pq.insert(libro)
            if pq.size() > m:
                pq.delMax()  # Mantenemos solo los top M

        return pq

    @staticmethod
    def estadisticasEditorial(libros):
        """Calcula estadísticas por editorial.

        Args:
            libros (list): Lista de objetos Libro

        Returns:
            BST: Árbol con editoriales como llaves y objetos Valoracion como valores
        """
        # Definimos la clase Valoracion aquí si no está definida a nivel global
        # Usamos un diccionario temporal para agrupar por editorial
        editoriales_dict = defaultdict(Valoracion)
        for libro in libros:
            editorial = libro.publisher
            if not editorial:  # Si no tiene editorial, saltamos
                continue
            valoracion = editoriales_dict[editorial]
            valoracion.agregar_libro(libro.average_rating)

        # Convertimos el diccionario a un BST
        bst = BST()
        for editorial, valoracion in editoriales_dict.items():
            bst.put(editorial, valoracion)

        return bst

    @staticmethod
    def topMEditoriales(valoracionEditorial, m):
        """Muestra las top M editoriales por valoración promedio.

        Args:
            valoracionEditorial (BST): BST con estadísticas de editoriales
            m (int): Cantidad de editoriales a mostrar
        """
        # Creamos una MaxPQ para ordenar por rating promedio
        pq = MaxPQ()
        for editorial in valoracionEditorial.keys():
            valoracion = valoracionEditorial.get(editorial)
            # Usamos una tupla (rating, editorial) para la comparación
            pq.insert((valoracion.promedio, editorial))

        # Mostramos las top M
        print(f"\nTop {m} editoriales por rating promedio:")
        for i in range(m):
            if pq.isEmpty():
                break
            rating, editorial = pq.delMax()
            editorial_short = (
                editorial[:30] + "..." if len(editorial) > 30 else editorial
            )
            print(f"{i + 1}. {editorial_short.ljust(33)} Rating promedio: {rating:.2f}")
