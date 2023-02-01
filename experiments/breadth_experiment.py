import sys, os
sys.path = [os.getcwd()] + sys.path

from code.classes import game
from code.algorithms.breadth_first import breadth_first
from code.visualisation.animate import animate
import time
import shutil
import csv

def breadth_script():

    time_list = []

    #-------------------------------------
    # Board 1 

    print("Board 1 is currently running")
    game1 = game.Game("Rushhour6x6_1.csv")
    start = time.time()
    breadth_first(game1)
    end = time.time()
    duration = end - start
    shutil.copy("results/breadth/output.csv", "results/breadth/output_breadth_board1.csv")
    game1.handle_output("breadth")
    animate("Rushhour6x6_1.csv", "breadth")
    time_list.append(("6x6_1", duration))

    #-------------------------------------
    # Board 2

    print("Board 2 is currently running")
    game2 = game.Game('Rushhour6x6_2.csv')
    start = time.time()
    breadth_first(game2)
    end = time.time()
    duration = end - start
    shutil.copy("results/breadth/output.csv", "results/breadth/output_breadth_board2.csv")
    game2.handle_output("breadth")
    animate("Rushhour6x6_2.csv", "breadth")
    time_list.append(("6x6_2", duration))

    #--------------------------------------
    # Board 3

    print("Board 3 is currently running")
    game3 = game.Game('Rushhour6x6_3.csv')
    start = time.time()
    breadth_first(game3)
    end = time.time()
    duration = end - start
    shutil.copy("results/breadth/output.csv", "results/breadth/output_breadth_board3.csv")
    game3.handle_output("breadth")
    animate('Rushhour6x6_3.csv', 'breadth')
    time_list.append(("6x6_3", duration))

    #--------------------------------------
    # Output Data

    with open("results/breadth/breadth_first_results_123.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["board", "time"])
        for move in time_list:
            writer.writerow(move)