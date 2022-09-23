from random import randint

ARRAY_SIZE = 10

class ArraySorter:
    # array = []

    def construct_array(self, n):
        self.array = []
        for i in range(0, n):
            self.array.append(randint(0, 10))


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
    array_sorter.construct_array(ARRAY_SIZE)
    result = array_sorter.insertion_sort()
    print("Insert sort = ", end=" ")
    print(result)

    # Selection sort
    array_sorter.construct_array(ARRAY_SIZE)
    result = array_sorter.selection_sort()
    print("Selection sort =", end=" ")
    print(result)

    # Merge sort
    array_sorter.construct_array(ARRAY_SIZE)
    result = array_sorter.merge_sort(array_sorter.array)
    print("Merge sort =", end=" ")
    print(result)
