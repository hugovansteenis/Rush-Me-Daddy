from car import Car

class Grid():
    """Holds all elements of a Grid."""

    def __init__(self, width):
        self.width = int(width)
        self.board = [['0' for i in range(self.width)] for j in range(self.width)]

    def add_car(self, car):
        if car.orientation == "H":
            for i in range(car.col, car.col + car.length):
                self.board[car.row - 1][i - 1] = car.type
        else:
            for i in range(car.row, car.row + car.length):
                self.board[i - 1][car.col - 1] = car.type 
    
    def __str__(self):
        return "\n".join(str(row) for row in self.board)

    