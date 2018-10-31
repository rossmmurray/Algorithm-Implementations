def main():

    list_a = [1, 5, 3, 7, 2, 6, 4, 8]
    sorted_list = merge_sort(list_a)
    # print(list_a[:len(list_a)//2])
    print(sorted_list)


def merge_sort(unsorted_list=[]):
    if len(unsorted_list) == 1:
        print(f'returning one element: {unsorted_list}')
        return unsorted_list
    else:
        midpoint = len(unsorted_list)//2
        print(f'Merge sorting Left: {unsorted_list[:midpoint]}')
        u = merge_sort(unsorted_list[:midpoint])
        print(f'Merge sorting Right: {unsorted_list[midpoint:]}')
        v = merge_sort(unsorted_list[midpoint:])
        # print(u, v)
        return merge(u, v)


def merge(list_a, list_b):
    print(f'merging: {list_a} and {list_b}')
    sorted_sublist = []
    while len(list_a) > 0 or len(list_b) > 0:
        if len(list_a) == 0:
            sorted_sublist.append(list_b.pop())
        elif len(list_b) == 0:
            sorted_sublist.append(list_a.pop())
        elif list_a[0] < list_b[0]:
            sorted_sublist.append(list_a.pop(0))
        else:
            sorted_sublist.append(list_b.pop(0))
    print(f'Merged {sorted_sublist}')
    return sorted_sublist


if __name__ == '__main__':
    main()