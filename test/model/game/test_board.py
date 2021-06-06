import pytest
import sys
sys.path.append('src')
from model.piece import *
from library.parser import *
from model.game import *

board = Board()

def test_board():
    expected = [[None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None]]
    assert(board.board) == expected

def test_board_str():
    assert(str(board)) == """ 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
"""


@pytest.mark.parametrize("board_piece", [
    (BoardPiece(King(Colour.WHITE), 6, 6)),
    (BoardPiece(King(Colour.BLACK), 1, 0)),
    (BoardPiece(Queen(Colour.WHITE), 3, 2)),
    (BoardPiece(Queen(Colour.BLACK), 0, 3)),
    (BoardPiece(Rook(Colour.WHITE), 3, 0)),
    (BoardPiece(Rook(Colour.BLACK), 2, 1)),
    (BoardPiece(Bishop(Colour.WHITE), 6, 3)),
    (BoardPiece(Bishop(Colour.BLACK), 7, 5)),
    (BoardPiece(Knight(Colour.WHITE), 0, 7)),
    (BoardPiece(Knight(Colour.BLACK), 0, 0)),
    (BoardPiece(Pawn(Colour.WHITE), 1, 1)),
    (BoardPiece(Pawn(Colour.BLACK), 2, 0)),
])
def test_place_piece(board_piece):
    chess_board = Board()
    chess_board.place_piece(board_piece.piece, board_piece.rank, board_piece.file)
    piece = chess_board.get_piece(board_piece.rank, board_piece.file)
    assert(board_piece.piece) == piece

testdata_test_place_piece = [
    ([BoardPiece(Pawn(Colour.BLACK), 1, 4)]),
    ([BoardPiece(Pawn(Colour.BLACK), 2, 2), BoardPiece(Queen(Colour.WHITE), 3, 2), BoardPiece(Rook(Colour.WHITE), 3, 6)]),
    ([BoardPiece(King(Colour.WHITE), 1, 4), BoardPiece(Knight(Colour.WHITE), 1, 4), BoardPiece(Rook(Colour.BLACK), 1, 4), BoardPiece(Rook(Colour.WHITE), 1, 4), BoardPiece(Queen(Colour.WHITE), 1, 4)]),
]

@pytest.mark.parametrize("piece_list", testdata_test_place_piece)
def test_get_piece_list(piece_list):
    chess_board = Board()
    for bp in piece_list:
        chess_board.place_piece(bp.piece, bp.rank, bp.file)
    
    bp_list = chess_board.get_piece_list()
    for index in range(len(bp_list)):
        assert(bp_list[index]) == piece_list[index]

@pytest.mark.parametrize("fen, expected_player_turn, expected_halfmove, expected_fullmove, expected_move_history, expected_has_moved", [
    ("8/ppp1k3/8/8/8/8/PP6/RN1K3R w KQ e3 0 1", Colour.WHITE, 0, 1, ["e3"], [(0, 0), (4, 0), (7, 0)]),
    ("r1bqkbnr/p1p1pppp/2np4/8/2BP4/4PN2/PP3PPP/RNBQK2R b KQkq - 0 5", Colour.BLACK, 0, 5, [], []),
    ("3b4/4kp2/7p/5p2/2r5/1P3N1P/P2R2PK/8 b - f2 60 111", Colour.BLACK, 60, 111, ["f2"], [(0, 0), (4, 0), (7, 0), (0, 7), (4, 7), (7, 7)]),
    ("r2qkbnr/p2bppp1/2p4p/4p3/2B5/2N1P3/PP1BQPPP/2R2RK1 b k - 1 12", Colour.BLACK, 1, 12, [], [(0, 0), (0, 7), (4, 7), (7, 7)]),
    ("1r1qkb1r/p3ppp1/2p1bn1p/8/2B1Pp2/2N1B2P/PP2Q1P1/2R2RK1 w Q g3 19 25", Colour.WHITE, 19, 25, ["g3"], [(0, 0), (4, 0), (7, 0), (7, 7)]),
])
def test_load_fen(fen, expected_player_turn, expected_halfmove, expected_fullmove, expected_move_history, expected_has_moved):
    fp = FenParser(fen)
    fp.parse()
    
    board = Board()
    board.load_from_fen(fp)
    
    assert(board.player_turn) == expected_player_turn
    assert(board.halfmove) == expected_halfmove
    assert(board.fullmove) == expected_fullmove
    assert(board.move_history) == expected_move_history
    for rank, file in expected_has_moved:
        piece = board.get_piece(rank, file)
        if piece is not None:
            assert(piece.has_moved)

