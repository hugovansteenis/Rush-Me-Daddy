class Car():
    """Holds all elements of a Car."""

    def __init__(self, type, orientation, col, row, length):
        self.type = type
        self.orientation = orientation
        self.col = col
        self.row = row
        self.length = length

    def __str__(self):
        return f'Car type: {self.type}, Orientation: {self.orientation}, Column: {self.col}, Row: {self.row}, Length: {self.length}.'
