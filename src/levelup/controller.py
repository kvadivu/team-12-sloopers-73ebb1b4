import logging
from dataclasses import dataclass
from enum import Enum
from levelup.character import Character


DEFAULT_CHARACTER_NAME = "Character"

#TODO: ADD THINGS YOU NEED FOR STATUS
@dataclass
class GameStatus:
    running: bool = False
    character_name: str = DEFAULT_CHARACTER_NAME
    # NOTE - Game status will have this as a tuple. The Position should probably be in a class
    current_position: tuple = (-100,-100)
    move_count: int = 0

class Direction(Enum):
    NORTH = "n"
    SOUTH = "s"
    EAST = "e"
    WEST = "w"

class CharacterNotFoundException(Exception):
    pass

class InvalidMoveException(Exception):
    pass

class GameController:


    status: GameStatus
    character: Character

    def __init__(self):
        self.status = GameStatus()

    def start_game(self):
        pass

    # Pre-implemented to demonstrate ATDD
    def create_character(self, character_name: str) -> None:
        if character_name is None or character_name == "":
            self.status.character_name = DEFAULT_CHARACTER_NAME
        else:
            self.status.character_name = character_name
        self.status.character_name = self.character.character_name

    def move(self, direction: Direction) -> None:
        self.character.move(direction)
        self.status.current_position = (self.character.current_position.x, self.character.current_position.y)
        self.status.move_count = self.status.move_count + 1
        status.movecount
   
    def set_character_position(self, xycoordinates: tuple) -> None:
        x = xycoordinates[0]
        y = xycoordinates[1]
        self.character.current_position = Position(x,y)
        self.status.current_position = xycoordinates

    def set_current_move_count(self, move_count: int) -> None:
        # IMPLEMENT THIS TO SET CURRENT MOVE COUNT -- exists to be testable
        self.status.move_count = move_count
        
    def get_total_positions(self) -> int:
        # IMPLEMENT THIS TO GET THE TOTAL POSITIONS FROM THE MAP - - exists to be
        # testable
        return self.character.gamemap.getTotalPositions()
        

    
