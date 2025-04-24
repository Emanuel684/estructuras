class MaxPQ:
    """
    La clase `MaxPQ` implementa una cola de prioridad máxima (Max Priority Queue) basada en un heap binario.

    Atributos:
        - pq (list): Lista que almacena los elementos de la cola de prioridad.

    Métodos:
        - isEmpty(): Verifica si la cola de prioridad está vacía.
        - size(): Devuelve el número de elementos en la cola de prioridad.
        - insert(item): Inserta un elemento en la cola de prioridad.
        - delMax(): Elimina y devuelve el elemento máximo de la cola de prioridad.
        - __iter__(): Permite iterar sobre los elementos de la cola en orden descendente.
    """

    def __init__(self):
        """
        Inicializa una cola de prioridad vacía.
        """
        self.pq = []

    def isEmpty(self):
        """
        Verifica si la cola de prioridad está vacía.

        Returns:
            bool: True si la cola está vacía, False en caso contrario.
        """
        return len(self.pq) == 0

    def size(self):
        """
        Devuelve el número de elementos en la cola de prioridad.

        Returns:
            int: Número de elementos en la cola.
        """
        return len(self.pq)

    def insert(self, item):
        """
        Inserta un elemento en la cola de prioridad.

        Args:
            item: Elemento a insertar. Puede ser un objeto con el atributo `average_rating` o una tupla.
        """
        if hasattr(item, "average_rating"):
            self.pq.append(item)
            self._swim(len(self.pq) - 1)
        elif isinstance(item, tuple):
            self.pq.append(item)
            self._swim(len(self.pq) - 1)

    def delMax(self):
        """
        Elimina y devuelve el elemento máximo de la cola de prioridad.

        Returns:
            El elemento máximo de la cola.
        """
        max_item = self.pq[0]
        self._exchange(0, len(self.pq) - 1)
        self.pq.pop()
        self._sink(0)
        return max_item

    def _swim(self, k):
        """
        Realiza la operación de swim para restaurar la propiedad del heap.

        Args:
            k (int): Índice del elemento que debe "flotar" hacia arriba.
        """
        while k > 0 and self._less((k - 1) // 2, k):
            self._exchange(k, (k - 1) // 2)
            k = (k - 1) // 2

    def _sink(self, k):
        """
        Realiza la operación de sink para restaurar la propiedad del heap.

        Args:
            k (int): Índice del elemento que debe "hundirse" hacia abajo.
        """
        N = len(self.pq) - 1
        while 2 * k + 1 <= N:
            j = 2 * k + 1
            if j < N and self._less(j, j + 1):
                j += 1
            if not self._less(k, j):
                break
            self._exchange(k, j)
            k = j

    def _less(self, i, j):
        """
        Compara dos elementos en la cola de prioridad.

        Args:
            i (int): Índice del primer elemento.
            j (int): Índice del segundo elemento.

        Returns:
            bool: True si el elemento en el índice `i` es menor que el elemento en el índice `j`.
        """
        if hasattr(self.pq[i], "average_rating") and hasattr(
            self.pq[j], "average_rating"
        ):
            return self.pq[i].average_rating < self.pq[j].average_rating
        elif isinstance(self.pq[i], tuple) and isinstance(self.pq[j], tuple):
            return self.pq[i][0] < self.pq[j][0]
        return False

    def _exchange(self, i, j):
        """
        Intercambia dos elementos en la cola de prioridad.

        Args:
            i (int): Índice del primer elemento.
            j (int): Índice del segundo elemento.
        """
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]

    def __iter__(self):
        """
        Permite iterar sobre los elementos de la cola en orden descendente.

        Returns:
            iter: Iterador sobre los elementos de la cola.
        """
        temp = list(self.pq)
        result = []
        while not self.isEmpty():
            result.append(self.delMax())
        self.pq = temp
        return iter(result)
