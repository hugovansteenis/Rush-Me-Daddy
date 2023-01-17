from .car import Car
from .grid import Grid
import csv

class Game():
    """Holds all elements of a Grid."""
    
    def __init__(self, game):
        self.game = game
        self.grid = 0
        self.load_input(f"data/{game}")
        self.history = []

    def load_input(self, filename):
        if self.game[8].isnumeric():
            number = self.game[8]
            if self.game[9].isnumeric():
                number += self.game[9]
            self.grid = Grid(number)
        
        with open(filename) as f:
            csv_reader = csv.reader(f, delimiter=',')
            next(csv_reader)
            for row in csv_reader:
                car = Car(row[0], row[1], row[2], row[3], row[4])
                self.grid.add_car(car)

    def move_car(self, car_type, movement):
        if not self.grid.move_car(car_type, movement):
            # print("You can't make this movement!")
            pass
        else:
            self.history.append((car_type, movement))
            # self.grid.print_grid()
            if self.red_unblocked():
                print("You Win")
                self.grid.print_grid()
                self.output_to_csv("solution.csv")
                return True
            return False

    def red_unblocked(self):
        exit_car = None 
        for car in self.grid.cars:
            if car.type == 'X':
                exit_car = car 
                break
        if self.grid.board[exit_car.row][self.grid.width - 1] == 'X':
            return True
        return False

    def output_to_csv(self, filename):
        with open(filename, "w") as file:
            writer = csv.writer(file)
            writer.writerow(["car", "move"])
            for move in self.history:
                writer.writerow(move)