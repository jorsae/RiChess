from abc import ABCMeta, abstractmethod
from model import Colour

class Piece(metaclass=ABCMeta):
    def __init__(self, colour: Colour):
        self._colour = colour
    
    @property
    @abstractmethod
    def name(self) -> str:
        return "Piece"
    
    @property
    @abstractmethod
    def abbreviation(self) -> str:
        return '?'
    
    @property
    @abstractmethod
    def value(self) -> int:
        return -1
    
    @property
    @abstractmethod
    def movement(self) -> 'Movement':
        pass
    
    @property
    def colour(self) -> Colour:
        return self._colour