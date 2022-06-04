import sys

class dane:
	def __init__(self):
		self.koszt = sys.maxsize
		self.poprzednik = -1

def AlgorytmPrima(macierz, s):
	n = len(macierz)
	wynik = [dane() for x in range(n)]
	wynik[s].koszt = 0
	kolejka = list(range(n))
	while len(kolejka) != 0:
		u = -1
		for q in kolejka:
			if wynik[q].koszt != sys.maxsize and (u == -1 or wynik[q].koszt < wynik[u].koszt):
				u = q
		for j in range(n):
			try:
				kolejka.index(j)
				if macierz[u][j] == 0:
					continue
			except ValueError:
				continue
			if wynik[j].koszt > macierz[u][j]:
				wynik[j].koszt = macierz[u][j]
				wynik[j].poprzednik = u
		kolejka.remove(u)
		print(str(u))
	return wynik


if __name__ == "__main__":
	macierz = [[0, 6, 3, 4, 1],
[6, 0, 1, 0, 0],
[3, 1, 0, 2, 1],
[4, 0, 2, 0, 3],
[1, 0, 1, 3, 0]]

	wynik = AlgorytmPrima(macierz, 1)
	suma = 0
	print("ID\tPoprzednik")
	for i in range(len(macierz)):
		print(str(i) + "\t" + str(wynik[i].poprzednik))
		suma += wynik[i].koszt
	print("ĹÄczny koszt wynosi: " + str(suma))


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