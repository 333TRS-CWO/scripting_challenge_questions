from phone_filter import phone_filter
import unittest

class SimpleTest(unittest.TestCase):

    def test_first(self):
        self.assertEqual(phone_filter(["(702)-388-2345", "(208)-577-7821","(228)-798-5656","(321)-188-7765"]), 2)

    def test_second(self):
        self.assertEqual(phone_filter(["(223)-128-2745","(208)-577-7782","(128)-628-5152","(222)-173-3265"]), 0)


if __name__ == "__main__":
    unittest.main()