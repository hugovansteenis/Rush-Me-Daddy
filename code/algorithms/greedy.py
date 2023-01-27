from code.classes.game import Game
from code.classes.grid import Grid

def greedy_algorithm(game):
    """Solves rushhour by prioritizing moves that will clear the path for the red car"""
    while not game.red_unblocked():
        # Check if red car can advance position if so move the red car.
        if game.grid.can_move('X', 1):
            game.move_car('X', 1)
            continue
        # Prioritize moving cars with horizontal orientation to the left
        for car in game.grid.cars:
            if car.orientation == 'H':
                if game.grid.can_move(car.type, -1):
                    game.move_car(car.type, -1)
                    break
        # Move cars with a vertical orientation up or down
        for car in game.grid.cars:
            if car.orientation == 'V':
                if game.grid.can_move(car.type, -1):
                    game.move_car(car.type, -1)
                    break
                elif game.grid.can_move(car.type, 1):
                    game.move_car(car.type, 1)
                    break