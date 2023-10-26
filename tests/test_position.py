from unittest import TestCase
from levelup.position import Position

class TestCharacterInitWithName(TestCase):
    def test_init(self):
        X=3
        Y=5
        pos = Position(5,6)
        testobj = Position(5,6)
        self.assertEqual(pos.x, testobj.x)


