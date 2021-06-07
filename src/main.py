from library.parser import *
import library.parser.annotator as annotator
from model.piece import *
from model.game import *
import model.game.game_helper as gh


fp = FenParser("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
fp.parse()
chess_game = ChessGame()
chess_game.variant.load_rules()
chess_game.board.load_from_fen(fp)


print(chess_game.board)
# chess_game.board.move_to(0, 0, 0, 0)
# print(chess_game.board)
# annotator.annotate_move(chess_game.board, (4, 6), (4, 4))

pawns = chess_game.board.filter_piece_list(piece_filter="Pawn", colour_filter=Colour.WHITE)
print(pawns)


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