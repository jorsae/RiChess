import re
from model.game import *

re_number = re.compile('\d')

class FenParser:
    def __init__(self, fen):
        self.fen = fen
        self.player_turn = None
        self.last_move = None # None if pawn was not moved last turn. Stored for en passant
        self.halfmove = 0 # Moves since last pawn move/capture, used for 50-move rule
        self.fullmove = 0
    
    def parse(self):
        ranks = self.fen.split(" ")[0].split("/")
        bl = self.parse_ranks(ranks)
        
        splits = self.fen.split(" ")
        print(splits)

        self.player_turn = self.parse_player_turn(splits[1])
        print(self.player_turn)

        self.parse_castling(splits[2])

        self.last_move = self.parse_en_passant(splits[3])

        self.halfmove = self.parse_integer(splits[4])
        
        self.fullmove = self.parse_integer(splits[5])

        print(self)
        
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
    
    def parse_player_turn(self, player_turn):
        if player_turn == 'b':
            return Colour.BLACK
        else:
            return Colour.WHITE
    
    def parse_castling(self, castling):
        print(castling)
    
    def parse_en_passant(self, en_passant):
        self.last_move = en_passant
    
    def parse_integer(self, text):
        try:
            return int(text)
        except Exception as e:
            print(e)
            return 0
    
    def __str__(self):
        return f'{self.player_turn}: {self.last_move}, {self.halfmove}, {self.fullmove}'
