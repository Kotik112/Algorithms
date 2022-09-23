# Linear search. Works on any array, sorted or otherwise.
def search(arr, target):
    for num in arr:
        if num == target:
            return num


# Binary search from sorted array
def binary_search(arr, start, end, target):
    if end >= start:

        # Find the middle of the array
        mid = (start + end) // 2

        if target > arr[mid]:
            return binary_search(arr, mid + 1, end, target)

        elif target < arr[mid]:
            return binary_search(arr, start, mid - 1, target)

        else:
            return mid
    else:
        return -1


if __name__ == '__main__':
    array = [2, 3, 5, 8, 10, 16, 22, 66]
    # print("Target = " + str(search(array, target_num)))

    target_num = int(input("Enter the number you want to search: "))

    result = binary_search(array, 0, len(array)-1, target_num)
    if result == -1:
        print("Did not find the element you searched for.")
    else:
        print("Target index = " + str(result))
        print("Value at target index = " + str(array[result]))
