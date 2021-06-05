from model import *

king = King(Colour.BLACK)
print(king)

pawn = Pawn(Colour.BLACK)
print(pawn)

board = Board()
print(board)
board.board[0][0] = pawn
print(board)