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

        # Wyciągam vertexy/nody
        # Używająć union (złączenie zbirów)
        self.vertices = {e.start for e in self.edges} | {e.end for e in self.edges}
        # {e.start for e in edges} | {e.end for e in edges}

        # Nadanie kolorów i wag dla wizualizacji
        for i in range(len(edges)):
            edges[i][2] = {'weight': edges[i][2], "color": "black"}

        # Wyświetlam graf
        self.G.add_edges_from(edges)
        nx.draw_networkx(self.G, with_labels=True)
        plt.show()

 
    def dijkstra(self, source, dest):
        if source not in self.vertices:
            raise ValueError
        # Ustawiam początkowe odleglosci od źródła na inf
        dist = {vertex: inf for vertex in self.vertices}
        previous = {vertex: None for vertex in self.vertices}
        # Odlglość source --> source == 0
        dist[source] = 0
        q = self.vertices.copy()
        neighbours = {vertex: set() for vertex in self.vertices}
        for start, end, cost in self.edges:
            # Dodajemy koszty podróży 
            neighbours[start].add((end, cost))
            neighbours[end].add((start, cost))
 
        while q:
            # TODO: uwagan a koljeki prir
            u = min(q, key=lambda vertex: dist[vertex])
            q.remove(u)
            if dist[u] == inf or u == dest:
                # przerwanie kiedy dojdzie do tragetu lub nie nadano dystansu:
                break
            for v, cost in neighbours[u]:
                alt = dist[u] + cost
                # Relaksacja (patrz Cormen) dla każdego z sąąsiadów
                # szukmy alternatywnej krótszej ścieżki
                if alt < dist[v]:                                 
                    dist[v] = alt
                    previous[v] = u
            # Doubly Ended Queue
        s, u = deque(), dest
        # odtworzenie ścieżki
        while previous[u]:
            s.appendleft(u)
            u = previous[u]
        s.appendleft(u)

        # Wizualizacja
        for i in range(len(s)-1):
            self.G[s[i]][s[i+1]]["color"] = "red"
            edges = self.G.edges()
            # weights = self.G.weight()
            colors = [self.G[p][o]['color'] for p,o in edges]
            edge_labels = nx.get_edge_attributes(self.G, "weight")
            nx.draw(self.G, edge_color=colors, with_labels=True)
            plt.show()
        return s
 
if __name__ == "__main__":
    # graph = Graph([["a", "b", 7],  ["a", "c", 9],  ["a", "f", 14], ["b", "c", 10],
    #             ["b", "d", 15], ["c", "d", 11], ["c", "f", 2],  ["d", "e", 6],
    #             ["e", "f", 9]])
    # pp(graph.dijkstra("a", "e"))

    # graph = Graph([
    #                 ["r", "o", 5],
    #                 ["r", "l", 4],
    #                 ["o", "b", 1],
    #                 ["o", "m", 3],
    #                 ["m", "bel", 5],
    #                 ["m", "athen", 4],
    #                 ["athen", "bel", 1],
    #                 ["rome", "b", 2],
    #                 ["rome", "athen", 2],
    #                ])
    
    # pp(graph.dijkstra("r", "bel"))
    # pp(graph.dijkstra("l", "bel"))

    graph = Graph([
        ["a", "e", 5],
        ["a", "b", 10],
        ["b", "d", 6],
        ["b", "c", 4],
        ["c", "f", 14],
        ["f", "a", 10],
        ["f", "e", 12],
        ["e", "b", 7],
        ["e", "c", 6],
    ])

    pp(graph.dijkstra("f", "d"))





















# $ python
# Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from collections import namedtuple
# >>> Edge = namedtuple('Edge', ['start', 'end', 'cost'])
# >>> edges = []
# >>> edges.append(Edge("a", "b", 7))
# >>> edges
# [Edge(start='a', end='b', cost=7)]
# >>> edges.append(Edge("a", "c", 9))
# >>> edges.append(Edge("c", "d", 11))
# >>> edges
# [Edge(start='a', end='b', cost=7), Edge(start='a', end='c', cost=9), Edge(start='c', end='d', cost=11)]
# >>> edges.append(Edge("d", "e", 6)) 
# >>> {e.start for e in edges} | {e.end for e in edges}
# {'d', 'c', 'e', 'a', 'b'}
# >>> edges
# [Edge(start='a', end='b', cost=7), Edge(start='a', end='c', cost=9), Edge(start='c', end='d', cost=11), Edge(start='d', end='e', cost=6)]
# >>>
