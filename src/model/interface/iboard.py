from abc import ABCMeta, abstractmethod
from model.game import Colour

from typing import List, Optional

class IBoard(metaclass=ABCMeta):
    def __init__(self, ranks: int = 8, files: int = 8, ):
        self.ranks = ranks
        self.files = files
        self.board = [[None for i in range(self.ranks)] for j in range(self.files)]
    
    def get_piece(self, rank, file):
        return self.board[rank][file]

    def __str__(self):
        output = ''
        for rank in range(self.ranks):
            line = ''
            for file in range(self.files):
                piece = self.get_piece(rank, file)
                if piece == None:
                    line += ' 0 |'
                else:
                    if piece.colour == Colour.BLACK:
                        line += f' {piece.abbreviation.lower()} |'
                    else:
                        line += f' {piece.abbreviation.upper()} |'
            output += f'{line[:-1]}\n'
        return output