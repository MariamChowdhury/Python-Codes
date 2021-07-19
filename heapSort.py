import numpy as np
import time
import matplotlib
import matplotlib.pyplot as plt

from pylab import *

plt.close('all')

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

# Driver code to test above 
arraySize = 10

#arr = np.random.randint(low=1, high=100, size= arraySize).tolist()
arr = [ 12, 11, 13, 5, 6, 7] 
heapSort(arr) 
n = len(arr) 
print ("Sorted array is", arr) 


#for i in range(n): 
#	print ("%d" %arr[i]), 
