from challenges.groceries import groceries
import unittest

class SimpleTest(unittest.TestCase):

    def test_first(self):
        self.assertEqual(groceries(["22-Popsicle", "37-Milk", "68-Bread", "70-Chips", "20-Chicken", "39-OJ"]), [["Popsicle","Chicken"],["Milk", "OJ"],["Bread", "Chips"]])

    def test_second(self):
        self.assertEqual(groceries(["32-Ice","33-Cheese", "40-Eggs", "60-Pop-Tarts", "21-Pizza", "66-Apple"]), [["Ice", "Pizza"], ["Cheese", "Eggs"], ["Pop-Tarts", "Apple"]])


if __name__ == "__main__":
    unittest.main()