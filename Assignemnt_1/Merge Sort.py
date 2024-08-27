import time
import matplotlib.pyplot as plt

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

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
    mergeSort(arr)
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
