from first_and_last import first_and_last
import unittest

class SimpleTest(unittest.TestCase):

    def test_first(self):
        self.assertEqual(first_and_last("These examples should work"), "Te es sd wk")

    def test_second(self):
        self.assertEqual(first_and_last("As long as the words have more than one letter"), "As lg as te ws he me tn oe lr")


if __name__ == "__main__":
    unittest.main()