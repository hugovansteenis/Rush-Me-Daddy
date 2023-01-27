from code.classes.grid import Grid

def find_red_car(game):
    for car in game.grid.cars:
        if car.type == 'X':
            red_car = car
    return red_car

# Heuristic function examples
# def heuristic_value1(game, red_car):
#     red_car = game.grid.cars[0]  # Assume the red car is the first car in the list
#     x, y = red_car.x, red_car.y
#     if red_car.orientation == Grid.HORIZONTAL:
#         return min(x, game.grid.width - x - red_car.length)
#     else:
#         return min(y, game.grid.height - y - red_car.length)

# Calculate the number of cars blocking the red car's exit path
def heuristic_value2(game):
    blocked_cars = 0
    for car in game.grid.cars:
        if game.is_blocking(car):
            blocked_cars += 1
    return blocked_cars


def heuristic_value3(game, red_car):
    red_car = game.grid.cars[0]  # Assume the red car is the first car in the list
    exit_x, exit_y = game.grid.exit
    return abs(red_car.x - exit_x) + abs(red_car.y - exit_y)

def heuristic_value4(game):
    available_moves = 0
    for car in game.grid.cars:
        if game.grid.can_move(car, 1) or game.grid.can_move(car, -1):
            available_moves += 1
    return available_moves

def heuristic_value5(game, red_car):
    cars_to_move = 0
    red_car = game.grid.cars[0]
    exit_x, exit_y = game.grid.exit
    if red_car.orientation == Grid.HORIZONTAL:
        cars_to_move = abs(red_car.x - exit_x)
    else:
        cars_to_move = abs(red_car.y - exit_y)
    return cars_to_move



