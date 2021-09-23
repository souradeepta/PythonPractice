# mistakes: forgot overflow mid value, forgot <= in while,
# forgot to keep mid in loop
from typing import Any


def binary_search(input: list, target: Any) -> Any:
    low, high = 0, len(input)-1
    while low <= high:
        mid = low + (high-low)//2
        if input[mid] == target:
            return mid
        elif input[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return -1


assert(binary_search([2, 4, 6, 34, 45, 56, 777], 34) == 3)
assert(binary_search([2, 4, 6, 34, 45, 56, 777], 211) == -1)
