from abc import ABCMeta, abstractmethod
from model import Colour

from typing import List, Optional

class IBoard(metaclass=ABCMeta):
    def __init__(self, files: int = 8, ranks: int = 8):
        self.files = files
        self.ranks = ranks
        self.board = [[None for i in range(self.files)] for j in range(self.ranks)]
    
    def get_piece(self, file, rank):
        return self.board[file][rank]

    def __str__(self):
        output = ''
        for file in range(self.files):
            line = ''
            for rank in range(self.ranks):
                piece = self.get_piece(file, rank)
                if piece == None:
                    line += ' 0 |'
                else:
                    line += f' {piece.abbreviation} |'
            output += f'{line[:-1]}\n'
        return output