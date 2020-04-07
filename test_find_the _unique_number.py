from find_the_unique_number import find_the_unique_number
import unittest

class SimpleTest(unittest.TestCase):

    def test_first(self):
        self.assertEqual(find_the_unique_number([2, 2, 3, 4, 1, 3, 5, 5, 4]), 1)

    def test_second(self):
        self.assertEqual(find_the_unique_number([6, 5, 4, 3, 2, 1, 7, 1, 2, 3, 4, 5, 6]), 7)


if __name__ == "__main__":
    unittest.main()