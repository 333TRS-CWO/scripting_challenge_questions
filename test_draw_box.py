from draw_box import draw_box
import unittest

class SimpleTest(unittest.TestCase):

    def test_first(self):
        self.assertEqual(draw_box(3), ["XXX","X X", "XXX"])

    def test_second(self):
        self.assertEqual(draw_box(5), ["XXXXX", "X   X", "X   X", "X   X", "XXXXX"])


if __name__ == "__main__":
    unittest.main()