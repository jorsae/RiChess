from abc import ABCMeta, abstractmethod
from model.game import Colour

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
    def has_moved(self) -> bool:
        return False

    @property
    @abstractmethod
    def movement(self) -> 'Movement':
        pass

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