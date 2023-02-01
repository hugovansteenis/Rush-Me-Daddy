import subprocess
import time
import csv
import re
from code.visualisation.histogram import make_histogram


def timer(duration, run_time, board_name):
    """Creates an experiment file which writes down the number of occurences and moves for the random algorithm"""
    start = time.time()
    n_runs = 0
    experiment_list = []

    while time.time() - start < duration:
        print(f"run: {n_runs}")
        output = subprocess.check_output(["timeout", f"{run_time}", "python3", "main.py", f"{board_name}", "greedy", "silent"])
        output_list = str(output).split("\n")

        # Regular expression to find the number after [Amount of Moves:]
        moves = re.findall(r"(?:\s\d+)", output_list[0])[1]
        moves = moves.strip()

        # Increment runs by 1 and add number of moves to experiment file
        n_runs += 1
        experiment_list.append((n_runs, moves))

    with open('results/greedy/greedy_experiment.csv', "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["iteration", "moves"])
        for iteration in experiment_list:
            writer.writerow(iteration)
    
    make_histogram("greedy")