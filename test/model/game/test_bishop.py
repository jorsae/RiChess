import pytest
import sys
sys.path.append('src')
from model.game import *

bishop = Bishop(Colour.BLACK)

def test_bishop_name():
    assert(bishop.name) == 'Bishop'

def test_bishop_abbreviation():
    assert(bishop.abbreviation) == 'B'

def test_bishop_value():
    assert(bishop.value) == 3