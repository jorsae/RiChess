def untranslate_square(rank, file):
    try:
        chars = 'abcdefgh'
        file = int(file)
        return chars.index(rank), 8-file
    except:
        return None, None

def get_move(move):
    try:
        start_pos = move[:2]
        end_pos = move[2:]

        start_rank, start_file = untranslate_square(start_pos[0], start_pos[1])
        end_rank, end_file = untranslate_square(end_pos[0], end_pos[1])
        return (start_rank, start_file), (end_rank, end_file)
    except Exception as e:
        print(e)
        return None, None