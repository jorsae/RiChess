from typing import Sequence

from model.piece import Colour, BoardPiece
import model.game.move_logic as move_logic
import model.game.game_helper as gh

class Board():
    def __init__(self, ranks: int = 8, files: int = 8):
        self.ranks = ranks
        self.files = files
        self.move_history = []
        self.piece_list = []
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
        self.piece_list.append(BoardPiece(piece, rank, file))

    def place_pieces(self, board_pieces):
        for bp in board_pieces:
            self.place_piece(bp.piece, bp.rank, bp.file)
    
    def move_to(self, start, end):
        piece = self.get_piece(start[0], start[1])
        if piece is None:
            return # TODO: raise exception
        
        available_moves = gh.get_available_moves(self, start[0], start[1])
        can_move = gh.can_move_to(available_moves, end[0], end[1])
        if can_move is False:
            return # TODO: raise exception
        
        loc_piece = self.get_piece(end[0], end[1])
        if loc_piece is not None:
            # TODO: remove piece from self.piece_list
            pass # TODO: implement so the move is seen as a capture move
        
        # check for pawn promotion
        if piece.name == 'Pawn':
            promotion_file = 0 if (piece.colour == Colour.WHITE) else 7
            if end[1] == promotion_file:
                piece = gh.get_pawn_promotion(piece.colour)


        self.board[start[0]][start[1]] = None
        self.board[end[0]][end[1]] = piece

    def filter_piece_list(self, piece_filter: str = None, colour_filter: Colour = None):
        current_list = self.piece_list
        if piece_filter is not None:
            current_list = list(filter(lambda p: p.piece.name == piece_filter, current_list))
        
        if colour_filter is not None:
            current_list = list(filter(lambda p: p.piece.colour == colour_filter, current_list))
        
        return current_list

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