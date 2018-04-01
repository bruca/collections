import unittest
from collection import List


class ListTestCase(unittest.TestCase):
    def test_vector(self):
        l = List()
        l.add(1)
        self.assertTrue(l.empty() is False)

    def test_vector_empty(self):
        l = List()
        self.assertTrue(l.empty())


if __name__ == '__main__':
    unittest.main()
