import numpy as np
from time import process_time
start_time = process_time() # Begin the time count
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
# Driver code to test above 
#arr = [12, 11, 13, 5, 6, 112, 111, 113, 15, 16, 112, 111, 213, 35, 46, 412, 411, 413, 45, 46]
#arr = [12, 11, 13, 5, 6, 112, 111, 113, 15, 16, 112, 111, 213, 35, 46, 412, 411, 413, 45, 46, 12, 11, 13, 5, 6, 112, 111, 113, 15, 16, 112, 111, 213, 35, 46, 412, 411, 413, 45, 46, 12, 11, 13, 5, 6, 112, 111, 113, 15, 16, 112, 111, 213, 35, 46, 412, 411, 413, 45, 46, 12, 11, 13, 5, 6, 112, 111, 113, 15, 16, 112, 111, 213, 35, 46, 412, 411, 413, 45, 46, 12, 11, 13, 5, 6, 112, 111, 113, 15, 16, 112, 111, 213, 35, 46, 412, 411, 413, 45, 46]  
arr = [55,2,3,31,19,21,10,25,67]
#arr = np.random.randint(low=1, high=1000, size=10000) #for generating random numbers
insertionSort(arr) 
for k in range(len(arr)): 
    print ("% d" % arr[k]) 
end_time = process_time()
time =end_time - start_time
print("Start Time:", start_time)
print("End Time:", end_time)
print ("Elapsed Time: ", time)
