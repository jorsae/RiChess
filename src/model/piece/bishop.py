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
        return [(1, 1)]
        # TODO: Change this to a MoveDescription obj