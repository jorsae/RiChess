from typing import Sequence

from model.piece import Colour, BoardPiece
import model.game.move_logic as move_logic
import model.game.game_helper as gh

class Board():
    def __init__(self, ranks: int = 8, files: int = 8):
        self.ranks = ranks
        self.files = files
        self.move_history = []
        self.turn = Colour.WHITE
        self.halfmove = 0
        self.fullmove = 0
        self.board = [[None for i in range(self.ranks)] for j in range(self.files)]

    def get_piece(self, rank, file):
        try:
            return self.board[rank][file]
        except:
            return None
    
    def place_piece(self, piece, rank, file):
        self.board[rank][file] = piece

    def place_pieces(self, board_pieces):
        for bp in board_pieces:
            self.place_piece(bp.piece, bp.rank, bp.file)
    
    def move_to(self, rank, file, new_rank, new_file):
        piece = self.get_piece(rank, file)
        if piece is None:
            return # TODO: raise exception
        
        available_moves = gh.get_available_moves(self, rank, file)
        can_move = gh.can_move_to(available_moves, new_rank, new_file)
        if can_move is False:
            return # TODO: raise exception
        
        loc_piece = self.get_piece(new_rank, new_file)
        if loc_piece is not None:
            pass # TODO: implement so the move is seen as a capture move
        
        self.board[rank][file] = None
        self.board[new_rank][new_file] = piece

    def load_from_fen(self, fen_parser):
        self.place_pieces(fen_parser.pieces)
        self.player_turn = fen_parser.player_turn
        self.halfmove = fen_parser.halfmove
        self.fullmove = fen_parser.fullmove
        if fen_parser.last_move is not None:
            self.move_history.append(fen_parser.last_move)
        
        # BEWARE: This can technically set non rook/king pieces to has_moved = True, but it should not matter.
        for rank, file in fen_parser.has_moved:
            piece = self.get_piece(rank, file)
            if piece is not None:
                piece.has_moved = True

    def get_piece_list(self):
        piece_list = []
        for file in range(self.files):
            for rank in range(self.ranks):
                piece = self.get_piece(rank, file)
                if piece is not None:
                    piece_list.append(BoardPiece(piece, rank, file))
        return piece_list

    def __str__(self):
        output = ''
        for file in range(self.files):
            line = ''
            for rank in range(self.ranks):
                piece = self.get_piece(rank, file)
                if piece is None:
                    line += ' 0 |'
                else:
                    abbr = piece.abbreviation
                    if piece.name == 'Pawn':
                        abbr = 'p'
                    if piece.colour == Colour.BLACK:
                        line += f' {abbr.lower()} |'
                    else:
                        line += f' {abbr.upper()} |'
            output += f'{line[:-2]}\n'
        return output