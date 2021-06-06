from abc import ABCMeta, abstractmethod
from model.piece import Colour

class Piece(metaclass=ABCMeta):
    def __init__(self, colour: Colour):
        self._colour = colour
        self._has_moved = False
    
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
    def has_moved(self) -> bool:
        return self._has_moved
    
    @has_moved.setter
    def has_moved(self, value):
        self._has_moved = value

    @staticmethod
    @abstractmethod
    def movement(self) -> 'Movement':
        return None
    
    @property
    def colour(self) -> Colour:
        return self._colour
    
    def __eq__(self, other):
        if self.name == other.name and self.colour == other.colour:
            return True
        else:
            return False

    def __str__(self) -> str:
        return f'[{self.abbreviation}] {self.name}: {self.value}'