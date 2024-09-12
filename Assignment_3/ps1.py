import matplotlib.pyplot as plt
import numpy as np
import time




def maxima(arr):
    m = 0
    for i in arr:
        if(m<i):
            m = i
    return m


def minima(arr):
    m = 0
    for i in arr:
        if(m>i):
            m = i
    return m



    

def quickSelect(arr,k):
    pivot = np.random.choice(arr)
    left = [x for x in arr if x<pivot]
    equal = [x for x in arr if x==pivot]
    right = [x for x in arr if x>pivot]
    
    if k<len(left):
        return quickSelect(left,k)
    elif k<len(left) + len(equal):
        return pivot
    else:
        return quickSelect(right,k-len(left) - len(equal))
    

    
def partition(arr, pivot):
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    return left, [x for x in arr if x == pivot], right

def select(arr, k):
    # Base case: if the array is small,we just sort and find the k-th element
    if len(arr) <= 5:
        return sorted(arr)[k]

    # Step 1: Dividing the array into subgroups of 5
    sublists = [arr[i:i+5] for i in range(0, len(arr), 5)]

    # Step 2: Sorting each subgroup and find the median
    medians = [sorted(sublist)[len(sublist)//2] for sublist in sublists]

    # Step 3: Recursively finding the median of the medians
    median_of_medians = select(medians, len(medians)//2)

    # Step 4: Using the median of medians as pivot to partition the array
    left, middle, right = partition(arr, median_of_medians)

    # Step 5: Determine the k-th smallest element
    if k < len(left):
        return select(left, k)
    elif k < len(left) + len(middle):
        return middle[0]
    else:
        return select(right, k - len(left) - len(middle))

    
    

arr = [i for i in np.random.randint(0,10000,200)]
k = int(input("Enter no. K for finding Kth smallest element: "))
start_time = time.time()
print("Value from quickSelect method: ",quickSelect(arr,k-1))
end_time = time.time()
t1 = end_time-start_time

start_time = time.time()
print("Value from Medians Of Medians method: ",select(arr,k-1))
end_time = time.time()

t2=end_time-start_time

plt.plot([0,200],[0,t1],color = "green",label = "quickSelect")
plt.plot([0,200],[0,t2],label = "Median of Medians")
plt.legend()
plt.show()


