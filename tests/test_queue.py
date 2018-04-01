import unittest
from collection import Queue


class QueueTestCase(unittest.TestCase):
    def test_queue(self):
        queue = Queue()
        queue.offer(1)
        queue.offer(2)
        self.assertEqual(1, queue.get(0))
        self.assertEqual(2, queue.get(1))
        self.assertEqual(1, queue.peek())
        self.assertEqual(1, queue.poll())
        self.assertEqual(2, queue.poll())
        self.assertTrue(queue.empty())

    def test_stack_empty(self):
        queue = Queue()
        self.assertTrue(queue.empty())
        self.assertEqual(None, queue.poll())


if __name__ == '__main__':
    unittest.main()
