"""This program contains all heuristics used for greedy and beam search"""


def find_red_car(game):
    """ Finds the red car within the grid and stores this in a variable. """
    for car in game.grid.cars:
        if car.type == 'X':
            red_car = car
    return red_car

# Calculate the number of cars blocking the red car's exit path
def heuristic_number_blocking(game):
    """ This heuristic calculates the number of cars blocking the red cars path and returns this number in an integer """
    blocked_cars = 0
    for car in game.grid.cars:
        if game.is_blocking(car):
            blocked_cars += 1
    return blocked_cars

def heuristic_blocking_red_car(game):
    """ This heuristic calculates the number of cars blocking the red cars path and puts each car_type in a list.
    Then returns the list """
    blocked_cars = []
    for car in game.grid.cars:
        if game.is_blocking(car):
            blocked_cars.append(car)
    return blocked_cars