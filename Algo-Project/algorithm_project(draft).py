import time 
from numpy.random import randint 
from random import randint

# create randomized, unsorted arrays for testing
def create_array(size=10, max=50):
    return [randint(0,max) for _ in range(size)]

# ---------- QUICK SORT ----------
def quickSort(a):
    if len(a) <= 1:
        return a
    smaller,equal,larger = [], [], []
    pivot= a[randint(0, len(a)-1)]

    for x in a:
        if x < pivot:
            smaller.append(x)
        elif x==pivot:
            equal.append(x)
        else:
            larger.append(x)
    return quickSort(smaller)+equal+quickSort(larger)

# ---------- MERGE SORT ----------
def mergeSort(arr): 
	if len(arr) >1: 
		mid = len(arr)//2 #Finding the mid of the array 
		L = arr[:mid] # Dividing the array elements 
		R = arr[mid:] # into 2 halves 

		mergeSort(L) # Sorting the first half 
		mergeSort(R) # Sorting the second half 

		i = j = k = 0
		
		# Copy data to temp arrays L[] and R[] 
		while i < len(L) and j < len(R): 
			if L[i] < R[j]: 
				arr[k] = L[i] 
				i+=1
			else: 
				arr[k] = R[j] 
				j+=1
			k+=1
		
		# Checking if any element was left 
		while i < len(L): 
			arr[k] = L[i] 
			i+=1
			k+=1
		
		while j < len(R): 
			arr[k] = R[j] 
			j+=1
			k+=1

# ---------- INSERTION SORT ----------
def insertionSort(alist, start, end): 
    for i in range(start, end + 1): 
        key = alist[i] 
        j = i-1
        while j >=0 and key < alist[j] : 
                alist[j+1] = alist[j] 
                j -= 1
        alist[j+1] = key 
		
	return alist
# ---------- HEAP SORT ----------
# find left child of node i 
def left(i): 
	return 2 * i + 1

# find right child of node i 
def right(i): 
	return 2 * i + 2

# calculate and return array size 
def heapSize(A): 
	return len(A)-1

def MaxHeapify(A, i): 
	# print("in heapy", i) 
	l = left(i) 
	r = right(i) 
	 
	if l<= heapSize(A) and A[l] > A[i] : 
		largest = l 
	else: 
		largest = i 
	if r<= heapSize(A) and A[r] > A[largest]: 
		largest = r 
	if largest != i: 
		A[i], A[largest]= A[largest], A[i]  
		MaxHeapify(A, largest) 
	
def BuildMaxHeap(A): 
	for i in range(int(heapSize(A)/2)-1, -1, -1): 
		MaxHeapify(A, i) 
		
def heapSort(A): 
	BuildMaxHeap(A) 
	B = list() 
	heapSize1 = heapSize(A) 
	for i in range(heapSize(A), 0, -1): 
		A[0], A[i]= A[i], A[0] 
		B.append(A[heapSize1]) 
		A = A[:-1] 
		heapSize1 = heapSize1-1
		MaxHeapify(A, 0) 

# ---------- RANDOMIZED QUICK SORT ----------
def randomized_quicksort(alist, start, end):
	if start < end:
		mid = partition_for_randomized(alist, start, end)
		randomized_quicksort(alist, start, mid - 1)
		randomized_quicksort(alist, mid + 1, end)
	
	return alist

def partition_for_randomized(alist, start, end):
	pivot = randint(start, end)
	temp = alist[end]
	alist[end] = alist[pivot]
	alist[pivot] = temp
	mid = start
	
	for i in range(start, end):
		if alist[i] <= alist[end]:
			temp = alist[i]
			alist[i] = alist[mid]
			alist[mid] = temp
			mid += 1

	temp1 = alist[end]
	alist[end] = alist[mid]
	alist[mid] = temp1
	
	return mid


#----------------------X-------------------X-----------------------

# Printing the time taken by each algorithm for random input arrays of different size
n = [10, 100, 1000]
times = {'quick': [], 'merge': [], 'insertion': [], 'heap': [], 'rand_quick': []}
samples = 3
from time import time

for size in n:
    tot_time = 0.0
    for _ in range(samples):
        a = create_array(size,size)
        t0 = time()
        s = quickSort(a)
        t1 = time()
        tot_time += (t1 - t0)
    times['quick'].append(tot_time/float(samples))

    tot_time = 0.0
    for _ in range(samples):
        a = create_array(size,size)
        t0 = time()
        s = mergeSort(a)
        t1 = time()
        tot_time += (t1 - t0)
    times['merge'].append(tot_time/float(samples))

    tot_time = 0.0
    for _ in range(samples):
        a = create_array(size,size)
        t0 = time()
        s = insertionSort(a, 0, len(a)-1)
        t1 = time()
        tot_time += (t1 - t0)
    times['insertion'].append(tot_time/float(samples))

    tot_time = 0.0
    for _ in range(samples):
        a = create_array(size,size)
        t0 = time()
        s = heapSort(a)
        t1 = time()
        tot_time += (t1 - t0)
    times['heap'].append(tot_time/float(samples))

    tot_time = 0.0
    for _ in range(samples):
        a = create_array(size,size)
        t0 = time()
        s = randomized_quicksort(a, 0, len(a)-1)
        t1 = time()
        tot_time += (t1 - t0)
    times['rand_quick'].append(tot_time/float(samples))

