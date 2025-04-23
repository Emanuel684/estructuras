import random
import sys
import time
from datetime import datetime
from typing import List

from libro import Libro

sys.setrecursionlimit(100000)


class LibroController:
    @staticmethod
    def ordenarPorRating(libros: List[Libro]) -> List[Libro]:
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
        return datetime.strptime(libro.publication_date, "%m/%d/%Y")

    @staticmethod
    def listarPorComparador(libros: List[Libro], key_func, reverse=False):
        """Ordena usando un comparador específico"""
        sorted_libros = sorted(libros, key=key_func, reverse=reverse)
        print("\nPrimeros 5:")
        LibroController.head(sorted_libros)
        print("\nÚltimos 5:")
        LibroController.tail(sorted_libros)
        return sorted_libros

    @staticmethod
    def quicksort(libros: List[Libro], key_func=None, reverse=False):
        if len(libros) <= 1:
            return libros

        # Mejor selección de pivote (mediana de tres)
        first = 0
        last = len(libros) - 1
        mid = (first + last) // 2

        # Ordenar first, mid, last
        candidates = [first, mid, last]
        if key_func:
            candidates.sort(key=lambda x: key_func(libros[x]))
        else:
            candidates.sort(key=lambda x: libros[x])

        pivot_index = candidates[1]  # La mediana
        pivot = libros[pivot_index]

        left = []
        middle = []
        right = []

        for x in libros:
            if key_func:
                x_val = key_func(x)
                p_val = key_func(pivot)
            else:
                x_val = x
                p_val = pivot

            if x_val == p_val:
                middle.append(x)
            elif (x_val < p_val) ^ reverse:
                left.append(x)
            else:
                right.append(x)

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
            LibroController.quicksort(libros_copy, key_func, reverse)

        return time.time() - start_time
