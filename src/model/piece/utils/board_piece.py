class BoardPiece:
    def __init__(self, piece, rank, file):
        self.piece = piece
        self.rank = rank
        self.file = file
    
    def __eq__(self, other):
        if self.piece == other.piece and self.rank == other.rank and self.file == other.file:
            return True
        else:
            return False
    
    def __str__(self):
        return f'{self.piece.name}({self.piece.colour}): {self.rank}, {self.file}'
    
    def __repr__(self):
        return self.__str__()