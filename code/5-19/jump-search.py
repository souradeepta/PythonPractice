# Jump Search
# Jump search would first determine the jump size by computing math.sqrt(len(lys)).
# Since we have 9 elements, the jump size would be √9 = 3.
# Next, we compute the value of the right variable,
# which is the minimum of the length of the array minus 1,
# or the value of left+jump, which in our case would be 0+3= 3.
# Since 3 is smaller than 8 we use 3 as the value of right.
# The time complexity of jump search is O(√n), where √n is the jump size, and n is the length of the list,
# placing jump search between the linear search and binary search algorithms in terms of efficiency.

import math


def jump_search(input: list, target: int) -> int:
    length = len(input)
    jump = int(math.sqrt(length))
    low, high = 0, 0
    while low < length and input[low] <= target:
        high = min(length-1, low+jump)
        if input[low] <= target and target <= input[high]:
            break
        low += jump

    if low >= length or input[low] > target:
        return -1

    high = min(length - 1, low)
    i = low
    while i <= high and input[i] <= target:
        if input[i] == target:
            return i
        i += 1

    return -1


print(jump_search([1, 2, 3, 4, 5, 6, 7, 8], 3))
print(jump_search([], 3))
print(jump_search([1, 2, 4, 5, 6, 7, 8], 3))
print(jump_search([1, 2, 3, 4, 15, 16, 17, 18], 18))
