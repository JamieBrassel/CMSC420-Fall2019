from projects.pqueue.lists.LinkedListNode import LinkedListNode


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def clear(self):
        self.head = None
        self.size = 0

    def contains(self, value):
        for node_value in self:
            if value == node_value:
                return True
        return False

    def delete(self, value):
        if self.is_empty():
            return False
        node = self.head
        if value == node.value:
            self.head = node.next_node
            self.size -= 1
            return True
        while node.next_node:
            if value == node.next_node.value:
                node.next_node = node.next_node.next_node
                self.size -= 1
                return True
            node = node.next_node
        return False

    def delete_all(self, value):
        deleted = False
        while self.delete(value):
            deleted = True
        return deleted

    def delete_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError
        node = self.head
        if index == 0:
            self.head = node.next_node
        else:
            for i in range(0, index - 1):
                node = node.next_node
            node.next_node = node.next_node.next_node
        self.size -= 1

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError
        node = self.head
        for i in range(0, index):
            node = node.next_node
        return node.value

    def get_first(self):
        return self.head.value if self.is_empty() else None

    def get_last(self):
        if self.is_empty():
            return None
        node = self.head
        while node.next_node:
            node = node.next_node
        return node.value

    def is_empty(self):
        return self.size == 0

    def push_back(self, value):
        temp = LinkedListNode(value)
        if self.is_empty():
            self.head = temp
        else:
            node = self.head
            while node.next_node:
                node = node.next_node
            node.next_node = temp
        self.size += 1

    def push_back_all(self, *values):
        for value in values:
            self.push_back(value)

    def push_front(self, value):
        self.head = LinkedListNode(value, self.head)
        self.size += 1

    def push_front_all(self, *values):
        for value in values:
            self.push_front(value)

    def __eq__(self, other):
        for value in self:
            if not other.contains(value):
                return False
        for value in other:
            if not self.contains(value):
                return False
        return True

    def __iadd__(self, other):
        for value in other:
            self.push_back(value)
        return self

    def __iter__(self):
        def iter_node(node):
            if not node:
                return None
            yield node.value
            yield from iter_node(node.next_node)
        return iter_node(self.head)

    def __str__(self):
        return " ".join(str(value) for value in self)
