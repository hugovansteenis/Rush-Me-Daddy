from code.classes import game
from code.algorithms.random import random_algorithm
from code.algorithms.depth_first import depth_first
from code.algorithms.breadth_first import breadth_first
from code.algorithms.greedy import greedy_algorithm
from code.visualisation.animate import animate
import subprocess
import time
import csv


def timer(duration, run_time, algorithm):
    start = time.time()
    n_runs = 0
    experiment_list = []

    while time.time() - start < duration:
        print(f"run: {n_runs}")
        subprocess.call(["timeout", run_time, "python3", algorithm])
        n_runs += 1
        experiment_list.append(n_runs, start)

    with open('experiment.csv', "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["iteration", "time"])
        for iteration in experiment_list:
            writer.writerow(iteration)
        

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
        elif argv[2] == "greedy":
            algorithm_name = "Greedy"
            test_game.grid.print_grid()
            greedy_algorithm(test_game)
            test_game.handle_output(algorithm_name)
            if len(argv) > 3 and argv[3] == "visual":
                animate(game_name)
            exit(5)
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


    

