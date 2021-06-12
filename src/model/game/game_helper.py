from model.piece import Colour, BoardPiece
from model.piece import *
import model.game.move_logic as move_logic
"""
    Helper file to add a lot of utility methods
"""

# checks if a position is out of the boards boundaries
def out_of_bounds(board, rank, file):
    if rank > (board.ranks - 1) or rank < 0:
        return True
    if file > (board.files - 1) or file < 0:
        return True
    return False

# Checks if move is available to the piece
def can_move_to(available_moves, rank, file):
    for moves in available_moves:
        if moves[0] == rank and moves[1] == file:
            return True
    return False

# Gets all available moves for a square on the board
def get_available_moves(board, rank, file):
    piece = board.get_piece(rank, file)
    if piece is None:
        return []
    
    available_moves = set()
    
    # Default movement
    for movement in piece.movement():
        available_moves.update(get_moves_in_direction(board, movement, rank, file))
    # Special movement(pawn moves, castling)
    if piece.name == 'Pawn':
        available_moves.update(move_logic.pawn_moves(board, piece, rank, file))
    elif piece.name == 'King':
        available_moves = move_logic.king_moves(board, piece, available_moves, rank, file)
    
    return list(available_moves)

# Helper function for get_available_moves. This gets all default moves, based on MoveDescription
def get_moves_in_direction(board, movement, rank_start, file_start):
    available_moves = set()
    this = board.get_piece(rank_start, file_start)

    def can_move_to(rank, file):
        if rank > (board.ranks - 1) or rank < 0:
            return False, False
        if file > (board.files - 1) or file < 0:
            return False, False
        piece = board.get_piece(rank, file)
        if piece is None:
            return True, True
        else:
            if piece.colour == this.colour:
                return False, False
            else:
                return True, False

    # rank, file. is current position
    for index in range(1, movement.range,):
        rank = rank_start + (movement.vector[0] * index)
        file = file_start + (movement.vector[1] * index)
        can_move, cont = can_move_to(rank, file)
        if can_move:
            available_moves.add((rank, file))
        if cont is False:
            break
    return available_moves

# User input that determines which piece a pawn is promoted too
def get_pawn_promotion(colour):
    promotion = input('which piece do you want to promote too?')
    if promotion == 'q':
        return Queen(colour)
    elif promotion == 'r':
        return Rook(colour)
    elif promotion == 'b':
        return Bishop(colour)
    elif promotion == 'n':
        return Knight(colour)
    else:
        return Queen(colour)

# returns en passant move
def get_en_passant(board, pawn, rank, file, advance_file):
    if len(board.move_history) > 0:
        last_move = board.move_history[len(board.move_history) - 1]
        p = board.get_piece(last_move.end[0], last_move.end[1])
        if p is not None:
            if p.name == 'Pawn':
                if file == last_move.end[1]:
                    if rank == last_move.end[0] + 1:
                        return last_move.end[0], last_move.end[1] + advance_file
                    elif rank == last_move.end[0] - 1:
                        return last_move.end[0], last_move.end[1] + advance_file
    return None, None

def get_castle_moves(board, king, rank, file):
    available_moves = set()
    if king.has_moved is False:
        if move_logic.is_threatened(board, king.colour, rank, file) is False:
            if king.colour == Colour.WHITE:
                kingside = can_castle(board, king.colour, file, [5, 6], 7)
                if kingside:
                    available_moves.add((6, 7))
                queenside = can_castle(board, king.colour, file, [1, 2, 3], 7)
                if queenside:
                    available_moves.add((2, 7))
            else:
                kingside = can_castle(board, king.colour, file, [5, 6], 0)
                if kingside:
                    available_moves.add((6, 0))
                queenside = can_castle(board, king.colour, file, [1, 2, 3], 0)
                if queenside:
                    available_moves.add((2, 0))
    return available_moves

def can_castle(board, colour, file, rank_check, rook_rank):
    rook = board.get_piece(rook_rank, file)
    if rook is None:
        return False
    if rook.has_moved is True:
        return False
    
    for rank in rank_check:
        piece = board.get_piece(rank, file)
        if piece is not None:
            return False
        if move_logic.is_threatened(board, colour, rank, file) is True:
            return False
    return True