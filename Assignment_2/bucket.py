import time
import matplotlib.pyplot as plt
import numpy as np



def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key
    return bucket

def bucket_sort(arr):
    # Determine the number of buckets to use
    max_value = max(arr)
    min_value = min(arr)

    # Creating empty buckets
    buckets = [[] for _ in range(len(arr))]

    # Distribute input array values into buckets
    for num in arr:
        # Determine the appropriate bucket for this element
        index = int((num - min_value) / (max_value - min_value + 1) * len(arr))
        buckets[index].append(num)

    # Sort individual buckets and concatenate them
    sorted_array = []
    for bucket in buckets:
        sorted_array.append(insertion_sort(bucket))

    return sorted_array



def array_random(n):
    array_random = [np.random.randint(0,1) for _ in range(n)]
    return array_random

def array_sorted(n):
    array_sorted = [i/(2*n) for i in range(n + 1)]
    return array_sorted

def array_rev_sorted(n):
    array_rev_sorted = [i/(2*n) for i in range(n, -1, -1)]
    return array_rev_sorted

def array_high_repetition(n):
    array_high_repetition = [round(i,1) for i in np.random.uniform(0,1)]
    return array_high_repetition


#arr = [array_random(),array_sorted,array_rev_sorted,array_high_repetition]


t = int(input())
sizes = []
times = []
grouped_times = []
grouped_sizes = []

for k in range(t):
    n = int(input())
    arr = [0]*n
    for i in range (n):
        arr[i] = float(input())
    sizes.append(n)
    
    start_time = time.time()
    bucket_sort(arr)
    
    end_time = time.time()
    times.append((end_time - start_time))
    if n==100:
        print(bucket_sort(arr))

# Grouping the times and sizes for plotting
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
plt.title('Bucket Sort Time Complexity')
plt.legend()
plt.show()