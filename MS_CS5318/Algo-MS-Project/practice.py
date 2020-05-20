import matplotlib.pyplot as plt #for plotting graph
import time
from matplotlib import style
from numpy.random import seed 
from numpy.random import randint 
# THIS CODE IS USED FOR FIGURING OUT THE CODE #
# THERE IS NOTHING MUCH TO IT
#--------------------------------------------------
# create randomized, unsorted arrays for testing
def create_array(size=10, max=50):
    return [randint(0,max) for _ in range(size)]

# ---------- QUICK SORT ----------
def quickSort(a):
    if len(a) <= 1:
        return a
    smaller,equal,larger = [], [], []
    pivot= a[len(a)-1]

    for x in a:
        if x < pivot:
            smaller.append(x)
        elif x==pivot:
            equal.append(x)
        else:
            larger.append(x)
    return quickSort(smaller)+equal+quickSort(larger)

#------------------------------------------
a = create_array()
print ("array: ", a)
print ("quick sort: ", quickSort(a))

