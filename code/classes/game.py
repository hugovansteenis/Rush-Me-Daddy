from .car import Car
from .grid import Grid
import csv

class Game():
    """Holds all elements of a Grid."""
    
    def __init__(self, game):
        """(insert description)"""
        self.game = game
        self.grid = 0
        self.load_input(f"data/{game}")
        self.history = []

    def load_input(self, filename):
        """(insert description)"""
        if self.game[8].isnumeric():
            number = self.game[8]
            if self.game[9].isnumeric():
                number += self.game[9]
            self.grid = Grid(number)
        
        # Reads the inputdata and creates all the necessary cars objects
        with open(filename) as f:
            csv_reader = csv.reader(f, delimiter=',')
            next(csv_reader)
            for row in csv_reader:
                car = Car(row[0], row[1], row[2], row[3], row[4])
                self.grid.add_car(car)

    def move_car(self, car_type, movement):
        """(insert description)"""
        if not self.grid.move_car(car_type, movement):
            pass
        else:
            # Stores the move in history for output
            self.history.append((car_type, movement))
            # Completes the program if the red car is in the right spot
            if self.red_unblocked():
                print("You Win")
                self.grid.print_grid()
                print(len(self.history))
                self.output_to_csv("output.csv")
                return True
            return False

    def red_unblocked(self):
        """(insert description)"""
        exit_car = None 
        for car in self.grid.cars:
            if car.type == 'X':
                exit_car = car 
                break
        # Checks if the red car is at the end of the board
        if self.grid.board[exit_car.row][self.grid.width - 1] == 'X':
            return True
        return False

    def output_to_csv(self, filename):
        """(insert description)"""
        with open(filename, "w") as file:
            writer = csv.writer(file)
            writer.writerow(["car", "move"])
            # Retrieves all the moves in history and writes these into the outputfile
            for move in self.history:
                writer.writerow(move)