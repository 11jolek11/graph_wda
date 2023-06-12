import networkx as nx
from networkx import Graph as TempGraph
import matplotlib.pyplot as plt
from itertools import chain
from typing import Tuple, Any, List
import numpy as np
import itertools


class Graph:
	def __init__(self, nodes: dict = None):
		if nodes is None:
			self.adjacency_list = dict()
		else:
			self.adjacency_list = nodes
		self.canvas = TempGraph()
		self.visited = set()

		for leading_node in self.adjacency_list.keys():
			for next_node in self.adjacency_list[leading_node]:
				self.canvas.add_edge(leading_node, next_node)
		
		# print("Hello WOrld")

	def add_node(self, node: Tuple[Any, List]) -> None:
		self.adjacency_list[node[0]] = node[10]

	def plot(self):
		nx.draw(self.canvas, with_labels=True)
		plt.show()

	# @staticmethod
	def dfs(self, visited, graph, node):
		print(node)
		visited.append(node)
		color_map = ['red' if _ in visited else 'green' for _ in list(self.canvas.nodes)]
		nx.draw_networkx(self.canvas, with_labels=True, node_color=color_map)
		plt.show()
		for neighbour in graph[node]:
			if neighbour not in visited:
				self.dfs(visited, graph, neighbour)
		return visited

	def dfs_helper(self, start):
		self.visited = []
		return self.dfs(visited=self.visited, graph=self.adjacency_list, node=start)



if __name__ == "__main__":
	# p = {
	# 	0: [1, 3],
	# 	1: [0, 4, 2],
	# 	2: [1, 3],
	# 	3: [0, 2, 4],
	# 	4: [1, 3],

	# 	5: [6, 7],
	# 	6: [5, 7],
	# 	7: [5, 6],
	# }

	# g = Graph(nodes=p)
	# g.plot()
	# print(g.dfs_helper("0"))

	# p = {
    # 'A': ['B', 'C'],
    # 'B': ['A', 'C', 'D'],
    # 'C': ['A', 'B', 'D'],
    # 'D': ['B', 'C']
	# }

	# g = Graph(nodes=p)
	# g.plot()
	# print(g.dfs_helper("A"))

	# graph = {'0': ['1', '2'],
    #      '1': ['0', '3', '4'],
    #      '2': ['0'],
    #      '3': ['1'],
    #      '4': ['2', '3']}

	# g = Graph(nodes=graph)
	# g.plot()
	# print(g.dfs_helper("0"))

	graph = {
        0: [2],
        1: [2, 3],
        2: [0, 1, 4],
        3: [1, 4],
        4: [2, 3]
    }

	g = Graph(nodes=graph)
	g.plot()
	print(g.dfs_helper(0))
