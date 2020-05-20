# Name: Aditi Abhang 
# Net ID: aaa333
#--------------------------------------------------
from random import randint
import time
from time import time
import matplotlib.pyplot as plt
from numpy.random import seed 
from numpy.random import randint

# create randomized, unsorted arrays for testing
def create_array(size=35, max=50):
    return [randint(0,max) for _ in range(size)]

#---------- HYBRID RANDOMIZED QUICK + INSERTION SORT ----------
m = 32

def hybridSort(numList, first, last):
    if first<last:
        sizeArr = last - first + 1
        if(sizeArr < m):
            insert_sort(numList, first, last)
        else:
            mid = partition_for_hybrid(numList, first, last)
            hybridSort(numList, first, mid-1)
            hybridSort(numList, mid + 1, last)

            return numList

def partition_for_hybrid(alist, first, last):
	pivot = randint(first, last)
	temp = alist[last]
	alist[last] = alist[pivot]
	alist[pivot] = temp
	mid = first
	
	for i in range(first, last):
		if alist[i] <= alist[last]:
			temp = alist[i]
			alist[i] = alist[mid]
			alist[mid] = temp
			mid += 1

	temp1 = alist[last]
	alist[last] = alist[mid]
	alist[mid] = temp1
	
	return mid

def insert_sort(numList, first, last):
    for x in range(first, last):
        key = numList[x]
        y = x-1
        while y > -1 and numList[y]> key:
            numList[y+1] = numList[y]
            y = y-1
        numList[y+1] = key
    return numList

# arr = create_array()
# print ("Given array is: ", arr)
# hybrid = hybridSort(arr, 0, len(arr)-1)
# print("Hybrid sort: ", hybrid)
# print ("\n")

# printing the time taken by each algorithm for a reverse inputs 
n = [100, 1000, 10000]
times = {'hybrid': []}
samples = 3

for size in n:
    tot_time = 0.0
    for _ in range(samples):
        a = create_array(size,size)
        b = sorted(a)
        b.reverse()
        t0 = time()
        s = hybridSort(a, 0, len(a)-1)
        t1 = time()
        tot_time += (t1 - t0)
    times['hybrid'].append(tot_time/float(samples))
print ("Runtime:")
for i, size in enumerate(n):
    print ("%d\t%0.5f "%(size, times['hybrid'][i]))
print("")

print ("-----Runtime of input size 1000 - 10,000----- ")
elements = list() 
times = list() 
for i in range(1, 10): 
	a = randint(0, 32, 1000 * i) 
	start = time()
	hybridSort(a, 0, len(a)-1) 
	end = time() 

	print(len(a), "Elements Sorted by Hybrid Sort in ", end-start) 
	elements.append(len(a)) 
	times.append(end-start) 

plt.xlabel('List Length') 
plt.ylabel('Time Complexity') 
plt.plot(elements, times, label ='Hybrid Sort') 
plt.grid() 
plt.legend() 
plt.show() 