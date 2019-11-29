# random_list = [3, 43, 21, 65, 91, 36, 66, 33, 99, 77]
# partially_sorted_list = [3, 21, 33, 36, 43, 99, 77, 66, 65, 91]
# sorted_list = [3, 21, 33, 36, 43, 65, 66, 77, 91, 99]
# import time
# from random import randint

# create randomized, unsorted arrays for testing
def create_array(size=10, max=50):
    return [randint(0,max) for _ in range(size)]

# # create randomized arrays of size 10, 100 and 1000 for testing
# randomListOf5 = [randint(0,100) for i in range(5)]
# randomListOf10 = [randint(0,100) for i in range(10)]
# randomListOf50 = [randint(0,100) for i in range(50)]

# # print("random list of 5: ", randomListOf5)
# # print("random list of 10: ", randomListOf10)
# # print("random list of 50: ", randomListOf50)

# sortedListOf5 = sorted(randomListOf5)
# sortedListOf10 = sorted(randomListOf10)
# sortedListOf50 = sorted(randomListOf50)

# # print("Sorted list of 5: ", sortedListOf5)
# # print("Sorted list of 10: ", sortedListOf10)
# # print("Sorted list of 50: ", sortedListOf50)

# #--------------------------------------------------------------------------------------
# elements = list() 
# times = list() 
# for i in range(1, 10): 

# 	# generate some integers 
# 	a = randint(0, 100 * i, 100 * i) 
# 	# print(i) 
# 	start = time.clock() 
# 	#HeapSort(a) 
# 	end = time.clock() 

# 	# print("Sorted list is ", a) 
# 	print(len(a), "Elements Sorted by HeapSort in ", end-start) 
# 	elements.append(len(a)) 
# 	times.append(end-start) 

# n = [10, 100, 1000]
# times = {'quick': [], 'merge': [], 'insertion': [], 'heap': [], 'rand_quick': []}
# samples = 3
# from time import time

# for size in n:
#     tot_time = 0.0
#     for _ in range(samples):
#         a = create_array(size,size)
#         t0 = time()
#         s = quickSort(sorted(a))
#         t1 = time()
#         tot_time += (t1 - t0)
#     times['quick'].append(tot_time/float(samples))
#--------------------------------------------------------------------------------------
import time
from numpy.random import seed 
from numpy.random import randint 
import matplotlib.pyplot as plt 
import matplotlib.pyplot as plt1
import numpy as np 

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

# elements = list() 
# times = list() 
# for i in range(1, 10): 
# 	a = randint(0, 100, 100 * i) 
# 	start = time.perf_counter() 
# 	insertionSort(a) 
# 	end = time.perf_counter() 
# 	elements.append(len(a)) 
# 	times.append(end-start) 


# # printing the time taken by each algorithm for a already sorted arrays 
# n = [10, 100, 1000]
# times = {'quick': [], 'merge': [], 'insertion': [], 'heap': [], 'rand_quick': []}
# samples = 3
# from time import time

# for size in n:  
#     tot_time = 0.0
#     for _ in range(samples):
#         a = create_array(size, size)
#         t0 = time()
#         s = insertionSort(a)
#         t1 = time()
#         tot_time += (t1 - t0)
#     times['insertion'].append(tot_time/float(samples))

#     tot_time = 0.0
#     for _ in range(samples):
#         a = create_array(size,size)
#         t0 = time()
#         s = quickSort(a)
#         t1 = time()
#         tot_time += (t1 - t0)
#     times['quick'].append(tot_time/float(samples))

# plt.xlabel('List Length') 
# plt.ylabel('Time Complexity') 
# plt.plot(elements_insertion, times_insertion, label = "Insertion Sort")
# plt.grid() 
# plt.legend() 
# plt.show()

elements_quick = list() 
times_quick = list() 
for i in range(1, 10): 
	a = randint(0, 100, 100 * i)
	start = time.perf_counter() 
	quickSort(a) 
	end = time.perf_counter() 
	elements_quick.append(len(a)) 
	times_quick.append(end-start) 

elements_insertion = list() 
times_insertion = list() 
for i in range(1, 10): 
	a = randint(0, 100, 100 * i)
	start = time.perf_counter() 
	insertionSort(a) 
	end = time.perf_counter() 
	elements_insertion.append(len(a)) 
	times_insertion.append(end-start) 

elements_rand_quick = list() 
times_rand_quick = list() 
for i in range(1, 10): 
	a = randint(0, 100, 100 * i)
	start = time.perf_counter() 
	quicksort(a, 0, len(a)-1) 
	end = time.perf_counter() 
	elements_rand_quick.append(len(a)) 
	times_rand_quick.append(end-start) 

# setting a style to use 
plt.style.use('ggplot')
# defining subplots and their positions 
plt1 = plt.subplot2grid((11,1), (0,0), rowspan = 3, colspan = 1) 
plt2 = plt.subplot2grid((11,1), (4,0), rowspan = 3, colspan = 1) 
plt3 = plt.subplot2grid((11,1), (8,0), rowspan = 3, colspan = 1)

plt1.set_xlabel('Legth') 
plt1.set_ylabel('Time') 
plt1.plot(elements_insertion, times_insertion, label = "InsertionSort")
#plt.show()

plt2.set_xlabel('Length') 
plt2.set_ylabel('Time') 
plt2.plot(elements_quick, times_quick, label = "Quick Sort")

plt3.set_xlabel('Length') 
plt3.set_ylabel('Time') 
plt3.plot(elements_rand_quick, times_rand_quick, label = "Randomised Quick Sort")

plt1.legend() 
plt2.legend()
plt3.legend() 

plt.show()







#--------------------------------------------------------------------------------------
# def create_array_10(size=10, max=100):
#     from random import randint
#     random_listOf10 = [randint(0,max) for _ in range(size)]

# # create randomized, unsorted arrays for testing
# def create_array(size=10, max=50):
#     return [randint(0,max) for _ in range(size)]
     
# random_list = create_array()

# mid = len(random_list)//2
# partial_sorted_one = sorted(random_list[0:mid])
# partial_unsorted_one = random_list[mid:]
# x = random_list[:mid].sort()



# mylist = []
# for i in range(size):
#     print(mylist.append(randint(0,max))

