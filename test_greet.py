from greet import greet
import unittest

class SimpleTest(unittest.TestCase):

    def test_first(self):
        self.assertEqual(greet("epi"), "Hello, epi.")

    def test_second(self):
        self.assertEqual(greet("darkness, my old friend"), "Hello, darkness, my old friend.")


if __name__ == "__main__":
    unittest.main()