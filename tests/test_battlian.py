import unittest
from Set2Problem1.battlian import Battlian

class TestBattlian(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # print("""\n\nSetting up class required instances that are not going to
        # change.""")
        cls.batt_1 = Battlian(5)
        cls.batt_2 = Battlian(10)


    def setUp(self):
        # print("""\n\nSetting up tests required instances and testing instance
        # assertEqual.""")

        self.curr = Battlian(-10)
        self.assertIsNotNone(self.batt_1)
        self.assertIsNotNone(self.batt_2)
        self.assertIsNotNone(self.curr)

        self.assertIsInstance(self.batt_1, Battlian)
        self.assertIsInstance(self.batt_2, Battlian)
        self.assertIsInstance(self.curr, Battlian)

    def test_sub(self):
        # """Testing opertor overloading for minus"""
        # print('\n\n',unittest.TestCase.shortDescription(self))
        self.batt_1 - self.batt_2
        self.assertEqual(self.batt_1.size, 0,
            msg="Test fail for Battlian.__sub__")

    def test_borrowFromLowerBatt(self):
        # """Testing borrowing from lower Battlians."""
        # print('\n\n',unittest.TestCase.shortDescription(self))
        self.lower = Battlian(20)
        self.curr.borrowFromLowerBatt(self.lower)
        self.assertEqual(self.curr.size, 0)
        self.assertEqual(self.lower.size, 0)

    def test_borrowFromHigherBatt(self):
        # """Testing borrowing from Higher Battlians."""
        # print('\n\n',unittest.TestCase.shortDescription(self))
        self.higher = Battlian(5)
        self.curr.borrowFromHigherBatt(self.higher)
        self.assertEqual(self.curr.size, 0)
        self.assertEqual(self.higher.size, 0)


if __name__ == '__main__':
    unittest.main()
