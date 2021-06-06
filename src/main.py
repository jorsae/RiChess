from model.parser import *
from model.game import *


board = Board()

fp = FenParser("1r1qkb1r/p3ppp1/2p1bn1p/8/2B1Pp2/2N1B2P/PP2Q1P1/2R2RK1 w Q g3 19 25")
fp.parse()
board.load_from_fen(fp)
print(fp.has_moved)