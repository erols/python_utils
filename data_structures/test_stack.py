import unittest
import stack


class StackTest(unittest.TestCase):

    def test_create_stack(self):
        test_stack = stack.Stack()
        self.assertEqual(test_stack.size(), 0)


    def test_push_stack(self):
        test_stack = stack.Stack()
        test_stack.push(5)
        self.assertEqual(test_stack.size(), 1)
        test_stack.push('two')
        self.assertEqual(test_stack.size(), 2)
        test_stack.push(True)
        self.assertEqual(test_stack.size(), 3)
        self.assertIsInstance(test_stack.pop(), bool)
        self.assertIsInstance(test_stack.pop(), str)
        self.assertIsInstance(test_stack.pop(), int)
        self.assertEqual(test_stack.size(), 0)


    def test_peek_stack(self):
        test_stack = stack.Stack()
        test_stack.push(5)
        self.assertEqual(test_stack.peek(), 5)
        test_stack.push("Three")
        self.assertEqual(test_stack.peek(), "Three")
        test_stack.push(False)
        self.assertEqual(test_stack.peek(), False)


    def test_pop_stack(self):
        test_stack = stack.Stack()
        test_stack.push(5)
        test_stack.push("hello")
        test_stack.push(True)
        self.assertEqual(test_stack.pop(), True)
        self.assertEqual(test_stack.pop(), "hello")
        self.assertEqual(test_stack.pop(), 5)
        self.assertEqual(test_stack.is_empty(), True)


if __name__ == "__main__":
    unittest.main()
