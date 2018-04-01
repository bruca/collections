import unittest
from collection import Stack


class StackTestCase(unittest.TestCase):
    def test_stack(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(1, stack.get(0))
        self.assertEqual(2, stack.get(1))
        self.assertEqual(2, stack.peek())
        self.assertEqual(2, stack.pop())
        self.assertEqual(1, stack.pop())
        self.assertTrue(stack.empty())

    def test_stack_empty(self):
        stack = Stack()
        self.assertTrue(stack.empty())
        self.assertEqual(None, stack.pop())


if __name__ == '__main__':
    unittest.main()