print ("\t\tRandom Inputs")
print (100*"_")
print ("n\tQuick Sort\tMerge Sort\tInsertion Sort\tHeap Sort\tRandomized Quick Sort")
print (100*"_")
for i, size in enumerate(n):
    print ("%d\t%0.5f \t%0.5f \t%0.5f \t%0.5f \t%0.5f"%(size, times['quick'][i], times['merge'][i], times['insertion'][i], times['heap'][i], times['rand_quick'][i]))
print("")
print("")

# printing the time taken by each algorithm for a partially sorted arrays 
n = [10, 100, 1000]
times = {'quick': [], 'merge': [], 'insertion': [], 'heap': [], 'rand_quick': []}
samples = 3
from time import time

for size in n:
    tot_time = 0.0
    for _ in range(samples):
        a = [1, 2, 3, 4, 5, 9, 8, 10, 3, 3]
        t0 = time()
        s = quickSort(sorted(a))
        t1 = time()
        tot_time += (t1 - t0)
    times['quick'].append(tot_time/float(samples))

    tot_time = 0.0
    for _ in range(samples):
        a = [1, 2, 3, 4, 5, 9, 8, 10, 3, 3]
        t0 = time()
        s = mergeSort(sorted(a))
        t1 = time()
        tot_time += (t1 - t0)
    times['merge'].append(tot_time/float(samples))


    tot_time = 0.0
    for _ in range(samples):
        a = [1, 2, 3, 4, 5, 9, 8, 10, 3, 3]
        t0 = time()
        s = insertionSort(a, 0, len(a)-1)
        t1 = time()
        tot_time += (t1 - t0)
    times['insertion'].append(tot_time/float(samples))

    tot_time = 0.0
    for _ in range(samples):
        a = [1, 2, 3, 4, 5, 9, 8, 10, 3, 3]
        t0 = time()
        s = heapSort(a)
        t1 = time()
        tot_time += (t1 - t0)
    times['heap'].append(tot_time/float(samples))

    tot_time = 0.0
    for _ in range(samples):
        a = [1, 2, 3, 4, 5, 9, 8, 10, 3, 3]
        t0 = time()
        s = randomized_quicksort(a, 0, len(a)-1)
        t1 = time()
        tot_time += (t1 - t0)
    times['rand_quick'].append(tot_time/float(samples))

print ("\t\tPartially Sorted Inputs")
print (100*"_")
print ("n\tQuick Sort\tMerge Sort\tInsertion Sort\tHeap Sort\tRandomized Quick Sort")
print (100*"_")
for i, size in enumerate(n):
    print ("%d\t%0.5f \t%0.5f \t%0.5f \t%0.5f \t%0.5f"%(size, times['quick'][i], times['merge'][i], times['insertion'][i], times['heap'][i], times['rand_quick'][i]))
print("")
print("")


# printing the time taken by each algorithm for a already sorted arrays 
n = [10, 100, 1000]
times = {'quick': [], 'merge': [], 'insertion': [], 'heap': [], 'rand_quick': []}
samples = 3
from time import time

for size in n:
    tot_time = 0.0
    for _ in range(samples):
        a = create_array(size,size)
        t0 = time()
        s = quickSort(sorted(a))
        t1 = time()
        tot_time += (t1 - t0)
    times['quick'].append(tot_time/float(samples))

    tot_time = 0.0
    for _ in range(samples):
        a = create_array(size,size)
        t0 = time()
        s = mergeSort(sorted(a))
        t1 = time()
        tot_time += (t1 - t0)
    times['merge'].append(tot_time/float(samples))


    tot_time = 0.0
    for _ in range(samples):
        a = create_array(size,size)
        t0 = time()
        s = insertionSort(a, 0, len(a)-1)
        t1 = time()
        tot_time += (t1 - t0)
    times['insertion'].append(tot_time/float(samples))

    tot_time = 0.0
    for _ in range(samples):
        a = create_array(size,size)
        t0 = time()
        s = heapSort(a)
        t1 = time()
        tot_time += (t1 - t0)
    times['heap'].append(tot_time/float(samples))

    tot_time = 0.0
    for _ in range(samples):
        a = create_array(size,size)
        t0 = time()
        s = randomized_quicksort(a, 0, len(a)-1)
        t1 = time()
        tot_time += (t1 - t0)
    times['rand_quick'].append(tot_time/float(samples))

print ("\t\tSorted Inputs")
print (100*"_")
print ("n\tQuick Sort\tMerge Sort\tInsertion Sort\tHeap Sort\tRandomized Quick Sort")
print (100*"_")
for i, size in enumerate(n):
    print ("%d\t%0.5f \t%0.5f \t%0.5f \t%0.5f \t%0.5f"%(size, times['quick'][i], times['merge'][i], times['insertion'][i], times['heap'][i], times['rand_quick'][i]))


