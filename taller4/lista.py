class DoubleLinkedList:
    """
    La clase `DoubleLinkedList` implementa una lista doblemente enlazada.

    Atributos:
        - head (Node): El primer nodo de la lista.
        - tail (Node): El último nodo de la lista.
        - size (int): El número de elementos en la lista.

    Métodos:
        - append(data): Agrega un nuevo nodo con el dato especificado al final de la lista.
        - __iter__(): Permite iterar sobre los elementos de la lista.
        - to_list(): Devuelve una representación de la lista como una lista de Python.
        - __len__(): Devuelve el número de elementos en la lista.
    """

    class Node:
        """
        La clase `Node` representa un nodo en la lista doblemente enlazada.

        Atributos:
            - data: El dato almacenado en el nodo.
            - next (Node): Referencia al siguiente nodo en la lista.
            - prev (Node): Referencia al nodo anterior en la lista.
        """

        def __init__(self, data):
            """
            Inicializa un nodo con el dato especificado.

            Args:
                data: El dato a almacenar en el nodo.
            """
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        """
        Inicializa una lista doblemente enlazada vacía.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        """
        Agrega un nuevo nodo con el dato especificado al final de la lista.

        Args:
            data: El dato a agregar a la lista.
        """
        new_node = self.Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def __iter__(self):
        """
        Permite iterar sobre los elementos de la lista.

        Yields:
            El dato de cada nodo en la lista.
        """
        current = self.head
        while current:
            yield current.data
            current = current.next

    def to_list(self):
        """
        Devuelve una representación de la lista como una lista de Python.

        Returns:
            list: Una lista con los datos de los nodos en la lista.
        """
        return [x for x in self]

    def __len__(self):
        """
        Devuelve el número de elementos en la lista.

        Returns:
            int: El tamaño de la lista.
        """
        return self.size
