from tacos import tacos
import unittest

class SimpleTest(unittest.TestCase):

    def test_first(self):
        self.assertEqual(tacos(['chicken','salsa','guac','cheese','tomato']), ['salsa','cheese','tomato'])

    def test_second(self):
        self.assertEqual(tacos(['beef','tomato','cheese','cabbage','hot sauce']), ['beef','tomato','cheese'])


if __name__ == "__main__":
    unittest.main()