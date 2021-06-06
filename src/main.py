from model.parser import *
from model.piece import *
from model.game import *


fp = FenParser("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
fp.parse()
chess_game = ChessGame()
chess_game.variant.load_rules()
chess_game.board.load_from_fen(fp)

print(chess_game.board)

bishop = chess_game.board.get_piece(2, 7)
print(bishop.name)
chess_game.board.get_available_moves(2, 7)
print('rook')
chess_game.board.get_available_moves(0, 0)
print('queen')
chess_game.board.get_available_moves(3, 0)
print('knight')
chess_game.board.get_available_moves(1, 0)
print('king')
chess_game.board.get_available_moves(4, 0)