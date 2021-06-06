import re
from model.piece import *

re_number = re.compile(r'\d')

class FenParser:
    def __init__(self, fen):
        self.fen = fen
        self.pieces = []
        self.has_moved = []
        self.player_turn = None
        self.last_move = None # None if pawn was not moved last turn. Stored for en passant
        self.halfmove = 0 # Moves since last pawn move/capture, used for 50-move rule
        self.fullmove = 0
    
    def parse(self):
        ranks = self.fen.split(" ")[0].split("/")
        self.pieces = self.parse_ranks(ranks)
        
        splits = self.fen.split(" ")

        self.player_turn = self.parse_player_turn(splits[1])
        self.has_moved = self.parse_castling(splits[2])
        self.last_move = self.parse_en_passant(splits[3])
        self.halfmove = self.parse_integer(splits[4])
        self.fullmove = self.parse_integer(splits[5])

    def parse_ranks(self, ranks):
        pieces = []
        rank_number = 0
        for index in range(len(ranks)):
            file_number = 0
            for char in ranks[index]:
                if re_number.match(char):
                    file_number += int(char)
                else:
                    piece = self.get_piece(char)
                    pieces.append(BoardPiece(piece, rank_number, file_number))
                    file_number += 1
            rank_number += 1
        return pieces
    
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
        def remove_has_moved(has_moved, value):
            try:
                has_moved.remove(value)
            except ValueError:
                pass

        has_moved = [(0, 0), (4, 0), (7, 0), (0, 7), (4, 7), (7, 7)]
        if castling == '-':
            return has_moved
        
        for char in castling:
            char_lower = char.lower()
            if char_lower == 'k':
                if char.isupper():
                    remove_has_moved(has_moved, (4, 7))
                    remove_has_moved(has_moved, (7, 7))
                else:
                    remove_has_moved(has_moved, (4, 0))
                    remove_has_moved(has_moved, (7, 0))
            elif char_lower == 'q':
                if char.isupper():
                    remove_has_moved(has_moved, (0, 7))
                    remove_has_moved(has_moved, (4, 7))
                else:
                    remove_has_moved(has_moved, (0, 0))
                    remove_has_moved(has_moved, (4, 0))
        
        return has_moved
    
    def parse_en_passant(self, en_passant):
        if en_passant == '-':
            return None
        else:
            return en_passant
    
    def parse_integer(self, text):
        try:
            return int(text)
        except Exception as e:
            return 0
    
    def __str__(self):
        return f'{self.player_turn}: {self.last_move}, {self.halfmove}, {self.fullmove}'
