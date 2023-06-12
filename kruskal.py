import networkx as nx
import matplotlib.pyplot as plt


class Graph:
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.G = nx.Graph()

 
    # Zbieram krawędzie
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
        self.G.add_edge(u, v, weight=w, color="black")
 
    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

    def KruskalMST(self): 
        # krawędzie wybrane do MST
        result = []
        # Sort po wagach krawędzi
        self.graph = sorted(self.graph,
                            key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.V):
            # MakeSet (patrz Cormen) dla każdego noda
            parent.append(node)
            rank.append(0)

        # Wskaźnik do przechodzenia po posortowanych krawędziach
        i = 0
        # Wskaźnik do przechodzenia po tablicy z wybranymi krawędziami
        e = 0
        # Przejścia po wszystkich krawędziach
        # indeks V-1 ponieważ indeksujemy od 0
        while e < self.V - 1:

            # Pick the smallest edge and increment
            # the index for next iteration
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # Detekcja cykli
            if x != y:
                e = e + 1
                # Dodawanie nie tworzących cykli w następnej decyzji krawędzi
                result.append([u, v, w])
                self.G[u][v]['color'] = "red"
                print("%d -- %d" % (u, v))
                self.union(parent, rank, x, y)
            # Kiedy krawędź tworzy cykl to ją odżucamy
            colors = [self.G[u][v]['color'] for u,v in self.G.edges()]
            nx.draw_networkx(self.G, with_labels=True, edge_color=colors)
            plt.show()

        cost = 0
        print("MST")
        for u, v, weight in result:
            cost += weight
            print(f"{u} -- {v} == {weight}")
        print("Total cost: ", cost)


if __name__ == '__main__':
    # g = Graph(4)
    # g.addEdge(0, 1, 10)
    # g.addEdge(0, 2, 6)
    # g.addEdge(0, 3, 5)
    # g.addEdge(1, 3, 15)
    # g.addEdge(2, 3, 4)

    # g = Graph(4)
    # g.addEdge(0, 1, 1) 
    # g.addEdge(0, 2, 3)
    # g.addEdge(0, 3, 4)
    # g.addEdge(1, 2, 2)
    # g.addEdge(2, 3, 5)

    # g.KruskalMST()

    g = Graph(8)

    g.addEdge(0, 1, 6)
    g.addEdge(0, 2, 3)
    g.addEdge(1, 2, 2)
    g.addEdge(1, 3, 4)
    g.addEdge(2, 3, 8)
    g.addEdge(2, 4, 1)
    g.addEdge(3, 4, 4)
    g.addEdge(3, 6, 9)
    g.addEdge(3, 7, 2)
    g.addEdge(4, 5, 5)
    g.addEdge(4, 7, 3)
    g.addEdge(5, 6, 3)
    g.addEdge(5, 7, 1)
    g.addEdge(6, 7, 4)


    g.KruskalMST()
