from car import Car

class Grid():
    """Holds all elements of a Grid."""

    def __init__(self, width):
        self.width = int(width)
        self.board = [['0' for i in range(self.width)] for j in range(self.width)]
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)
        self.refresh_grid()

    def move_car(self, car_type, direction, places):
        for car in self.cars:
            if car.type == car_type:
                x, y = car.col, car.row
                if 0 <= x < self.width and 0 <= y < self.width:
                    print("Check")
                    if self.can_move(car, direction, places):
                        car.move(direction, places)
                        self.refresh_grid()
                        return True
                    # else:
                    #     print("Doei")
                    #     car.move(direction, places)
                    #     self.refresh_grid()
                    #     return True
        return False
    
    def can_move(self, car, direction, places):
        places = int(places) + 1
        counter = 0 
        if car.orientation == "H":
            if direction == "left":
                if car.col - places >= 0:
                    for i in range(car.col - places, car.col - places + car.length):
                        counter += 1
                        print(counter)
                        if self.board[car.row - 1][i] != 0 or self.board[car.row][i] != car.type:
                            print(i)
                            print(car.type)
                            print(self.board[car.row - 1][i])
                            return False
                    return True
            elif direction == "right":
                if car.col + places + car.length - 1 < self.width:
                    for i in range(car.col + places, car.col + places + car.length):
                        if self.board[car.row][i] != 0:
                            return False
                    return True 
        else:
            if direction == "up":
                if car.row - places >= 0:
                    for i in range(car.row - places, car.row - places + car.length):
                        if self.board[i][car.col] != 0:
                            return False 
                    return True
            elif direction == "down":
                if car.row +  places + car.length - 1 < self.width:
                    for i in range(car.row + places, car.row + places + car.length):
                        if self.board[i][car.col] != 0:
                            return False
                    return True
        return False


    def refresh_grid(self):
        self.board = [['0' for i in range(self.width)] for j in range(self.width)]
        for car in self.cars:
            x, y = car.col, car.row
            if car.orientation == "H":
                for i in range(car.col, car.col + car.length):
                    self.board[car.row - 1][i - 1] = car.type
            else:
                for i in range(car.row, car.row + car.length):
                    self.board[i - 1][car.col - 1] = car.type 

    def print_grid(self):
        for row in self.board:
            print(row)

    def __str__(self):
        return "\n".join(str(row) for row in self.board)

    