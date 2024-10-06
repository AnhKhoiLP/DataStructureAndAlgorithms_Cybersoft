import random

# Generate an array of 100 random integers
arr = [random.randint(0, 1000) for _ in range(100)]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Before sorting
print("Before sorting:", arr)

# Sorting the array using Selection Sort
selection_sort(arr)

# After sorting
print("After sorting:", arr)


import random
# Generate an array of 100 random integers
arr = [random.randint(0, 1000) for _ in range(100)]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Before sorting
print("Before sorting:", arr)

# Sorting the array using Insertion Sort
insertion_sort(arr)

# After sorting
print("After sorting:", arr)