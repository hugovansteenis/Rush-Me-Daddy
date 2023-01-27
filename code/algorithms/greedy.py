import random
import copy
from code.classes.game import Game
from code.classes.grid import Grid
from code.algorithms import heuristic

def greedy_algorithm(game):
    """Solves rushhour by random an algoritm that selects random cars and makes random moves"""
    # Makes a list with steps from -5 to 5
    moves = list(range(-5, 6))
    exclude_zero = {0}
    numbers = list(num for num in moves if num not in exclude_zero)
    red_car = heuristic.find_red_car(game)
    while not game.red_unblocked():
        if game.grid.can_move(red_car, 1):
            game.move_car(red_car, 1)
        for car in heuristic.heuristic_value6(game):
            if game.grid.can_move(car, 1):
                game.move_car(car.type, 1)
        # Chooses a random amount of steps and a random car
        random_move = random.choice(numbers)
        random_car = random.choice(game.grid.cars)
        cartype = random_car.type
        game.move_car(cartype, random_move)
    # """Solves rushhour by prioritizing moves that will clear the path for the red car"""
    # for car in game.grid.cars:
    #     if car.type == 'X':
    #         red_car = car

    # while not game.red_unblocked():
    #     # Check if red car can advance position if so move the red car.
    #     if game.grid.can_move(red_car, 1):
    #         game.move_car(red_car, 1)
    #         continue
    #     # Prioritize moving cars with horizontal orientation to the left
    #     for car in game.grid.cars:
    #         if car.orientation == 'H':
    #             if game.grid.can_move(car, -1):
    #                 game.move_car(car.type, -1)
    #                 break
    #     # Move cars with a vertical orientation up or down
    #     for car in game.grid.cars:
    #         if car.orientation == 'V':
    #             if game.grid.can_move(car, -1):
    #                 game.move_car(car.type, -1)
    #                 break
    #             elif game.grid.can_move(car, 1):
    #                 game.move_car(car.type, 1)
    #                 break
        
    #     for car in game.grid.cars:
    #         if car.orientation == 'H':
    #             if game.grid.can_move(car, -1):
    #                 game.move_car(car.type, -1)
    #                 break
    #             else:
    #                 game.move_car(car.type, 1)
    #                 break