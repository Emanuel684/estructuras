class Node:
    """
    Clase `Node` que representa un nodo en un árbol binario.

    Atributos:
        key: La clave asociada al nodo.
        val: El valor almacenado en el nodo.
        left: Referencia al nodo hijo izquierdo (inicialmente `None`).
        right: Referencia al nodo hijo derecho (inicialmente `None`).

    Métodos:
        __init__(key, val): Constructor que inicializa un nodo con una clave, un valor y referencias nulas a los hijos.
    """

    def __init__(self, key, val):
        """
        Constructor de la clase `Node`.

        Args:
            key: La clave asociada al nodo.
            val: El valor almacenado en el nodo.
        """
        self.key = key
        self.val = val
        self.left = None
        self.right = None