@pytest.mark.parametrize("fen, rank, file, expected_moves", [
    ("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", 0, 0, []),
    ("3k4/8/4p3/4Rp2/4p3/8/1K6/8 w - - 0 1", 4, 3, [(4, 4), (2, 3), (3, 3), (5, 3), (0, 3), (1, 3), (4, 2)]),
    ("3k4/8/4P3/4RP2/4P3/8/1K6/8 w - - 0 1", 4, 3, [(2, 3), (3, 3), (1, 3), (0, 3)]),
])
def test_rook_moves(fen, rank, file, expected_moves):
    fp = FenParser(fen)
    fp.parse()

    chess_game = ChessGame()
    chess_game.variant.load_rules()
    chess_game.board.load_from_fen(fp)

    available_moves = chess_game.board.get_available_moves(rank, file)
    assert(available_moves) == expected_moves
    assert(chess_game.board.get_piece(rank, file).name) == 'Rook'

@pytest.mark.parametrize("fen, rank, file, expected_moves", [
    ("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", 2, 0, []),
    ("3k4/8/2p1p3/3b4/8/8/1K6/8 w - - 0 1", 3, 3, [(4, 4), (2, 4), (5, 5), (7, 7), (1, 5), (6, 6), (0, 6)]),
    ("3k4/8/2p1p3/3B4/8/8/1K6/8 w - - 0 1", 3, 3, [(4, 4), (2, 4), (5, 5), (7, 7), (1, 5), (4, 2), (0, 6), (2, 2), (6, 6)])
])
def test_bishop_moves(fen, rank, file, expected_moves):
    fp = FenParser(fen)
    fp.parse()

    chess_game = ChessGame()
    chess_game.variant.load_rules()
    chess_game.board.load_from_fen(fp)

    available_moves = chess_game.board.get_available_moves(rank, file)
    assert(available_moves) == expected_moves
    assert(chess_game.board.get_piece(rank, file).name) == 'Bishop'

@pytest.mark.parametrize("fen, rank, file, expected_moves", [
    ("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", 3, 0, []),
    ("3k2nQ/6n1/2p1p3/3B4/8/8/1K6/8 w - - 0 1", 7, 0, [(7, 4), (7, 1), (7, 7), (6, 1), (7, 3), (7, 6), (7, 2), (6, 0), (7, 5)]),
    ("3k4/8/1RR5/1qRR4/1RB5/8/7K/8 w - - 0 1", 1, 3, [(2, 3), (2, 4), (1, 2), (0, 4), (0, 2), (2, 2), (0, 3), (1, 4)])
])
def test_queen_moves(fen, rank, file, expected_moves):
    fp = FenParser(fen)
    fp.parse()

    chess_game = ChessGame()
    chess_game.variant.load_rules()
    chess_game.board.load_from_fen(fp)

    available_moves = chess_game.board.get_available_moves(rank, file)
    assert(available_moves) == expected_moves
    assert(chess_game.board.get_piece(rank, file).name) == 'Queen'


@pytest.mark.parametrize("fen, rank, file, expected_moves", [
    ("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", 1, 0, [(0, 2), (2, 2)]),
    ("k7/8/8/4N3/8/8/8/7K w - - 0 1", 4, 3, [(2, 4), (5, 5), (6, 2), (5, 1), (2, 2), (3, 1), (6, 4), (3, 5)]),
    ("k6n/5P2/6r1/8/8/8/8/7K w - - 0 1", 7, 0, [(5, 1)])
])
def test_queen_moves(fen, rank, file, expected_moves):
    fp = FenParser(fen)
    fp.parse()

    chess_game = ChessGame()
    chess_game.variant.load_rules()
    chess_game.board.load_from_fen(fp)

    available_moves = chess_game.board.get_available_moves(rank, file)
    assert(available_moves) == expected_moves
    assert(chess_game.board.get_piece(rank, file).name) == 'Knight'