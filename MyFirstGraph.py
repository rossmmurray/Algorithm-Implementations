import networkx as nx
import matplotlib.pyplot as plt
import re

G = nx.Graph()

nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

edges_string = '(a,b),(c,b),(b,e),(c,d),(d,e),(e,f),(c,f),(c,g),(g,h)'
edge_list = list(re.sub(r'\W', '', edges_string))
arcs = []
for i in range(0, len(edge_list), 2):
	arcs.append((edge_list[i], edge_list[i + 1]))

G.add_nodes_from(nodes)
G.add_edges_from(arcs)
pos = nx.drawing.nx_agraph.graphviz_layout(G, prog='twopi')

nx.draw_networkx(G, pos, with_labels=True, node_size=1000, font_size=20, edgecolors='black', node_color='pink')
print(list(G.adjacency()))

plt.xlim(0, 400)
plt.ylim(-10, 350)

plt.axis('off')
graph_q1 = plt.gcf()
plt.show()
graph_q1.savefig("graph_q1.png")


