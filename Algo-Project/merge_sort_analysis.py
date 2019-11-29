import time 
from numpy.random import seed 
from numpy.random import randint 
import matplotlib.pyplot as plt 

# # create randomized arrays for testing
# def create_array(size=5, max=50):
#     from random import randint
#     return [randint(0,max) for _ in range(size)]

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
# randomly generates list of different 
# sizes and call HeapSort funtion 
elements = list() 
times = list() 
for i in range(1, 10): 

	# generate some integers 
	a = randint(0, 1000 * i, 1000 * i) 
	# print(i) 
	start = time.clock() 
	mergeSort(a) 
	end = time.clock() 

	# print("Sorted list is ", a) 
	print(len(a), "Elements Sorted by mergeSort in ", end-start) 
	elements.append(len(a)) 
	times.append(end-start) 

plt.xlabel('List Length') 
plt.ylabel('Time Complexity') 
plt.plot(elements, times, label ='Merge Sort') 
plt.grid() 
plt.legend() 
plt.show() 
