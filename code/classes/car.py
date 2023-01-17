class Car():
    """Holds all elements of a Car."""

    def __init__(self, type, orientation, col, row, length):
        self.type = type
        self.orientation = orientation
        self.col = int(col) - 1
        self.row = int(row) - 1
        self.length = int(length)

    def move(self, movement):
        length = len(movement)
        if self.orientation == "H":
            if movement[0] == '-':
                self.col -= int(movement[1: length])
            elif movement[0].isnumeric():
                self.col += int(movement[0: length])
            else: 
                print("Wrong Usage")
        else:
            if movement[0] == '-':
                self.row -= int(movement[1: length]) 
            elif movement[0].isnumeric():
                self.row += int(movement[0: length])
            else: 
                print("Wrong Usage")

    def __str__(self):
        return f'Car type: {self.type}, Orientation: {self.orientation}, Column: {self.col}, Row: {self.row}, Length: {self.length}.'
