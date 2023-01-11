class Grid():
    """Holds all elements of a Grid."""

    def __init__(self, width):
        self.width = width 

    def __str__(self):
        return f'This grid is {self.width}x{self.width}.'

    