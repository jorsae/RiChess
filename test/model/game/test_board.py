import pytest
import sys
sys.path.append('src')
from model.piece import *
from library.parser import *
from model.game import *
import model.game.game_helper as gh
from model.interface.move_history import MoveHistory

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

@pytest.mark.parametrize("fen, expected_player_turn, expected_halfmove, expected_fullmove, expected_move_history, expected_has_moved", [
    ("8/ppp1k3/8/8/8/8/PP6/RN1K3R w KQ - 0 1", Colour.WHITE, 0, 1, [], [(0, 0), (4, 0), (7, 0)]),
    ("r1bqkbnr/p1p1pppp/2np4/8/2BP4/4PN2/PP3PPP/RNBQK2R b KQkq - 0 5", Colour.BLACK, 0, 5, [], []),
    ("3b4/4kp2/7p/5p2/2r5/1P3N1P/P2R2PK/8 b - - 60 111", Colour.BLACK, 60, 111, [], [(0, 0), (4, 0), (7, 0), (0, 7), (4, 7), (7, 7)]),
    ("r2qkbnr/p2bppp1/2p4p/4p3/2B5/2N1P3/PP1BQPPP/2R2RK1 b k - 1 12", Colour.BLACK, 1, 12, [], [(0, 0), (0, 7), (4, 7), (7, 7)]),
    ("1r1qkb1r/p3ppp1/2p1bn1p/8/2B1Pp2/2N1B2P/PP2Q1P1/2R2RK1 w Q - 19 25", Colour.WHITE, 19, 25, [], [(0, 0), (4, 0), (7, 0), (7, 7)]),
    ("rnbqkbnr/pp2pppp/2p5/3pP3/8/8/PPPP1PPP/RNBQKBNR w KQkq d6 0 3", Colour.WHITE, 0, 3, [MoveHistory((3, 1), (3, 3))], []),
])
def test_load_fen(fen, expected_player_turn, expected_halfmove, expected_fullmove, expected_move_history, expected_has_moved):
    fp = FenParser(fen)
    fp.parse()
    
    board = Board()
    board.load_from_fen(fp)
    
    assert(board.player_turn) == expected_player_turn
    assert(board.halfmove) == expected_halfmove
    assert(board.fullmove) == expected_fullmove
    assert(str(board.move_history)) == str(expected_move_history)
    for rank, file in expected_has_moved:
        piece = board.get_piece(rank, file)
        if piece is not None:
            assert(piece.has_moved)

@pytest.mark.parametrize("piece_filter, colour_filter, expected", [
    (None, None, 32),
    ("Pawn", None, 16),
    ("Pawn", Colour.WHITE, 8),
    ("Rook", Colour.BLACK, 2),
    (None, Colour.WHITE, 16),
])
def test_filter_piece_list(piece_filter, colour_filter, expected):
    fp = FenParser("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    fp.parse()

    board = Board()
    board.load_from_fen(fp)
    filtered_list = board.filter_piece_list(piece_filter, colour_filter)
    assert(len(filtered_list)) == expected