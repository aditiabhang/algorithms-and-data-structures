import matplotlib.pyplot as plt #for plotting graph
import time
from matplotlib import style
from numpy.random import seed 
from numpy.random import randint 

# create randomized, unsorted arrays for testing
def create_array(size=10, max=50):
    return [randint(0,max) for _ in range(size)]

# ---------- INSERTION SORT ----------
def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
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

# ---------- RANDOMIZED QUICK SORT ----------
def quicksort(alist, start, end):
	if start < end:
		pIndex = partition(alist, start, end)
		quicksort(alist, start, pIndex-1)
		quicksort(alist, pIndex+1, end)
	
	return alist

def partition(alist, start, end):
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
# ---------- HYBRID RANDOMIZED QUICK + INSERTION SORT ----------
m = 32

def hybridSort(numList, first, last):
    if first<last:
        sizeArr = last - first + 1
        if(sizeArr < m):
            insert_sort(numList, first, last)
        else:
            mid = partition(numList, first, last)
            hybridSort(numList, first, mid-1)
            hybridSort(numList, mid + 1, last)

def partition(numList, first, last):
    piv = numList[last]
    i = first-1
    for j in range(first,last):
        if numList[j] < piv:
            i += 1
            temp = numList[i]
            numList[i] = numList[j]
            numList[j] = temp

    tempo = numList[i+1]
    numList[i+1] = numList[last]
    numList[last] = tempo

    return i+1

def insert_sort(numList, first, last):
    for x in range(first, last):
        key = numList[x]
        y = x-1
        while y > -1 and numList[y]> key:
            numList[y+1] = numList[y]
            y = y-1
        numList[y+1] = key
    return numList
#---------------------------------------------
elements_quick = list() 
times_quick = list() 
for i in range(1, 10): 
	a = randint(0, 100, 100*i)
	start = time.perf_counter() 
	quickSort(a) 
	end = time.perf_counter() 
	elements_quick.append(len(a)) 
	times_quick.append(end-start) 

elements_insertion = list() 
times_insertion = list() 
for i in range(1, 10): 
	a = randint(0, 100, 100*i)
	start = time.perf_counter() 
	insertionSort(a) 
	end = time.perf_counter() 
	elements_insertion.append(len(a)) 
	times_insertion.append(end-start) 

elements_rand_quick = list() 
times_rand_quick = list() 
for i in range(1, 10): 
	a = randint(0, 100, 100*i)
	start = time.perf_counter() 
	quicksort(a, 0, len(a)-1) 
	end = time.perf_counter() 
	elements_rand_quick.append(len(a)) 
	times_rand_quick.append(end-start) 

elements_heap = list() 
times_heap = list() 
for i in range(1, 10): 
	a = randint(0, 100, 100*i)
	start = time.perf_counter() 
	heapSort(a) 
	end = time.perf_counter() 
	elements_heap.append(len(a)) 
	times_heap.append(end-start) 

elements_merge = list() 
times_merge = list() 
for i in range(1, 10): 
	a = randint(0, 100, 100*i)
	start = time.perf_counter() 
	mergeSort(a) 
	end = time.perf_counter() 
	elements_merge.append(len(a)) 
	times_merge.append(end-start) 

elements_hybrid = list() 
times_hybrid = list() 
for i in range(1, 10): 
	a = randint(0, 100, 100*i)
	start = time.perf_counter() 
	hybridSort(a, 0, len(a)-1) 
	end = time.perf_counter() 
	elements_hybrid.append(len(a)) 
	times_hybrid.append(end-start) 
#------------------------------------------------
# Here, we work with the data visualization part using subplots
# style.use('fivethirtyeight')
plt.style.use('ggplot')
fig = plt.figure()

ax1 = fig.add_subplot(3,2,1)
ax2 = fig.add_subplot(3,2,2)
ax3 = fig.add_subplot(3,2,3)
ax4 = fig.add_subplot(3,2,4)
ax5 = fig.add_subplot(3,2,5)
ax6 = fig.add_subplot(3,2,6)

ax1 = plt.subplot2grid((16,23), (0,0), rowspan = 4, colspan = 10) 
ax2 = plt.subplot2grid((16,23), (7,0), rowspan = 4, colspan = 10) 
ax3 = plt.subplot2grid((16,23), (13,0), rowspan = 4, colspan = 10)
ax4 = plt.subplot2grid((16,23), (0,13), rowspan = 4, colspan = 10) 
ax5 = plt.subplot2grid((16,23), (7,13), rowspan = 4, colspan = 10) 
ax6 = plt.subplot2grid((16,23), (13,13), rowspan = 4, colspan = 10)

ax1.plot(elements_insertion, times_insertion, label = "InsertionSort")
ax2.plot(elements_quick, times_quick, label = "Quick Sort")
ax3.plot(elements_rand_quick, times_rand_quick, label = "Randomised Quick Sort")
ax4.plot(elements_heap, times_heap, label = "Heap Sort")
ax5.plot(elements_merge, times_merge, label = "Merge Sort")
ax6.plot(elements_hybrid, times_hybrid, label = "Hybrid Sort")

ax1.legend()
ax2.legend()
ax3.legend()
ax4.legend()
ax5.legend()
ax6.legend()

plt.show()
# plt3.set_xlabel('Length') 
# plt3.set_ylabel('Time') 
