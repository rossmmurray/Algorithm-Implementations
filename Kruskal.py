import math
from operator import itemgetter


def xor_search(u, v, L):
    """
        function to tell if there is one and only one of two elements
        in a sublist. if so, return the first element as one in the
        sublist and the second as outside the sublist. otherwise return false.
    """
    if (u in L) ^ (v in L):
        if u in L:
            return u, v
        else:
            return v, u
    else:
        False


def two_d_index(x, L):
    for key, inner_list in L:
        try:
            return key, inner_list.index
        except ValueError:
            continue
    return False


f = math.inf

# set up graph data structure
L = [
    [f, 1, f, 4, f, f, f],
    [1, f, 2, 6, 4, f, f],
    [f, 2, f, f, 5, 6, f],
    [4, 6, f, f, 3, f, 4],
    [f, 4, 5, 3, f, 8, 7],
    [f, f, 6, f, 8, f, 3],
    [f, f, f, 4, 7, 3, f]
    ]

# create a dictionary with tuples as the keys e.g. {(0,0): f,
graph = {}
sorted_list = []
T = {}  # solution dict
connected_components = [[0], [1], [2], [3], [4], [5], [6]]

# how to merge two sublists
# print('before merge', connected_components)
# connected_components[2].extend(connected_components.pop(4))
# print('after merge', connected_components)

for index1, row in enumerate(L):
    for index2, element in enumerate(row):
        graph[(index1, index2)] = element

print('graph is', graph)

sorted_list = sorted(graph.items(), key=itemgetter(1))

print('sorted list is', sorted_list)

n = len(sorted_list)

# repeat (u,v) is the shortest edge not yet considered - loop through sorted_list
# shortest_edge is like ((node1, node2), node_length)
for shortest_edge in sorted_list:
    node1 = shortest_edge[0][0]
    node2 = shortest_edge[0][1]
    # ignore checking a node with itself
    if node1 == node2:
        break
    else:
        # check there is at least one node not in connected_components
        for sublist in connected_components:
            if xor_search(node1, node2, sublist):
                n, m = xor_search(node1, node2, sublist)
                # two_d_index()

                # find i[0][0] and i[0][1] in connected_components and merge the sublists they're in
                print(sublist)
                # sublist.extend()
                sublist.append(shortest_edge[0][0])
                sublist.append(shortest_edge[0][1])
                print(sublist)
                print(connected_components)
                # print(sublist[shortest_edge[0]])
                print(T)
                T[sublist][shortest_edge[0]] = shortest_edge[1]

print(T)



