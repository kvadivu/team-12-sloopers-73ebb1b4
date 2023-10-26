from unittest import TestCase
from levelup.character import Character

class TestCharacterInitWithName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = "MyName"
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.name)

    def TestCharacterInitWithPosition(TestCase):
        ARBITRARY_NAME = "MyName"
        testobj = Character(ARBITRARY_NAME)
        testobj.setPosition(current_position)
        compare_position = Position(2,3)
        self.assertEqual(compare_position, testobj1.position)




