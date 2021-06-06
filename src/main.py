from model.parser import *
from model.piece import *


board = Board()

fp = FenParser("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
fp.parse()
board.load_from_fen(fp)
print(board)
print(f'{board.turn} {board.halfmove} : {board.fullmove}')