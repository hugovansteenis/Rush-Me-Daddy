from code.classes import game
from code.algorithms.random import random_algorithm
from code.algorithms.depth_first import depth_first
from code.algorithms.breadth_first import breadth_first
from code.algorithms.greedy import greedy_algorithm
from code.algorithms.beam_search import beam_search
from code.visualisation.animate import animate
import time
from experiments import random_experiment
from experiments import greedy_experiment
from experiments import beam_experiment
from experiments import breadth_experiment
from experiments import depth_experiment

if __name__ == "__main__":

    from sys import argv
    
    # Check the command input
    if len(argv) == 1:
        print("Usage: python rushhour.py [gameboardfile] (algorithm)")
        exit(1)

    # Load the data and print the begin-state of the grid
    game_name = argv[1]
    test_game = game.Game(game_name)

    # Check if the user wants to work with an algorithm or use it manually.
    if len(argv) > 2:
        if argv[2] == "random":
            algorithm_name = "Random"
            random_algorithm(test_game)
            test_game.handle_output(algorithm_name)
        elif argv[2] == "depth":
            algorithm_name = "Depth"
            test_game.grid.print_grid()
            start = time.time()
            depth_first(test_game)
            end = time.time()
            print(end - start)
            test_game.handle_output(algorithm_name)
            if len(argv) > 3 and argv[3] == "visual":
                animate(game_name)
        elif argv[2] == "breadth":
            algorithm_name = "Breadth"
            test_game.grid.print_grid()
            breadth_first(test_game)
            test_game.handle_output(algorithm_name)
            if len(argv) > 3 and argv[3] == "visual":
                animate(game_name)
        elif argv[2] == "greedy":
            algorithm_name = "Greedy"
            test_game.grid.print_grid()
            greedy_algorithm(test_game)
            test_game.handle_output(algorithm_name)
            if len(argv) > 3 and argv[3] == "visual":
                animate(game_name)
        elif argv[2] == "beam":
            algorithm_name = "Beam"
            test_game.grid.print_grid()
            beam_search(test_game)
            test_game.handle_output(algorithm_name)
            if len(argv) > 3 and argv[3] == "visual":
                animate(game_name)
        elif argv[2] == "random_exp":
            random_experiment.timer(100, 10)
        elif argv[2] == "greedy_exp":
            greedy_experiment.timer(100, 100)
        elif argv[2] == "beam_exp":
            beam_experiment.timer(100, 100)
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


    

