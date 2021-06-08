import pytest
import sys
sys.path.append('src')
from library.parser import *
from model.piece import *
from model.game import *
import model.game.game_helper as gh
import library.parser.annotator as annotator

@pytest.mark.parametrize("fen, start, end, expected", [
    ("8/r1B2kBp/2q5/8/b6n/2B3B1/P1P1P1P1/RN1QKBNR w KQ - 11 27", (6, 5), (4, 3), 'Bg3e5'),
    ("rnbqkb1r/pppp1ppp/5n2/4p3/4P3/8/PPPPNPPP/RNBQKB1R w KQkq - 0 1", (1, 7), (2, 5), 'Nbc3'),
    ("r4rk1/ppp1qppp/2npbn2/2b1p1B1/2B1P3/2NP1N2/PPPQ1PPP/R4RK1 w Qq - 0 1", (0, 0), (3, 0), 'Rad8'),
    ("r4rk1/ppp1qppp/Q1npbn2/2b1p1B1/2B1P3/3P1N2/QPP2PPP/R4RK1 w Qq - 0 1", (0, 2), (0, 4), 'Q6a4'),
    ("r4rk1/Qpp1qppp/2npbn2/2b1p1B1/2B1P3/3P1N2/QPP2PPP/R4RK1 w Qq - 0 1", (0, 1), (0, 4), 'Q7a4')
])
def test_conflicting_moves(fen, start, end, expected):
    fp = FenParser(fen)
    fp.parse()
    
    chess_game = ChessGame()
    chess_game.variant.load_rules()
    chess_game.board.load_from_fen(fp)
    board = Board()
    board.load_from_fen(fp)
    
    annotation = annotator.annotate_move(board, start, end)
    assert(annotation) == expected