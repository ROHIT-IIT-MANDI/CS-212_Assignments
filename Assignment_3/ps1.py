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
    if len(arr) <= 5:
        return sorted(arr)[k]

    sublists = [arr[i:i+5] for i in range(0, len(arr), 5)]

    medians = [sorted(sublist)[len(sublist)//2] for sublist in sublists]
    median_of_medians = select(medians, len(medians)//2)
    left, middle, right = partition(arr, median_of_medians)

    if k < len(left):
        return select(left, k)
    elif k < len(left) + len(middle):
        return middle[0]
    else:
        return select(right, k - len(left) - len(middle))

    
    

arr = [i for i in np.random.randint(0,10000,20)]
k = int(input("Enter no. K for finding Kth smallest element: "))
print("Sorted array : ",sorted(arr))
print("Value from quickSelect method: ",quickSelect(arr,k-1))


print("Max. of the array is: ",max(arr))
print("Min. of the array is: ",min(arr))



print("Value from Medians Of Medians method: ",select(arr,k-1))




