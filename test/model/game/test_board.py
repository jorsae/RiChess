import pytest
import sys
sys.path.append('src')
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