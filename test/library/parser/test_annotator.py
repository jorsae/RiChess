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
])
def test_board_position(fen, start, end, expected):
    fp = FenParser(fen)
    fp.parse()
    
    chess_game = ChessGame()
    chess_game.variant.load_rules()
    chess_game.board.load_from_fen(fp)
    board = Board()
    board.load_from_fen(fp)
    
    annotation = annotator.annotate_move(board, start, end)
    assert(annotation) == expected