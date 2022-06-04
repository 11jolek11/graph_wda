import numpy as np
import numpy.ma as ma
import networkx as nx
import matplotlib.pyplot as plt


theta = np.asarray([[0, 6, 3, 4, 1],
                    [6, 0, 1, 0, 0],
                    [3, 1, 0, 2, 1],
                    [4, 0, 2, 0, 3],
                    [1, 0, 1, 3, 0]])

# theta = np.asarray([[1, 0],
#                     [0, 0]])
G = nx.Graph()
counter = np.count_nonzero(theta)
# print(counter)
t = []
for _ in range(counter):
    i = list(np.unravel_index(np.where(theta != 0, theta, theta.max() + 1).argmin(), theta.shape))
    # print((i, theta[i[0]][i[1]]))
    t.append([i, theta[i[0]][i[1]]])
    theta[i[0]][i[1]] = 0
t = np.asarray(t)
# print(t)
# print("###############")
# print(t[:, 0])
for edge in t[:, 0]:
    edge = tuple(edge)
    G.add_edge(*edge)
    if len(nx.cycle_basis(G)) != 0:
        G.remove_edge(*edge)
nx.draw(G, with_labels=True)
plt.show()
print(G.number_of_nodes())
