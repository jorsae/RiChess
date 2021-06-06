from model.piece import *
from model.piece.utils import *
from model.interface import *

class Standard:
    def __init__(self):
        pass
    
    def load_rules(self):
        Bishop.movement = self.bishop_movement
    
    @staticmethod
    def bishop_movement(self):
        # TODO: Make 100 a non-magical number
        return [MoveDescription((1, 1), 100), 
                MoveDescription((1, -1), 100),
                MoveDescription((-1, 1), 100),
                MoveDescription((-1, -1), 100)]