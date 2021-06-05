from interface import Piece

class Pawn(Piece):
    @property
    def name(self):
        return "Pawn"
    
    @property
    def abbreviation(self):
        return "p"
    
    @property
    def value(self):
        return 1
    
    @property
    def movement(self):
        pass