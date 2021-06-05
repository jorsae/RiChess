class BoardPiece:
    def __init__(self, piece, rank, file):
        self.piece = piece
        self.rank = rank
        self.file = file
    
    def __eq__(self, other):
        if self.piece == self.piece and self.rank == other.rank and self.file == other.file:
            return True
        else:
            return False