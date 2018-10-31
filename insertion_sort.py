# insertion sort in increasing order

A = [1, 2, 4, 6, 3, 20]

j = 1
while j < len(A):
    key = A[j]
    i = j - 1
    while i > -1 and A[i] < key:
        # swap A[i] and A[i+1]
        A[i+1] = A[i]
        i -= 1
    A[i+1] = key
    j += 1

print(A)

