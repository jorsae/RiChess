from model.game import Colour, BoardPiece

class Board():
    def __init__(self, ranks: int = 8, files: int = 8, ):
        self.ranks = ranks
        self.files = files
        self.move_history = []
        self.turn = Colour.WHITE
        self.halfmove = 0
        self.fullmove = 0
        self.board = [[None for i in range(self.ranks)] for j in range(self.files)]

    def get_piece(self, rank, file):
        return self.board[rank][file]

    def place_piece(self, piece, rank, file):
        self.board[rank][file] = piece

    def place_pieces(self, board_pieces):
        for bp in board_pieces:
            self.place_piece(bp.piece, bp.rank, bp.file)
    
    def load_from_fen(self, fen_parser):
        self.place_pieces(fen_parser.pieces)
        self.player_turn = fen_parser.player_turn
        self.halfmove = fen_parser.halfmove
        self.fullmove = fen_parser.fullmove
        if fen_parser.last_move is not None:
            self.move_history.append(fen_parser.last_move)
        # TODO: Parse castling rules from fen

    def get_piece_list(self):
        piece_list = []
        for rank in range(self.ranks):
            for file in range(self.files):
                piece = self.get_piece(rank, file)
                if piece is not None:
                    piece_list.append(BoardPiece(piece, rank, file))
        return piece_list

    def __str__(self):
        output = ''
        for rank in range(self.ranks):
            line = ''
            for file in range(self.files):
                piece = self.get_piece(rank, file)
                if piece is None:
                    line += ' 0 |'
                else:
                    if piece.colour == Colour.BLACK:
                        line += f' {piece.abbreviation.lower()} |'
                    else:
                        line += f' {piece.abbreviation.upper()} |'
            output += f'{line[:-2]}\n'
        return output