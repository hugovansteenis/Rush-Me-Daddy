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
    # Board 3 

    print("Board 3 is currently running")
    game1 = game.Game("Rushhour6x6_3.csv")
    start = time.time()
    beam_search(game1)
    end = time.time()
    duration = end - start
    shutil.copy("results/beam/output.csv", "results/beam/output_beam_board3.csv")
    game1.handle_output("beam")
    animate("Rushhour6x6_3.csv", "beam")
    time_list.append(("6x6_3", duration))

    #-------------------------------------
    # Board 6

    print("Board 6 is currently running")
    game2 = game.Game('Rushhour9x9_6.csv')
    start = time.time()
    beam_search(game2)
    end = time.time()
    duration = end - start
    shutil.copy("results/beam/output.csv", "results/beam/output_beam_board6.csv")
    game2.handle_output("beam")
    animate("Rushhour9x9_6.csv", "beam")
    time_list.append(("9x9_6", duration))

    #--------------------------------------
    # Board 7

    print("Board 7 is currently running")
    game3 = game.Game('Rushhour12x12_7.csv')
    start = time.time()
    beam_search(game3)
    end = time.time()
    duration = end - start
    shutil.copy("results/beam/output.csv", "results/beam/output_beam_board7.csv")
    game3.handle_output("beam")
    animate('Rushhour12x12_7.csv', 'beam')
    time_list.append(("12x12_7", duration))

    #--------------------------------------
    # Output Data

    with open("results/beam/beam_search_results.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["board", "time"])
        for move in time_list:
            writer.writerow(move)