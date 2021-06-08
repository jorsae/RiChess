import model.game.game_helper as gh
from model.piece.utils.colour import Colour

def translate_square(rank, file):
    chars = 'abcdefgh'
    return f'{chars[rank]}{8-file}'

# TODO: Clean this up
def get_piece_identifier(board, piece, start, end):
    if piece.name == 'Pawn':
        return ''
    
    start_pos = []
    same_pieces = board.filter_piece_list(piece_filter=piece.name, colour_filter=piece.colour)
    for same_piece in same_pieces:
        moves = gh.get_available_moves(board, same_piece.rank, same_piece.file)
        moves = list(filter(lambda m: m[0] == end[0] and m[1] == end[1], moves))
        if moves == [end]:
            print(f'{same_piece}: {moves} vs {end[0]}, {end[1]}')
            start_pos.append((same_piece.rank, same_piece.file))
    
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
        if rank_id <= 1:
            chars = 'abcdefgh' #TODO: This is ugly
            return f'{chars[start[0]]}'
        else:
            if piece.colour == Colour.BLACK:
                return start[1] + 1
            else:
                return 8 - start[1]

def annotate_move(board, start, end):
    piece = board.get_piece(start[0], start[1])
    if piece is None:
        return None
    
    cap_piece = board.get_piece(end[0], end[1])
    capture = ''
    if cap_piece is not None:
        capture = f'x{translate_square(end[0], end[1])}'
    
    # checking for conflicting moves. More than 1 piece of that type, can go to that square
    print(f'{piece} | {translate_square(start[0], start[1])} -> {translate_square(end[0], end[1])}')
    identifier = get_piece_identifier(board, piece, start, end)
    print(f'{identifier=}')

    # TODO: add annotation for castling
    print(f'{piece.abbreviation}{identifier}{capture}{translate_square(end[0], end[1])}')
    return f'{piece.abbreviation}{identifier}{capture}{translate_square(end[0], end[1])}'