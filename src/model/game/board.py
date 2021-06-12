from model.piece import Colour, BoardPiece
import model.game.move_logic as move_logic
import model.game.game_helper as gh
import library.parser.annotator as annotator
import library.parser.uci as uci
from model.interface.move_history import MoveHistory

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
        for moves in available_moves:
            print(f'{moves}')
            self.board[start[0]][start[1]] = None
            self.board[moves[0]][moves[1]] = piece
            king = self.filter_piece_list(piece_filter='King', colour_filter=piece.colour)[0]
            print(f'{king.piece.colour}: {king.rank}, {king.file}')
            invalid_move = False
            if move_logic.is_check(self, piece.colour, king.rank, king.file):
                invalid_move = True
                print('invalid move, in check') # TODO: remove from available_moves
            self.board[start[0]][start[1]] = piece
            self.board[moves[0]][moves[1]] = None
            if invalid_move:
                return

        can_move = gh.can_move_to(available_moves, end[0], end[1])
        if can_move is False:
            return # TODO: raise exception
        
        # Remove captured piece
        if self.get_piece(end[0], end[1]) is not None:
            self.remove_list_piece(end[0], end[1])
        
        # check for pawn promotion
        promotion_piece = None
        if piece.name == 'Pawn':
            promotion_file = 0 if (piece.colour == Colour.WHITE) else 7
            if end[1] == promotion_file:
                promotion_piece = gh.get_pawn_promotion(piece.colour)
                promotion_piece.has_moved = True
        
        # check for en passant
        advance_file = -1 if (piece.colour == Colour.WHITE) else 1
        ep_rank, ep_file = gh.get_en_passant(self, piece, start[0], start[1], advance_file)
        if ep_rank is not None:
            self.remove_list_piece(ep_rank, ep_file - advance_file)
            self.board[ep_rank][ep_file - advance_file] = None
        
        # check for castling
        if piece.name == 'King':
            diff = abs(start[0] - end[0])
            # player castled, change location of the rook
            if diff > 1:
                print(f'castled: {end[0]=}')
                if end[0] == 6:
                    rook = self.get_piece(7, start[1])
                    print(f'{start[1]=} | {rook=}')
                    self.board[7][start[1]] = None
                    self.board[5][start[1]] = rook
                    castled_rook = list(filter(lambda p: p.rank == 7 and p.file == start[1], self.piece_list))[0]
                    print(f'{castled_rook=}')
                    castled_rook.rank = 5
                else:
                    rook = self.get_piece(0, start[1])
                    print(f'{start[1]=} | {rook=}')
                    self.board[0][start[1]] = None
                    self.board[3][start[1]] = rook
                    castled_rook = list(filter(lambda p: p.rank == 0 and p.file == start[1], self.piece_list))[0]
                    print(f'{castled_rook=}')
                    castled_rook.rank = 3

        if start is not None and end is not None:
            self.move_history.append(MoveHistory(start, end))

        piece.has_moved = True
        
        self.board[start[0]][start[1]] = None
        self.board[end[0]][end[1]] = piece if promotion_piece is None else promotion_piece
        # Update piece moved in self.piece_list location
        bp = list(filter(lambda p: p.rank == start[0] and p.file == start[1], self.piece_list))[0]
        bp.rank = end[0]
        bp.file = end[1]
        if promotion_piece is not None:
            bp.piece = promotion_piece
        
    def remove_list_piece(self, rank, file):
        for bp in self.piece_list:
            if bp.rank == rank and bp.file == file:
                self.piece_list.remove(bp)

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