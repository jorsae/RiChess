from model.piece import *
from model.piece.utils import *
from model.interface import *

class Standard:
    def load_rules(self):
        King.movement = self.king_movement
        Queen.movement = self.queen_movement
        Rook.movement = self.rook_movement
        Bishop.movement = self.bishop_movement
        Knight.movement = self.knight_movement
        Pawn.movement = self.pawn_movement
    
    def king_movement(self):
        return [MoveDescription((1, 0), 2), 
                MoveDescription((0, 1), 2),
                MoveDescription((-1, 0), 2),
                MoveDescription((0, -1), 2),
                MoveDescription((1, 1), 2), 
                MoveDescription((1, -1), 2),
                MoveDescription((-1, 1), 2),
                MoveDescription((-1, -1), 2)]

    def queen_movement(self):
        return [MoveDescription((1, 0), 100), 
                MoveDescription((0, 1), 100),
                MoveDescription((-1, 0), 100),
                MoveDescription((0, -1), 100),
                MoveDescription((1, 1), 100), 
                MoveDescription((1, -1), 100),
                MoveDescription((-1, 1), 100),
                MoveDescription((-1, -1), 100)]

    def rook_movement(self):
        return [MoveDescription((1, 0), 100), 
                MoveDescription((0, 1), 100),
                MoveDescription((-1, 0), 100),
                MoveDescription((0, -1), 100)]

    def bishop_movement(self):
        return [MoveDescription((1, 1), 100), 
                MoveDescription((1, -1), 100),
                MoveDescription((-1, 1), 100),
                MoveDescription((-1, -1), 100)]
    
    def knight_movement(self):
        return [MoveDescription((2, 1), 2), 
                MoveDescription((1, 2), 2),
                MoveDescription((-2, 1), 2),
                MoveDescription((2, -1), 2),
                MoveDescription((-2, -1), 2),
                MoveDescription((-1, -2), 2),
                MoveDescription((-1, 2), 2),
                MoveDescription((1, -2), 2)]

    def pawn_movement(self):
        return []