import time
import matplotlib.pyplot as plt

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+ 1] = arr[j]
            j -= 1
        arr[j+1] = key





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
    insertionSort(arr)
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
plt.title('Insertion Sort Time Complexity')
plt.legend()
plt.show()
