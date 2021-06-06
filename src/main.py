from model.parser import *
from model.piece import *
from model.game import *


fp = FenParser("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
fp.parse()
chess_game = ChessGame()
chess_game.variant.load_rules()
chess_game.board.load_from_fen(fp)

print(chess_game.board)

bishop = chess_game.board.get_piece(7, 2)
print(bishop.name)
# for p in chess_game.board.get_piece_list():
    # print(p)