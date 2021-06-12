import model.game.game_helper as gh
from model.piece.utils.colour import Colour
from model.piece import *

def translate_square(rank, file):
    chars = 'abcdefgh'
    return f'{chars[rank]}{8-file}'

# TODO: Clean this up
def get_piece_identifier(board, piece, start, end):
    if piece.name == 'Pawn':
        return ''
    
    start_pos = []
    same_pieces = board.filter_piece_list(piece_filter=piece.name, colour_filter=piece.colour)
    print(f'{same_pieces=}')
    for same_piece in same_pieces:
        moves = gh.get_available_moves(board, same_piece.rank, same_piece.file)
        moves = list(filter(lambda m: m[0] == end[0] and m[1] == end[1], moves))
        print(f'{moves=} | {end=}')
        if moves == [end]:
            print(f'added: {same_piece}: {moves} vs {end[0]}, {end[1]}')
            start_pos.append((same_piece.rank, same_piece.file))
    
    print(f'{start_pos=}')
    identifier = ''
    rank_id = 0
    file_id = 0
    for s_pos in start_pos:
        if s_pos[0] == start[0]:
            rank_id += 1
        if s_pos[1] == start[1]:
            file_id += 1
    
    id_min = min(rank_id, file_id)
    print(id_min)
    if id_min > 1:
        return f'{translate_square(start[0], start[1])}'
    elif id_min < 1:
        return ''
    else:
        # TODO: clean up, this is ugly af
        if len(start_pos) == 1:
            if start_pos[0][0] == start[0] and start_pos[0][1] == start[1]:
                return ''
        if rank_id <= 1:
            chars = 'abcdefgh' #TODO: This is ugly
            return f'{chars[start[0]]}'
        else:
            if piece.colour == Colour.BLACK:
                return start[1] + 1
            else:
                return 8 - start[1]

def annotate_move(board, start, end, promotion_piece = None):
    piece = board.get_piece(start[0], start[1])
    if piece is None:
        return None
    
    cap_piece = board.get_piece(end[0], end[1])
    capture = ''
    if cap_piece is not None:
        if piece.name == 'Pawn':
            chars = 'abcdefgh' #TODO: This is ugly
            capture = f'{chars[start[0]]}x'
        else:
            capture = f'x'
    
    promotion = ''
    if promotion_piece is not None:
        promotion = f'={promotion_piece.abbreviation}'
    
    advance_file = -1 if (piece.colour == Colour.WHITE) else 1
    ep_rank, ep_file = gh.get_en_passant(board, piece, start[0], start[1], advance_file)
    if ep_rank is not None:
        chars = 'abcdefgh' # TODO: This is ugly
        capture = f'{chars[start[0]]}x'

    # annotation for castling
    if piece.name == 'King':
        rank_diff = abs(start[0] - end[0])
        if rank_diff == 2:
            if start[0] > end[0]:
                return 'O-O-O'
            else:
                return 'O-O'
    
    # checking for conflicting moves. More than 1 piece of that type, can go to that square
    identifier = get_piece_identifier(board, piece, start, end)

    # print(f'{piece} | {translate_square(start[0], start[1])} -> {translate_square(end[0], end[1])}')
    # print(f'{identifier=}')
    # print(f'{piece.abbreviation}{identifier}{capture}{translate_square(end[0], end[1])}')
    
    return f'{piece.abbreviation}{identifier}{capture}{translate_square(end[0], end[1])}{promotion}'