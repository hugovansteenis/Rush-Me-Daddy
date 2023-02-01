from code.classes.grid import Grid


def find_red_car(game):
    """ Finds the red car within the grid and stores this in a variable. """
    for car in game.grid.cars:
        if car.type == 'X':
            red_car = car
    return red_car

# Calculate the number of cars blocking the red car's exit path
def heuristic_value2(game):
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

def heuristic_value3(game, red_car):
    """ This heuristic assumes the red car is the first car in the list and calculates the distance between the red car and the exit. """
    red_car = game.grid.cars[0]  # Assume the red car is the first car in the list
    exit_x, exit_y = game.grid.exit
    return abs(red_car.x - exit_x) + abs(red_car.y - exit_y)

def heuristic_value4(game):
    """ This heuristic goes through all the cars in the grid and moves the cars that can move to an empty space. """
    available_moves = 0
    for car in game.grid.cars:
        if game.grid.can_move(car, 1) or game.grid.can_move(car, -1):
            available_moves += 1
    return available_moves

def heuristic_value5(game, red_car):
    """ This heuristic calculates the number of moves the red car has to make to reach the exit. """
    cars_to_move = 0
    red_car = game.grid.cars[0]
    exit_x, exit_y = game.grid.exit
    if red_car.orientation == Grid.HORIZONTAL:
        cars_to_move = abs(red_car.x - exit_x)
    else:
        cars_to_move = abs(red_car.y - exit_y)
    return cars_to_move