from sum_em_up import sum_em_up
import unittest

class SimpleTest(unittest.TestCase):

    def test_first(self):
        self.assertEqual(sum_em_up(123), 6)

    def test_second(self):
        self.assertEqual(sum_em_up(451), 10)


if __name__ == "__main__":
    unittest.main()