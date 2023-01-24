from .car import Car
from .grid import Grid
from matplotlib.patches import Rectangle
from matplotlib import animation
from colorama import Style
from collections import defaultdict
from code.visualisation.colors import COLORS2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import os
import csv

class Game():
    """Holds all elements of a Grid."""
    
    def __init__(self, game):
        """(insert description)"""
        self.game = game
        self.grid = 0 
        self.load_input(f"data/{game}")
        self.history = []
        self.rectangles = {}
        self.counter = 0

    def load_input(self, filename):
        """Checks the grid size in the file name.
        Also reads the input data given and creates all the car objects."""
        if self.game[8].isnumeric():
            number = self.game[8]
            if self.game[9].isnumeric():
                number += self.game[9]
            self.grid = Grid(number)
            number = int(number)
        
        # Reads the inputdata and creates all the necessary cars objects
        with open(filename) as f:
            csv_reader = csv.reader(f, delimiter=',')
            next(csv_reader)
            for row in csv_reader:
                car = Car(row[0], row[1], row[2], row[3], row[4])
                self.grid.add_car(car)

    def move_car(self, car_type, movement):
        """Uses the move_car function made in the grid class to move.
        Also checks if the red car is at the destination it is meant to be to win.
        If so it prints the moves of all the cars into the output.csv file."""
        self.counter += 1
        if self.grid.move_car(car_type, movement):
            # Stores the move in history for output
            self.history.append((car_type, movement))
            # Completes the program if the red car is in the right spot
            if self.red_unblocked():
                bold = '\033[1m'
                print(f"{bold}You Win{Style.RESET_ALL}")
                self.grid.print_grid()
                print(f"{bold}Amount of attempts: {self.counter}{Style.RESET_ALL}")
                print(f"{bold}Amount of moves: {len(self.history)}{Style.RESET_ALL}")
                self.output_to_csv("output.csv")
                return True
            return False

    def red_unblocked(self):
        """Checks if the red car is unblocked and if it can move to the end of the board/grid
        also checks if the red car is at the end of the board/grid."""
        exit_car = None 
        for car in self.grid.cars:
            if car.type == 'X':
                exit_car = car 
                break
        if exit_car.orientation == "H":
            # Check if there is any car blocking the red car from moving to the right
            for i in range(exit_car.col + exit_car.length, self.grid.width):
                if self.grid.board[exit_car.row][i] != '_':
                    return False
        else:
            # Check if there is any car blocking the red car from moving down
            for i in range(exit_car.row + exit_car.length, self.grid.width):
                if self.grid.board[i][exit_car.col] != '_':
                    return False
        # Check if the red car is at the end of the board
        if self.grid.board[exit_car.row][self.grid.width - 1] == 'X':
            return True
        return False


    # def red_unblocked(self):
    #     """Checks if the red car is unblocked and if it can move to the end of the board/grid
    #     also checks if the red car is at the end of the board/grid."""
    #     exit_car = None 
    #     for car in self.grid.cars:
    #         if car.type == 'X':
    #             exit_car = car 
    #             break
    #     # Checks if the red car is at the end of the board
    #     if self.grid.board[exit_car.row][self.grid.width - 1] == 'X':
    #         return True
    #     return False

    def output_to_csv(self, filename):
        """Creates an output file which writes down all the cars that made moves and which moves they made."""
        with open(filename, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["car", "move"])
            # Retrieves all the moves in history and writes these into the outputfile
            for move in self.history:
                writer.writerow(move)
    
    def update_cars(self):
        """Creates all the car-rectangles for the animation."""
        for car in self.grid.cars:
            # Create the rectangles depening on the different car aspects. https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html
            if car.orientation == 'H' and car.type != 'X':
                self.rectangles[car] = (Rectangle((car.col, car.row), car.length, 1, facecolor = car.color, edgecolor = 'black', label = car.type))
            elif car.type == 'X':
                self.rectangles[car] =(Rectangle((car.col, car.row), 2, 1, facecolor = car.color, edgecolor = 'black', label = car.type))
            elif car.orientation == 'V' and car.length ==  3:
                self.rectangles[car] =(Rectangle((car.col, car.row), 1, 3, facecolor = car.color, edgecolor = 'black', label = car.type))
            else:
                self.rectangles[car] =(Rectangle((car.col, car.row), 1, car.length, facecolor = car.color, edgecolor = 'black', label = car.type))

    def create_animationboard(self):
        """Creates the board and places all the rectangles."""
        # Creates a subplot (https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html)
        fig, ax = plt.subplots()
        ax.set_xlim(0, self.grid.width)
        ax.set_ylim(self.grid.width, 0)
        ax.set_yticklabels([])
        ax.set_xticklabels([])

        # Places all the rectangles on the board. (https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html)
        for rec in self.rectangles.values():
            ax.add_patch(rec)

        # Adds a legend to the graph and makes the graph into a square.
        # ax.legend(loc='upper center', bbox_to_anchor=(0.5, 0),
        #   fancybox=True, shadow=True, ncol=5)
        ax.set_aspect('equal', adjustable='box')

        return plt

    def handle_output(self, algorithm_name):
        """Makes a graph based on the scanned outputfile."""  
        reader = csv.reader(open('output.csv'))
        counter = defaultdict(int)

        # Goes through the entire file and counts all car_types.
        for i, row in enumerate(reader):
            if i == 0:
                continue
        
            column_value = row[0]
            counter[column_value] += 1

        # Puts all the car_types and their amount of moves in a list and sorts the list on alphabetical order.
        list_counter = [(column_value, cnt) for column_value, cnt in counter.items()]
        list_counter.sort(key = lambda x: x[0])

        # Defines the empty lists for later use.
        list_cars = []
        list_data = []
        list_colors = []

        # Fills the lists
        for data in list_counter:
            list_cars.append(data[0])
            list_data.append(data[1])

        # Gets the right color of the car_type.
        for char in list_cars:
            for key in COLORS2:
                if char == key:
                    list_colors.append(COLORS2[key])
                    
        # Plots the graph.
        fig, ax = plt.subplots()
        rect = ax.bar(list_cars, list_data, color = list_colors)
        ax.bar_label(rect)
        ax.set_xlabel("Cars")
        ax.set_ylabel("Amount of moves")
        results = pd.read_csv('output.csv')
        ax.set_title(f"{algorithm_name} Algorithm | Total Moves: {len(results)}", fontsize=14, fontweight='bold') 

        # Calculates the spacing needed between x-axis ticks to not overlap. (https://stackoverflow.com/questions/44863375/how-to-change-spacing-between-ticks#:~:text=The%20spacing%20between%20ticklabels%20is,to%20make%20the%20axes%20larger.)
        tl = plt.gca().get_xticklabels() 
        maxsize = max([t.get_window_extent().width for t in tl])
        m = 0.5
        s = maxsize/plt.gcf().dpi*200*m
        margin = m/plt.gcf().get_size_inches()[0]
        plt.gcf().subplots_adjust(left=margin, right=1.-margin)
        plt.gcf().set_size_inches(s, plt.gcf().get_size_inches()[1])

        # Saves the graph
        plt.savefig('graph.png')

        
    def __hash__(self) -> int:
        return hash(str(self.grid))

        




