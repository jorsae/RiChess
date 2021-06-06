from model.parser import *
from model.game import *

king = King(Colour.BLACK)
print(king)

pawn = Pawn(Colour.BLACK)
pawn2 = Pawn(Colour.WHITE)

board = Board()
print(board)

fp = FenParser("8/ppp1k3/8/8/8/8/PP6/RN1K3R w KQ - 0 1")
board.place_pieces(fp.parse())
print(board)