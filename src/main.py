from library.parser import *
import library.parser.uci as uci
import library.parser.annotator as annotator
from model.piece import *
from model.game import *
import model.game.game_helper as gh


def play_game(fen):
    fp = FenParser(fen)
    fp.parse()

    chess_game = ChessGame()
    chess_game.variant.load_rules()
    chess_game.board.load_from_fen(fp)
    play = True
    while play:
        move = input('move: ')
        if move == 'q':
            play = False
            continue
        elif move == 'board':
            print(chess_game.board)
        elif move == 'pl':
            p = input('piece: ')
            if p == '':
                pieces = chess_game.board.filter_piece_list()
                print(pieces)
            else:
                pieces = chess_game.board.filter_piece_list(piece_filter=p)
                print(pieces)
        elif move == 'mh':
            print(chess_game.board.move_history)
        elif move == 'amove':
            sq = input('square:')
            rank, file = uci.untranslate_square(sq[:1], sq[1:])
            print('available moves for')
            print(gh.get_available_moves(chess_game.board, rank, file))
        start, end = uci.get_move(move)
        if start is not None and end is not None:
            annotation = annotator.annotate_move(chess_game.board, start, end, None)
            chess_game.board.move_to(start, end)
            print(chess_game.board)
            print(annotation)

# play_game("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
play_game("rnb1kbnr/ppp1pppp/4q3/8/8/8/PPPPQPPP/RNB1KBNR w KQkq - 2 4")

# fp = FenParser("r1b1kbnr/pppppppp/2n5/5K2/3q4/8/PPPPPPPP/RNBQ1BNR w kq - 0 1")
# fp = FenParser("8/r1B2kBp/2q5/8/b6n/2B3B1/P1P1P1P1/RN1QKBNR w KQ - 11 27")
# fp = FenParser("8/rPB2kBp/2q5/4p3/b6n/2B3B1/P1P1P3/RN1QKBNR w KQ - 11 27")
# # ("8/r1B2kBp/2q5/8/b6n/2B3B1/P1P1P1P1/RN1QKBNR w KQ - 11 27", (6, 5), (4, 3), 'Bhe5'),
# fp.parse()
# chess_game = ChessGame()
# chess_game.variant.load_rules()
# chess_game.board.load_from_fen(fp)

# print(chess_game.board)
# print(gh.get_available_moves(chess_game.board, 5, 3))

# # print(chess_game.board)
# annotation = annotator.annotate_move(chess_game.board, (6, 5), (4, 3))
# print(annotation)
# print(chess_game.board)
# chess_game.board.move_to((1, 1), (1, 0))
# print(chess_game.board)


# fp = FenParser("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
# fp.parse()
# chess_game = ChessGame()
# chess_game.variant.load_rules()
# chess_game.board.load_from_fen(fp)

# print(chess_game.board)
# print('bishop')
# print(chess_game.board.get_available_moves(2, 7))
# print('rook')
# print(chess_game.board.get_available_moves(0, 0))
# print('queen')
# print(chess_game.board.get_available_moves(3, 0))
# print('knight')
# print(chess_game.board.get_available_moves(1, 0))
# print('king')
# print(chess_game.board.get_available_moves(4, 0))
# print('pawn')
# print(chess_game.board.get_available_moves(0, 6))