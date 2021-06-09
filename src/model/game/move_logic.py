from model.piece.utils.colour import Colour
import model.game.game_helper as gh

def pawn_moves(board, pawn, rank, file):
    available_moves = set()
    
    # Get correct direction, depending on pawn colour
    advance_file = -1 if (pawn.colour == Colour.WHITE) else 1
    
    # check move forward + captures
    if gh.out_of_bounds(board, rank, file + advance_file) is False:
        if board.get_piece(rank, file + advance_file) is None:
            available_moves.add((rank, file + advance_file))
    
    if gh.out_of_bounds(board, rank + 1, file + advance_file) is False:
        piece = board.get_piece(rank + 1, file + advance_file)
        if piece is not None:
            if piece.colour != pawn.colour:
                available_moves.add((rank + 1, file + advance_file))

    if gh.out_of_bounds(board, rank - 1, file + advance_file) is False:
        piece = board.get_piece(rank - 1, file + advance_file)
        if piece is not None:
            if piece.colour != pawn.colour:
                available_moves.add((rank - 1, file + advance_file))
    
    # check first pawn move, for 2 moves:
    if pawn.has_moved is False:
        new_file = file + (advance_file*2)
        if gh.out_of_bounds(board, rank, new_file) is False:
            if board.get_piece(rank, new_file) is None:
                available_moves.add((rank, new_file))

    # TODO: implement en passant
    if len(board.move_history) > 0:
        pass
    
    return available_moves

# available_moves = move_logic.king_moves(board, piece, available_moves, rank, file)
def king_moves(board, king, old_moves, rank, file):
    available_moves = set()
    
    enemy_colour = Colour.WHITE if king.colour == Colour.BLACK else Colour.BLACK
    enemy_pieces = board.filter_piece_list(colour_filter=enemy_colour)
    for move in old_moves:
        threat = is_threatened(board, king.colour, rank, move[0], move[1])
        if threat is False:
            available_moves.add(move)
    
    enemy_king = board.filter_piece_list(piece_filter='King', colour_filter=enemy_colour)[0]
    enemy_sum = enemy_king.rank + enemy_king.file
    for move in reversed(list(available_moves)):
        rank_diff = max(move[0], enemy_king.rank) - min(move[0], enemy_king.rank)
        file_diff = max(move[1], enemy_king.file) - min(move[1], enemy_king.file)
        if rank_diff <= 1 and file_diff <= 1:
            available_moves.remove(move)
    
    return available_moves

# returns True if rank, file can be captured by opponent. False otherwise
def is_threatened(board, colour, start_rank, rank, file):
    enemy_colour = Colour.WHITE if colour == Colour.BLACK else Colour.BLACK
    enemies = board.filter_piece_list(colour_filter=enemy_colour)
    for enemy in enemies:
        if enemy.piece.name == 'King':
            continue
        elif enemy.piece.name == 'Pawn':
            advance_file = -1 if colour == Colour.WHITE else 1
            pawn_file = file + advance_file
            if enemy.file == pawn_file:
                if enemy.rank == rank + 1 or enemy.rank == rank - 1:
                    return True
            continue
        enemy_moves = gh.get_available_moves(board, enemy.rank, enemy.file)
        if (rank, file) in enemy_moves:
            return True
    return False