class Car():
    """Holds all elements of a Car."""

    def __init__(self, type, orientation, col, row, length):
        """Defines the elements of the car which are given in the input file.
        The car is defined by the type which is the Letter of the car, orientation which is Horizontal or Vertical,
        the position of the car on the grid and the length of the car."""
        self.type = type
        self.orientation = orientation
        self.col = int(col) - 1
        self.row = int(row) - 1
        self.length = int(length)

    def move(self, movement):
        """If orientation of the car is Horizontal move the car to a different column.
        Otherwise the orientation of the car is Vertical then move the car through the rows."""
        if self.orientation == "H":
            self.col += movement
        else:
            self.row += movement

    def __str__(self):
        """Returns the string function of the car object"""
        return f'Car type: {self.type}, Orientation: {self.orientation}, Column: {self.col}, Row: {self.row}, Length: {self.length}.'
