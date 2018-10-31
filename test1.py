def main():

	foo = [1, 2, 3, 4, 5]
	i = 0
	j = 1
	foo[i], foo[j] = foo[j], foo[i]

	print(foo)

	print(swap(foo))


def swap(foo):
	i = 0
	j = 1
	foo[i], foo[j] = foo[j], foo[i]
	return foo


if __name__ == '__main__':
	main()




