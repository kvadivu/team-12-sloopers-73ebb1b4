from levelup.positionStub import Position

class PositionLibrary:
    x: int
    y: int

    def initialize_character_xposition_with(self, x_position):
        self.start_x = x_position

    def initialize_character_yposition_with(self, y_position):
        self.start_y = y_position

    def initialize_character_movecount_with(self, move_count):
        self.controller.set_current_move_count(move_count)

    def move_in_direction(self, direction):
        self.controller.set_character_position((self.start_x, self.start_y))
        self.controller.move(Direction[direction])

    def character_xposition_should_be(self, expected):
        x = self.getX
        assert x == 3

    def character_yposition_should_be(self, expected):
        y = self.y
        assert y == 4

   
