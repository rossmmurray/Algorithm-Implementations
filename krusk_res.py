import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import write_dot, graphviz_layout

G = nx.Graph()


nodes = ['a'+str(x) for x in range(1, 8, 1)]
print(nodes)
arcs = [('a1', 'a4', 2), ('a1', 'a2', 3), ('a2', 'a3', 3), ('a2','a4', 2), ('a2', 'a5', 2), ('a3', 'a5', 2), ('a3', 'a6', 2), ('a4', 'a5', 1), ('a4', 'a7', 1), ('a5', 'a7', 1), ('a5', 'a6', 1), ('a6', 'a7', 1)]

G.add_nodes_from(nodes)
G.add_weighted_edges_from(arcs)

pos = graphviz_layout(G, prog='neato')
nx.draw_networkx_nodes(G, pos, with_labels=True, node_size=1000, arrows=True, edgecolors='black', node_color='pink')

nx.draw_networkx_labels(G, pos,  font_size=20)
#
nx.draw_networkx_edges(G, pos, edge_color='red', style='dashed')
#
nx.draw_networkx_edges(G, pos, edge_color='black', edgelist=[('a4', 'a7'), ('a5', 'a7'), ('a6', 'a7'), ('a1', 'a4'), ('a4', 'a2'), ('a5', 'a3')])

edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12, rotate=False)

print(G.edges())


# , edgelist=[('a', 'b'),('b', 'c'), ('c', 'd')]
#
# nx.draw_networkx_edges(G, pos, edge_color='red')
# edge_labels = nx.get_edge_attributes(G, 'weight')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=20, rotate=False)

plt.xlim(0, 300)
plt.ylim(-0, 300)


plt.axis('off')
graph_q1 = plt.gcf()
plt.show()
graph_q1.savefig("krusk_res.png")


