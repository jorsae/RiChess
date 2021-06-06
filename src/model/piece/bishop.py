from model.interface import Piece

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
    
    @staticmethod
    def movement():
        return Movement[(0, 1), (1, 1)]