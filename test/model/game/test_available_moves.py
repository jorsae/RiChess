import pytest
import sys
sys.path.append('src')
from library.parser import *
from model.game import *
import model.game.game_helper as gh
from model.interface import *

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

    available_moves = gh.get_available_moves(chess_game.board, rank, file)
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

    available_moves = gh.get_available_moves(chess_game.board, rank, file)
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

    available_moves = gh.get_available_moves(chess_game.board, rank, file)
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

    available_moves = gh.get_available_moves(chess_game.board, rank, file)
    assert(available_moves) == expected_moves
    assert(chess_game.board.get_piece(rank, file).name) == 'Knight'

# MoveDescription((-1, -1), 100)]
@pytest.mark.parametrize("fen, move_description, rank, file, expected_moves", [
    ("k7/8/8/4B3/8/8/8/1K6 w - - 0 1", MoveDescription((1, 1), 100), 4, 3, {(5, 4), (7, 6), (6, 5)}),
    ("k7/8/8/4B3/8/8/8/1K6 w - - 0 1", MoveDescription((-1, 1), 100), 4, 3, {(0, 7), (1, 6), (2, 5), (3, 4)}),
    ("k7/8/8/4B3/8/8/8/1K6 w - - 0 1", MoveDescription((1, -1), 100), 4, 3, {(6, 1), (7, 0), (5, 2)}),
    ("k7/8/8/4B3/8/8/8/1K6 w - - 0 1", MoveDescription((-1, -1), 100), 4, 3, {(1, 0), (3, 2), (2, 1)}),
])
def test_get_moves_in_direction(fen, move_description, rank, file, expected_moves):
    fp = FenParser(fen)
    fp.parse()
    
    chess_game = ChessGame()
    chess_game.variant.load_rules()
    chess_game.board.load_from_fen(fp)

    moves = gh.get_moves_in_direction(chess_game.board, move_description, rank, file)
    assert(moves) == expected_moves
