import pytest
import sys
sys.path.append('src')
from model import *

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