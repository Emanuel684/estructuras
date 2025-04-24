class Bag:
    """
    La clase `Bag` representa una colección de elementos que permite agregar elementos
    y recorrerlos de manera iterativa. Es una estructura de datos simple que no impone
    restricciones en los elementos almacenados.

    Métodos:
        - __init__(): Inicializa una nueva instancia de `Bag` con una lista vacía.
        - add(item): Agrega un elemento a la bolsa.
        - __iter__(): Devuelve un iterador para recorrer los elementos de la bolsa.
        - __len__(): Devuelve la cantidad de elementos en la bolsa.
    """

    def __init__(self):
        """Inicializa una nueva instancia de `Bag` con una lista vacía."""
        self.items = []

    def add(self, item):
        """
        Agrega un elemento a la bolsa.

        Args:
            item: El elemento a agregar.
        """
        self.items.append(item)

    def __iter__(self):
        """
        Devuelve un iterador para recorrer los elementos de la bolsa.

        Returns:
            iter: Un iterador sobre los elementos de la bolsa.
        """
        return iter(self.items)

    def __len__(self):
        """
        Devuelve la cantidad de elementos en la bolsa.

        Returns:
            int: El número de elementos en la bolsa.
        """
        return len(self.items)
