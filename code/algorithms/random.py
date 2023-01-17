import random
from code.classes.game import Game
from code.classes.grid import Grid

def solve_rushhour(game):
    moves = list(range(-5, 6))
    exclude_zero = {0}
    numbers = list(num for num in moves if num not in exclude_zero)
    while not game.red_unblocked():
        move = str(random.choice(numbers))
        kar = random.choice(game.grid.cars)
        cartype = kar.type
        game.move_car(cartype, move)