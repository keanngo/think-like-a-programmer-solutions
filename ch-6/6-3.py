def targetNumberOccurances(array, target):
    if len(array) == 1:
        if array[0] == target:
            return 1
        else:
            return 0
    else:
        return 0
    
    lastValue = array[len(array) - 1]
    array.pop()
    if( lastValue == target):
        return 1 + targetNumberOccurances(array, target)
    else:
        return targetNumberOccurances(array, target)


arr = []
print(targetNumberOccurances(arr, 2))
