import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from pylab import *
from time import process_time
start_time = process_time() # Begin the time count
plt.close('all')
def countingSort(the_list, max_value):  
    counts = [0] * (max_value + 1)
    for item in the_list:
        counts[item] += 1
    num_items_before = 0
    for i, count in enumerate(counts):
        counts[i] = num_items_before
        num_items_before += count
    # Output list to be filled in
    sorted_list = [None] * len(the_list)
    # Run through the input list
    for item in the_list:
        # Place the item in the sorted list
        sorted_list[ counts[item] ] = item
        # And, make sure the next item we see with the same value
        # goes after the one we just placed
        counts[item] += 1
    return sorted_list
arraySize = 10
#arr = [14,15,46,43,27,26,57,41,45,21,70,10,100,1000,500,499,789,113]
#mu, sigma = 10, 2 # mean and standard deviation
#arr = np.random.normal(mu, sigma, 100)
start_time = time.perf_counter()
arr = np.random.randint(low=1, high=10, size= arraySize).tolist()
max_value=np.max(arr)
sortedArray=countingSort(arr,max_value)
print ("The sorted list is:", sortedArray)
timeCount =process_time() - start_time
print ("The required time is: ", timeCount)
#for plotting
plt.plot(timeCount) 
plt.xlabel('Input Size (x25)') 
plt.ylabel('Time (second)') 
plt.title('Performance analysis of Counting Sort') 
plt.show() 
