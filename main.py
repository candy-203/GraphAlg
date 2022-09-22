import graphics
import parse
import search


# draws one edge between two nodes on the graph
def draw_edge(node_id_1: int, node_id_2: int, parse_object: parse.Parse):
    x_coord_1 = parse_object.x_coord_list[node_id_1]
    y_coord_1 = parse_object.y_coord_list[node_id_1]
    x_coord_2 = parse_object.x_coord_list[node_id_2]
    y_coord_2 = parse_object.y_coord_list[node_id_2]

    graphics.add_solution_line((x_coord_1, y_coord_1), (x_coord_2, y_coord_2))


# draws a way on the graph using a predecessor list
def draw_way(pre_list: list, parse_object: parse.Parse, end_node_id: int):
    current_node_id = end_node_id

    while pre_list[current_node_id] > -1:  # iterates through predecessor list while end is reached
        draw_edge(pre_list[current_node_id], current_node_id, parse_object)
        current_node_id = pre_list[current_node_id]


if __name__ == '__main__':
    parse_obj = parse.Parse("./geo/xcoords", "./geo/ycoords", "./geo/edges")  # parse the txt-files
    start, end = 1758, 584  # start and end node

    pre, dist = search.dijkstra(parse_obj.graph, start)  # dijkstra search on resulting graph

    graphics.mark(parse_obj.x_coord_list[end], parse_obj.y_coord_list[end])  # mark start and end node
    graphics.mark(parse_obj.x_coord_list[start], parse_obj.y_coord_list[start])
    draw_way(pre, parse_obj, end)  # draws result of searching algorithm
    graphics.show()
