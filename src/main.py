from model.parser import *
from model.game import *


board = Board()

fp = FenParser("7k/p1p2p1p/3p4/1p2pP2/1PP4P/3PP1p1/P5P1/RNBQKBNR w K    q e6 0 8")
fp.parse()
board.load_from_fen(fp)
print(fp.has_moved)