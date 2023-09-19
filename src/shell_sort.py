def shell_sort(arr):
    """
    Sort an array using the Shell Sort algorithm.

    Parameters:
        arr (list): List of elements to be sorted.

    Returns:
        list: Sorted list.
    """
    n = len(arr)
    gap = n // 2  # Initialize the gap sequence

    # Main sorting loop
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]  # Store the current element in a temporary variable
            j = i

            # Inner loop for the insertion sort
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp  # Place the temp at its correct position

        gap = gap // 2  # Reduce the gap

    return arr

# Basic unit test to verify the algorithm's functionality
test_array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
sorted_array = shell_sort(test_array.copy())

print(test_array, sorted_array)