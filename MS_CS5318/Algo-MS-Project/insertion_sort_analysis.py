# THIS CODE IS USED FOR FIGURING OUT THE CODE #
# THERE IS NOTHING MUCH TO IT
#--------------------------------------------------

import time 
from numpy.random import seed 
from numpy.random import randint 
import matplotlib.pyplot as plt 

# create randomized arrays for testing
def create_array(size=5, max=50):
    from random import randint
    return [randint(0,max) for _ in range(size)]

# Python program for implementation of MergeSort 
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


# Function to do insertion sort 
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


# # randomly generates list of different 
# # sizes and call HeapSort funtion 
# elements = list() 
# times = list() 
# for i in range(1, 5): 
  
#     # generate some integers 
#     a = randint(0, 1000 * i, 1000 * i) 
#     # print(i) 
#     start = time.clock() 
#     insertionSort(a) 
#     end = time.clock() 
  
#     # print("Sorted list is ", a) 
#     print(len(a), "Elements Sorted by insertionSort in ", end-start) 
#     elements.append(len(a)) 
#     times.append(end-start) 

def benchmark(n =[10, 100, 1000]):
    from time import time
    insertion_times = []
    merge_times = []

    for size in n:
        a=create_array(size, size)
        t0=time()
        insertionSort(a)
        t1=time()
        insertion_times.append(t1-t0)

        a=create_array(size, size)
        t0=time()
        mergeSort(a)
        t1=time()
        insertion_times.append(t1-t0)

    print ("\nn\tInsertion\tMerge")
    print (50*"_")
    for i,size in enumerate(n):
        print ("%d\t%0.5f   \t%0.5f   \t%0.5f"%(size,insertion_times[i],merge_times[i]))
    print ("\n")

# benchmark the 3 algorithms
benchmark()


  
plt.xlabel('List Length') 
plt.ylabel('Time Complexity') 
plt.plot(elements, times, label ='Insertion Sort') 
plt.grid() 
plt.legend() 
plt.show() 