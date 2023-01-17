from code.classes import game
from code.algorithms.random import solve_rushhour
               
if __name__ == "__main__":

    from sys import argv

    if len(argv) != 2:
        print("Usage: python rushhour.py [gameboardfile]")
        exit(1)

    game_name = argv[1]

    test_game = game.Game(game_name)

    test_game.grid.print_grid()

    solve_rushhour(test_game)

    # while True:
    #     move = input("Which car do you want to move? (e.g. A -1) ")
    #     x = move.split()
    #     if test_game.move_car(x[0], x[1]):
    #         break

