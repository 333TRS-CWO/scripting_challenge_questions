from word_sort import word_sort
import unittest

class SimpleTest(unittest.TestCase):

    def test_first(self):
        self.assertEqual(word_sort("Who is your daddy, and what does he do?"), "is he Who and do? your what does daddy,")

    def test_second(self):
        self.assertEqual(word_sort("Don't do chasing waterfalls, Please stick to the rivers and the lakes that you're used to"), "go to to the and the that used Don't stick lakes Please  rivers you're chasing waterfalls,")


if __name__ == "__main__":
    unittest.main()