def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to optimize and check if any swapping happened
        swapped = False

        # Last i elements are already sorted, so skip them
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if the element is greater than the next element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no elements were swapped, the array is already sorted
        if not swapped:
            break


# Simple test to demonstrate Bubble Sort
test_array = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(test_array)
print(test_array)
