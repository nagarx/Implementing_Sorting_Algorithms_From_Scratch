# Counting sort algorithm used for sorting based on individual digit place (exp).
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n  # Initialize output array
    count = [0] * 10  # Initialize counting array with 10 buckets for digits 0-9

    # Count occurrences of each digit at the exp-th place in the array elements
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Update count[i] to store the position of the next occurrence of the same digit
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array using the count array
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copy the sorted elements back into the original array
    for i in range(n):
        arr[i] = output[i]

    return arr

# Implementing Radix Sort algorithm.
def radix_sort(arr):
    # Handle empty array
    if len(arr) == 0:
        return arr

    # Separate the array into positive and negative numbers
    positive_nums = [num for num in arr if num >= 0]
    negative_nums = [-num for num in arr if num < 0]

    # Find the maximum elements for positive and negative arrays
    max_positive = max(positive_nums) if positive_nums else 0
    max_negative = max(negative_nums) if negative_nums else 0

    # Sorting positive numbers using existing radix sort logic
    exp = 1
    while max_positive // exp > 0:
        counting_sort(positive_nums, exp)
        exp *= 10

    # Sorting negative numbers using existing radix sort logic
    exp = 1
    while max_negative // exp > 0:
        counting_sort(negative_nums, exp)
        exp *= 10

    # Inverting the negative numbers back to their original sign and reversing to maintain order
    negative_nums = [-num for num in reversed(negative_nums)]

    # Merging positive and negative arrays to get the final sorted array
    arr = negative_nums + positive_nums

    return arr
