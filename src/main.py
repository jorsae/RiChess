from model.parser import *
from model.game import *


board = Board()

fp = FenParser("r4nk1/pp2r1p1/2p1P2p/3p1P1N/8/8/PPPK4/6RR w - e3 0 1")
fp.parse()
board.load_from_fen(fp)
print(board.move_history)