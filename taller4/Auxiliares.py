class BST:
    def __init__(self):
        self.root = None

    def put(self, key, val):
        self.root = self._put(self.root, key, val)

    def _put(self, node, key, val):
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
        return self._get(self.root, key)

    def _get(self, node, key):
        if node is None:
            return None
        if key < node.key:
            return self._get(node.left, key)
        elif key > node.key:
            return self._get(node.right, key)
        else:
            return node.val

    def keys(self):
        keys = []
        self._inorder(self.root, keys)
        return keys

    def _inorder(self, node, keys):
        if node is None:
            return
        self._inorder(node.left, keys)
        keys.append(node.key)
        self._inorder(node.right, keys)


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class Bag:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __iter__(self):
        return iter(self.items)

    def __len__(self):
        return len(self.items)


class MaxPQ:
    def __init__(self):
        self.pq = []

    def isEmpty(self):
        return len(self.pq) == 0

    def size(self):
        return len(self.pq)

    def insert(self, item):
        # Implementación para libros (comparar por average_rating)
        if hasattr(item, "average_rating"):
            self.pq.append(item)
            self._swim(len(self.pq) - 1)
        # Implementación para tuplas (usado en topMEditoriales)
        elif isinstance(item, tuple):
            self.pq.append(item)
            self._swim(len(self.pq) - 1)

    def delMax(self):
        max_item = self.pq[0]
        self._exchange(0, len(self.pq) - 1)
        self.pq.pop()
        self._sink(0)
        return max_item

    def _swim(self, k):
        while k > 0 and self._less((k - 1) // 2, k):
            self._exchange(k, (k - 1) // 2)
            k = (k - 1) // 2

    def _sink(self, k):
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
        # Comparación para libros
        if hasattr(self.pq[i], "average_rating") and hasattr(
            self.pq[j], "average_rating"
        ):
            return self.pq[i].average_rating < self.pq[j].average_rating
        # Comparación para tuplas (usado en topMEditoriales)
        elif isinstance(self.pq[i], tuple) and isinstance(self.pq[j], tuple):
            return self.pq[i][0] < self.pq[j][0]
        return False

    def _exchange(self, i, j):
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]

    def __iter__(self):
        # Para iterar en orden (del mayor al menor)
        temp = list(self.pq)
        result = []
        while not self.isEmpty():
            result.append(self.delMax())
        self.pq = temp
        return iter(result)
