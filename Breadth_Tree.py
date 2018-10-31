import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import write_dot, graphviz_layout

G = nx.DiGraph()


nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
arcs = [('a', 'b'), ('b', 'c'), ('b', 'e'), ('e', 'f'), ('e', 'd'), ('c', 'g'), ('g', 'h')]

G.add_nodes_from(nodes)
G.add_edges_from(arcs)
pos = graphviz_layout(G, prog='dot')
nx.draw_networkx(G, pos, with_labels=True, node_size=1000, font_size=20, arrows=True, edgecolors='black', node_color='pink')

plt.xlim(0, 200)
plt.ylim(-30, 450)


plt.axis('off')
graph_q1 = plt.gcf()
plt.show()
graph_q1.savefig("graph_breadth.png")


