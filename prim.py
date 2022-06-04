import sys

import numpy as np

def adj_list_to_matrix(adj_list):
    n = len(adj_list)
    adj_matrix = np.nan * np.ones((n,n))
    np.fill_diagonal(adj_matrix,0)

    for i in range(n):
        for j, w in adj_list[i]:
            adj_matrix[i,j] = w
    return adj_matrix

class dane:
    def __init__(self):
        self.koszt = sys.maxsize
        self.poprzednik = -1

def AlgorytmPrima(macierz, s):
  n = len(macierz)
  wynik = [dane() for x in range(n)];
  wynik[s].koszt = 0
  kolejka = list(range(n))
  while (len(kolejka) != 0):
    u = -1
    for q in kolejka:
      if (wynik[q].koszt != sys.maxsize and
        (u == -1 or wynik[q].koszt < wynik[u].koszt)):
        u = q;
    for j in range(n):
      try:
        kolejka.index(j)
        if (macierz[u][j] == 0):
          continue
      except ValueError:
        continue
      if (wynik[j].koszt > macierz[u][j]):
        wynik[j].koszt = macierz[u][j]
        wynik[j].poprzednik = u
    kolejka.remove(u)
    print(str(u))
  return wynik

if __name__ == "__main__":
	n = int(input("Ile wierzchołków ma graf?\n n = "))
	s = int(input("Od którego wierzchołka zacząć?\n s = "))
	print("Podaj input_matrix:")
	macierz = [[int(x) for x in input().split()] for y in range(n)]
	wynik = AlgorytmPrima(macierz, s)
	suma = 0
	print("ID\tPoprzednik")
	for i in range(n):
	  print(str(i) + "\t" + str(wynik[i].poprzednik))
	  suma += wynik[i].koszt
	print("Łączny koszt wynosi: " + str(suma))