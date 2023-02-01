"""Gemaakt door Sarah Blok"""

import copy
from code.classes.game import Game
from code.algorithms.heuristic import heuristic_value2


def beam_search(game:Game):
    """Searches a graph for a solution state by selecting only the w most promising states"""
    # Initialize states and archive
    states = [copy.deepcopy(game)]
    archive = set()
    w = 3

    while len(states) > 0:
        # Create new game board state
        game = states.pop(0)

        # If board is solved, save solution in a CSV file
        if game.red_unblocked():
            print(f"length game history: {len(game.history)}")
            game.output_to_csv("results/beam/output.csv")
            return True
        else:
            # Build children for current node/state
            moves = list(range(-5, 6))
            exclude_zero = {0}
            moves = list(num for num in moves if num not in exclude_zero)
            
            temp_states = []

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
                            temp_states.append(newest_game)
            
            # Keep only the w most promising states which have the least cars blocking the red car
            temp_states = sorted(temp_states, key=lambda x: heuristic_value2(x))[:w]
            states.extend(temp_states)

