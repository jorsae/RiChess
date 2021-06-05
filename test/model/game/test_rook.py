import pytest
import sys
sys.path.append('src')
from model.game import *

rook = Rook(Colour.BLACK)

def test_rook_name():
    assert(rook.name) == 'Rook'

def test_rook_abbreviation():
    assert(rook.abbreviation) == 'R'

def test_rook_value():
    assert(rook.value) == 5