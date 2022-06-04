from collections import defaultdict
from typing import Type
import networkx as nx
from networkx import Graph as TempGraph
import matplotlib.pyplot as plt

# FIXME: all
class Weight:

    def __init__(self, node_id: int, weight: int):
        self.id = node_id
        self.weight = weight

    def __repr__(self):
        return str(self.id)



class Graph:

    def __init__(self, node_count: int):
        # Store the adjacency list as a dictionary
        # The default dictionary would create an empty list as a default (value)
        # for the nonexistent keys.
        self.adjacency_list = defaultdict(list)
        # self.adjacency_list = dict()
        self.node_count = node_count
        self.canvas = TempGraph()

    def add_node(self, src: int, node_dist: Weight(Type[int], Type[int])):
        self.adjacency_list[src].append(node_dist)

    def plot(self):
        for leading_node in self.adjacency_list.keys():
            for next_node in self.adjacency_list[leading_node]:
                self.canvas.add_edge(leading_node, next_node)
        nx.draw(self.canvas, with_labels=True)
        plt.show()

    def dijkstras(self, source: int):

        # Initialize the distance of all the nodes from the source node to infinity
        distance = [1000000000] * self.node_count
        # Distance of source node to itself is 0
        distance[source] = 0

        # Create a dictionary of { node, distance_from_source }
        dict_node_length = {source: 0}

        while dict_node_length:

            # Get the key for the smallest value in the dictionary
            # i.e Get the node with the shortest distance from the source
            current_source_node = min(dict_node_length, key=lambda k: dict_node_length[k])
            del dict_node_length[current_source_node]

            for node_dist in self.adjacency_list[current_source_node]:
                adjnode = node_dist.id
                length_to_adjnode = node_dist.weight

                # Edge relaxation
                if distance[adjnode] > distance[current_source_node] + length_to_adjnode :
                    distance[adjnode] = distance[current_source_node] + length_to_adjnode
                    dict_node_length[adjnode] = distance[adjnode]

        for i in range(self.node_count):
            # print(distance)
            print("("+str(source)+") -> (" + str(i) + ") ||| " + str(distance[i]))


if __name__ == "__main__":

    g = Graph(6)

    # Node 0: <1,5> <2,1> <3,4>
    g.add_node(0, Weight(1, 5))
    g.add_node(0, Weight(2, 1))
    g.add_node(0, Weight(3, 4))

    # Node 1: <0,5> <2,3> <4,8>
    g.add_node(1, Weight(0, 5))
    g.add_node(1, Weight(2, 3))
    g.add_node(1, Weight(4, 8))

    # Node 2: <0,1> <1,3> <3,2> <4,1>
    g.add_node(2, Weight(0, 1))
    g.add_node(2, Weight(1, 3))
    g.add_node(2, Weight(3, 2))
    g.add_node(2, Weight(4, 1))

    # Node 3: <0,4> <2,2> <4,2> <5,1>
    g.add_node(3, Weight(0, 4))
    g.add_node(3, Weight(2, 2))
    g.add_node(3, Weight(4, 2))
    g.add_node(3, Weight(5, 1))

    # Node 4: <1,8> <2,1> <3,2> <5,3>
    g.add_node(4, Weight(1, 8))
    g.add_node(4, Weight(2, 1))
    g.add_node(4, Weight(3, 2))
    g.add_node(4, Weight(5, 3))

    # Node 5: <3,1> <4,3>
    g.add_node(5, Weight(3, 1))
    g.add_node(5, Weight(4, 3))


    g.dijkstras(0)
    print("\n")
    g.dijkstras(5)
    g.plot()
