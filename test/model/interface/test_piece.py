import pytest
import sys
sys.path.append('src')
from model.game import *

def test_eq():
    pawn = Pawn(Colour.BLACK)
    pawn2 = Pawn(Colour.BLACK)
    assert(pawn) == pawn2