def untranslate_square(rank, file):
    try:
        chars = 'abcdefgh'
        file = int(file)
        return chars.index(rank), 8-file
    except:
        return None, None

def get_move(board):
    try:
        move = input('move: ')
        if move == 'q':
            return False
        
        start_pos = move[:2]
        end_pos = move[2:]

        start_rank, start_file = untranslate_square(start_pos[0], start_pos[1])
        end_rank, end_file = untranslate_square(end_pos[0], end_pos[1])
        print(f'{start_rank}{start_file}')
        print(f'{end_rank}{end_file}')

        board.move_to((start_rank, start_file), (end_rank, end_file))
        print(board)

        return True
    except Exception as e:
        print(e)
        return True