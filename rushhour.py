from car import Car
from grid import Grid
import csv

class Game():
    """Holds all elements of a Grid."""
    
    def __init__(self, game):
        self.game = game
        self.load_input(f"gameboards/{game}")

    def load_input(self, filename):
        with open(filename) as f:
            csv_reader = csv.reader(f, delimiter=',')
            next(csv_reader)
            for row in csv_reader:
                    car = Car(row[0], row[1], row[2], row[3], row[4])
                    print(car)

        if self.game[8].isnumeric():
            number = self.game[8]
            if self.game[9].isnumeric():
                number += self.game[9]
            grid = Grid(number)
            print(grid)
        

if __name__ == "__main__":

    from sys import argv

    # Check command line arguments.
    if len(argv) not in [1, 2]:
        print("Usage: python rushhour.py [gameboardfile]")
        exit(1)

    game_name = argv[1]

    game = Game(game_name)