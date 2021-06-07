def translate_square(rank, file):
    chars = 'abcdefgh'
    return f'{chars[rank]}{file}'

def annotate_move(board, start, end):
    piece = board.get_piece(start[0], start[1])
    if piece is None:
        return None
    
    cap_piece = board.get_piece(end[0], end[1])
    capture = ''
    if cap_piece is not None:
        capture = f'x{translate_square(end[0], end[1])}'
    
    # TODO: check for conflicting moves (bishop/rook/knight/queen). e.g: Rad1
    # TODO: add annotation for castling

    print(f'{piece.abbreviation}{translate_square(start[0], start[1])}{capture}')