import subprocess
import time


def timer(duration, run_time):
        """Creates an experiment file which writes down the results from all experiments for the random algorithm"""
        start = time.time()
        n_runs = 0
        experiment_list = []

        while time.time() - start < duration:
            print(f"run: {n_runs}")
            subprocess.call(["timeout", run_time, "python3", "random"])
            n_runs += 1
            stop = time.time()
            experiment_list.append(n_runs, runnnnntime)

        with open('results/experiment.csv', "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["iteration", "time"])
            for iteration in experiment_list:
                writer.writerow(iteration)