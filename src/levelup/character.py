

from levelup.gamemap import GameMap
from levelup.direction import Direction
from levelup.position import Position
class Character:


    name = ""
    current_position :Position = Position(0,0)
    gamemap :GameMap = GameMap()

    def __init__(self, character_name):
        self.name = character_name
    
    def getName(self):
        return self.getName()

    def getPosition(self):
        return self.position
        
    def setPosition(self, position):
        self.position = position1
        
    def enterMap(self, gamemap):
        self.gamemap = gamemap

    def move(self, direction :Direction) -> None:
        self.current_position=self.gamemap.calculate_new_position(self.current_position, direction)
    
  