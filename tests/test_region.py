import unittest
from Set2Problem1.region import Region

class TestRegion(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.region = Region(name="test", kwargs={})

    def setUp(self):
        defenceKwargs = {'H':100, 'E':50, 'AT':10, 'SG':5}
        attackKwargs = {'H':250, 'E':50, 'AT':20, 'SG' : 15}

        self.defence = Region(name="defence", kwargs=defenceKwargs)
        self.attack = Region(name="attack", kwargs=attackKwargs)

    def test_isinstance(self):
        # """Testing if self is instance of Region."""
        # print('\n\n',unittest.TestCase.shortDescription(self))
        self.assertIsInstance(self.region, Region)

    def test_deployBattlian(self):
        # """Testing defence Battlian deployment against attack."""
        # print('\n\n',unittest.TestCase.shortDescription(self))
        self.defence.deployBattlian(self.attack, 'H')
        self.assertEqual(self.defence.H.size, -25)
        self.defence.deployBattlian(self.attack, 'E')
        self.assertEqual(self.defence.E.size, 25)
        self.defence.deployBattlian(self.attack, 'AT')
        self.assertEqual(self.defence.AT.size, 0)
        self.defence.deployBattlian(self.attack, 'SG')
        self.assertEqual(self.defence.SG.size, -3)

if __name__ == '__main__':
    unittest.main()
