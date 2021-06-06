from model.parser import *
from model.game import *

king = King(Colour.BLACK)
print(king)

pawn = Pawn(Colour.BLACK)
pawn2 = Pawn(Colour.WHITE)

board = Board()
print(board)

fp = FenParser("r4nk1/pp2r1p1/2p1P2p/3p1P1N/8/8/PPPK4/6RR w - - 0 1")
board.place_pieces(fp.parse())
print(board)