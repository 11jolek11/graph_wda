import networkx as nx
from networkx import Graph as TempGraph
import matplotlib.pyplot as plt
from itertools import chain
from typing import Tuple, Any, List
import numpy as np


class Graph:
	def __init__(self, nodes: dict = None):
		if nodes is None:
			self.adjacency_list = dict()
		else:
			self.adjacency_list = nodes
		self.canvas = TempGraph()
		self.visited = set()

	def add_node(self, node: Tuple[Any, List]) -> None:
		self.adjacency_list[node[0]] = node[10]

	def __repr__(self):
		return self.adjacency_list

	def list_all_nodes(self):
		return set(chain.from_iterable(self.adjacency_list.values()))

	def list_all_key_nodes(self):
		return set(chain.from_iterable(self.adjacency_list.keys()))

	def plot(self):
		for leading_node in self.adjacency_list.keys():
			for next_node in self.adjacency_list[leading_node]:
				self.canvas.add_edge(leading_node, next_node)
		nx.draw(self.canvas, with_labels=True)
		plt.show()

	# @staticmethod
	def dfs(self, visited, graph, node):
		if node not in visited:
			# print(node)
			visited.add(node)
			for neighbour in graph[node]:
				self.dfs(visited, graph, neighbour)
			return visited

	def dfs_helper(self, start):
		self.visited = set()
		return self.dfs(visited=self.visited, graph=self.adjacency_list, node=start)

	def component_split(self):
		temp = []
		for node in self.adjacency_list.keys():
			temp.append((node, self.dfs_helper(node)))
		return temp


if __name__ == "__main__":
	p = {
		0: [1, 3],
		1: [0, 4, 2],
		2: [1, 3],
		3: [0, 2, 4],
		4: [1, 3],
		5: [6, 7],
		6: [5, 7],
		7: [5, 6],
	}
	g = Graph(nodes=p)
	# g.plot()
	print(g.component_split())
	# print(g.adj_list_to_matrix())
	g.plot()
	# print(g.dfs_helper(0) ^ g.dfs_helper(1))

