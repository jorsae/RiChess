import pytest
import sys
sys.path.append('src')
from library.parser import *
from model.piece import *
from model.game import *
import model.game.game_helper as gh
import library.parser.annotator as annotator
from model.piece import Colour, BoardPiece

# TODO: add test for en passant, check and checkmate

@pytest.mark.parametrize("fen, start, end, promotion_piece, expected", [
    ("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", (4, 1), (4, 2), None, 'e6'),
    ("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", (4, 1), (4, 3), None, 'e5'),
    ("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", (4, 6), (4, 4), None, 'e4'),
    ("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", (0, 6), (0, 5), None, 'a3'),
    ("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", (0, 6), (0, 5), None, 'a3'),
    ("rnbqkbnr/ppp1p1pp/5p2/3p4/2PP4/4P3/PP3PPP/RNBQKBNR b KQkq - 0 3", (3, 3), (2, 4), None, 'dxc4'),
    ("rnbqkbnr/pp2pppp/2p5/3pP3/8/8/PPPP1PPP/RNBQKBNR w KQkq d6 0 3", (4, 3), (3, 2), None, 'exd6'),
    ("8/rPB2kBp/2q5/4p3/b6n/2B3B1/P1P1P3/RN1QKBNR w KQ - 11 27", (1, 1), (1, 0), Queen(Colour.WHITE), 'b8=Q'),
    ("8/rPB2kBp/2q5/4p3/b6n/2B3B1/P1P1P3/RN1QKBNR w KQ - 11 27", (1, 1), (1, 0), Rook(Colour.WHITE), 'b8=R'),
    ("8/rPB2kBp/2q5/4p3/b6n/2B3B1/P1P1P3/RN1QKBNR w KQ - 11 27", (1, 1), (1, 0), Bishop(Colour.WHITE), 'b8=B'),
    ("8/rPB2kBp/2q5/4p3/b6n/2B3B1/P1P1P3/RN1QKBNR w KQ - 11 27", (1, 1), (1, 0), Knight(Colour.WHITE), 'b8=N'),
])
def test_pawn_annotation(fen, start, end, promotion_piece, expected):
    fp = FenParser(fen)
    fp.parse()
    
    chess_game = ChessGame()
    chess_game.variant.load_rules()
    chess_game.board.load_from_fen(fp)
    
    annotation = annotator.annotate_move(chess_game.board, start, end, promotion_piece)
    assert(annotation) == expected

@pytest.mark.parametrize("fen, start, end, expected", [
    ("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", (6, 7), (5, 5), 'Nf3'),
    ("rnbqkb1r/pppppppp/8/5n2/8/5N2/PPPPPPPP/RNBQKB1R w KQkq - 0 1", (5, 3), (3, 4), 'Nd4'),
    ("rnbqkb1r/pppp1ppp/8/4pn2/2N5/5N2/PPPPPPPP/R1BQKB1R w KQkq - 0 1", (2, 4), (4, 3), 'Ncxe5'),
    ("rnbqkb1r/pppp1ppp/5n2/4p3/4P3/8/PPPPNPPP/RNBQKB1R w KQkq - 0 1", (1, 7), (2, 5), 'Nbc3'),
    ("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", (6, 7), (5, 5), 'Nf3'),
])
def test_knight_annotation(fen, start, end, expected):
    fp = FenParser(fen)
    fp.parse()
    
    chess_game = ChessGame()
    chess_game.variant.load_rules()
    chess_game.board.load_from_fen(fp)
    
    annotation = annotator.annotate_move(chess_game.board, start, end)
    assert(annotation) == expected

@pytest.mark.parametrize("fen, start, end, expected", [
    ("rnbqkbnr/pppp1ppp/8/4p3/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 1", (5, 0), (1, 4), 'Bb4'),
    ("rnbqk1nr/pppp1ppp/8/2b1p3/1PB1P3/2N5/P1PP1PPP/R1BQK1NR w KQkq - 0 1", (2, 3), (1, 4), 'Bxb4'),
    ("8/r1B2kBp/2q5/8/b6n/2B3B1/P1P1P1P1/RN1QKBNR w KQ - 11 27", (6, 5), (4, 3), 'Bg3e5'),
    ("8/r1B2kBp/2q5/4p3/b6n/2B3B1/P1P1P1P1/RN1QKBNR w KQ - 11 27", (2, 1), (4, 3), 'Bc7xe5'),
])
def test_bishop_annotation(fen, start, end, expected):
    fp = FenParser(fen)
    fp.parse()
    
    chess_game = ChessGame()
    chess_game.variant.load_rules()
    chess_game.board.load_from_fen(fp)
    
    annotation = annotator.annotate_move(chess_game.board, start, end)
    assert(annotation) == expected

@pytest.mark.parametrize("fen, start, end, expected", [
    ("r1bq1rk1/pppp1ppp/2n2n2/2b1p3/2B1P3/2N2N2/PPPP1PPP/R1BQ1RK1 w Qq - 0 1", (0, 7), (1, 7), 'Rb1'),
    ("r4rk1/ppp1qppp/R1npbn2/2b1p1B1/2B1P3/1PNP1NQ1/1PP2PPP/R4RK1 w Qq - 0 1", (0, 2), (0, 5), 'R6a3'),
    ("r4rk1/ppp1qppp/2npbn2/2b1p1B1/2B1P3/2NP1NQ1/PPPR1PPP/R4RK1 w Qq - 0 1", (3, 6), (3, 7), 'Rdd1'),
    ("r4rk1/ppp1qppp/2npbn2/2b1p1B1/2B1P3/2NP1N2/PPPQ1PPP/R4RK1 w Qq - 0 1", (0, 0), (3, 0), 'Rad8'),
])
def test_rook_annotation(fen, start, end, expected):
    fp = FenParser(fen)
    fp.parse()
    
    chess_game = ChessGame()
    chess_game.variant.load_rules()
    chess_game.board.load_from_fen(fp)
    
    annotation = annotator.annotate_move(chess_game.board, start, end)
    assert(annotation) == expected

@pytest.mark.parametrize("fen, start, end, expected", [
    ("r4rk1/ppp1qppp/R1npbn2/2b1p1B1/2B1P3/1PNP1NQ1/1PP2PPP/R4RK1 w Qq - 0 1", (4, 1), (3, 1), 'Qd7'),
    ("r4rk1/ppp1qppp/Q1npbn2/2b1p1B1/2B1P3/3P1N2/QPP2PPP/R4RK1 w Qq - 0 1", (0, 2), (0, 4), 'Q6a4'),
    ("r4rk1/Qpp1qppp/2npbn2/2b1p1B1/2B1P3/3P1N2/QPP2PPP/R4RK1 w Qq - 0 1", (0, 1), (0, 4), 'Q7a4'),
])
def test_queen_annotation(fen, start, end, expected):
    fp = FenParser(fen)
    fp.parse()
    
    chess_game = ChessGame()
    chess_game.variant.load_rules()
    chess_game.board.load_from_fen(fp)
    
    annotation = annotator.annotate_move(chess_game.board, start, end)
    assert(annotation) == expected