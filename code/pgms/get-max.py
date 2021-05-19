"""Get the max value of array with rules:
    1. first element should be 1
    2. difference between elements will not be more than 1

    you can arrange the array or change the element to do so
    return max value in array
    """

from typing import List
import time


def getMax(input: List) -> int:
    sortedInput = sorted(input)
    if sortedInput[0] != 1:
        sortedInput[0] = 1

    for i in range(len(sortedInput) - 1):
        if sortedInput[i +1] - sortedInput[i] > 1:
            sortedInput[i + 1] = sortedInput[i] + 1

    print(f'{sortedInput}')
    return sortedInput[-1]


if __name__ == '__main__':
    start = time.time()
    print(f'max value for [1,3,3,5] is {getMax([1,3,3,5])}')
    print(f'max value for [1,3,3,5,15,2,3,4,7,8] is {getMax([1,3,3,5,15,2,3,4,7,8])}')
    print(f'max value for [12,3,3,5,6,7,8,12] is {getMax([12,3,3,5,6,7,8,12])}')
    end = time.time()
    print(f'time taken is {end - start} s')
