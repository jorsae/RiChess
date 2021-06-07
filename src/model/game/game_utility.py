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
    print(available_moves)
    for moves in available_moves:
        print(f'{moves[0]}, {moves[1]}')
        if moves[0] == rank and moves[1] == file:
            return True
    return False