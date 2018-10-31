def main():

	# my_list = [8, 7, 6, 5, 4, 3, 2, 1]
	my_list = [6, 2, 8, 3, 1, 7, 9, 5, 4]
	quick_sort(my_list, 0, len(my_list)-1)
	print(my_list)


def quick_sort(numbers, i, j):
	if i < j:
		l = pivot(numbers, i, j)
		print(l)
		print(numbers[i:l])
		quick_sort(numbers, i, l-1)
		print(numbers[l:j])
		quick_sort(numbers, l, j)


# noinspection PyPep8Naming
def pivot(numbers, i, j):
	p = numbers[i]
	k = i
	l = j + 1
	# move pointer k from left until it points to a value larger than the pivot (p) - or the end of list
	while True:
		k += 1
		if numbers[k] > p or k >= j:
			break
	# move pointer l from right until it points to a value smaller or equal to the pivot (p)
	while True:
		l -= 1
		if numbers[l] <= p:
			break
	# if pointer k is to the left of l, swap the elements at k and l - so larger element moves to right; smaller: left.
	# do until k is to the right of l i.e. so that everything on the
	while k < l:
		numbers[k], numbers[l] = numbers[l], numbers[k]
		# look for next value larger than pivot from left
		while True:
			k += 1
			if numbers[k] > p:
				break
		# look for next value smaller than pivot from right
		while True:
			l -= 1
			if numbers[l] <= p:
				break
	# If pivot smallest value, move to end of sublist...
	if l == i:
		numbers.insert(j, numbers.pop(l))
		print(numbers)
	# Otherwise, move pivot to right side of list
	else:
		numbers[i], numbers[l] = numbers[l], numbers[i]
	return l


if __name__ == '__main__':
	main()


