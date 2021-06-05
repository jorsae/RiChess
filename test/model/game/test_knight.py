import pytest
import sys
sys.path.append('src')
from model import *

knight = Knight(Colour.BLACK)

def test_knight_name():
    assert(knight.name) == 'Knight'

def test_knight_abbreviation():
    assert(knight.abbreviation) == 'N'

def test_knight_value():
    assert(knight.value) == 3