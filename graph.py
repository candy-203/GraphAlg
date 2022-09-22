from collections import defaultdict
from typing import Dict


# Node class
class Node:

    def __init__(self, node_id: int):
        self.NODE_ID = node_id
        # dictionary of outgoing edges (node_id: weight)
        self.out_dict: Dict[int, float] = defaultdict(lambda _: float("inf"))

    def add_edge(self, node_id: int, weight: float):  # adds edge from this to other
        self.out_dict[node_id] = weight

    def get_weight(self, node_id: int) -> float:  # returns weight of edge, inf if not connected
        return self.out_dict[node_id]

    def get_post(self):  # returns immutable list of all outgoing neighbors
        return self.out_dict.keys()


# Graph class
class Graph:

    def __init__(self, node_num: int):  # node_num -> maximum number of nodes
        if node_num < 2:
            raise ValueError("Node num must be at least 2")

        self.NODE_NUM = node_num
        self.NODE_LIST = [Node(i) for i in range(0, self.NODE_NUM)]  # list of all Node objects

    def add_edge(self, node_id_1: int, node_id_2: int, weight: float):  # adds edge from 1 to 2 with weight
        self.__proof_node(node_id_1)
        self.__proof_node(node_id_2)

        node_1 = self.NODE_LIST[node_id_1]
        node_1.add_edge(node_id_2, weight)

    def get_weight(self, node_id_1: int, node_id_2: int) -> float:  # returns weight of edge
        self.__proof_node(node_id_1)
        self.__proof_node(node_id_2)

        node_1 = self.NODE_LIST[node_id_1]
        return node_1.get_weight(node_id_2)

    def get_post(self, node_id: int):  # returns all outgoing neighbors
        self.__proof_node(node_id)

        node = self.NODE_LIST[node_id]
        return node.get_post()

    def __proof_node(self, node_id: int):  # proofs existence of node
        if node_id >= self.NODE_NUM or node_id < 0:
            raise ValueError("Not a valid Node")
