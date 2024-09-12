import time
import matplotlib.pyplot as plt

def radix_sort(arr):

  
  max_digits = len(str(max(arr)))

  
  temp = [0] * len(arr)

  
  for i in range(max_digits):
   
    count = [0] * 10

    
    for j in range(len(arr)):
      digit = (arr[j] // (10 ** i)) % 10
      count[digit] += 1

    
    for j in range(1, 10):
      count[j] += count[j - 1]

    
    for j in range(len(arr) - 1, -1, -1):
      digit = (arr[j] // (10 ** i)) % 10
      temp[count[digit] - 1] = arr[j]
      count[digit] -= 1

    
    arr = temp.copy()

  return arr




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
    radix_sort(arr)
    end_time = time.time()
    times.append((end_time - start_time))

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
plt.title('Radix Sort Time Complexity')
plt.legend()
plt.show()
