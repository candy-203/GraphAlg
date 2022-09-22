import csv

import numpy as np

import graph
import graphics


#  help-function maps map_foo on arr
def list_map(arr: list, map_foo):
    for i in range(len(arr)):
        arr[i] = map_foo(arr[i])

 
#  help-function converts csv file to list, and maps map_foo on every row
def parse_file(filename: str, map_foo) -> list:
    res = []
    with open(filename) as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            list_map(row, map_foo)
            res.append(row)
    return res


#  Parses the graph files, and saves results
class Parse:

    def __init__(self, x_coords: str, y_coords: str, edges: str):
        self.x_coord_list = parse_file(x_coords, lambda x: float(x))
        self.y_coord_list = parse_file(y_coords, lambda x: float(x))

        list_map(self.x_coord_list, lambda sublist: sublist[0])  # removes redundant list brackets
        list_map(self.y_coord_list, lambda sublist: sublist[0])

        self.edge_list = parse_file(edges, lambda x: int(x))

        if len(self.x_coord_list) != len(self.y_coord_list):  # control
            raise ValueError("Not enough coordinates")

        self.graph = graph.Graph(len(self.x_coord_list) + 1)  # creates result graph
        self.edge_iter()

    def edge_iter(self):  # iterates through the edges and saves them to the graph
        for edge in self.edge_list:
            start = edge[0]
            end = edge[1]

            start_x = self.x_coord_list[start]  # x_coords
            end_x = self.x_coord_list[end]

            start_y = self.y_coord_list[start]  # y_coords
            end_y = self.y_coord_list[end]

            dx = start_x - end_x
            dy = start_y - end_y
            dist = np.linalg.norm((dx, dy))  # calculates euclidian distance between nodes
            self.graph.add_edge(start, end, dist)
            self.graph.add_edge(end, start, dist)  # adds edge both ways

            graphics.add_street_line((start_x, start_y), (end_x, end_y))  # draws the edge
