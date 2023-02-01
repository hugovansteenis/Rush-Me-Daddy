import sys, os
sys.path = [os.getcwd()] + sys.path

from code.classes import game
from code.algorithms.depth_first import depth_first
from code.visualisation.animate import animate
import time
import shutil
import csv

def depth_script():

    time_list = []

    #-------------------------------------
    # Board 1 

    print("Board 1 is currently running")
    game1 = game.Game("Rushhour6x6_1.csv")
    start = time.time()
    depth_first(game1)
    end = time.time()
    duration = end - start
    shutil.copy("results/depth/output.csv", "results/depth/output_depth_board1.csv")
    game1.handle_output("depth")
    animate("Rushhour6x6_1.csv", "depth")
    time_list.append(("6x6_1", duration))

    #-------------------------------------
    # Board 2

    print("Board 2 is currently running")
    game2 = game.Game('Rushhour6x6_2.csv')
    start = time.time()
    depth_first(game2)
    end = time.time()
    duration = end - start
    shutil.copy("results/depth/output.csv", "results/depth/output_depth_board2.csv")
    game2.handle_output("depth")
    animate("Rushhour6x6_2.csv", "depth")
    time_list.append(("6x6_2", duration))

    #--------------------------------------
    # Board 3

    print("Board 3 is currently running")
    game3 = game.Game('Rushhour6x6_3.csv')
    start = time.time()
    depth_first(game3)
    end = time.time()
    duration = end - start
    shutil.copy("results/depth/output.csv", "results/depth/output_depth_board3.csv")
    game3.handle_output("depth")
    animate('Rushhour6x6_3.csv', "depth")
    time_list.append(("6x6_3", duration))

    #--------------------------------------
    # Output Data

    with open("results/depth/depth_first_results_123.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["board", "time"])
        for move in time_list:
            writer.writerow(move)