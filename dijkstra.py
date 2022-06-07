import sys
# https://graphonline.ru/en/


"""
Algorytm Dijkstry przy użyciu macierzy (w materiałach źródłowych nie było
opisu listy z wagami, więc użyłem macierzy)
"""


class Helper(object):
	def __init__(self, v, p, d):
		self.visiteddd = v
		self.predecessor = p
		self.dist = d


def print_out(line, d):
	txt = str(line) + "\t"
	if not d.visiteddd:
		txt += "not visited"
	else:
		if d.predecessor == -1:
			txt += "None"
		# else:
		# 	txt += str(d.predecessor)
		txt += "\t" + str(d.dist)
	print(txt)


def search_for_minimal(matrix):
	minimal = -1
	minimal_dist = 100000
	for i in range(0, len(matrix)):
		if (not matrix[i].visiteddd) and matrix[i].dist < minimal_dist:
			minimal = i
			minimal_dist = matrix[i].dist
	return minimal


def dijkstra(input_matrix, starting_pont):
	temp = []
	for p in range(0, len(input_matrix)):
		temp.append(Helper(False, -1, 100000))
	temp[starting_pont].dist = 0
	u = starting_pont
	while u != -1:
		temp[u].visiteddd = True
		for p in range(0, len(input_matrix)):
			if input_matrix[u][p] > 0 and temp[u].dist + input_matrix[u][p] < temp[p].dist:
				temp[p].dist = temp[u].dist + input_matrix[u][p]
				temp[p].predecessor = u
		u = search_for_minimal(temp)
	return temp


if __name__ == "__main__":
	# tablica = [[0, 6, 3, 4, 1],
	# [6, 0, 1, 0, 0],
	# [3, 1, 0, 2, 1],
	# [4, 0, 2, 0, 3],
	# [1, 0, 1, 3, 0]]

# 	tablica = [[0, 6, 3, 4, 1, 0, ],
# 	[6, 0, 1, 0, 0, 3, ],
# 	[3, 1, 0, 2, 1, 0, ],
# 	[4, 0, 2, 0, 3, 0, ],
# 	[1, 0, 1, 3, 0, 0, ],
# 	[0, 3, 0, 0, 0, 0, ]]

	# http://graphonline.ru/en/?graph=XAGNhhbcLDgFUMcc
	# tablica = [[0, 6, 3, 4, 1, 0, 0, 0,],
	# [6, 0, 1, 0, 0, 3, 0, 0,],
	# [3, 1, 0, 2, 1, 0, 0, 0,],
	# [4, 0, 2, 0, 3, 0, 0, 0,],
	# [1, 0, 1, 3, 0, 0, 0, 0,],
	# [0, 3, 0, 0, 0, 0, 0, 0,],
	# [0, 0, 0, 0, 0, 0, 0, 1,],
	# [0, 0, 0, 0, 0, 0, 1, 0,]]

	# http://graphonline.ru/en/?graph=XAGNhhbcLDgFUMcc
	tablica = [[0, 12, 12, 12, 1, 0, 0, 0,],
[12, 0, 1, 0, 0, 3, 0, 0,],
[12, 1, 0, 2, 12, 0, 0, 0,],
[12, 0, 2, 0, 3, 0, 0, 0,],
[1, 0, 12, 3, 0, 0, 0, 0,],
[0, 3, 0, 0, 0, 0, 0, 0,],
[0, 0, 0, 0, 0, 0, 0, 1,],
[0, 0, 0, 0, 0, 0, 1, 0,]]

	dij = dijkstra(tablica, 0)
	print("Node Direction Dist")
	for i in range(0, len(tablica)):
		# print(dij[i])
		print_out(i, dij[i])

"""

Numeracja wierzchołków zaczyna się od zera (patrz: graf_diksta.png)
http://graphonline.ru/en/?graph=MMqnxjyMrgDKeDDq

0 6 3 4 1
6 0 1 0 0
3 1 0 2 1
4 0 2 0 3
1 0 1 3 0
"""

"""
[[0, 6, 3, 4, 1, 0,],
[6, 0, 1, 0, 0, 3,],
[3, 1, 0, 2, 1, 0,],
[4, 0, 2, 0, 3, 0,],
[1, 0, 1, 3, 0, 0,],
[0, 3, 0, 0, 0, 0,]]

"""