from library.parser import *
from model.piece import *
from model.game import *


fp = FenParser("r1bqkbnr/pppppppp/8/8/4K3/8/PPPPPPPP/RNBQ1B1R w kq - 0 1")
fp.parse()
chess_game = ChessGame()
chess_game.variant.load_rules()
chess_game.board.load_from_fen(fp)

rank = 4
file = 4

piece = chess_game.board.get_piece(rank, file)
print(piece.name)
print(chess_game.board.get_available_moves(rank, file))
print(chess_game.board)
chess_game.board.move_to(0, 0, 1, 0)
print(chess_game.board)

"""
fp = FenParser("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
fp.parse()
chess_game = ChessGame()
chess_game.variant.load_rules()
chess_game.board.load_from_fen(fp)

print(chess_game.board)
print('bishop')
print(chess_game.board.get_available_moves(2, 7))
print('rook')
print(chess_game.board.get_available_moves(0, 0))
print('queen')
print(chess_game.board.get_available_moves(3, 0))
print('knight')
print(chess_game.board.get_available_moves(1, 0))
print('king')
print(chess_game.board.get_available_moves(4, 0))
print('pawn')
print(chess_game.board.get_available_moves(0, 6))
"""
