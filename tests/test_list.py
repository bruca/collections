import unittest
from collection import List


class ListTestCase(unittest.TestCase):
    def test_vector(self):
        l = List()
        l.add(1)
        self.assertTrue(l.is_empty() is False)

    def test_vector_empty(self):
        l = List()
        self.assertTrue(l.is_empty())


if __name__ == '__main__':
    unittest.main()
