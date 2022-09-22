from typing import Tuple

from matplotlib import pyplot as plt


# draws line in from x_coord to y_coord in color
def add_line(x_coord: Tuple[float, float], y_coord: Tuple[float, float], color='k'):  # default color black
    x_val = [x_coord[0], y_coord[0]]
    y_val = [x_coord[1], y_coord[1]]
    plt.plot(x_val, y_val, color)


# draws black line
def add_street_line(x_coord: Tuple[float, float], y_coord: Tuple[float, float]):
    add_line(x_coord, y_coord)


# draws red line
def add_solution_line(x_coord: Tuple[float, float], y_coord: Tuple[float, float]):
    add_line(x_coord, y_coord, color='r')


# marks a point on the screen
def mark(x_coord: float, y_cord: float):
    plt.scatter(x_coord, y_cord, s=100)


# shows all changes
def show():
    plt.show()
