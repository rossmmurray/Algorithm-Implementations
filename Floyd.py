import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import write_dot, graphviz_layout, to_agraph


G = nx.DiGraph()


nodes = ['a', 'b', 'c', 'd']
arcs = [('a', 'b', 1), ('a', 'd', 10), ('b', 'a', 13), ('b', 'c', 2), ('c', 'b', 12), ('c', 'd', 3), ('d', 'a', 4), ('d', 'c', 11)]

G.add_nodes_from(nodes)
G.add_weighted_edges_from(arcs)

pos = graphviz_layout(G, prog='neato',)
nx.draw_networkx(G, pos, with_labels=True, node_size=1000, font_size=20, arrows=True, edgecolors='black', node_color='pink', splines='curved')

# edge_labels = nx.get_edge_attributes(G, 'weight')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=20, rotate=False)
G.graph = {'arrowsize': '0.6', 'splines': 'curved'}

A = to_agraph(G)
A.layout('fdp')
A.draw('multi.png', args='-Gdecorate=False')
# ‘neato’|’dot’|’twopi’|’circo’|’fdp’|’nop’]


adj = nx.to_numpy_matrix(G)
adj2 = nx.adjacency_matrix(G)
print(adj2)

# plt.xlim(0, 300)
# plt.ylim(-0, 300)

#
# plt.axis('off')
# graph_q1 = plt.gcf()
# plt.show()
# graph_q1.savefig("floyd.png")


