import networkx as nx
import numpy as np
import csv
# from math import inf


G = nx.DiGraph()

nodes = ['a', 'b', 'c', 'd']
arcs = [('a', 'b', 1), ('a', 'd', 10), ('b', 'a', 13), ('b', 'c', 2), ('c', 'b', 12), ('c', 'd', 3), ('d', 'a', 4), ('d', 'c', 11)]

G.add_nodes_from(nodes)
G.add_weighted_edges_from(arcs)

adj = np.array(nx.to_numpy_matrix(G), dtype=float)

adj[0][2] = np.inf
adj[1][2] = np.inf
adj[2][0] = np
np.set_printoptions(infstr='∞', precision=0)

with open('adj1.csv', 'w') as f:
	csv.writer(f).writerows(adj)
	print('', file=f)


print(adj)
