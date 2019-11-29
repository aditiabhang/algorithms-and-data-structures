from random import randint

def rand_quicksort(alist, start, end):
	'''This function calls the partition and then recurse itself using the index returned by partition'''
	if start < end:
		pIndex = partition(alist, start, end)
		rand_quicksort(alist, start, pIndex-1)
		rand_quicksort(alist, pIndex+1, end)
	
	return alist

def partition(alist, start, end):
	'''This function will devide the list in two halves wrt pivot'''
	'''This will return the index of pivot after deviding'''
	pivot = randint(start, end)
	temp = alist[end]
	alist[end] = alist[pivot]
	alist[pivot] = temp
	pIndex = start
	
	for i in range(start, end):
		if alist[i] <= alist[end]:
			temp = alist[i]
			alist[i] = alist[pIndex]
			alist[pIndex] = temp
			pIndex += 1
	temp1 = alist[end]
	alist[end] = alist[pIndex]
	alist[pIndex] = temp1
	
	return pIndex

# create randomized arrays for testing
def create_array(size=5, max=50):
    from random import randint
    return [randint(0,max) for _ in range(size)]

a = create_array()
print ('Unsorted array: ', a)
rand_quicksort(a, 0, len(a)-1)
print ('Sorted array: ', a)