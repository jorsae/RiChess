class MoveHistory:
    def __init__(self, start: tuple, end: tuple):
        self.start = start
        self.end = end
    
    def __str__(self):
        return f'{self.start}, {self.end}'