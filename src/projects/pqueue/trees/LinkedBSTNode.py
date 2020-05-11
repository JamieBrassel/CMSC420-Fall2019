class LinkedBSTNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def delete(self, value):
        if value == self.value:
            if self.left and self.right:
                self.value = self.right.get_min()
                self.right = self.right.delete(self.value)
                return self
            if self.left:
                return self.left
            if self.right:
                return self.right
            return None
        if value < self.value:
            self.left = self.left.delete(value)
        else:
            self.right = self.right.delete(value)
        return self

    def get_min(self):
        return self.left.get_min() if self.left else self.value

    def get_max(self):
        return self.right.get_max() if self.right else self.value
