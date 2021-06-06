from model.piece import *
from model.piece.utils import *
from model.interface import *

class Standard:
    def __init__(self):
        pass
    
    def load_rules(self):
        King.movement = self.king_movement
        Queen.movement = self.queen_movement
        Rook.movement = self.rook_movement
        Bishop.movement = self.bishop_movement
        Knight.movement = self.knight_movement
        Pawn.movement = self.pawn_movement
    
    @staticmethod
    def king_movement(self):
        # TODO: Make 100 a non-magical number
        return [MoveDescription((1, 0), 2), 
                MoveDescription((0, 1), 2),
                MoveDescription((-1, 0), 2),
                MoveDescription((0, -1), 2),
                MoveDescription((1, 1), 2), 
                MoveDescription((1, -1), 2),
                MoveDescription((-1, 1), 2),
                MoveDescription((-1, -1), 2)]

    @staticmethod
    def queen_movement(self):
        # TODO: Make 100 a non-magical number
        return [MoveDescription((1, 0), 100), 
                MoveDescription((0, 1), 100),
                MoveDescription((-1, 0), 100),
                MoveDescription((0, -1), 100),
                MoveDescription((1, 1), 100), 
                MoveDescription((1, -1), 100),
                MoveDescription((-1, 1), 100),
                MoveDescription((-1, -1), 100)]

    @staticmethod
    def rook_movement(self):
        # TODO: Make 100 a non-magical number
        return [MoveDescription((1, 0), 100), 
                MoveDescription((0, 1), 100),
                MoveDescription((-1, 0), 100),
                MoveDescription((0, -1), 100)]

    @staticmethod
    def bishop_movement(self):
        # TODO: Make 100 a non-magical number
        return [MoveDescription((1, 1), 100), 
                MoveDescription((1, -1), 100),
                MoveDescription((-1, 1), 100),
                MoveDescription((-1, -1), 100)]
    
    @staticmethod
    def knight_movement(self):
        # TODO: Make 100 a non-magical number
        return [MoveDescription((2, 1), 2), 
                MoveDescription((1, 2), 2),
                MoveDescription((-2, 1), 2),
                MoveDescription((2, -1), 2),
                MoveDescription((-2, -1), 2),
                MoveDescription((-1, -2), 2),
                MoveDescription((-1, 2), 2),
                MoveDescription((1, -2), 2)]

    @staticmethod
    def pawn_movement(self):
        # TODO: How to code it so that move depends on colour
        # TODO: Make 100 a non-magical number
        return []