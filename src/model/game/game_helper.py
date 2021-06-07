from model.piece import Colour, BoardPiece
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
        pass # TODO: Implement castling in move_logic.py
    
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

# Returns a list of all pieces on the board. optional filter to only get 1 type of piece
def get_piece_list(board, filter: str = None):
    piece_list = []
    for file in range(board.files):
        for rank in range(board.ranks):
            piece = board.get_piece(rank, file)
            if piece is not None:
                if filter is not None:
                    if piece.name == filter:
                        piece_list.append(BoardPiece(piece, rank, file))
                else:
                    piece_list.append(BoardPiece(piece, rank, file))
    return piece_list