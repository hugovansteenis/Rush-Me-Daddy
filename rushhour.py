from car import Car
from grid import Grid
from history import History
import csv

class Game():
    """Holds all elements of a Grid."""
    
    def __init__(self, game):
        self.game = game
        self.grid = 0
        self.load_input(f"gameboards/{game}")
        self.exit_car_type = "X"
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

    def move_car(self, car_type, direction, places):
        if not self.grid.move_car(car_type, direction, places):
            print("Can't move the car in that direction")
        else:
            self.history.append((car_type, direction, places))
            if self.red_unblocked():
                print("You Win")
                self.output_to_csv("solution.csv")

    def red_unblocked(self):
        exit_car = None 
        for car in self.grid.cars:
            if car.type == self.exit_car_type:
                exit_car = car 
                break
        if exit_car.orientation == "H":
            if self.grid.board[exit_car.row][exit_car.col - 1] == 0  and self.grid.board[exit_car.row][exit_car.row + exit_car.length] == 0:
                return True
        else: 
            if self.grid.board[exit_car.row - 1][exit_car.col] == 0 and self.grid.board[exit_car.row + exit_car.length][exit_car.col] == 0:
                return True
        return False

    def output_to_csv(self, filename):
        with open(filename, "w") as file:
            writer = csv.writer(file)
            writer.writerow(["Car", "Direction", "Places"])
            for move in self.history:
                writer.writerow(move)
               

if __name__ == "__main__":

    from sys import argv

    # Check command line arguments.
    if len(argv) not in [1, 2]:
        print("Usage: python rushhour.py [gameboardfile]")
        exit(1)

    game_name = argv[1]

    game = Game(game_name)

    while True:
        game.grid.print_grid()
        move = input("What car do you want to move? ")
        x = move.split()
        game.move_car(x[0], x[1], x[2])
