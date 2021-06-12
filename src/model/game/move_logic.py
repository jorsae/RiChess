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
    
    # check for en passant
    ep_rank, ep_file = gh.get_en_passant(board, pawn, rank, file, advance_file)
    if ep_rank is not None:
        available_moves.add((ep_rank, ep_file))

    return available_moves

# available_moves = move_logic.king_moves(board, piece, available_moves, rank, file)
def king_moves(board, king, old_moves, rank, file):
    available_moves = set()
    
    enemy_colour = Colour.WHITE if king.colour == Colour.BLACK else Colour.BLACK
    enemy_pieces = board.filter_piece_list(colour_filter=enemy_colour)
    for move in old_moves:
        threat = is_threatened(board, king.colour, move[0], move[1])
        if threat is False:
            available_moves.add(move)
    
    enemy_king = board.filter_piece_list(piece_filter='King', colour_filter=enemy_colour)[0]
    enemy_sum = enemy_king.rank + enemy_king.file
    for move in reversed(list(available_moves)):
        rank_diff = max(move[0], enemy_king.rank) - min(move[0], enemy_king.rank)
        file_diff = max(move[1], enemy_king.file) - min(move[1], enemy_king.file)
        if rank_diff <= 1 and file_diff <= 1:
            available_moves.remove(move)
    
    if king.has_moved is False:
        if is_threatened(board, king.colour, rank, file) is False:
            if king.colour == Colour.WHITE:
                # rank: 7
                print('white king')
                kingside = can_castle(board, king.colour, file, [5, 6], 7)
                if kingside:
                    available_moves.add((7, 6))
                print(f'can castle kingside: {kingside}')
                queenside = can_castle(board, king.colour, file, [1, 2, 3], 7)
                if queenside:
                    available_moves.add((7, 2))
                print(f'can castle queenside: {queenside}')
            else:
                # rank: 0
                print('black king')
                kingside = can_castle(board, king.colour, file, [5, 6], 0)
                if kingside:
                    available_moves.add((0, 6))
                print(f'can castle kingside: {kingside}')
                queenside = can_castle(board, king.colour, file, [1, 2, 3], 0)
                if queenside:
                    available_moves.add((0, 2))
                print(f'can castle queenside: {queenside}')
    
    return available_moves

def can_castle(board, colour, file, rank_check, rook_rank):
    print(f'can_castle: {file}, {rank_check}, {rook_rank}')
    rook = board.get_piece(rook_rank, file)
    if rook is None:
        return False
    if rook.has_moved is True:
        return False
    
    for rank in rank_check:
        piece = board.get_piece(rank, file)
        print(f'{rank}, {file} : {piece}')
        if piece is not None:
            print('piece: return false')
            return False
        if is_threatened(board, colour, rank, file) is True:
            print('is_threatened: return false')
            return False
    return True

# returns True if rank, file can be captured by opponent. False otherwise
def is_threatened(board, colour, rank, file):
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