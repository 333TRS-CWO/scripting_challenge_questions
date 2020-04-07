from binary_words import binary_words
import unittest

class SimpleTest(unittest.TestCase):

    def first(self):
        self.assertEqual(binary_words("Words can have different lengths"), "11011")

    def second(self):
        self.assertEqual(binary_words("Examples are hard to make"), '01000')


if __name__ == "__main__":
    unittest.main()