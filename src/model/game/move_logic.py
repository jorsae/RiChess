from model.piece.utils.colour import Colour

def pawn_moves(board, pawn, rank, file):
    available_moves = set()
    # TODO: Move out_of_bounds to utility file?
    def out_of_bounds(rank, file):
        if rank > (board.ranks - 1) or rank < 0:
            return True
        if file > (board.files - 1) or file < 0:
            return True
        return False
    
    # Get correct direction, depending on pawn colour
    advance_file = -1 if (pawn.colour == Colour.WHITE) else 1
    
    # check move forward + captures
    if out_of_bounds(rank, file + advance_file) is False:
        if board.get_piece(rank, file + advance_file) is None:
            available_moves.add((rank, file + advance_file))
    
    if out_of_bounds(rank + 1, file + advance_file) is False:
        piece = board.get_piece(rank + 1, file + advance_file)
        if piece is not None:
            if piece.colour != pawn.colour:
                available_moves.add((rank + 1, file + advance_file))

    if out_of_bounds(rank - 1, file + advance_file) is False:
        piece = board.get_piece(rank - 1, file + advance_file)
        if piece is not None:
            if piece.colour != pawn.colour:
                available_moves.add((rank - 1, file + advance_file))
    
    # check first pawn move, for 2 moves:
    if pawn.has_moved is False:
        new_file = file + (advance_file*2)
        if out_of_bounds(rank, new_file) is False:
            if board.get_piece(rank, new_file) is None:
                available_moves.add((rank, new_file))

    # TODO: implement en passant
    if len(board.move_history) > 0:
        pass
    
    # TODO: implement promotion
    
    return list(available_moves)