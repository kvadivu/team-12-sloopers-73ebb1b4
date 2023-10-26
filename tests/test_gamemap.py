from unittest import TestCase
from levelup.gamemap import GameMap

class TestCharacterInitWithName(TestCase):
    def test_init(self):
        numpositions = 5
        
        gm = GameMap (4)
        testobj = GameMap (4)
        self.assertEqual(gm.numpositions, testobj.numpositions)


