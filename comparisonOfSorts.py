import numpy as np
import time
import matplotlib
import matplotlib.pyplot as plt

from pylab import *
plt.close('all')
# Python program for implementation of Insertion Sort 
  
# Function to do insertion sort 
def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for j in range(1, len(arr)): 
  
        key = arr[j] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        i = j-1
        while i >= 0 and key < arr[i] : 
                arr[i + 1] = arr[i] 
                i -= 1
        arr[i + 1] = key 

# Function to do Merge sort 
def mergeSort(nlist):
    #print("Splitting ",nlist)
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
    #print("Merging ",nlist)


# Python program for implementation of heap Sort 

def heapSort( aList ):
  # convert aList to heap
  length = len( aList ) - 1
  leastParent = int(length / 2)
  for i in range ( leastParent, -1, -1 ):
    moveDown( aList, i, length )
 
  # flatten heap into sorted array
  for i in range ( length, 0, -1 ):
    if aList[0] > aList[i]:
      swap( aList, 0, i )
      moveDown( aList, 0, i - 1 )
 
 
def moveDown( aList, first, last ):
  largest = 2 * first + 1
  while largest <= last:
    # right child exists and is larger than left child
    if ( largest < last ) and ( aList[largest] < aList[largest + 1] ):
      largest += 1
 
    # right child is larger than parent
    if aList[largest] > aList[first]:
      swap( aList, largest, first )
      # move down to largest child
      first = largest;
      largest = 2 * first + 1
    else:
      return # force exit
 
 
def swap( A, x, y ):
  tmp = A[x]
  A[x] = A[y]
  A[y] = tmp



steps = 301


timeCountIS = np.zeros(steps)

for i in range(steps):
    start_time = time.clock()
    
    arraySize = 25*i
    arr = np.random.randint(low=1, high=10000, size= arraySize).tolist()
    insertionSort(arr)

    print ("Loop Rotation: for Insertion Sort", arraySize, "numbers ...")

    timeCountIS[i] =time.clock() - start_time    
    # print timeCount


timeCountHS = np.zeros(steps)

for i in range(steps):
    start_time = time.clock()
    
    arraySize = 25*i
    arr = np.random.randint(low=1, high=10000, size= arraySize).tolist()
    heapSort(arr)

    print ("Loop Rotation: for Heap Sort", arraySize, "numbers ...")

    timeCountHS[i] =time.clock() - start_time    
    # print timeCount


timeCountMS = np.zeros(steps)

for i in range(steps):
    start_time = time.clock()
    
    arraySize = 25*i
    arr = np.random.randint(low=1, high=10000, size= arraySize).tolist()
    #insertionSort(arr)
    mergeSort(arr)

    print ("Loop Rotation: For Merge Sort", arraySize, "numbers ...")

    timeCountMS[i] =time.clock() - start_time    
    # print timeCount


plt.plot(timeCountIS, 'b', label='Insertion Sort', lw=2)
plt.plot(timeCountHS, 'r', label='Heap Sort', lw=2)
plt.plot(timeCountMS, 'g', label='Merge Sort', lw=2)

plt.xlabel('Input Size (x25)')
plt.ylabel('Time (second)')
plt.title('Performance analysis of Insertion Sort and Merge Sort')
plt.legend(loc='upper left')
plt.show()
