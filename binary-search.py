#Time Complexity of 
# O(log2 n) = O(log n)

import math

arr = [-2,3,4,7,8,9,11,13]

target = 11

def search (arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) / 2
        mid_rounded = math.floor(mid)
        if arr[mid_rounded] == target:
            return mid_rounded
        elif target < arr[mid_rounded]:
            right = mid_rounded - 1
        else:
            left = mid_rounded + 1
    return -1

print(search(arr, target))