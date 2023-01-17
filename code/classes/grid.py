from .car import Car
from colorama import Fore, Style, Back
from code.visualisation.colors import COLORS
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

    def move_car(self, car_type, movement):
        for car in self.cars:
            if car.type == car_type:
                x, y = car.col, car.row
                if 0 <= x < self.width and 0 <= y < self.width:
                    if self.can_move(car, movement):
                        car.move(movement)
                        self.refresh_grid()
                        return True
        return False
    
    def can_move(self, car, movement):
        length = len(movement)
        if car.orientation == "H":
            if movement[0] == '-':
                places = int(movement[1:length])
                if car.col - places >= 0:
                    for i in range(car.col - places, car.col - places + car.length):
                        if self.board[car.row][i] != '_' and self.board[car.row][i] != car.type:
                            return False
                    return True
            elif movement[0].isnumeric():
                places = int(movement[0:length])
                if car.col + places + car.length <= self.width:
                    for i in range(car.col , car.col + places + car.length):
                        if self.board[car.row][i] != '_' and self.board[car.row][i] != car.type:
                            return False
                    return True 
        else:
            if movement[0] == '-':
                places = int(movement[1:length])
                if car.row - places >= 0:
                    for i in range(car.row - places, car.row - places + car.length):
                        if self.board[i][car.col] != '_' and self.board[i][car.col] != car.type:
                            return False 
                    return True
            elif movement[0].isnumeric():
                places = int(movement[0:length])
                if car.row + places + car.length <= self.width:
                    for i in range(car.row , car.row + places + car.length):
                        if self.board[i][car.col] != '_' and self.board[i][car.col] != car.type:
                            return False
                    return True
        return False


    def refresh_grid(self):
        self.board = [['_' for i in range(self.width)] for j in range(self.width)]
        for car in self.cars:
            x, y = car.col, car.row
            if car.orientation == "H":
                for i in range(car.col, car.col + car.length):
                    self.board[car.row][i] = car.type
            else:
                for i in range(car.row, car.row + car.length):
                    self.board[i][car.col] = car.type 

    def print_grid(self):
        for i in range(self.width):
            for j in range(self.width):
                color = COLORS[self.board[i][j]]
                if len(self.board[i][j]) == 1:
                    print(f"   {color}{self.board[i][j]}{Style.RESET_ALL}", end="")
                else:
                    print(f"  {color}{self.board[i][j]}{Style.RESET_ALL}", end="")
            print()

    def __str__(self):
        return "\n".join(str(row) for row in self.board)

    