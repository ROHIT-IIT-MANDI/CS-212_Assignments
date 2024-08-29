import time
import matplotlib.pyplot as plt
import numpy as np

def partition(arr, low, high):
    pivot = arr[np.random.randint(0,high+1)]  # Taking the last element as pivot
    i = low - 1  # Index of smaller element
    for j in range(low, high):
        if arr[j] < pivot:  # If the current element is smaller than or equal to pivot
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Place the pivot in the correct position
    return i + 1

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)  # Partition index
        quickSort(arr, low, pi - 1)  # Sort elements before partition
        quickSort(arr, pi + 1, high)  # Sort elements after partition

t = int(input())
sizes = []
times = []
grouped_times = []
grouped_sizes = []

for k in range(t):
    n = int(input())
    arr = [0]*n
    for i in range (n):
        arr[i] = int(input())
    sizes.append(n)
    start_time = time.time()
    quickSort(arr,0,n-1)
    end_time = time.time()
    times.append((end_time - start_time))

# Group the times and sizes for plotting
for i in range(0, len(times), 3):
    grouped_times.append(times[i:i+3])
    grouped_sizes.append(sizes[i:i+3])

# Plotting the graph
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
label = ["Random no.s", "Sorted no.s" , "Reverse Sorted no.s", "Duplicate no.s"]

plt.figure()

for i in range(len(grouped_times)):
    plt.plot(grouped_sizes[i], grouped_times[i], color=colors[i % len(colors)], label=f'{label[i]}')

plt.xlabel('Size of the array')
plt.ylabel('Time taken (seconds)')
plt.title('Merge Sort Time Complexity')
plt.legend()
plt.show()
