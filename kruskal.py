import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


parent, rank = [], []

def make_set(v):
    parent[v] = v
    rank[v] = 0

def find_set(v):
    if v == parent[v]:
        return v
    parent[v] = find_set(parent[v])
    return parent

def union_set(a, b):
    a = find_set(a)
    b = find_set(b)

    if a != b:
        if rank[a] < rank[b]:
            # swap
            temp = a
            a = b
            b = temp
            parent[b] = a
        if rank[a] == rank[b]:
            rank[a]+=1

# FIXME: Change this
class Edge:
    def __init__(self):
        self.u = None
        self.v = None
        self.weight = None
    
    def operator(self, other):
        return self.weight < other.weight

def kruskal(edges: list[Edge], n):
    cost = 0
    results = []
    for i in range(n):
        make_set(i)
    edges.sort(key=lambda x: x.weight)

    for edge in edges:
        if find_set(edge.u) != find_set(edge.v):
            cost += edge.weight
            results.append(edge)
            union_set(edge.u, edge.v)
