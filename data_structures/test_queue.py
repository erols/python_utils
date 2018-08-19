import unittest
import queue

class QueueTest(unittest.TestCase):

    def test_create_queue(self):
        test_queue = queue.Queue()
        self.assertEqual(test_queue.size(), 0)
        self.assertEqual(test_queue.is_empty(), True)


    def test_enqueue_queue(self):
        test_queue = queue.Queue()
        test_queue.enqueue(1)
        self.assertEqual(test_queue.size(), 1)
        test_queue.enqueue("Two")
        self.assertEqual(test_queue.size(), 2)
        test_queue.enqueue(False)
        self.assertEqual(test_queue.size(), 3)


    def test_dequeue_queue(self):
        test_queue = queue.Queue()
        test_queue.enqueue(1)
        test_queue.enqueue("two")
        test_queue.enqueue(True)
        self.assertEqual(test_queue.dequeue(), True)
        self.assertEqual(test_queue.dequeue(), "two")
        self.assertEqual(test_queue.dequeue(), True)
        self.assertEqual(test_queue.is_empty(), True)
