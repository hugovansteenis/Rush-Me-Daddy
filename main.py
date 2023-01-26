from code.classes import game
from code.algorithms.random import random_algorithm
from code.algorithms.depth_first import depth_first
from code.algorithms.breadth_first import breadth_first
from code.visualisation.animate import animate
               
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
            test_game.grid.print_grid()
            random_algorithm(test_game)
            test_game.handle_output(algorithm_name)
            exit(2)
        elif argv[2] == "depth":
            algorithm_name = "Depth First"
            test_game.grid.print_grid()
            depth_first(test_game)
            test_game.handle_output(algorithm_name)
            if len(argv) > 3 and argv[3] == "visual":
                animate(game_name)
            exit(3)
        elif argv[2] == "breadth":
            algorithm_name = "Breadth First"
            test_game.grid.print_grid()
            breadth_first(test_game)
            test_game.handle_output(algorithm_name)
            if len(argv) > 3 and argv[3] == "visual":
                animate(game_name)
            exit(4)
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


    

