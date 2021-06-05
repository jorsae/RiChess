class FenParser:
    def __init__(self, fen):
        self.fen = fen
    
    def parse(self):
        ranks = self.fen.split(" ")[0].split("/")
        print(ranks)