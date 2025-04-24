from node import Node


class BST:
    """
    La clase `BST` (Binary Search Tree) implementa un árbol binario de búsqueda,
    que permite almacenar pares clave-valor de manera ordenada y eficiente.

    Métodos:
        - __init__(): Inicializa un árbol binario de búsqueda vacío.
        - put(key, val): Inserta un par clave-valor en el árbol. Si la clave ya existe, actualiza su valor.
        - _put(node, key, val): Método auxiliar recursivo para insertar un nodo en el árbol.
        - get(key): Recupera el valor asociado a una clave específica.
        - _get(node, key): Método auxiliar recursivo para buscar un nodo en el árbol.
        - keys(): Devuelve una lista de todas las claves en el árbol en orden ascendente.
        - _inorder(node, keys): Método auxiliar recursivo para realizar un recorrido en orden del árbol.
    """

    def __init__(self):
        """
        Inicializa un árbol binario de búsqueda vacío.
        """
        self.root = None

    def put(self, key, val):
        """
        Inserta un par clave-valor en el árbol. Si la clave ya existe, actualiza su valor.

        Args:
            key: La clave del elemento a insertar.
            val: El valor asociado a la clave.
        """
        self.root = self._put(self.root, key, val)

    def _put(self, node, key, val):
        """
        Método auxiliar recursivo para insertar un nodo en el árbol.

        Args:
            node: El nodo actual en el recorrido.
            key: La clave del elemento a insertar.
            val: El valor asociado a la clave.

        Returns:
            Node: El nodo actualizado después de la inserción.
        """
        if node is None:
            return Node(key, val)
        if key < node.key:
            node.left = self._put(node.left, key, val)
        elif key > node.key:
            node.right = self._put(node.right, key, val)
        else:
            node.val = val
        return node

    def get(self, key):
        """
        Recupera el valor asociado a una clave específica.

        Args:
            key: La clave del elemento a buscar.

        Returns:
            El valor asociado a la clave, o None si la clave no existe.
        """
        return self._get(self.root, key)

    def _get(self, node, key):
        """
        Método auxiliar recursivo para buscar un nodo en el árbol.

        Args:
            node: El nodo actual en el recorrido.
            key: La clave del elemento a buscar.

        Returns:
            El valor asociado a la clave, o None si la clave no existe.
        """
        if node is None:
            return None
        if key < node.key:
            return self._get(node.left, key)
        elif key > node.key:
            return self._get(node.right, key)
        else:
            return node.val

    def keys(self):
        """
        Devuelve una lista de todas las claves en el árbol en orden ascendente.

        Returns:
            list: Una lista de claves ordenadas.
        """
        keys = []
        self._inorder(self.root, keys)
        return keys

    def _inorder(self, node, keys):
        """
        Método auxiliar recursivo para realizar un recorrido en orden del árbol.

        Args:
            node: El nodo actual en el recorrido.
            keys: La lista donde se almacenan las claves en orden.
        """
        if node is None:
            return
        self._inorder(node.left, keys)
        keys.append(node.key)
        self._inorder(node.right, keys)
