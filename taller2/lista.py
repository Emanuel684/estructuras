class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


class LinkedList:
    def __init__(self):
        self.cabeza = None
        self.longitud = 0

    def agregar(self, valor: int) -> None:
        """Agrega un valor al final de la lista."""
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        self.longitud += 1

    def obtener(self, indice: int) -> 'Nodo':
        """Obtiene el valor en el índice especificado."""
        if indice < 0 or indice >= self.longitud:
            raise IndexError("Índice fuera de rango")
        actual = self.cabeza
        for _ in range(indice):
            actual = actual.siguiente
        return actual

    def __iter__(self):
        """Iterador para recorrer la lista."""
        actual = self.cabeza
        while actual:
            yield actual.valor
            actual = actual.siguiente

    def __len__(self):
        """Devuelve la longitud de la lista."""
        return self.longitud

    def __str__(self):
        """Representación en cadena de la lista."""
        return " -> ".join(str(valor) for valor in self)
