from math import inf


def create_prim_structures(matrix=[[]]):
    """Creates and returns Nearest and MinDist data structures."""
    n = len(matrix)
    near_node_array = []
    dists = []
    i = 1
    while i < n:
        near_node_array.append(0)
        dists.append(matrix[i][0])
        i += 1
    return near_node_array, dists


def update_min_dist(near_nodes, matrix, dists):
    """Updates MinDist array"""
    for index_node, nearest_node in enumerate(near_nodes):
        if dists[index_node] > matrix[index_node][nearest_node]:
            dists[index_node] = matrix[index_node][nearest_node]
    return dists


def update_node_lists(tree_nodes, matrix, near_nodes, dists):
    """Updates Nearest array"""
    for i in range(len(near_nodes)):
        # search through min dist to see if there are any closer nodes
        for j in range(len(dists)):
            if matrix[i][j] < dists[j]:
                dists[j] = matrix[i][j]
                near_nodes[j] = i



def get_closest_node_index(dist):
    minimum_dist = inf
    for i in range(len(dist)):
        if 0 < dist[i] < minimum_dist:
            minimum_dist = dist[i]
            closest_node = i
    print(f'next closest node is: a{closest_node}')
    return closest_node


def print_results(near_node_array, dists, T):
    print('\nNearest into B: \t MinDist into B:')
    for i in range(len(near_node_array)):
        print(f'a{i} => a{near_node_array[i]} \t\t\t a{i} = {dists[i]}')
    print()
    print('T is:', T)


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

    nearest, min_dist = create_prim_structures(L)
    print_results(nearest, min_dist, T)

    # loop through all nodes minus one: since # arcs for MST = N-1
    n = len(L)
    i = 0
    while i < n-1:

        k = get_closest_node_index(min_dist)
        T.append((k, nearest[k]))
        min_dist[k] = -1

        j = 1
        while j < n-1:
            print(L[k][j])
            print(min_dist[j])
            if L[k][j] < min_dist[j]:
                min_dist[j] = L[k][j]
                nearest[j] = k
            j += 1

        print_results(nearest, min_dist, T)
        i += 1


if __name__ == "__main__":
    main()





