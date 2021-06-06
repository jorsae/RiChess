import pytest
import sys
sys.path.append('src')
from model.piece import *

king = King(Colour.BLACK)

def test_king_name():
    assert(king.name) == 'King'

def test_king_abbreviation():
    assert(king.abbreviation) == 'K'

def test_king_value():
    assert(king.value) == 100