from expand import expand
import unittest

class SimpleTest(unittest.TestCase):

    def test_first(self):
        self.assertEqual(expand(123), "100 + 20 + 3")

    def test_second(self):
        self.assertEqual(expand(605030), "600000 + 5000 + 30")


if __name__ == "__main__":
    unittest.main()