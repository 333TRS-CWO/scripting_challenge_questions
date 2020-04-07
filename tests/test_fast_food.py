from challenges.fast_food import fast_food
import unittest

class SimpleTest(unittest.TestCase):

    def test_first(self):
        self.assertEqual(fast_food([1,2,3]), ['burger', 'fries', 'fries','drink','drink','drink'])

    def test_second(self):
        self.assertEqual(fast_food([2, 3, 1]), ['burger', 'burger', 'fries', 'fries', 'fries', 'drink'])


if __name__ == "__main__":
    unittest.main()