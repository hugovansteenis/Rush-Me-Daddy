import random
from code.classes.game import Game
from code.classes.grid import Grid

def solve_rushhour(game):
    """(insert description)"""
    # Makes a list with steps from -5 to 5
    moves = list(range(-5, 6))
    exclude_zero = {0}
    numbers = list(num for num in moves if num not in exclude_zero)
    while not game.red_unblocked():
        # Chooses a random amount of steps and a random car
        random_move = random.choice(numbers)
        random_car = random.choice(game.grid.cars)
        cartype = random_car.type
        game.move_car(cartype, random_move)