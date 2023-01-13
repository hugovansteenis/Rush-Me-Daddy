from game import Game
               
if __name__ == "__main__":

    from sys import argv

    # Check command line arguments.
    if len(argv) not in [1, 2]:
        print("Usage: python rushhour.py [gameboardfile]")
        exit(1)

    game_name = argv[1]

    game = Game(game_name)

    while True:
        game.grid.print_grid()
        move = input("Which car do you want to move? ")
        x = move.split()
        if game.move_car(x[0], x[1], x[2]):
            break

