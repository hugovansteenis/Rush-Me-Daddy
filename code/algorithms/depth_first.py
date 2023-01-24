import copy
from code.classes.game import Game
from code.classes.grid import Grid

    # Initial state of game board
    # states.append(game.grid.board)
    
    # 'A': ['B', 'C'], 
    # 'B': ['D', 'E']

def depth_first2(game):
    # Initialize states and archive
    states = copy.deepcopy(game.grid.board)
    archive = {tuple(x) for x in states}
    print(archive)
    1/0

    while states:
        # Create new game board state
        new_state = states.pop()

        # If board is solved, return solution.csv
        # Build children 
        moves = list(range(-5, 6))
        exclude_zero = {0}
        moves = list(num for num in moves if num not in exclude_zero)

        # Iterate over the possible moves per car
        for car in game.grid.cars:
            for move in moves:
                # Get all possible moves for every car and add board to states
                if game.grid.can_move(car, move):
                    new_game = copy.deepcopy(game)
                    new_game.grid.move_car(car.type, move)

                    # Get new game board
                    new_game_board = new_game.grid.board
                    new_game_board = {tuple(x) for x in new_game_board}
                    if new_game_board not in archive:
                        archive.add(tuple(new_game_board))
                        states.append(new_game_board)
        print(states)


def depth_first(game):
    # Initialize states and archive
    states = [copy.deepcopy(game)]
    archive = set()

    while len(states) > 0:
        # Create new game board state
        game = states.pop()
        game.grid.print_grid()
        print(game.grid)

        # If board is solved, return solution.csv
        if game.red_unblocked():
            return True

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
                        print(len(archive))
                        #print(f"archive: {archive[newest_game]}")
                        states.append(newest_game)
                        #print(f"States: {states}")
    return False