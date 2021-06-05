from model.interface import Piece

class Knight(Piece):
    @property
    def name(self):
        return "Knight"
    
    @property
    def abbreviation(self):
        return "N"
    
    @property
    def value(self):
        return 3
    
    @property
    def movement(self):
        pass