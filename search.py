from typing import Tuple

import graph


# Dijkstra-Algorithm
def dijkstra(gr: graph.Graph, start_id: int) -> Tuple[list, list]:  # returns predecessor and distance for every node
    queue = [i for i in range(gr.NODE_NUM)]  # all nodes
    dist = [float("inf") for _ in range(gr.NODE_NUM)]  # distance array
    pre = [-1 for _ in range(gr.NODE_NUM)]  # predecessor array
    dist[start_id] = 0.0  # distance of origin
 
    while queue:  # while queue not empty
        queue.sort(key=lambda node_id: dist[node_id])
        min_node = queue.pop(0)  # pops node with minimum distance

        neighbors = gr.get_post(min_node)  # outgoing neighbors of min_node
        for neigh in neighbors:
            weight = gr.get_weight(min_node, neigh)
            new_dist = dist[min_node] + weight  # new distance
            if dist[neigh] > new_dist:  # checks new distance
                dist[neigh] = new_dist
                pre[neigh] = min_node  # set predecessor
    return pre, dist
