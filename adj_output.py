import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import write_dot, graphviz_layout

G = nx.DiGraph()


nodes = ['a', 'b', 'c', 'd']
arcs = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'a')]

G.add_nodes_from(nodes)
G.add_edges_from(arcs)
G['a']['b']['weight'] = 1
G['b']['c']['weight'] = 1
G['c']['d']['weight'] = 1
G['d']['a']['weight'] = 2
pos = graphviz_layout(G, prog='circo')
nx.draw_networkx(G, pos, with_labels=True, node_size=1000, font_size=20, arrows=True, edgecolors='black', node_color='pink', edgelist=[('a', 'b'),('b', 'c'), ('c', 'd')])
nx.draw_networkx_edges(G, pos, edgelist=[('d', 'a')], style='dashed', edge_color='red')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=20, rotate=False)

plt.xlim(0, 300)
plt.ylim(-0, 300)


plt.axis('off')
graph_q1 = plt.gcf()
plt.show()
graph_q1.savefig("counter.png")


