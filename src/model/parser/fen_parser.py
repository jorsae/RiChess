import re
from model.game import *

re_number = re.compile('\d')

class FenParser:
    def __init__(self, fen):
        self.fen = fen
    
    def parse(self):
        ranks = self.fen.split(" ")[0].split("/")
        bl = self.parse_ranks(ranks)
        return bl
    
    def parse_ranks(self, ranks):
        board_list = []
        rank_number = 0
        for index in range(len(ranks)):
            file_number = 0
            for char in ranks[index]:
                print(f'{char}: {rank_number} {file_number}')
                if re_number.match(char):
                    file_number += int(char)
                else:
                    piece = self.get_piece(char)
                    board_list.append(BoardPiece(piece, rank_number, file_number))
                    file_number += 1
            rank_number += 1
        return board_list
    
    def get_piece(self, char):
        char_lower = char.lower()
        if char_lower == 'k':
            return King(self.get_colour(char))
        elif char_lower == 'q':
            return Queen(self.get_colour(char))
        if char_lower == 'r':
            return Rook(self.get_colour(char))
        if char_lower == 'b':
            return Bishop(self.get_colour(char))
        if char_lower == 'n':
            return Knight(self.get_colour(char))
        else:
            return Pawn(self.get_colour(char))
    
    def get_colour(self, char):
        if char.isupper():
            return Colour.WHITE
        else:
            return Colour.BLACK