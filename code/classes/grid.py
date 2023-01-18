from .car import Car
from colorama import Fore, Style, Back
from code.visualisation.colors import COLORS
import random

class Grid():
    """Holds all elements of a Grid."""

    def __init__(self, width):
        """(insert description)"""
        self.width = int(width)
        self.board = [['_' for i in range(self.width)] for j in range(self.width)]
        self.cars = []

    def add_car(self, car):
        """(insert description)"""
        self.cars.append(car)
        self.refresh_grid()

    def move_car(self, car_type, movement):
        """(insert description)"""
        for car in self.cars:
            # Checks if the input car is on the grid
            if car.type == car_type:
                x, y = car.col, car.row
                # Checks if the input car can move the input amount of places
                if self.can_move(car, movement):
                    car.move(movement)
                    self.refresh_grid()
                    return True
        return False
    
    def can_move(self, car, movement):
        """(insert description)"""
        if car.orientation == "H":
            # Checks negative movement
            if movement < 0:
                # Checks if the user doesn't move out of the board 
                if car.col + movement >= 0:
                    # Creates a list with all the places on the board that must be empty or the input cartype
                    for i in range(car.col + movement, car.col):
                        if self.board[car.row][i] != '_' and self.board[car.row][i] != car.type:
                            return False
                    return True
            else:
                # Checks if the user doesn't move out of the board
                if car.col + movement + car.length <= self.width:
                    # Creates a list with all the places on the board that must be empty or the input cartype
                    for i in range(car.col, car.col + movement + car.length):
                        if self.board[car.row][i] != '_' and self.board[car.row][i] != car.type:
                            return False
                    return True 
        else:
            # Checks negative movement
            if movement < 0:
                # Checks if the user doesn't move out of the board
                if car.row + movement >= 0:
                    # Creates a list with all the places on the board that must be empty or the input cartype
                    for i in range(car.row + movement, car.row):
                        if self.board[i][car.col] != '_' and self.board[i][car.col] != car.type:
                            return False 
                    return True
            else:
                # Checks if the user doesn't move out of the board
                if car.row + movement + car.length <= self.width:
                    # Creates a list with all the places on the board that must be empty or the input cartype
                    for i in range(car.row, car.row + movement + car.length):
                        if self.board[i][car.col] != '_' and self.board[i][car.col] != car.type:
                            return False
                    return True
        return False


    def refresh_grid(self):
        """(insert description)"""
        self.board = [['_' for i in range(self.width)] for j in range(self.width)]
        # Places all the cars in the 2D array
        for car in self.cars:
            x, y = car.col, car.row
            if car.orientation == "H":
                for i in range(car.col, car.col + car.length):
                    self.board[car.row][i] = car.type
            else:
                for i in range(car.row, car.row + car.length):
                    self.board[i][car.col] = car.type 

    def print_grid(self):
        """(insert description)"""
        for i in range(self.width):
            for j in range(self.width):
                # Gets the color of the car
                color = COLORS[self.board[i][j]]
                # Prints the car or empty place in the right place
                if len(self.board[i][j]) == 1:
                    print(f"   {color}{self.board[i][j]}{Style.RESET_ALL}", end="")
                else:
                    print(f"  {color}{self.board[i][j]}{Style.RESET_ALL}", end="")
            print()

    def __str__(self):
        """(insert description)"""
        return "\n".join(str(row) for row in self.board)

    