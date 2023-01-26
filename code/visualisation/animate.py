from code.classes.game import Game
from matplotlib.patches import Rectangle
from matplotlib.animation import FuncAnimation
from matplotlib import animation
import matplotlib.pyplot as plt


def animate(file_name):

    # ------------------------------------------------------
    # Retrieving all the variables for the animation.

    animation_test = Game(file_name)
    rectangles = animation_test.update_cars()
    x_cords = animation_test.x_coordinates()
    y_cords = animation_test.y_coordinates()
    x_move_list = animation_test.x_moves()
    y_move_list = animation_test.y_moves()
    cars_moved_list = animation_test.cars_moved()
    plt, fig, ax = animation_test.create_animationboard()

    # -----------------------------------------
    # Set up the animation.

    def init():
        for rec in rectangles.values():
            ax.add_patch(rec)
        
        for rec in rectangles.values():
            return rec

    def animate(i):
        for rec in rectangles:
            if cars_moved_list[i] == rec:
                rectangles[rec].set_xy([x_move_list[i], y_move_list[i]])
        return rec

    animated_board = FuncAnimation(fig, animate, frames = len(x_move_list), interval = 1000,
                                    init_func = init, repeat = True, repeat_delay = 5000)
    writergif = animation.PillowWriter(fps = 1)
    animated_board.save('animation.gif', writer = writergif)