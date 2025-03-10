from lista import LinkedList


class Matriz:
    def __init__(self, filas: int, columnas: int):
        """Constructor de la clase Matriz.
        :param filas: Número de filas (m).
        :param columnas: Número de columnas (n).
        """
        self.filas = filas
        self.columnas = columnas
        self.datos = LinkedList()  # Lista enlazada de listas enlazadas
        for _ in range(filas):
            fila = LinkedList()
            for _ in range(columnas):
                fila.agregar(0)
            self.datos.agregar(fila)

    def obtener(self, fila, columna):
        """Obtiene el valor en la posición (fila, columna)."""
        return self.datos.obtener(fila).valor.obtener(columna).valor

    def asignar(self, fila: int, columna: int, valor: int) -> None:
        """Asigna un valor a la posición (fila, columna)."""
        nodo_lista = self.datos.obtener(fila).valor.obtener(columna)
        nodo_lista.valor = valor

    def __eq__(self, otra: "Matriz") -> bool:
        """Compara si dos matrices son iguales."""
        if not isinstance(otra, Matriz):
            return False
        if self.filas != otra.filas or self.columnas != otra.columnas:
            return False
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.obtener(i, j) != otra.obtener(i, j):
                    return False
        return True

    def __str__(self) -> str:
        """Representación en cadena de la matriz."""
        return (
            "["
            + "\n ".join(
                "["
                + " - ".join(str(self.obtener(i, j)) for j in range(self.columnas))
                + "]"
                for i in range(self.filas)
            )
            + "]"
        )

    def suma(self, otra: "Matriz") -> "Matriz":
        """Suma dos matrices."""
        if self.filas != otra.filas or self.columnas != otra.columnas:
            raise ValueError(
                "Las matrices deben tener las mismas dimensiones para sumarse."
            )
        resultado = Matriz(self.filas, self.columnas)
        for i in range(self.filas):
            for j in range(self.columnas):
                resultado.asignar(i, j, self.obtener(i, j) + otra.obtener(i, j))
        return resultado

    def producto(self, otra: "Matriz") -> "Matriz":
        """Multiplica dos matrices."""
        if self.columnas != otra.filas:
            raise ValueError(
                "El número de columnas de la primera matriz debe coincidir con el número de filas de la segunda."
            )
        resultado = Matriz(self.filas, otra.columnas)
        for i in range(self.filas):
            for j in range(otra.columnas):
                suma = 0
                for k in range(self.columnas):
                    suma += self.obtener(i, k) * otra.obtener(k, j)
                resultado.asignar(i, j, suma)
        return resultado

    def eliminacion_gaussiana(self) -> list:
        """
        Realiza la eliminación gaussiana para resolver un sistema de ecuaciones lineales.
        :return: Una lista con las soluciones del sistema.
        """
        n = self.filas
        m = self.columnas

        # Crear una copia de la matriz para no modificar la original
        matriz = Matriz(n, m)
        for i in range(n):
            for j in range(m):
                matriz.asignar(i, j, self.obtener(i, j))

        # Eliminación hacia adelante
        for i in range(n):
            # Pivoteo parcial: encontrar la fila con el máximo valor en la columna actual
            max_fila = i
            for k in range(i + 1, n):
                if abs(matriz.obtener(k, i)) > abs(matriz.obtener(max_fila, i)):
                    max_fila = k

            # Intercambiar filas
            if max_fila != i:
                for j in range(m):
                    temp = matriz.obtener(i, j)
                    matriz.asignar(i, j, matriz.obtener(max_fila, j))
                    matriz.asignar(max_fila, j, temp)

            # Hacer cero los elementos debajo del pivote
            for k in range(i + 1, n):
                factor = matriz.obtener(k, i) / matriz.obtener(i, i)
                for j in range(i, m):
                    matriz.asignar(
                        k, j, matriz.obtener(k, j) - factor * matriz.obtener(i, j)
                    )

        # Sustitución hacia atrás
        soluciones = [0] * n
        for i in range(n - 1, -1, -1):
            soluciones[i] = matriz.obtener(i, m - 1)
            for j in range(i + 1, n):
                soluciones[i] -= matriz.obtener(i, j) * soluciones[j]
            soluciones[i] /= matriz.obtener(i, i)

        return soluciones
