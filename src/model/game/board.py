from model.interface import IBoard

# rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1

class Board(IBoard):
    def parse(self, fen):
        ranks = fen.split(" ")[0].split("/")
        print(ranks)
    
    def parse_ranks(self, fen):
        pass

# rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1