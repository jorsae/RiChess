from abc import ABCMeta, abstractmethod
from pieces import Piece
from model import Colour

class King(Piece):
    @property
    def name(self):
        return "King"
    
    @property
    def abbreviation(self):
        return "K"
    
    @property
    def value(self):
        return 100
    
    @property
    def movement(self):
        pass