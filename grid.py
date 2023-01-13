from car import Car
from colorama import Fore, Style, Back
from colors import COLORS
import random

class Grid():
    """Holds all elements of a Grid."""

    def __init__(self, width):
        self.width = int(width)
        self.board = [['_' for i in range(self.width)] for j in range(self.width)]
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)
        self.refresh_grid()

    def move_car(self, car_type, direction, places):
        for car in self.cars:
            if car.type == car_type:
                x, y = car.col, car.row
                if 0 <= x <= self.width and 0 <= y <= self.width:
                    if self.can_move(car, direction, places):
                        car.move(direction, places)
                        self.refresh_grid()
                        return True
        return False
    
    def can_move(self, car, direction, places):
        places = int(places)
        counter = 0 
        if car.orientation == "H":
            if direction == "left":
                if car.col - places >= 0:
                    for i in range(car.col - (places + 1), car.col - (places + 1) + car.length):
                        counter += 1
                        if self.board[car.row - 1][i] != '_' and self.board[car.row - 1][i] != car.type:
                            return False
                    return True
            elif direction == "right":
                if car.col + places + car.length - 1 < self.width:
                    for i in range(car.col + (places - 1), car.col + (places - 1) + car.length):
                        if self.board[car.row - 1][i] != '_' and self.board[car.row - 1][i] != car.type:
                            return False
                    return True 
        else:
            if direction == "up":
                if car.row - places >= 0:
                    for i in range(car.row - (places + 1), car.row - (places + 1) + car.length):
                        if self.board[i][car.col - 1] != '_' and self.board[i][car.col - 1] != car.type:
                            return False 
                    return True
            elif direction == "down":
                if car.row + places + car.length - 1 <= self.width:
                    for i in range(car.row + (places - 1), car.row + (places - 1) + car.length):
                        if self.board[i][car.col - 1] != '_' and self.board[i][car.col - 1] != car.type:
                            print(self.board[i][car.col - 1])
                            return False
                    return True
        return False


    def refresh_grid(self):
        self.board = [['_' for i in range(self.width)] for j in range(self.width)]
        for car in self.cars:
            x, y = car.col, car.row
            if car.orientation == "H":
                for i in range(car.col, car.col + car.length):
                    self.board[car.row - 1][i - 1] = car.type
            else:
                for i in range(car.row, car.row + car.length):
                    self.board[i - 1][car.col - 1] = car.type 

    def print_grid(self):
        for i in range(self.width):
            for j in range(self.width):
                color = COLORS[self.board[i][j]]
                print(f"  {color}{self.board[i][j]}{Style.RESET_ALL}", end="")
            print()

    def __str__(self):
        return "\n".join(str(row) for row in self.board)

    