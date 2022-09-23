class ArraySorter:
    array = [5, 2, 4, 6, 1, 3]

    def reset_array(self):
        self.array = [5, 2, 4, 6, 1, 3]

    # Not stable
    def selection_sort(self):
        for i in range(len(self.array) - 1):
            min_idx = i

            for j in range(i+1, len(self.array)):
                if self.array[min_idx] > self.array[j]:
                    min_idx = j

            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]

        return self.array

    # Is a stable algorithm
    def insertion_sort(self):
        # Loop through the array
        for j in range(1, len(self.array)):
            key = self.array[j]
            i = j - 1
            # i >= 0 ensures the algorithm does not look outside the array, when j = 0.
            while i >= 0 and self.array[i] > key:
                self.array[i + 1] = self.array[i]
                i -= 1
            self.array[i + 1] = key
        return self.array

    # Is a stable sorting algorithm
    def merge_sort(self, array):
        if len(array) > 1:
            mid = len(array) // 2

            # Divide the array into two halves
            left = array[:mid]
            right = array[mid:]

            # Merge sort each half recursively
            self.merge_sort(left)
            self.merge_sort(right)

            # merge lefts and rights sequentially
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    array[k] = left[i]
                    i += 1
                else:
                    array[k] = right[j]
                    j += 1
                k += 1

            """Looping over the left over elements in left and right array respectively and 
            adding them to the k'th index in array variable."""
            while i < len(left):
                array[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                array[k] = right[j]
                j += 1
                k += 1

        return self.array

    # Stable
    def counting_sort(self):
        pass


if __name__ == '__main__':
    array_sorter = ArraySorter()

    # Insert sort test
    print("Insert sort = ", end=" ")
    result = array_sorter.insert_sort()
    print(result)
    array_sorter.reset_array()

    # Selection sort
    print("Selection sort =", end=" ")
    result = array_sorter.selection_sort()
    print(result)
    array_sorter.reset_array()

    # Merge sort
    print("Merge sort =", end=" ")
    result = array_sorter.merge_sort(array_sorter.array)
    print(result)
