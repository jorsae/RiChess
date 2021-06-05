from model.game import *

king = King(Colour.BLACK)
print(king)

pawn = Pawn(Colour.BLACK)
pawn2 = Pawn(Colour.WHITE)

board = Board()
print(board)
board.board[0][0] = pawn
board.board[0][1] = pawn2
print(board)

print(board.parse("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"))