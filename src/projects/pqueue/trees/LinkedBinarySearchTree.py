class LinkedBSTNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


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

    def clear(self):
        self.root = None
        self.size = 0

    def delete(self, value):
        def delete_node(node):
            # TODO
            return node
        if self.find(value):
            self.root = delete_node(self.root)
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
        def get_max_node(node):
            return get_max_node(node.right) if node.right else node.value
        return get_max_node(self.root)

    def get_min(self):
        def get_min_node(node):
            return get_min_node(node.left) if node.left else node.value
        return get_min_node(self.root)

    def height(self):
        def height_node(node, height):
            if not node:
                return height
            height += 1
            return max(height_node(node.left, height), height_node(node.right, height))
        return height_node(self.root, 0)

    def is_empty(self):
        return self.size == 0

    def __iadd__(self, value):
        self.add(value)
        return self

    def __str__(self):
        return " ".join(str(value) for value in test)

    def __iter__(self):
        def iter_node(node):
            if not node:
                return None
            yield from iter_node(node.left)
            yield node.value
            yield from iter_node(node.right)
        return iter_node(self.root)
