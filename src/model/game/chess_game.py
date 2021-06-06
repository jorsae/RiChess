from model.game.board import Board
from model.game.variant.standard import Standard

from typing import Sequence

class ChessGame:
    def __init__(self):
        self.board = Board()
        self.variant = Standard()
    
    def load_variant():
        self.variant.load_rules()