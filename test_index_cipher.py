from index_cipher import index_cipher
import unittest

class SimpleTest(unittest.TestCase):

    def test_first(self):
        self.assertEqual(index_cipher(["hole", "03221"]), "hello")

    def test_second(self):
        self.assertEqual(index_cipher(["python", "0452445"]), "pontoon")


if __name__ == "__main__":
    unittest.main()