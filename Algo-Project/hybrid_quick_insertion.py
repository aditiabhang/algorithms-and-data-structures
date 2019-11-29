# from random import randint

# # ---------- INSERTION SORT ----------
# def insertionSort(arr): 
  
#     # Traverse through 1 to len(arr) 
#     for i in range(1, len(arr)): 
#         key = arr[i] 
#         j = i-1
#         while j >=0 and key < arr[j] : 
#                 arr[j+1] = arr[j] 
#                 j -= 1
#         arr[j+1] = key 

# # ---------- RANDOMIZED QUICK SORT ----------
# def randomized_quicksort(alist, start, end):
#     size = (end + 1) - start
# 	if start < end:
#         if end < 32:
#             insertionSort(alist, start, size)

#         pIndex = partition(alist, start, end)
# 		randomized_quicksort(alist, start, pIndex-1)
# 		randomized_quicksort(alist, pIndex+1, end)

# 	    return alist

# def partition(alist, start, end):
# 	pivot = randint(start, end)
# 	temp = alist[end]
# 	alist[end] = alist[pivot]
# 	alist[pivot] = temp
# 	pIndex = start
	
# 	for i in range(start, end):
# 		if alist[i] <= alist[end]:
# 			temp = alist[i]
# 			alist[i] = alist[pIndex]
# 			alist[pIndex] = temp
# 			pIndex += 1
# 	temp1 = alist[end]
# 	alist[end] = alist[pIndex]
# 	alist[pIndex] = temp1
	
# 	return pIndex


# a_list = [33, 22, 34, 54, 32, 11, 32, 78, 99]
# result = randomized_quicksort(a_list, 0, len(a_list)-1)
# print("Hybrid of Randomized Quick and Insertion Sort: ", result)
#-------------------X--------------------X-------------------X----------------------
from random import randint
import time
import random

m = 32

def hybrid_quicksort(numList, first, last):
    if first<last:
        sizeArr = last - first + 1
        if(sizeArr < m):
            insert_sort(numList, first, last)
        else:
            mid = partition(numList, first, last)
            hybrid_quicksort(numList, first, mid-1)
            hybrid_quicksort(numList, mid + 1, last)

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

# create randomized, unsorted arrays for testing
def create_array(size=10, max=50):
    return [randint(0,max) for _ in range(size)]

n = [10, 100, 1000]
times = {'insertion': []}
samples = 3
from time import time

for size in n:
    tot_time = 0.0
    for _ in range(samples):
        a = create_array(size,size)
        t0 = time()
        s = hybrid_quicksort(a, 0, len(a)-1)
        t1 = time()
        tot_time += (t1 - t0)
    times['insertion'].append(tot_time/float(samples))

print ("Inputs")
print (10*"_")
print ("n\Hybrid Insertion Sort")
print (10*"_")
for i, size in enumerate(n):
    print ("%d\t%0.5f"%(size, times['insertion'][i]))


