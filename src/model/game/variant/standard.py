from model.piece import *
from model.piece.utils import *

class Standard:
    def __init__(self):
        pass
    
    def load_rules(self):
        Bishop.movement = self.new
    
    @staticmethod
    def new():
        print('new')