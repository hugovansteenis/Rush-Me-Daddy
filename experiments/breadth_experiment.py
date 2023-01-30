import sys, os
sys.path = [os.getcwd()] + sys.path

from code.classes import game
from code.algorithms.breadth_first import breadth_first
from code.visualisation.animate import animate
import time
import shutil
import csv

time_list = []

#-------------------------------------
# Board 3 

print("Board 3 is currently running")
game1 = game.Game("Rushhour6x6_3.csv")
start = time.time()
breadth_first(game1)
end = time.time()
duration = end - start
shutil.copy("results/output.csv", "results/output_breadth_board3.csv")
game1.handle_output("breadth")
animate("Rushhour6x6_3.csv")
time_list.append(("6x6_3", duration))

#-------------------------------------
# Board 6

print("Board 6 is currently running")
game2 = game.Game('Rushhour9x9_6.csv')
start = time.time()
breadth_first(game2)
end = time.time()
duration = end - start
shutil.copy("results/output.csv", "results/output_breadth_board6.csv")
game2.handle_output("breadth")
animate("Rushhour9x9_6.csv")
time_list.append("9x9_6", duration)

#--------------------------------------
# Board 9

print("Board 7 is currently running")
game3 = game.Game('Rushhour12x12_7.csv')
start = time.time()
breadth_first(game3)
end = time.time()
duration = end - start
shutil.copy("results/output.csv", "results/output_breadth_board6.csv")
game3.handle_output("breadth")
animate('Rushhour12x12_7.csv')
time_list.append("12x12_7", duration)

#--------------------------------------
# Output Data

with open("results/breadth_first_results.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["board", "time"])
    for move in time_list:
        writer.writerow(move)