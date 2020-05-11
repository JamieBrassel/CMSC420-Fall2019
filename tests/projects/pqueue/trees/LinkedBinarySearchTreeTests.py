import unittest
from projects.pqueue.trees.LinkedBinarySearchTree import LinkedBinarySearchTree


class LinkedBinarySearchTreeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = LinkedBinarySearchTree()
        self.tree.add_all(1, 11, 4, -1, 2, 11, 22, 0, -3)

    def test_add(self):
        self.assertEqual(str(self.tree), "-3 -1 0 1 2 4 11 11 22")
        self.tree.add(5)
        self.assertEqual(str(self.tree), "-3 -1 0 1 2 4 5 11 11 22")

    def test_clear(self):
        self.assertFalse(self.tree.is_empty())
        self.tree.clear()
        self.assertEqual(str(self.tree), "")
        self.assertTrue(self.tree.is_empty())

    def test_delete(self):
        self.assertEqual(str(self.tree), "-3 -1 0 1 2 4 11 11 22")
        self.assertEqual(self.tree.delete(5), None)
        self.assertEqual(str(self.tree), "-3 -1 0 1 2 4 11 11 22")
        self.assertEqual(self.tree.delete(1), 1)
        self.assertEqual(str(self.tree), "-3 -1 0 2 4 11 11 22")
        self.assertEqual(self.tree.delete(11), 11)
        self.assertEqual(str(self.tree), "-3 -1 0 2 4 11 22")
        self.assertEqual(self.tree.delete(0), 0)
        self.assertEqual(str(self.tree), "-3 -1 2 4 11 22")
        self.assertEqual(self.tree.delete(0), None)
        self.assertEqual(str(self.tree), "-3 -1 2 4 11 22")

    def test_find(self):
        for value in self.tree:
            self.assertTrue(self.tree.find(value))
        self.assertFalse(self.tree.find(-2))
        self.assertFalse(self.tree.find(12))
        self.assertFalse(self.tree.find(-5))
        self.assertFalse(self.tree.find(500))

    def test_get_max(self):
        self.assertEqual(self.tree.get_max(), 22)
        self.tree.clear()
        self.assertEqual(self.tree.get_max(), None)

    def test_get_min(self):
        self.assertEqual(self.tree.get_min(), -3)
        self.tree.clear()
        self.assertEqual(self.tree.get_min(), None)

    def test_height(self):
        self.assertEqual(self.tree.height(), 4)
        self.tree.clear()
        self.assertEqual(self.tree.height(), 0)

    def test_is_empty(self):
        self.assertFalse(self.tree.is_empty())
        self.tree.clear()
        self.assertTrue(self.tree.is_empty())

    def test_eq(self):
        other = LinkedBinarySearchTree()
        other.add_all(22, 1, 4, 0, 11, -1, 2, -3, 11)
        self.assertEqual(self.tree, other)
        other.delete(0)
        self.assertNotEqual(self.tree, other)
        other.add(0)
        self.assertEqual(self.tree, other)
        other.add(17)
        self.assertNotEqual(self.tree, other)

    def test_iadd(self):
        other = LinkedBinarySearchTree()
        other.add_all(17, 2, 15, -9, 8, 11)
        self.tree += other
        self.assertEqual(str(self.tree), "-9 -3 -1 0 1 2 2 4 8 11 11 11 15 17 22")


if __name__ == '__main__':
    unittest.main()
