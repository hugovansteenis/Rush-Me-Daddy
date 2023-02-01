import random
import copy
from code.classes.game import Game
from code.classes.grid import Grid
from code.algorithms import heuristic

def greedy_algorithm(game):
    """ Uses the random algorithm as baseline and added heuristics to 'improve' the algorithm """
    # Makes a list with steps from -5 to 5
    moves = list(range(-5, 6))
    exclude_zero = {0}
    numbers = list(num for num in moves if num not in exclude_zero)
    # Red_car is a variable which represents the red car so it is easier to use in the algorithm and heuristics
    red_car = heuristic.find_red_car(game)
    while not game.red_unblocked():
        # Checks if the red car can move to the right
        if game.grid.can_move(red_car, 1):
            game.move_car(red_car, 1)
            continue
        # Checks if the cars blocking the red car can move using the chosen heuristic in heuristic.py
        for car in heuristic.heuristic_blocking_red_car(game):
            if game.grid.can_move(car, 1):
                game.move_car(car.type, 1)
                break
        # Chooses a random amount of steps and a random car
        random_move = random.choice(numbers)
        random_car = random.choice(game.grid.cars)
        cartype = random_car.type
        game.move_car(cartype, random_move)
    game.output_to_csv("results/greedy/output.csv")