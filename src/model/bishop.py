from interface import Piece

class Bishop(Piece):
    @property
    def name(self):
        return "Bishop"
    
    @property
    def abbreviation(self):
        return "B"
    
    @property
    def value(self):
        return 3
    
    @property
    def movement(self):
        pass