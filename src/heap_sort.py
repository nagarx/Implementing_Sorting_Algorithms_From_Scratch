class HeapSort:
    def __init__(self, array):
        self.array = array
        self.n = len(array)

    def heapify(self, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.array[i] < self.array[left]:
            largest = left

        if right < n and self.array[largest] < self.array[right]:
            largest = right

        if largest != i:
            self.array[i], self.array[largest] = self.array[largest], self.array[i]
            self.heapify(n, largest)

    def sort(self):
        # Build a max heap
        for i in range(self.n // 2 - 1, -1, -1):
            self.heapify(self.n, i)

        # Extract elements one by one
        for i in range(self.n - 1, 0, -1):
            self.array[i], self.array[0] = self.array[0], self.array[i]  # Swap
            self.heapify(i, 0)
        return self.array


# Sample usage
sample_array = [12, 11, 13, 5, 6, 7]
heap_sort = HeapSort(sample_array)
sorted_array = heap_sort.sort()
print(sorted_array)
