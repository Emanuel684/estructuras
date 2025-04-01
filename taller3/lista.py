class DoubleLinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
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
        current = self.head
        while current:
            yield current.data
            current = current.next

    def to_list(self):
        return [x for x in self]

    def __len__(self):
        return self.size
