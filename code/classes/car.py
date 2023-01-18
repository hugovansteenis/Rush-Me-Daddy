class Car():
    """Holds all elements of a Car."""

    def __init__(self, type, orientation, col, row, length):
        """(insert description)"""
        self.type = type
        self.orientation = orientation
        self.col = int(col) - 1
        self.row = int(row) - 1
        self.length = int(length)

    def move(self, movement):
        """(insert description)"""
        if self.orientation == "H":
            self.col += movement
        else:
            self.row += movement

    def __str__(self):
        """(insert description)"""
        return f'Car type: {self.type}, Orientation: {self.orientation}, Column: {self.col}, Row: {self.row}, Length: {self.length}.'
