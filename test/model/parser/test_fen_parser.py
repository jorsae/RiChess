import pytest
import sys
sys.path.append('src')
from model.parser import *
from model.game import *

"""
    self.fen = fen
    self.player_turn = None
    self.last_move = None # None if pawn was not moved last turn. Stored for en passant
    self.halfmove = 0 # Moves since last pawn move/capture, used for 50-move rule
    self.fullmove = 0
"""

@pytest.mark.parametrize("fen, expected", [
    ("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", " r | n | b | q | k | b | n | r\n p | p | p | p | p | p | p | p\n 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0\n 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0\n 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0\n 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0\n P | P | P | P | P | P | P | P\n R | N | B | Q | K | B | N | R\n"),
    ("rnbqkbnr/p1p1pp1p/3p4/1p6/1PP2PpP/3PP3/P5P1/RNBQKBNR b - f3 0 6", " r | n | b | q | k | b | n | r\n p | 0 | p | 0 | p | p | 0 | p\n 0 | 0 | 0 | p | 0 | 0 | 0 | 0\n 0 | p | 0 | 0 | 0 | 0 | 0 | 0\n 0 | P | P | 0 | 0 | P | p | P\n 0 | 0 | 0 | P | P | 0 | 0 | 0\n P | 0 | 0 | 0 | 0 | 0 | P | 0\n R | N | B | Q | K | B | N | R\n"),
    ("r4nk1/pp2r1p1/2p1P2p/3p1P1N/8/8/PPPK4/6RR w - - 0 1", " r | 0 | 0 | 0 | 0 | n | k | 0\n p | p | 0 | 0 | r | 0 | p | 0\n 0 | 0 | p | 0 | P | 0 | 0 | p\n 0 | 0 | 0 | p | 0 | P | 0 | N\n 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0\n 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0\n P | P | P | K | 0 | 0 | 0 | 0\n 0 | 0 | 0 | 0 | 0 | 0 | R | R\n")
])
def test_board_position(fen, expected):
    fp = FenParser(fen)
    fp.parse()
    board = Board()
    board.place_pieces(fp.pieces)
    board.get_piece_list()
    assert(str(board)) == expected

@pytest.mark.parametrize("fen, expected", [
    ("8/ppp1k3/8/8/8/8/PP6/RN1K3R w KQ - 0 1", Colour.WHITE),
    ("r1bqkbnr/p1p1pppp/2np4/8/2BP4/4PN2/PP3PPP/RNBQK2R b KQkq - 0 5", Colour.BLACK),
    ("r1bqkbnr/p1p1ppp1/2np3p/8/2BP4/2N1PN2/PP3PPP/R1BQ1RK1 w - - 2 8", Colour.WHITE),
    ("2rqkb1r/p2b1pp1/2p1Qn1p/8/2B2P2/2N4P/PP1B2P1/2R2RK1 b - - 0 16", Colour.BLACK),
])
def test_player_turn(fen, expected):
    fp = FenParser(fen)
    fp.parse()
    assert(fp.player_turn) == expected

@pytest.mark.parametrize("fen, expected", [
    ("8/ppp1k3/8/8/8/8/PP6/RN1K3R w KQ - 0 1", 0),
    ("r1bqkbnr/p1p1pppp/2np4/8/2BP4/4PN2/PP3PPP/RNBQK2R b KQkq - 0 5", 0),
    ("r1bqkbnr/p1p1ppp1/2np3p/8/2BP4/2N1PN2/PP3PPP/R1BQ1RK1 w - - 2 8", 2),
    ("r2qkbnr/p2bppp1/2p4p/4p3/2B5/2N1P3/PP1BQPPP/2R2RK1 b - - 1 12", 1),
    ("1r1qkb1r/p3ppp1/2p1bn1p/8/2B1Pp2/2N1B2P/PP2Q1P1/2R2RK1 w - - 19 25", 19),
])
def test_halfmove(fen, expected):
    fp = FenParser(fen)
    fp.parse()
    assert(fp.halfmove) == expected

@pytest.mark.parametrize("fen, expected", [
    ("8/ppp1k3/8/8/8/8/PP6/RN1K3R w KQ - 0 1", 1),
    ("r1bqkbnr/p1p1pppp/2np4/8/2BP4/4PN2/PP3PPP/RNBQK2R b KQkq - 0 5", 5),
    ("3b4/4kp2/7p/5p2/2r5/1P3N1P/P2R2PK/8 b - - 60 111", 111),
    ("r2qkbnr/p2bppp1/2p4p/4p3/2B5/2N1P3/PP1BQPPP/2R2RK1 b - - 1 12", 12),
    ("1r1qkb1r/p3ppp1/2p1bn1p/8/2B1Pp2/2N1B2P/PP2Q1P1/2R2RK1 w - - 19 25", 25),
])
def test_fullmove(fen, expected):
    fp = FenParser(fen)
    fp.parse()
    assert(fp.fullmove) == expected

@pytest.mark.parametrize("fen, expected", [
    ("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", None),
    ("rnbqkbnr/pp2pppp/2p5/3pP3/8/8/PPPP1PPP/RNBQKBNR w KQkq d6 0 3", "d6"),
    ("rnbqkbnr/2p1p1pp/8/PPPp4/5pP1/3P4/4PP1P/RNBQKBNR b KQkq g3 0 8", "g3"),
    ("rnbqkbnr/p1p1pp1p/3p4/1p6/1PP2PpP/3PP3/P5P1/RNBQKBNR b - f3 0 6", "f3"),
    ("7k/p1p2p1p/3p4/1p2pP2/1PP4P/3PP1p1/P5P1/RNBQKBNR w KQkq e6 0 8", "e6"),
])
def test_last_move(fen, expected):
    fp = FenParser(fen)
    fp.parse()
    assert(fp.last_move) == expected