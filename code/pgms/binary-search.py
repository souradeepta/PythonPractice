from typing import List


def binary_search(input: List, target: int) -> int:
    left = 0
    right = len(input)
    while left <= right:
        mid = left + (right-left)//2
        if input[mid] == target:
            return mid
        elif input[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1


print(f'{binary_search([1,2,3,4,5,6,7,8,9], 5)}')
