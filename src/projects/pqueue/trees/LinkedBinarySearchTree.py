from projects.pqueue.trees.LinkedBSTNode import LinkedBSTNode


class LinkedBinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def add(self, value):
        def add_node(node):
            if not node:
                return LinkedBSTNode(value)
            if value < node.value:
                node.left = add_node(node.left)
            else:
                node.right = add_node(node.right)
            return node
        self.root = add_node(self.root)
        self.size += 1

    def add_all(self, *values):
        for value in values:
            self.add(value)

    def clear(self):
        self.root = None
        self.size = 0

    def delete(self, value):
        if self.find(value):
            self.root = self.root.delete(value)
            self.size -= 1
            return value
        return None

    def find(self, value):
        def find_node(node):
            if not node:
                return False
            return value == node.value or find_node(node.left if value < node.value else node.right)
        return find_node(self.root)

    def get_max(self):
        return self.root.get_max() if self.root else None

    def get_min(self):
        return self.root.get_min() if self.root else None

    def height(self):
        def height_node(node, height):
            if not node:
                return height
            height += 1
            return max(height_node(node.left, height), height_node(node.right, height))
        return height_node(self.root, 0)

    def is_empty(self):
        return self.size == 0

    def __eq__(self, other):
        for value in self:
            if not other.find(value):
                return False
        for value in other:
            if not self.find(value):
                return False
        return True

    def __iadd__(self, other):
        for value in other:
            self.add(value)
        return self

    def __iter__(self):
        def iter_node(node):
            if not node:
                return None
            yield from iter_node(node.left)
            yield node.value
            yield from iter_node(node.right)
        return iter_node(self.root)

    def __str__(self):
        return " ".join(str(value) for value in self)
