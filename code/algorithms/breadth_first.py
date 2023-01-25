"""Gemaakt door Sarah Blok"""

import copy
from code.classes.game import Game
from code.classes.grid import Grid

def breadth_first(game):
    # Initialize states and archive
    states = [copy.deepcopy(game)]
    archive = set()

    while len(states) > 0:
        # Create new game board state
        game = states.pop(0)

        # If board is solved, return solution.csv
        if game.red_unblocked():
            return True

        else:
            # Build children 
            moves = list(range(-5, 6))
            exclude_zero = {0}
            moves = list(num for num in moves if num not in exclude_zero)
            
            # Iterate over the possible moves per car
            for car in game.grid.cars:
                for move in moves:
                    # Get all possible moves for every car and add board to states
                    if game.grid.can_move(car, move):
                        new_car = copy.deepcopy(car)
                        newest_game = copy.deepcopy(game)
                        newest_game.move_car(new_car.type, move)
                        
                        _str = str(newest_game.grid)
                        if _str not in archive:
                            archive.add(_str)
                            states.append(newest_game)
    return False