class MoveDescription:
    def __init__(self, vector: tuple, range: int, walk_through: bool = False):
        self.vector = vector
        self.range = range
        self.walk_through = walk_through
    
    def __str__(self):
        return f'{self.vector}: {self.range}, {self.walk_through=}'