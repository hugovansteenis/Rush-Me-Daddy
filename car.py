class Car():
    """Holds all elements of a Car."""

    def __init__(self, type, orientation, col, row, length):
        self.type = type
        self.orientation = orientation
        self.col = int(col)
        self.row = int(row)
        self.length = int(length)

    def move(self, direction, places):
        places = int(places)
        if self.orientation == "H":
            if direction == "left":
                self.col -= places
            elif direction == "right":
                self.col += places
        else:
            if direction == "up":
                self.row -= places 
            elif direction == "down":
                self.row += places

    def __str__(self):
        return f'Car type: {self.type}, Orientation: {self.orientation}, Column: {self.col}, Row: {self.row}, Length: {self.length}.'
