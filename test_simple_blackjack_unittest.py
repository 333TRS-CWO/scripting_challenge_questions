from simple_blackjack import simple_blackjack
import unittest

class SimpleTest(unittest.TestCase):



    def test_number_over_twelve(self):
        self.assertEqual(simple_blackjack([10, 11, 12]), -1, "Passed a number greater than 11, Should return -1")
    
    def test_over_21_with_11(self):
        self.assertEqual(simple_blackjack([11, 11, 11]), 13 )
        self.assertEqual(simple_blackjack([10, 11, 11]), 12 )
        self.assertEqual(simple_blackjack([11,11,11,10,11]), 14)

    def test_over_21(self):
        self.assertEqual(simple_blackjack([9, 8, 10]), 0, "Should be 0")

    def test_sum_under_22(self):
        self.assertEqual(simple_blackjack([11,10]), 21)
        self.assertEqual(simple_blackjack([4,10,6]), 20)

if __name__ == "__main__":
    unittest.main()