def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle of the array
        left_half = arr[:mid]  # Divide the array into two halves
        right_half = arr[mid:]

        merge_sort(left_half)  # Recursive call on the left half
        merge_sort(right_half)  # Recursive call on the right half

        # Merge the sorted halves
        merge(arr, left_half, right_half)

def merge(arr, left_half, right_half):
    i, j, k = 0, 0, 0  # Initialize pointers for left_half, right_half, and arr

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    # Check if any elements are left in the two halves
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

# Simple test to demonstrate Merge Sort
test_array = [64, 34, 25, 12, 22, 11, 90]
merge_sort(test_array)
test_array
