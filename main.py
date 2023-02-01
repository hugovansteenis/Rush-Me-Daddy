from code.classes import game
from code.algorithms.random import random_algorithm
from code.algorithms.depth_first import depth_first
from code.algorithms.breadth_first import breadth_first
from code.algorithms.greedy import greedy_algorithm
from code.algorithms.beam_search import beam_search
from code.visualisation.animate import animate

from code.visualisation.histogram import make_histogram

from experiments import random_experiment
from experiments import greedy_experiment
from experiments import beam_experiment
from experiments import breadth_experiment
from experiments import depth_experiment


def run_algorithm(algorithm, name, is_silent):
    """Runs a specified algorithm and prints output if is_silent is False"""
    if is_silent:        
        test_game.print_grid = False
    else:
        test_game.grid.print_grid()

    # Run algorithm
    algorithm(test_game)
    
    if not is_silent:
        test_game.handle_output(name)

    # Create visualisations for all algorithms except random
    if len(argv) > 3 and argv[3] == "visual" and name != "Random":
        animate(game_name, name)

if __name__ == "__main__":

    from sys import argv
    
    # Check the command input for correct usage
    if len(argv) == 1:
        print("Usage: python rushhour.py [gameboardfile] (algorithm)")
        exit(1)

    # Load the data and print the begin-state of the grid
    game_name = argv[1]
    test_game = game.Game(game_name)

    # Check if the user wants to work with an algorithm or use it manually.
    if len(argv) > 2:   
        # Don't print output if there are more than three arguments given and one is "silent" 
        is_silent = (len(argv) > 3) and ("silent" in argv)
    
        if argv[2] == "random":
            run_algorithm(random_algorithm, "Random", is_silent)
        elif argv[2] == "depth":
            run_algorithm(depth_first, "Depth", is_silent)
        elif argv[2] == "breadth":
            run_algorithm(breadth_first, "Breadth", is_silent)
        elif argv[2] == "greedy":
            make_histogram("greedy")
            # run_algorithm(greedy_algorithm, "Greedy", is_silent)
        elif argv[2] == "beam":
            run_algorithm(beam_search, "Beam", is_silent)
        elif argv[2] == "random_exp":
            random_experiment.timer(1800, 60, game_name)
        elif argv[2] == "greedy_exp":
            greedy_experiment.timer(3600, 60, game_name)
        elif argv[2] == "beam_exp":
            beam_experiment.beam_script()
        elif argv[2] == "breadth_exp":
            breadth_experiment.breadth_script()
        elif argv[2] == "depth_exp":
            depth_experiment.depth_script()
        else:
            print("Wrong algorithm usage")
    else:
        test_game.grid.print_grid()
        while True:
            move = input("Which car do you want to move? (e.g. A -1) ")
            x = move.split()
            if test_game.move_car(x[0], int(x[1])):
                break
            test_game.grid.print_grid()