from math import inf


def create_prim_structures(first_node=2, matrix=[[]]):
    """Creates and returns Nearest and MinDist data structures."""
    near_node_array = []
    dists = []
    for _ in matrix:
        near_node_array.append(first_node)
        dists.append(inf)
    dists[first_node] = -1
    dists = update_min_dist(near_node_array, matrix, dists)
    return near_node_array, dists


def update_min_dist(near_nodes, matrix, dists):
    """Updates MinDist array"""
    for index_node, nearest_node in enumerate(near_nodes):
        if dists[index_node] > matrix[index_node][nearest_node]:
            dists[index_node] = matrix[index_node][nearest_node]
    return dists


def update_nearest(tree_nodes, matrix, near_nodes):
    """Updates Nearest array"""
    for i in range(len(near_nodes)):
        # search through tree_nodes to see if there is a new closest node
        minimum = inf
        for j in tree_nodes:
            if matrix[i][j] < minimum:
                minimum = matrix[i][j]
                k = j
        near_nodes[i] = k



def get_closest_node_index(dist):
    minimum_dist = inf
    for i in range(len(dist)):
        if 0 < dist[i] < minimum_dist:
            minimum_dist = dist[i]
            closest_node = i
    print(f'next closest node is: a{closest_node}')
    return closest_node


def print_results(near_node_array, dists, T, B):
    print('\nNearest into B: \t MinDist into B:')
    for i in range(len(near_node_array)):
        print(f'a{i} => a{near_node_array[i]} \t\t\t a{i} = {dists[i]}')
    print()
    print('T is:', T)
    print('B is:', B)


def main():

    f = inf
    L = [
        [f, 1, f, 4, f, f, f],
        [1, f, 2, 6, 4, f, f],
        [f, 2, f, f, 5, 6, f],
        [4, 6, f, f, 3, f, 4],
        [f, 4, 5, 3, f, 8, 7],
        [f, f, 6, f, 8, f, 3],
        [f, f, f, 4, 7, 3, f]
        ]

    T = []
    # random choice of node to start from
    B = [2]

    nearest, min_dist = create_prim_structures(B[0], L)

    # loop through all nodes minus one: since # arcs for MST = N-1
    i = 0
    while i < len(L)-1:

        # add node index into B and arc into T
        k = get_closest_node_index(min_dist)
        B.append(k)
        T.append((k, nearest[k]))
        min_dist[k] = -1

        update_nearest(B, L, nearest)
        update_min_dist(nearest, L, min_dist)

        print_results(nearest, min_dist, T, B)
        i += 1


if __name__ == "__main__":
    main()





