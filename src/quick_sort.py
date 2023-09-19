def quick_sort(arr, low, high):
    if low < high:
        # Find the partition index
        pi = partition(arr, low, high)

        # Sort the elements before and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def partition(arr, low, high):
    # Choose the rightmost element as the pivot
    pivot = arr[high]

    # Pointer for greater elements
    i = low - 1

    # Iterate through all elements to rearrange them
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    # Swap the pivot element with the greater element at i
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    # Return the partition index
    return i + 1


# Simple test to demonstrate Quick Sort
test_array = [64, 34, 25, 12, 22, 11, 90]
quick_sort(test_array, 0, len(test_array) - 1)
print(test_array)
