import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout

G = nx.DiGraph()


nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
arcs = [('a', 'b'), ('b', 'c'), ('c', 'g'), ('g', 'h'), ('c', 'f'), ('f', 'e'), ('e', 'd')]

G.add_nodes_from(nodes)
G.add_edges_from(arcs)
pos = graphviz_layout(G, prog='dot')
nx.draw_networkx(G, pos, with_labels=True, node_size=1000, font_size=20, arrows=True, edgecolors='black', node_color='pink')

# canvas resizing/moving
plt.xlim(0, 150)
plt.ylim(-30, 450)


plt.axis('off')
graph_q1 = plt.gcf()
plt.show()
graph_q1.savefig("graph_q2.png")


