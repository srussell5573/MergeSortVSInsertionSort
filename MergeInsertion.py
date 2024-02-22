import timeit
import random
import matplotlib.pyplot as plt

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

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

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def measure_time(sort_func, arr):
    start_time = timeit.default_timer()
    sort_func(arr)
    elapsed = timeit.default_timer() - start_time
    if elapsed == 0.0:
        runs = 1000
        total_time = 0.0
        for _ in range(runs):
            start_time = timeit.default_timer()
            sort_func(arr.copy())
            total_time += timeit.default_timer() - start_time
        elapsed = total_time / runs
    return elapsed

def generate_random_array(n):
    return [random.randint(0, 1000) for _ in range(n)]

if __name__ == "__main__":
    results = {'Insertion Sort': [], 'Merge Sort': []}
    ns = [10, 50, 100, 500, 1000, 5000, 10000, 12500, 15000, 17500, 20000] #, 22500, 25000, 27500, 30000, 32500, 35000, 37500, 40000] # Range of values for n

    for n in ns:
        arr = generate_random_array(n)
        insertion_time = measure_time(insertion_sort, arr.copy())
        merge_time = measure_time(merge_sort, arr.copy())
        results['Insertion Sort'].append(insertion_time)
        results['Merge Sort'].append(merge_time)

    # Plotting the results
    plt.figure(figsize=(10, 6))
    for algo, times in results.items():
        plt.plot(ns, times, label=algo)
    plt.xlabel('Input Size (n)')
    plt.ylabel('Time (s)')
    plt.title('Comparison of Insertion Sort and Merge Sort')
    plt.legend()
    plt.grid(True)
    plt.xscale('log')
    plt.yscale('log')
    plt.show()