from library.parser import *
import library.parser.annotator as annotator
from model.piece import *
from model.game import *
import model.game.game_helper as gh


fp = FenParser("r1b1kbnr/pppppppp/2n5/5K2/3q4/8/PPPPPPPP/RNBQ1BNR w kq - 0 1")
fp = FenParser("8/r1B2kBp/2q5/8/b6n/2B3B1/P1P1P1P1/RN1QKBNR w KQ - 11 27")
fp.parse()
chess_game = ChessGame()
chess_game.variant.load_rules()
chess_game.board.load_from_fen(fp)

print(chess_game.board)
print(gh.get_available_moves(chess_game.board, 5, 3))

# chess_game.board.move_to(0, 0, 0, 0)
# print(chess_game.board)
annotator.annotate_move(chess_game.board, (5, 1), (4, 3))

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