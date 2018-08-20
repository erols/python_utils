import unittest
import deque


class TestDeque(unittest.TestCase):

    def test_create_deque(self):
        test_deque = deque.Deque()
        self.assertEqual(test_deque.is_empty(), True)
        self.assertEqual(test_deque.size(), 0)


    def test_add_deque(self):
        test_deque = deque.Deque()
        test_deque.add_front("cat")
        self.assertEqual(test_deque.size(), 1)
        test_deque.add_front("dog")
        self.assertEqual(test_deque.size(), 2)
        test_deque.add_front(1)
        self.assertEqual(test_deque.size(), 3)


    def test_remove_deque(self):
        test_deque = deque.Deque()
        test_deque.add_front("cat")
        test_deque.add_front("dog")
        test_deque.add_front(1)
        self.assertEqual(test_deque.remove_rear(), "cat")
        self.assertEqual(test_deque.remove_front(), 1)


