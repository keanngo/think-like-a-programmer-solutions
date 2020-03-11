def findSumRecursive(array, size):
    if size == 0:
        return 0
    sum = array[size-1]
    return sum + findSumRecursive(array, size-1)

arr = [1, 2, 3, 4, 5]
print(findSumRecursive(arr, len(arr)))