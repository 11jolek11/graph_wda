class Helper:
	def __init__(self):
		# self.cost = sys.maxsize
		self.cost = 1000000
		self.predecessor = -1


def prim(matrix, s):
	n = len(matrix)
	result = [Helper() for _ in range(n)]
	result[s].cost = 0
	queue = list(range(n))
	while len(queue) != 0:
		u = -1
		for q in queue:
			if result[q].cost != 1000000 and (u == -1 or result[q].cost < result[u].cost):
				u = q
		for j in range(n):
			try:
				queue.index(j)
				if matrix[u][j] == 0:
					continue
			except ValueError:
				continue
			if result[j].cost > matrix[u][j]:
				result[j].cost = matrix[u][j]
				result[j].predecessor = u
		queue.remove(u)
	return result


if __name__ == "__main__":
	macierz = [[0, 6, 3, 4, 1],
[6, 0, 1, 0, 0],
[3, 1, 0, 2, 1],
[4, 0, 2, 0, 3],
[1, 0, 1, 3, 0]]

	wynik = prim(macierz, 1)
	suma = 0
	for i in range(len(macierz)):
		suma += wynik[i].cost
	print("Cost: " + str(suma))


"""
[[0, 6, 3, 4, 1],
[6, 0, 1, 0, 0],
[3, 1, 0, 2, 1],
[4, 0, 2, 0, 3],
[1, 0, 1, 3, 0]]


0, 6, 3, 4, 1
6, 0, 1, 0, 0
3, 1, 0, 2, 1
4, 0, 2, 0, 3
1, 0, 1, 3, 0
"""