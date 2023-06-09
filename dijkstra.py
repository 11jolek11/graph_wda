from collections import namedtuple, deque
from pprint import pprint as pp
import matplotlib.pyplot as plt
import networkx as nx
 
 
inf = float('inf')
Edge = namedtuple('Edge', ['start', 'end', 'cost'])

class Graph():
    def __init__(self, edges):
        self.G = nx.Graph()
        self.edges = [Edge(*edge) for edge in edges]
        # print(dir(self.edges[0]))
        self.vertices = {e.start for e in self.edges} | {e.end for e in self.edges}

        for i in range(len(edges)):
            edges[i][2] = {'weight': edges[i][2], "color": "black"}

        self.G.add_edges_from(edges)
        nx.draw_networkx(self.G, with_labels=True)
        plt.show()

 
    def dijkstra(self, source, dest):
        if source not in self.vertices:
            raise ValueError
        dist = {vertex: inf for vertex in self.vertices}
        previous = {vertex: None for vertex in self.vertices}
        dist[source] = 0
        q = self.vertices.copy()
        neighbours = {vertex: set() for vertex in self.vertices}
        for start, end, cost in self.edges:
            neighbours[start].add((end, cost))
            neighbours[end].add((start, cost))

        #pp(neighbours)
 
        while q:
            # pp(q)
            u = min(q, key=lambda vertex: dist[vertex])
            q.remove(u)
            if dist[u] == inf or u == dest:
                break
            for v, cost in neighbours[u]:
                alt = dist[u] + cost
                # Relaksacja (patrz Cormen)
                if alt < dist[v]:                                 
                    dist[v] = alt
                    previous[v] = u
        #pp(previous)
        s, u = deque(), dest
        while previous[u]:
            s.appendleft(u)
            u = previous[u]
        s.appendleft(u)
        for i in range(len(s)-1):
            self.G[s[i]][s[i+1]]["color"] = "red"
            edges = self.G.edges()
            colors = [self.G[p][o]['color'] for p,o in edges]
            nx.draw(self.G, edge_color=colors, with_labels=True)
            plt.show()
        return s
 
 
graph = Graph([["a", "b", 7],  ["a", "c", 9],  ["a", "f", 14], ["b", "c", 10],
               ["b", "d", 15], ["c", "d", 11], ["c", "f", 2],  ["d", "e", 6],
               ["e", "f", 9]])
pp(graph.dijkstra("a", "e"))
