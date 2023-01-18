from code.classes import game
from code.algorithms.random import solve_rushhour
               
if __name__ == "__main__":

    from sys import argv

    # Check the command input
    if len(argv) == 1:
        print("Usage: python rushhour.py [gameboardfile] (algorithm)")
        exit(1)

    # Load the data and print the begin-state of the grid
    game_name = argv[1]
    test_game = game.Game(game_name)
    test_game.grid.print_grid()

    # Check if the user wants to work with an algorithm or use it manually.
    if len(argv) > 2:
        if argv[2] == "algorithm":
            solve_rushhour(test_game)
            exit(2)
        else:
            print("Wrong algorithm usage")
    else:
        while True:
            move = input("Which car do you want to move? (e.g. A -1) ")
            x = move.split()
            if test_game.move_car(x[0], int(x[1])):
                break
            test_game.grid.print_grid()


    

