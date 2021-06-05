print('1')
from model.parser import *
print('2')
from model.game import *
print('3')

king = King(Colour.BLACK)
print(king)

pawn = Pawn(Colour.BLACK)
pawn2 = Pawn(Colour.WHITE)

board = Board()
print(board)
board.board[0][0] = pawn
board.board[0][1] = pawn2
print(board)

fp = FenParser("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
print(fp.parse())