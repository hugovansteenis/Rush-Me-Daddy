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
    # Board 3 

    print("Board 3 is currently running")
    game1 = game.Game("Rushhour6x6_3.csv")
    start = time.time()
    depth_first(game1)
    end = time.time()
    duration = end - start
    shutil.copy("results/depth/output.csv", "results/depth/output_depth_board3.csv")
    game1.handle_output("depth")
    animate("Rushhour6x6_3.csv", "depth")
    time_list.append(("6x6_3", duration))

    #-------------------------------------
    # Board 6

    print("Board 6 is currently running")
    game2 = game.Game('Rushhour9x9_6.csv')
    start = time.time()
    depth_first(game2)
    end = time.time()
    duration = end - start
    shutil.copy("results/depth/output.csv", "results/depth/output_depth_board6.csv")
    game2.handle_output("depth")
    animate("Rushhour9x9_6.csv", "depth")
    time_list.append("9x9_6", duration)

    #--------------------------------------
    # Board 7

    print("Board 7 is currently running")
    game3 = game.Game('Rushhour12x12_7.csv')
    start = time.time()
    depth_first(game3)
    end = time.time()
    duration = end - start
    shutil.copy("results/depth/output.csv", "results/depth/output_depth_board7.csv")
    game3.handle_output("depth")
    animate('Rushhour12x12_7.csv', "depth")
    time_list.append("12x12_7", duration)

    #--------------------------------------
    # Output Data

    with open("results/depth/depth_first_results.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["board", "time"])
        for move in time_list:
            writer.writerow(move)