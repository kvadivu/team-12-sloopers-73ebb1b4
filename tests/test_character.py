from unittest import TestCase
from levelup.character import Character
from levelup.gamemap import GameMap
from levelup.direction import Direction
from fake_map import FakeMap
from levelup.position import Position

class TestCharacterInitWithName(TestCase):
    ARBITRARY_NAME = "MyName"

    def test_init(self):   
        testobj = Character(self.ARBITRARY_NAME)
        self.assertEqual(self.ARBITRARY_NAME, testobj.name)

    def TestCharacterInitWithPosition(self):
        testobj=Character(self.ARBITRARY_NAME)
        
        stubbed_map = FakeMap()
        testobj.enter_map(stubbed_map)
        self.assertEqual(stubbed_map, testobj.gamemap)
        self.assertEqual(testobj.current_position, stubbed_map.starting_position)

    def test_move_updates_position(self):
        testobj = Character(self.ARBITRARY_NAME)
        stubbed_map = FakeMap()
        testobj.map = stubbed_map
        pos = Position(0,0)
        testobj.move( Direction.EAST)

        self.assertEqual(stubbed_map.STUBBED_X, testobj.current_position.x)
        self.assertEqual(stubbed_map.STUBBED_Y, testobj.current_position.y)
        
       




