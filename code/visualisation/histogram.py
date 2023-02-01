import matplotlib as plt
import pandas as pd


def make_histogram(algorithm_name):
    """Creates a histogram from a dataframe"""
    # Making dataframe 
    experiment_df = pd.read_csv(f"results/{algorithm_name}/{algorithm_name}_experiment.csv")
    
    # Plot and histogram
    hist = experiment_df.plot.hist(bins=15, column=['moves'])
    fig = hist.get_figure()
    fig.savefig(f'results/{algorithm_name}/exp_graph.png')