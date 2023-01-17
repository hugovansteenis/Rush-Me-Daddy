import random
from code.classes.game import Game
from code.classes.grid import Grid

def solve_rushhour(game):
    moves = list(range(-5, 6))
    while not game.red_unblocked():
        move = str(random.choice(moves))
        kar = random.choice(game.grid.cars)
        cartype = kar.type
        game.move_car(cartype, move)