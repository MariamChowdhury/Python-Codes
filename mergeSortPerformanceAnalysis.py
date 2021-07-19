import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from time import process_time

from pylab import *

plt.close('all')
# Python program for implementation of Insertion Sort 

def mergeSort(nlist):
    print("Splitting ",nlist)
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0       
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",nlist)

# loop for plotting 
arraySize = 200
steps = 300
timeCount = np.zeros(steps) 
for i in range(steps): 
 start_time = process_time() 
arraySize = 200*i 


#arr = [14,15,46,43,27,26,57,41,45,21,70,10,100,1000,500,499,789,113]
#mu, sigma = 10, 2 # mean and standard deviation
#arr = np.random.normal(mu, sigma, 100)

arr = np.random.randint(low=1, high=10000, size= arraySize)

mergeSort(arr)

print ("The sorted list is:", arr)

timeCount = process_time() - start_time

print ("The required time is: ", timeCount)

plt.plot(timeCount) 
plt.xlabel('Input Size (x300)') 
plt.ylabel('Time (second)') 
plt.title('Performance analysis of Merge Sort') 
plt.show() 
