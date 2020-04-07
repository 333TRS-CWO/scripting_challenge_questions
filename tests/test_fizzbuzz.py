from challenges.fizzbuzz import fizzbuzz
import unittest

class SimpleTest(unittest.TestCase):

    def test_divisible_by_three(self):
        self.assertEqual(fizzbuzz(9), 'Fizz')

    def test_divisible_by_five(self):
        self.assertEqual(fizzbuzz(25), "Buzz")
    
    def test_divisible_by_there_and_five(self):
        self.assertEqual(fizzbuzz(30), "FizzBuzz")

if __name__ == "__main__":
    unittest.main()