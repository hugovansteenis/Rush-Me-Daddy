import subprocess
import time
import csv


def timer(duration, run_time):
        """Creates an experiment file which writes down the number of occurences and moves for the random algorithm"""
        start = time.time()
        n_runs = 0
        experiment_list = []

        while time.time() - start < duration:
            print(f"run: {n_runs}")
            subprocess.call(["timeout", run_time, "python3", "main.py Rushhour6x6_1.csv random"])
            n_runs += 1
            experiment_list.append(n_runs, number_moves)

        with open('results/experiment.csv', "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["iteration", "moves"])
            for iteration in experiment_list:
                writer.writerow(iteration)