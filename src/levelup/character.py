class Character:

    name = ""
    position=0
    gamemap=""

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

    def move(self, direction):
        self.gamemap.calculatePosition(position, direction)
    
    