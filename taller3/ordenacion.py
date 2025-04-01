import random
import time
from datetime import datetime
from typing import List

from libro import Libro


class LibroController:
    @staticmethod
    def ordenar_por_rating(libros: List[Libro]) -> List[Libro]:
        """Ordena libros por rating descendente usando sorted"""
        libros.sort(reverse=True)
        return libros

    @staticmethod
    def head(libros: List[Libro], n: int = 5):
        """Muestra los primeros n libros"""
        for libro in libros[:n]:
            print(libro)

    @staticmethod
    def tail(libros: List[Libro], n: int = 5):
        """Muestra los últimos n libros"""
        for libro in libros[-n:]:
            print(libro)

    @staticmethod
    def comparador_autor(libro: Libro):
        return libro.authors.lower()

    @staticmethod
    def comparador_ratings_count(libro: Libro):
        return libro.ratings_count

    @staticmethod
    def comparador_fecha(libro: Libro):
        try:
            return datetime.strptime(libro.publication_date, "%m/%d/%Y")
        except ValueError:
            return datetime.min  # Fecha mínima para libros con fecha inválida

    @staticmethod
    def listar_por_comparador(libros: List[Libro], key_func, reverse=False):
        """Ordena usando un comparador específico"""
        sorted_libros = sorted(libros, key=key_func, reverse=reverse)
        print("\nPrimeros 5:")
        LibroController.head(sorted_libros)
        print("\nÚltimos 5:")
        LibroController.tail(sorted_libros)
        return sorted_libros

    @staticmethod
    def quicksort(libros: List[Libro], key_func=None, reverse=False):
        """Implementación de quicksort"""
        if len(libros) <= 1:
            return libros

        pivot = libros[len(libros) // 2]

        if key_func:
            left = [x for x in libros if (key_func(x) < key_func(pivot)) ^ reverse]
            middle = [x for x in libros if key_func(x) == key_func(pivot)]
            right = [x for x in libros if (key_func(x) > key_func(pivot)) ^ reverse]
        else:
            left = [x for x in libros if (x < pivot) ^ reverse]
            middle = [x for x in libros if x == pivot]
            right = [x for x in libros if (x > pivot) ^ reverse]

        return (
            LibroController.quicksort(left, key_func, reverse)
            + middle
            + LibroController.quicksort(right, key_func, reverse)
        )

    @staticmethod
    def medir_tiempo_alg(
        libros: List[Libro], key_func=None, alg="builtin", reverse=False
    ) -> float:
        """Mide tiempo de ordenación"""
        libros_copy = libros.copy()
        random.shuffle(libros_copy)  # Aleatorizar

        start_time = time.time()

        if alg == "builtin":
            if key_func:
                libros_copy.sort(key=key_func, reverse=reverse)
            else:
                libros_copy.sort(reverse=reverse)
        elif alg == "quicksort":
            libros_copy = LibroController.quicksort(libros_copy, key_func, reverse)

        return time.time() - start_time
