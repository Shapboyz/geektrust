import unittest
from Set2Problem1.war import createRegion, compareArmyStrength
from Set2Problem1.region import Region

class TestWar(unittest.TestCase):

    def setUp(self):
        defaultStr = [100, 'H', 50, 'E',10, 'AT', 5, 'SG']
        self.default = createRegion()
        self.lengaburu = createRegion(name="lengaburu", userInput=defaultStr)
        self.assertIsInstance(self.default, Region)
        self.assertIsInstance(self.lengaburu, Region)

    def test_createRegion(self):
        # """Testing Region Creation with user input"""
        # print('\n\n',unittest.TestCase.shortDescription(self))

        self.assertEqual(self.lengaburu.__name__, 'lengaburu')
        self.assertEqual(self.default.__name__, 'Temp')
        self.assertEqual(str(self.lengaburu), str(self.default))


    def test_compareArmyStrength(self):
        # """Testing battlian deployment and result of war of some test cases."""
        # print('\n\n',unittest.TestCase.shortDescription(self))

        # Input: Falicornia attacks with 100 H, 101 E, 20 AT, 5 SG
        # Expected Output: Lengaburu deploys 52 H, 50 E, 10 AT, 3 SG and wins

        defaultattack1 = [100, 'H', 101, 'E', 20, 'AT', 5, 'SG']
        self.attack1 = createRegion(name="attack1", userInput=defaultattack1)
        self.assertEqual(compareArmyStrength(self.lengaburu, self.attack1),
            "Lengaburu deploys 52 H, 50 E, 10 AT, 3 SG and wins")


        # Input: Falicornia attacks with 150 H, 96 E, 26 AT, 8 SG
        # Expected Output: Lengaburu deploys 75 H, 50 E, 10 AT, 5 SG and wins

        defaultattack2 = [150, 'H', 96, 'E', 26, 'AT', 8, 'SG']
        self.attack1 = createRegion(name="attack1", userInput=defaultattack2)
        self.assertEqual(compareArmyStrength(self.lengaburu, self.attack1),
            "Lengaburu deploys 75 H, 50 E, 10 AT, 5 SG and wins")

        # Input: Falicornia attacks with 250 H, 50 E, 20 AT, 15 SG
        # Expected Output: Lengaburu deploys 100 H, 38 E, 10 AT, 5 SG and loses
        defaultattack3 = [250, 'H', 50, 'E', 20, 'AT', 15, 'SG']
        self.attack1 = createRegion(name="attack1", userInput=defaultattack3)
        self.assertEqual(compareArmyStrength(self.lengaburu, self.attack1),
            "Lengaburu deploys 100 H, 38 E, 10 AT, 5 SG and loses")

        # Input: Falicornia attacks with 250 H, 50 E, 20 AT, 1 SG, 1 DF
        # Expected Output: Lengaburu deploys 100 H, 38 E, 10 AT, 3 SG and loses
        defaultattack3 = [200, 'H', 100, 'E', 20, 'AT', 1, 'SG', 1, 'DF']
        self.attack1 = createRegion(name="attack1", userInput=defaultattack3)
        self.assertEqual(compareArmyStrength(self.lengaburu, self.attack1),
            "Lengaburu deploys 100 H, 50 E, 10 AT, 3 SG and wins")
