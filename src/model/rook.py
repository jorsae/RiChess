from interface import Piece

class Rook(Piece):
    @property
    def name(self):
        return "Rook"
    
    @property
    def abbreviation(self):
        return "R"
    
    @property
    def value(self):
        return 5
    
    @property
    def movement(self):
        pass