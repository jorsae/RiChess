class MoveDescription:
    def __init__(self, vector: tuple, range: int):
        self.vector = vector
        self.range = range
    
    def __str__(self):
        return f'{self.vector}: {self.range}, {self.walk_through=}'