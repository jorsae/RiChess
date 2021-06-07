import pytest
import sys
sys.path.append('src')
from model.piece import *
from library.parser import *
from model.game import *
import model.game.game_helper as gh

board = Board()

@pytest.mark.parametrize("rank, file, expected", [
    (7, 7, False),
    (8, 0, True),
    (0, 0, False),
    (0, -1, True),
    (-1, 0, True),
])
def test_out_of_bounds(rank, file, expected):
    assert(gh.out_of_bounds(board, rank, file)) == expected

@pytest.mark.parametrize("available_moves, rank, file, expected", [
    ([(0, 1), (7,7), (6, 2)], 6, 3, False),
    ([(0, 1), (7,7), (6, 2)], 0, 1, True),
    ([(0, 1), (7,7), (6, 2)], 6, 2, True),
    ([(0, 1), (7,7), (6, 2)], 0, 0, False),
    ([(0, 1), (7,7), (6, 2)], -1, -2, False),
])
def test_can_move_to(available_moves, rank, file, expected):
    assert(gh.can_move_to(available_moves, rank, file)) == expected