import sys, os
sys.path = [os.getcwd()] + sys.path

from code.classes import game
from code.algorithms.beam_search import beam_search
from code.visualisation.animate import animate
import time
import shutil
import csv

def beam_script():

    time_list = []

    #-------------------------------------
    # Board 1 

    print("Board 1 is currently running")
    game1 = game.Game("Rushhour6x6_3.csv")
    start = time.time()
    beam_search(game1)
    end = time.time()
    duration = end - start
    shutil.copy("results/beam/output.csv", "results/beam/output_beam_board1.csv")
    game1.handle_output("beam")
    animate("Rushhour6x6_1.csv", "beam")
    time_list.append(("6x6_1", duration))

    #-------------------------------------
    # Board 2

    print("Board 2 is currently running")
    game2 = game.Game('Rushhour6x6_2.csv')
    start = time.time()
    beam_search(game2)
    end = time.time()
    duration = end - start
    shutil.copy("results/beam/output.csv", "results/beam/output_beam_board2.csv")
    game2.handle_output("beam")
    animate("Rushhour6x6_2.csv", "beam")
    time_list.append(("6x6_2", duration))

    #--------------------------------------
    # Board 3

    print("Board 3 is currently running")
    game3 = game.Game('Rushhour6x6_3.csv')
    start = time.time()
    beam_search(game3)
    end = time.time()
    duration = end - start
    shutil.copy("results/beam/output.csv", "results/beam/output_beam_board3.csv")
    game3.handle_output("beam")
    animate('Rushhour6x6_3.csv', 'beam')
    time_list.append(("6x6_3", duration))

    #--------------------------------------
    # Output Data

    with open("results/beam/beam_search_results_123.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["board", "time"])
        for move in time_list:
            writer.writerow(move)