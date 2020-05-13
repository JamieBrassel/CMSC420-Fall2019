import unittest

from projects.pqueue.lists.LinkedList import LinkedList


class LinkedListTests(unittest.TestCase):
    def setUp(self) -> None:
        self.list = LinkedList()
        self.list.push_back_all(1, 11, 4, -1, 2, 11, 22, 0, -3)

    def test_clear(self):
        self.assertFalse(self.list.is_empty())
        self.list.clear()
        self.assertEqual("", str(self.list))
        self.assertTrue(self.list.is_empty())

    def test_contains(self):
        for value in self.list:
            self.assertTrue(self.list.contains(value))
        self.assertFalse(self.list.contains(-2))
        self.assertFalse(self.list.contains(12))
        self.assertFalse(self.list.contains(-5))
        self.assertFalse(self.list.contains(500))

    def test_delete(self):
        self.assertEqual("1 11 4 -1 2 11 22 0 -3", str(self.list))
        self.assertEqual(9, self.list.size)
        self.assertFalse(self.list.delete(5))
        self.assertEqual("1 11 4 -1 2 11 22 0 -3", str(self.list))
        self.assertTrue(self.list.delete(1))
        self.assertEqual("11 4 -1 2 11 22 0 -3", str(self.list))
        self.assertTrue(self.list.delete(11))
        self.assertEqual("4 -1 2 11 22 0 -3", str(self.list))
        self.assertTrue(self.list.delete(0))
        self.assertEqual("4 -1 2 11 22 -3", str(self.list))
        self.assertFalse(self.list.delete(0))
        self.assertEqual("4 -1 2 11 22 -3", str(self.list))
        self.assertTrue(self.list.delete(4))
        self.assertEqual("-1 2 11 22 -3", str(self.list))
        self.assertEqual(5, self.list.size)

    def test_delete_all(self):
        self.assertEqual("1 11 4 -1 2 11 22 0 -3", str(self.list))
        self.assertEqual(9, self.list.size)
        self.assertFalse(self.list.delete_all(5))
        self.assertEqual("1 11 4 -1 2 11 22 0 -3", str(self.list))
        self.assertTrue(self.list.delete_all(1))
        self.assertEqual("11 4 -1 2 11 22 0 -3", str(self.list))
        self.assertTrue(self.list.delete_all(11))
        self.assertEqual("4 -1 2 22 0 -3", str(self.list))
        self.assertTrue(self.list.delete_all(0))
        self.assertEqual("4 -1 2 22 -3", str(self.list))
        self.assertFalse(self.list.delete_all(0))
        self.assertEqual("4 -1 2 22 -3", str(self.list))
        self.assertTrue(self.list.delete_all(4))
        self.assertEqual("-1 2 22 -3", str(self.list))
        self.assertEqual(4, self.list.size)

    def test_delete_at(self):
        self.assertEqual("1 11 4 -1 2 11 22 0 -3", str(self.list))
        self.assertEqual(9, self.list.size)
        self.list.delete_at(0)
        self.assertEqual("11 4 -1 2 11 22 0 -3", str(self.list))
        self.list.delete_at(0)
        self.assertEqual("4 -1 2 11 22 0 -3", str(self.list))
        self.list.delete_at(5)
        self.assertEqual("4 -1 2 11 22 -3", str(self.list))
        self.list.delete_at(0)
        self.assertEqual("-1 2 11 22 -3", str(self.list))
        self.assertEqual(5, self.list.size)

    def test_is_empty(self):
        self.assertFalse(self.list.is_empty())
        self.list.clear()
        self.assertTrue(self.list.is_empty())

    def test_push_back(self):
        self.assertEqual("1 11 4 -1 2 11 22 0 -3", str(self.list))
        self.list.push_back(5)
        self.assertEqual("1 11 4 -1 2 11 22 0 -3 5", str(self.list))

    def test_eq(self):
        other = LinkedList()
        other.push_back_all(22, 1, 4, 0, 11, -1, 2, -3, 11)
        self.assertEqual(self.list, other)
        other.delete(0)
        self.assertNotEqual(self.list, other)
        other.push_back(0)
        self.assertEqual(self.list, other)
        other.push_back(17)
        self.assertNotEqual(self.list, other)

    def test_iadd(self):
        other = LinkedList()
        other.push_back_all(17, 2, 15, -9, 8, 11)
        self.list += other
        self.assertEqual("1 11 4 -1 2 11 22 0 -3 17 2 15 -9 8 11", str(self.list))


if __name__ == '__main__':
    unittest.main()
